import streamlit as st
import pandas as pd

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(
    page_title="EduMetrics Quest",
    page_icon="🚀",
    layout="wide"
)


# =========================
# ESTILO VISUAL
# =========================

st.markdown(
    """
    <style>

    .main {
        background: linear-gradient(
            180deg,
            #081b33,
            #123b63
        );
    }


    h1, h2, h3 {
        color: white;
    }


    p {
        color: white;
        font-size: 18px;
    }


    .card {

        background-color: rgba(255,255,255,0.12);
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.2);

    }


    .titulo {

        text-align:center;
        font-size:45px;
        font-weight:bold;
        color:#FFD700;

    }


    .subtitulo {

        text-align:center;
        font-size:22px;
        color:white;

    }


    .missao {

        background:#1f7aec;
        padding:20px;
        border-radius:20px;
        color:white;

    }


    </style>

    """,
    unsafe_allow_html=True
)



# =========================
# CARREGAR ALUNOS
# =========================

@st.cache_data
def carregar_alunos():

    return pd.read_csv(
        "dados/alunos.csv",
        encoding="utf-8"
    )


alunos = carregar_alunos()



# =========================
# CABEÇALHO
# =========================

st.markdown(
    """
    <div class="titulo">
    🚀 EduMetrics Quest
    </div>

    <div class="subtitulo">
    🌌 Uma viagem pelo universo do conhecimento
    </div>
    """,
    unsafe_allow_html=True
)


st.write("")



# =========================
# ESCOLHA DO PERFIL
# =========================


if "modo" not in st.session_state:

    st.session_state.modo = None



col1, col2 = st.columns(2)



with col1:

    st.markdown(
        """
        <div class="card">

        <h2>🧑‍🚀 Aluno</h2>

        <p>
        Entre na sua jornada espacial,
        conquiste XP e desbloqueie novos mundos.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    if st.button(
        "🚀 Entrar na aventura",
        use_container_width=True
    ):

        st.session_state.modo = "aluno"



with col2:

    st.markdown(
        """
        <div class="card">

        <h2>👨‍🏫 Professor</h2>

        <p>
        Acompanhe habilidades,
        evolução e desempenho da turma.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    if st.button(
        "📊 Área do Professor",
        use_container_width=True
    ):

        st.session_state.modo = "professor"



# =========================
# ÁREA DO ALUNO
# =========================


if st.session_state.modo == "aluno":


    st.divider()


    st.header("🪐 Perfil do Explorador")


    nome = st.selectbox(
        "Escolha seu explorador:",
        alunos["Nome"]
    )


    aluno = alunos[
        alunos["Nome"] == nome
    ].iloc[0]


    st.success(
        f"Olá, {nome}! Sua aventura começou 🚀"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "⭐ XP",
            aluno["XP"]
        )


    with col2:

        st.metric(
            "🏆 Nível",
            aluno["Nivel"]
        )


    with col3:

        st.metric(
            "🔥 Sequência",
            "1 dia"
        )



    st.divider()


    st.header("🌎 Planetas de Aprendizagem")



    p1, p2, p3 = st.columns(3)



    with p1:

        st.markdown(
            """
            <div class="card">

            <h2>🔢</h2>

            <h3>Planeta Matemática</h3>

            <p>
            Desafios dos números,
            problemas e estratégias.
            </p>

            ⭐⭐⭐☆☆

            </div>
            """,
            unsafe_allow_html=True
        )



    with p2:

        st.markdown(
            """
            <div class="card">

            <h2>📚</h2>

            <h3>Galáxia da Leitura</h3>

            <p>
            Explore histórias,
            textos e aventuras.
            </p>

            ⭐⭐⭐⭐☆

            </div>
            """,
            unsafe_allow_html=True
        )



    with p3:

        st.markdown(
            """
            <div class="card">

            <h2>🔬</h2>

            <h3>Laboratório</h3>

            <p>
            Descubra os segredos
            da ciência.
            </p>

            ⭐⭐☆☆☆

            </div>
            """,
            unsafe_allow_html=True
        )



    st.divider()


    st.header("🚀 Missão Atual")


    st.markdown(
        """
        <div class="missao">

        🪐 Missão: O Desafio dos Números

        <br><br>

        Habilidade BNCC:

        <b>EF05MA07</b>

        <br><br>

        Resolver problemas envolvendo
        diferentes estratégias matemáticas.

        </div>
        """,
        unsafe_allow_html=True
    )



    st.button(
        "🚀 Iniciar Missão",
        use_container_width=True
    )



# =========================
# ÁREA DO PROFESSOR
# =========================


if st.session_state.modo == "professor":

    st.divider()

    st.header("👨‍🏫 Área do Professor")

    st.info(
        """
        Em breve:

        📊 Análise da turma

        📈 Evolução das habilidades

        📝 Relatórios BNCC

        🎯 Indicadores SAEB/SARESP
        """
    )