import base64
import json
import os
import random
import pandas as pd
import streamlit as st
from streamlit_extras.let_it_rain import rain
from componentes.css import carregar_css

CONFIG_FILE = "config.json"

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Vistar Quest",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# CARREGAR CSS
carregar_css()

# ESTILO GLOBAL COM TEXTO BRANCO NÍDITO E SEM BORRÃO
st.markdown(
    """
    <style>
    /* Textos gerais com branco nítido e sombra leve para destaque sem desfoque */
    p, span, .stMarkdown {
        color: #FFFFFF !important;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.9) !important;
        font-weight: 500 !important;
    }
    /* Labels e opções de rádio com sombra limpa e sem borrão */
    label, .stRadio label, div[data-baseweb="radio"] div {
        color: #FFFFFF !important;
        text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.7) !important;
    }
    /* Excluir menus suspensos (selectbox) para manter o texto nítido sem distorção */
    div[data-baseweb="menu"] *, div[data-baseweb="popover"] *, div[data-baseweb="select"] * {
        text-shadow: none !important;
    }
    /* Títulos em branco puro de alta nitidez */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.95) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Função para carregar imagens em Base64 (para HTML/CSS no Streamlit)
def carregar_imagem_base64(caminho_arquivo):
    try:
        diretorio_raiz = os.path.dirname(os.path.abspath(__file__))
        caminho_completo = os.path.join(diretorio_raiz, caminho_arquivo)
        with open(caminho_completo, "rb") as f:
            data = f.read()
        encoded_string = base64.b64encode(data).decode()
        return f"data:image/png;base64,{encoded_string}"
    except Exception:
        return None

# Carrega a imagem da mochila
mochila_img_b64 = carregar_imagem_base64("assets/mochila.png")

# ==========================================
# FUNÇÕES DE CARREGAMENTO (JSON E DADOS)
# ==========================================
@st.cache_data
def carregar_json(caminho_arquivo):
    """Carrega dados de qualquer arquivo JSON do projeto."""
    try:
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    except Exception as e:
        st.error(f"Erro ao carregar {caminho_arquivo}: {e}")
        return []

# ==========================================
# CARREGAMENTO DOS DADOS SEPARADOS
# ==========================================
QUESTOES_MATEMATICA = carregar_json("dados/questoes_matematica.json")
QUESTOES_PORTUGUES = carregar_json("dados/questoes_portugues.json")
RECOMPENSAS_LOJA = carregar_json("config/loja_recompensas.json")

def carregar_audio_base64(caminho_arquivo):
    """Lê um arquivo de áudio local e retorna no formato Base64 para HTML5."""
    try:
        with open(caminho_arquivo, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

# ==========================================
# CARREGAMENTO DOS ÁUDIOS EM BASE64
# ==========================================
musica_fundo_b64 = carregar_audio_base64("assets/musica_fundo.mp3")
som_nave_b64 = carregar_audio_base64("assets/som_nave.wav")
som_robo_b64 = carregar_audio_base64("assets/som_robo.mp3")
som_comando_b64 = carregar_audio_base64("assets/som_nave.wav")

# Controla se o jogador já deu "Start" no jogo
if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False

# Tela inicial para capturar o primeiro clique e liberar o áudio
if not st.session_state.jogo_iniciado:
    st.title("🚀 Vistar Quest")
    st.write("Clique no botão abaixo para ligar os motores e iniciar a missão!")

    if st.button("▶ INICIAR JOGO", use_container_width=True):
        st.session_state.jogo_iniciado = True
        st.rerun()

else:
    if musica_fundo_b64:
        st.markdown(
            f"""
            <audio id="bg-music" autoplay loop style="display:none;">
                <source src="data:audio/mp3;base64,{musica_fundo_b64}" type="audio/mp3">
            </audio>
            <script>
                var audio = document.getElementById("bg-music");
                if (audio) {{
                    audio.volume = 0.05;
                }}
            </script>
            """,
            unsafe_allow_html=True,
        )

# ==========================================
# CENÁRIO ESPACIAL (Fundo Vivo, Estrelas, Planetas e Espaçonave)
# ==========================================
img_nave_b64 = carregar_imagem_base64("assets/nave.png")
img_fundo_b64 = carregar_imagem_base64("assets/fundo_espaco.jpg") or carregar_imagem_base64("assets/fundo_espaco.jpeg")

if img_fundo_b64:
    st.markdown(
        f"""
        <style>
            .stApp {{
                background-image: url("{img_fundo_b64}") !important;
                background-size: cover !important;
                background-position: center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed !important;
            }}
            .space-bg {{
                background: transparent !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

nave_html = (
    f'<img src="{img_nave_b64}" class="spaceship">'
    if img_nave_b64
    else '<div class="spaceship">🛸</div>'
)

st.markdown(
    f"""
    <div class="space-bg">
        <div class="stars"></div>
        <div class="twinkling"></div>
        <div class="planet planet-1">🪐</div>
        <div class="planet planet-2">🌕</div>
        {nave_html}
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# MASCOTES INTERATIVOS
# ==========================================
def exibir_robo(mensagem="Olá, Explorador! Vamos aprender juntos?", estado="normal"):
    img_b64 = carregar_imagem_base64("assets/robo.png")
    emojis_estado = {"normal": "✨", "feliz": "😊", "pensativo": "🤔", "comemora": "🎉", "erro": "⚠️"}
    icone_estado = emojis_estado.get(estado, "✨")

    if img_b64:
        avatar_html = f"""
            <div style="position: relative; display: inline-block;">
                <img src="{img_b64}" alt="Robô" style="width: 80px; height: auto;">
                <span style="position: absolute; bottom: 0; right: 0; font-size: 20px;">{icone_estado}</span>
            </div>
        """
    else:
        avatar_html = f"🤖 {icone_estado}"

    st.markdown(
        f"""
        <div class="robo-container">
            <div class="robo-avatar">{avatar_html}</div>
            <div class="robo-balao-fala">
                <strong>🤖 Robô Astro:</strong><br>
                {mensagem}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def exibir_astrobaldo(mensagem="", estado="normal"):
    img_b64 = carregar_imagem_base64("assets/astrobaldo.png")
    emojis_estado = {"normal": "✨", "comemora": "🎉", "erro": "🧐"}
    icone_estado = emojis_estado.get(estado, "✨")

    if img_b64:
        avatar_html = f"""<div style="position: relative; display: inline-block;"><img src="{img_b64}" alt="Astrobaldo" style="width: 100px; height: auto;"><span style="position: absolute; bottom: 0; right: 0; font-size: 22px;">{icone_estado}</span></div>"""
    else:
        avatar_html = f"👾 {icone_estado}"

    cor_borda_balao = "#2ecc71" if estado == "comemora" else ("#e74c3c" if estado == "erro" else "#a29bfe")

    html_astrobaldo = f"""<div style="display: flex; flex-direction: column; align-items: center; width: 100%; margin-top: 10px;"><div style="margin-bottom: 12px; text-align: center;">{avatar_html}</div><div style="position: relative; background: rgba(20, 20, 35, 0.95); border: 2px solid {cor_borda_balao}; border-radius: 12px; padding: 12px 16px; color: #ffffff; width: 100%; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.3);"><div style="position: absolute; top: -10px; left: 50%; transform: translateX(-50%); width: 0; height: 0; border-left: 10px solid transparent; border-right: 10px solid transparent; border-bottom: 10px solid {cor_borda_balao};"></div><strong style="color: {cor_borda_balao}; font-size: 16px;">👾 Astrobaldo:</strong><br><span style="font-size: 15px; color: #FFFFFF;">{mensagem}</span></div></div>"""

    st.markdown(html_astrobaldo, unsafe_allow_html=True)

# ==========================================
# CARREGAR DADOS DE ALUNOS E QUESTÕES
# ==========================================
def carregar_alunos():
    caminho = "dados/alunos.csv"
    if not os.path.exists("dados"):
        os.makedirs("dados")

    try:
        df = pd.read_csv(caminho, encoding="utf-8")
    except Exception:
        df = pd.DataFrame(columns=["Nome", "Turma", "XP", "Nivel"])

    if "XP" not in df.columns:
        df["XP"] = 0
    if "Nivel" not in df.columns:
        df["Nivel"] = 1

    df["XP"] = df["XP"].astype(int)
    df["Nivel"] = df["Nivel"].astype(int)
    return df

def salvar_alunos(df):
    df.to_csv("dados/alunos.csv", index=False, encoding="utf-8")

alunos = carregar_alunos()

@st.cache_data
def carregar_questoes():
    try:
        with open("dados/questoes.json", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except Exception:
        return []

questoes = carregar_questoes()

questoes_matematica = [q for q in questoes if q.get("disciplina") == "Matemática"]
questoes_portugues = [q for q in questoes if q.get("disciplina") == "Português"]

# ==========================================
# ESTADOS DA APLICAÇÃO
# ==========================================
if "modo" not in st.session_state:
    st.session_state.modo = None
if "missao_ativa" not in st.session_state:
    st.session_state.missao_ativa = False
if "xp_ganho" not in st.session_state:
    st.session_state.xp_ganho = 0
if "planeta" not in st.session_state:
    st.session_state.planeta = None
if "questao_atual" not in st.session_state:
    st.session_state.questao_atual = None
if "ultimo_feedback" not in st.session_state:
    st.session_state.ultimo_feedback = None

# ==========================================
# CABEÇALHO PRINCIPAL
# ==========================================
img_logo_b64 = carregar_imagem_base64("assets/logo.png")
logo_html = f'<img src="{img_logo_b64}" style="height: 70px; vertical-align: middle; margin-right: 15px;">' if img_logo_b64 else ""

html_cabecalho = f'<div style="text-align: center; margin-bottom: 25px; filter: drop-shadow(0px 4px 10px rgba(0,0,0,0.9));"><div style="display: inline-flex; align-items: center; justify-content: center;">{logo_html}<span style="color: #FFFFFF; font-size: 65px; font-weight: 800; vertical-align: middle; letter-spacing: 2px; text-shadow: 0px 0px 15px rgba(255, 255, 255, 0.6);">VISTAR QUEST</span></div><div style="color: #FFD700; font-size: 21px; font-weight: 700; margin-top: 8px; letter-spacing: 1px; text-transform: uppercase;">UMA AVENTURA PELO UNIVERSO DO CONHECIMENTO</div></div>'

st.markdown(html_cabecalho, unsafe_allow_html=True)

# ==================================================
# TELA INICIAL
# ==================================================
if st.session_state.modo is None:
    st.write("")
    exibir_robo("Bem-vindo à estação espacial! Escolha o seu modo de acesso para começar.", "normal")
    st.write("")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="card">
                <h2 style="text-align:center;">🧑‍🚀 Explorador Espacial</h2>
                <br>
                <p style="text-align:center;font-size:18px;">
                ✔ Ganhe XP<br>
                ✔ Complete missões<br>
                ✔ Suba de nível<br>
                ✔ Conquiste medalhas<br>
                ✔ Explore novos planetas
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("🚀 Iniciar Aventura", key="btn_aluno", use_container_width=True):
            if som_nave_b64:
                st.markdown(f'<audio autoplay src="data:audio/wav;base64,{som_nave_b64}"></audio>', unsafe_allow_html=True)
            rain(emoji="⭐", font_size=40, falling_speed=5, animation_length="medium")
            st.session_state.modo = "aluno"
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="card">
                <h2 style="text-align:center;">👨‍🏫 Centro de Comando</h2>
                <br>
                <p style="text-align:center;font-size:18px;">
                ✔ Ranking da turma<br>
                ✔ Evolução dos alunos<br>
                ✔ XP conquistado<br>
                ✔ Níveis alcançados<br>
                ✔ Relatórios pedagógicos
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("📊 Entrar no Painel", key="btn_professor", use_container_width=True):
            if som_comando_b64:
                st.markdown(f'<audio autoplay src="data:audio/wav;base64,{som_comando_b64}"></audio>', unsafe_allow_html=True)
            st.session_state.modo = "professor"
            st.rerun()

    st.stop()

def exibir_mochila_aluno():
    st.markdown("## 🎒 Mochila de Benefícios & Loja Espacial")
    st.write("Troque suas moedas conquistadas nas missões por prêmios e privilégios na sala de aula!")

    if "moedas" not in st.session_state:
        st.session_state.moedas = 0
    if "xp" not in st.session_state:
        st.session_state.xp = 0
    if "itens_resgatados" not in st.session_state:
        st.session_state.itens_resgatados = []

    col_xp, col_moedas, col_itens = st.columns(3)
    with col_xp:
        st.metric("XP Total", f"⭐ {st.session_state.xp}")
    with col_moedas:
        st.metric("Suas Moedas", f"🪙 {st.session_state.moedas}")
    with col_itens:
        st.metric("Itens na Mochila", f"📦 {len(st.session_state.itens_resgatados)}")

    st.markdown("---")

    aba_loja, aba_minha_mochila = st.tabs(["🏪 Loja de Recompensas", "🎒 Meus Resgates"])

    with aba_loja:
        if not RECOMPENSAS_LOJA:
            st.info("Nenhuma recompensa disponível na loja no momento.")
            return

        cols = st.columns(2)
        for index, item in enumerate(RECOMPENSAS_LOJA):
            col_atual = cols[index % 2]

            with col_atual:
                custo = item.get("custo_moedas", 0)
                tem_saldo = st.session_state.moedas >= custo

                st.markdown(
                    f"""
                    <div style="
                        background-color: rgba(30, 30, 46, 0.9);
                        border: 2px solid {'#4cc9f0' if tem_saldo else '#444'};
                        border-radius: 12px;
                        padding: 15px;
                        margin-bottom: 10px;
                        min-height: 140px;
                    ">
                        <h4 style="margin:0; color:#FFFFFF;">{item.get('icone', '🎁')} {item.get('nome', 'Item')}</h4>
                        <p style="font-size: 13px; color: #FFFFFF; margin: 8px 0;">{item.get('descricao', '')}</p>
                        <p style="margin:0; font-weight:bold; color: {'#a6e3a1' if tem_saldo else '#f38ba8'};">
                            Custo: 🪙 {custo} moedas
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(f"Resgatar {item.get('nome')}", key=f"btn_resgate_{item.get('id')}", disabled=not tem_saldo, use_container_width=True):
                    st.session_state.moedas -= custo
                    st.session_state.itens_resgatados.append({
                        "nome": item.get("nome"),
                        "icone": item.get("icone", "🎁"),
                        "data": "Hoje",
                    })
                    try:
                        rain(emoji="🎉", font_size=32, falling_speed=3, animation_length=1)
                    except Exception:
                        pass
                    st.success(f"🎉 Você resgatou '{item.get('nome')}'! Avise seu professor para utilizar.")
                    st.rerun()

    with aba_minha_mochila:
        if not st.session_state.itens_resgatados:
            st.write("Sua mochila está vazia. Acumule moedas nas missões para trocar por benefícios!")
        else:
            st.write("### 📜 Benefícios Conquistados")
            for idx, resgate in enumerate(st.session_state.itens_resgatados):
                st.info(f"{resgate['icone']} **{resgate['nome']}** — Resgatado e pronto para usar!")

# ==================================================
# ÁREA DO ALUNO
# ==================================================
if st.session_state.modo == "aluno":
    st.divider()

    nome = st.selectbox(
        "Escolha seu explorador:",
        alunos["Nome"] if len(alunos) > 0 else ["Nenhum aluno"],
        key="selecionar_aluno",
    )

    if len(alunos) > 0 and nome in alunos["Nome"].values:
        idx_aluno = alunos[alunos["Nome"] == nome].index[0]
        aluno = alunos.loc[idx_aluno]
        xp = int(aluno["XP"])
        nivel = int(aluno["Nivel"])
    else:
        xp = 0
        nivel = 1
        idx_aluno = 0

    progresso = (xp % 100) / 100.0

    col_logo, col_xp, col_nivel, col_avatar = st.columns([4, 1.5, 1.5, 1])

    with col_logo:
        st.markdown(
            """
            <div class="logo-quest">
                🚀 <span class="azul">VISTAR</span><span class="amarelo">QUEST</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_xp:
        st.markdown(
            f"""
            <div class="status-quest">
                <div class="status-icone">⭐</div>
                <div class="status-titulo">XP</div>
                <div class="status-valor">{xp}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    with col_nivel:
        st.markdown(
            f"""
            <div class="status-quest">
                <div class="status-icone">🏆</div>
                <div class="status-titulo">Nível</div>
                <div class="status-valor">{nivel}</div>
            </div>""",
            unsafe_allow_html=True,
        )

    with col_avatar:
        st.markdown('<div class="avatar-quest">🧑‍🚀</div>', unsafe_allow_html=True)

    exibir_robo(f"Olá, {nome}! Prepare sua nave, escolha um planeta e vamos resolver desafios!", "feliz")

    st.progress(progresso)
    st.divider()

    # TELA DE SELEÇÃO DOS PLANETAS
    if st.session_state.planeta is None:
        img_planeta_principal_b64 = carregar_imagem_base64("assets/planeta.png")
        img_mat_b64 = carregar_imagem_base64("assets/icone_matematica.png")
        img_port_b64 = carregar_imagem_base64("assets/icone_portugues.png")
        img_mochila_b64 = carregar_imagem_base64("assets/mochila.png")

        logo_planeta_html = f'<img src="{img_planeta_principal_b64}" style="height: 85px; vertical-align: middle; margin-right: 14px;">' if img_planeta_principal_b64 else ""
        html_titulo_planetas = f'<div style="display: flex; align-items: center; margin-bottom: 20px;">{logo_planeta_html}<span style="color: #FFFFFF; font-size: 28px; font-weight: 800; text-shadow: 0px 0px 8px rgba(0,0,0,0.9);">Planetas de Aprendizagem & Loja</span></div>'
        st.markdown(html_titulo_planetas, unsafe_allow_html=True)

        p1, p2, p3 = st.columns(3)

        with p1:
            icon_html = f'<img src="{img_mat_b64}" style="height: 50px; vertical-align: middle; margin-right: 8px;">' if img_mat_b64 else ""
            st.markdown(
                f"""
                <div class="planeta">
                    {icon_html}<h3>Planeta Matemática</h3>
                    Desafios de números, operações e problemas.<br><br>
                    🔓 Desbloqueado
                </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button("🚀 Entrar", key="entrar_matematica", use_container_width=True):
                if som_nave_b64:
                    st.markdown(f'<audio autoplay src="data:audio/wav;base64,{som_nave_b64}"></audio>', unsafe_allow_html=True)
                st.session_state.planeta = "matematica"
                st.session_state.missao_ativa = False
                st.session_state.questao_atual = None
                st.session_state.ultimo_feedback = None
                st.rerun()

        with p2:
            icon_html = f'<img src="{img_port_b64}" style="height: 50px; vertical-align: middle; margin-right: 8px;">' if img_port_b64 else ""
            st.markdown(
                f"""
                <div class="planeta">
                    {icon_html}<h3>Planeta Português</h3>
                    Leitura, interpretação e gramática.<br><br>
                    🔓 Desbloqueado
                </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button("🚀 Entrar", key="entrar_portugues", use_container_width=True):
                if som_nave_b64:
                    st.markdown(f'<audio autoplay src="data:audio/wav;base64,{som_nave_b64}"></audio>', unsafe_allow_html=True)
                st.session_state.planeta = "portugues"
                st.session_state.missao_ativa = False
                st.session_state.questao_atual = None
                st.session_state.ultimo_feedback = None
                st.rerun()

        with p3:
            icon_html = f'<img src="{img_mochila_b64}" style="height: 50px; vertical-align: middle; margin-right: 8px;">' if img_mochila_b64 else "🎒 "
            st.markdown(
                f"""
                <div class="planeta" style="border-color: #4cc9f0;">
                    {icon_html}<h3>Mochila de Loja</h3>
                    Troque suas moedas por recompensas na sala!<br><br>
                    🪙 Loja Aberta
                </div>
            """,
                unsafe_allow_html=True,
            )
            if st.button("🎒 Abrir Mochila", key="entrar_mochila", use_container_width=True):
                if som_comando_b64:
                    st.markdown(f'<audio autoplay src="data:audio/wav;base64,{som_comando_b64}"></audio>', unsafe_allow_html=True)
                st.session_state.planeta = "mochila"
                st.session_state.missao_ativa = False
                st.session_state.questao_atual = None
                st.session_state.ultimo_feedback = None
                st.rerun()

    # TELA DA MOCHILA
    elif st.session_state.planeta == "mochila":
        if st.button("⬅ Voltar aos Planetas", key="voltar_mochila", use_container_width=True):
            if som_nave_b64:
                st.markdown(f'<audio autoplay src="data:audio/wav;base64,{som_nave_b64}"></audio>', unsafe_allow_html=True)
            st.session_state.planeta = None
            st.rerun()
            
        exibir_mochila_aluno()

    # PLANETA MATEMÁTICA
    elif st.session_state.planeta == "matematica":
        st.header("🪐 Planeta Matemática")

        if st.button("⬅ Voltar aos Planetas", key="voltar_planetas", use_container_width=True):
            if som_nave_b64:
                st.markdown(f'<audio autoplay src="data:audio/wav;base64,{som_nave_b64}"></audio>', unsafe_allow_html=True)
            st.session_state.planeta = None
            st.session_state.missao_ativa = False
            st.session_state.questao_atual = None
            st.session_state.ultimo_feedback = None
            st.session_state.xp_ganho = 0
            st.rerun()

        if not st.session_state.missao_ativa:
            exibir_robo("Pronto para encarar os desafios matemáticos? Clique no botão abaixo para iniciar!", "pensativo")
            if st.button("🚀 Iniciar Missão Matemática", key="iniciar_matematica", use_container_width=True):
                if som_nave_b64:
                    st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{som_nave_b64}"></audio>', unsafe_allow_html=True)
                st.session_state.missao_ativa = True
                st.session_state.xp_ganho = 0
                st.session_state.ultimo_feedback = None
                if questoes_matematica:
                    st.session_state.questao_atual = random.choice(questoes_matematica)
                rain(emoji="🚀", font_size=45, falling_speed=5, animation_length="medium")
                st.rerun()

        if st.session_state.missao_ativa:
            if not questoes_matematica:
                st.error("❌ Nenhuma questão de Matemática foi encontrada.")
            else:
                if st.session_state.questao_atual is None:
                    st.session_state.questao_atual = random.choice(questoes_matematica)

                questao = st.session_state.questao_atual
                col_pergunta, col_mascote = st.columns([2.2, 1], gap="medium")

                with col_pergunta:
                    st.markdown(
                        f"""
                        <div class="card">
                            <h3>🎯 Habilidade BNCC: {questao['habilidade']}</h3>
                            <p style="font-size:20px;">{questao['pergunta']}</p>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )

                    resposta = st.radio(
                        "Escolha a alternativa correta:",
                        questao["alternativas"],
                        key=f"mat_{questao['id']}",
                    )

                    col_resp, col_prox = st.columns(2)
                    with col_resp:
                        if st.button("✅ Responder", key=f"resp_mat_{questao['id']}", use_container_width=True):
                            if som_robo_b64:
                                st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{som_robo_b64}"></audio>', unsafe_allow_html=True)

                            if resposta == questao["resposta"]:
                                xp_questao = int(questao["xp"])
                                st.session_state.xp_ganho += xp_questao

                                alunos.at[idx_aluno, "XP"] = int(alunos.at[idx_aluno, "XP"]) + xp_questao
                                novos_xp = int(alunos.at[idx_aluno, "XP"])
                                alunos.at[idx_aluno, "Nivel"] = (novos_xp // 100) + 1
                                salvar_alunos(alunos)

                                st.session_state.ultimo_feedback = {
                                    "status": "sucesso",
                                    "msg": "Sensacional! Você acertou em cheio!",
                                    "estado": "comemora"
                                }
                                st.balloons()
                            else:
                                st.session_state.ultimo_feedback = {
                                    "status": "erro",
                                    "msg": "Ops, essa resposta não está certa. Vamos tentar de novo?",
                                    "estado": "erro"
                                }

                    with col_prox:
                        if st.button("Próxima Questão ➔", key="prox_mat", use_container_width=True):
                            st.session_state.ultimo_feedback = None
                            st.session_state.questao_atual = random.choice(questoes_matematica)
                            st.rerun()

                with col_mascote:
                    if st.session_state.ultimo_feedback:
                        exibir_astrobaldo(
                            st.session_state.ultimo_feedback["msg"],
                            st.session_state.ultimo_feedback["estado"]
                        )
                    else:
                        exibir_astrobaldo("Estou de olho na sua resposta! Concentre-se e escolha com sabedoria.", "normal")

    # PLANETA PORTUGUÊS
    elif st.session_state.planeta == "portugues":
        st.header("📚 Planeta Português")

        if st.button("⬅ Voltar aos Planetas", key="voltar_planetas_portugues", use_container_width=True):
            if som_nave_b64:
                st.markdown(f'<audio autoplay src="data:audio/wav;base64,{som_nave_b64}"></audio>', unsafe_allow_html=True)
            st.session_state.planeta = None
            st.session_state.missao_ativa = False
            st.session_state.questao_atual = None
            st.session_state.ultimo_feedback = None
            st.session_state.xp_ganho = 0
            st.rerun()

        if not st.session_state.missao_ativa:
            exibir_robo("Pronto para encarar os desafios de Português? Clique no botão abaixo para iniciar!", "pensativo")
            if st.button("🚀 Iniciar Missão Português", key="iniciar_portugues", use_container_width=True):
                if som_nave_b64:
                    st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{som_nave_b64}"></audio>', unsafe_allow_html=True)
                st.session_state.missao_ativa = True
                st.session_state.xp_ganho = 0
                st.session_state.ultimo_feedback = None
                if questoes_portugues:
                    st.session_state.questao_atual = random.choice(questoes_portugues)
                rain(emoji="🚀", font_size=45, falling_speed=5, animation_length="medium")
                st.rerun()

        if st.session_state.missao_ativa:
            if not questoes_portugues:
                st.error("❌ Nenhuma questão de Português foi encontrada.")
            else:
                if st.session_state.questao_atual is None:
                    st.session_state.questao_atual = random.choice(questoes_portugues)

                questao = st.session_state.questao_atual
                col_pergunta, col_mascote = st.columns([2.2, 1], gap="medium")

                with col_pergunta:
                    st.markdown(
                        f"""
                        <div class="card">
                            <h3>🎯 Habilidade BNCC: {questao['habilidade']}</h3>
                            <p style="font-size:20px;">{questao['pergunta']}</p>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )

                    resposta = st.radio(
                        "Escolha a alternativa correta:",
                        questao["alternativas"],
                        key=f"port_{questao['id']}",
                    )

                    col_resp, col_prox = st.columns(2)
                    with col_resp:
                        if st.button("✅ Responder", key=f"resp_port_{questao['id']}", use_container_width=True):
                            if som_robo_b64:
                                st.markdown(f'<audio autoplay src="data:audio/mp3;base64,{som_robo_b64}"></audio>', unsafe_allow_html=True)

                            if resposta == questao["resposta"]:
                                xp_questao = int(questao["xp"])
                                st.session_state.xp_ganho += xp_questao

                                alunos.at[idx_aluno, "XP"] = int(alunos.at[idx_aluno, "XP"]) + xp_questao
                                novos_xp = int(alunos.at[idx_aluno, "XP"])
                                alunos.at[idx_aluno, "Nivel"] = (novos_xp // 100) + 1
                                salvar_alunos(alunos)

                                st.session_state.ultimo_feedback = {
                                    "status": "sucesso",
                                    "msg": "Sensacional! Você acertou em cheio!",
                                    "estado": "comemora"
                                }
                                st.balloons()
                            else:
                                st.session_state.ultimo_feedback = {
                                    "status": "erro",
                                    "msg": "Ops, essa resposta não está certa. Vamos tentar de novo?",
                                    "estado": "erro"
                                }

                    with col_prox:
                        if st.button("Próxima Questão ➔", key="prox_port", use_container_width=True):
                            st.session_state.ultimo_feedback = None
                            st.session_state.questao_atual = random.choice(questoes_portugues)
                            st.rerun()

                with col_mascote:
                    if st.session_state.ultimo_feedback:
                        exibir_astrobaldo(
                            st.session_state.ultimo_feedback["msg"],
                            st.session_state.ultimo_feedback["estado"]
                        )
                    else:
                        exibir_astrobaldo("Estou de olho na sua resposta! Concentre-se e escolha com sabedoria.", "normal")