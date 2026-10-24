import streamlit as st


def carregar_css():
    st.markdown(
        """
        <style>

        /* =====================================================
           EDU METRICS QUEST
           IDENTIDADE VISUAL
           ===================================================== */


        /* =====================================================
           FONTE
           ===================================================== */

        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');


        html,
        body,
        [class*="css"],
        .stApp {

            font-family:
                'Nunito',
                Arial,
                Helvetica,
                sans-serif !important;

        }

/* =====================================================
           FUNDO ESPACIAL E ELEMENTOS FLUTUANTES
           ===================================================== */

        .stApp {
            background:
                radial-gradient(
                    circle at 15% 20%,
                    rgba(80, 80, 255, 0.18),
                    transparent 20%
                ),
                radial-gradient(
                    circle at 85% 15%,
                    rgba(0, 220, 255, 0.12),
                    transparent 18%
                ),
                radial-gradient(
                    circle at 50% 90%,
                    rgba(120, 40, 255, 0.12),
                    transparent 25%
                ),
                linear-gradient(
                    135deg,
                    #02051C 0%,
                    #07133A 45%,
                    #062B55 100%
                );
            background-attachment: fixed;
            min-height: 100vh;
        }

        /* Container do cenário fixo */
        .space-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
        }

        /* Planeta distante (pequeno e desfocado) */
        .planet-fundo {
            position: absolute;
            top: 15%;
            left: 8%;
            font-size: 50px;
            filter: blur(1px);
            opacity: 0.6;
        }

        /* Planeta no plano intermediário */
        .planet-medio {
            position: absolute;
            top: 60%;
            right: 10%;
            font-size: 80px;
            opacity: 0.85;
        }

        /* Planeta em primeiro plano */
        .planet-frente {
            position: absolute;
            bottom: -30px;
            left: -20px;
            font-size: 130px;
            opacity: 0.9;
        }

        /* Estilização da Nave Espacial */
        .spaceship {
            position: absolute;
            top: 25%;
            right: 8%;
            width: 110px;
            height: auto;
            z-index: 2;
            animation: flutuarNave 4s ease-in-out infinite alternate;
        }

        /* Animação de flutuação suave da nave */
        @keyframes flutuarNave {
            0% {
                transform: translateY(0px) rotate(0deg);
            }
            50% {
                transform: translateY(-12px) rotate(-3deg);
            }
            100% {
                transform: translateY(-25px) rotate(2deg);
            }
        }

        /* =====================================================
           TEXTOS
           ===================================================== */

        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        p,
        label,
        span {

            font-family:
                'Nunito',
                Arial,
                Helvetica,
                sans-serif !important;

        }


        h1,
        h2,
        h3,
        h4,
        h5,
        h6 {

            color: #FFFFFF !important;

            font-weight: 800 !important;

        }


        p,
        label {

            color: #F4F7FF !important;

            font-weight: 600;

        }


        /* =====================================================
           TÍTULOS DO STREAMLIT
           ===================================================== */

        [data-testid="stMarkdownContainer"] h1,
        [data-testid="stMarkdownContainer"] h2,
        [data-testid="stMarkdownContainer"] h3,
        [data-testid="stMarkdownContainer"] h4 {

            color: #FFFFFF !important;

        }


        /* =====================================================
           CARDS DOS PLANETAS
           ===================================================== */

        .planeta {

            background:
                linear-gradient(
                    145deg,
                    rgba(92, 45, 190, 0.72),
                    rgba(27, 45, 140, 0.72)
                );

            border:
                2px solid rgba(151, 91, 255, 0.85);

            border-radius: 24px;

            padding: 28px;

            margin-bottom: 16px;

            text-align: center;

            box-shadow:
                0 0 18px rgba(112, 58, 255, 0.30),
                0 12px 35px rgba(0, 0, 0, 0.35);

            backdrop-filter: blur(10px);

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;

        }


        .planeta:hover {

            transform: translateY(-4px);

            box-shadow:
                0 0 28px rgba(145, 82, 255, 0.55),
                0 18px 40px rgba(0, 0, 0, 0.40);

        }


        .planeta h3 {

            color: #FFFFFF !important;

            font-size: 24px;

            font-weight: 900 !important;

        }


        /* =====================================================
           CARTÃO DE MISSÃO
           ===================================================== */

        .missao {

            background:
                linear-gradient(
                    145deg,
                    rgba(20, 35, 100, 0.85),
                    rgba(15, 20, 70, 0.85)
                );

            border:
                1px solid rgba(75, 210, 255, 0.35);

            border-radius: 22px;

            padding: 25px;

            margin-top: 20px;

            margin-bottom: 20px;

            box-shadow:
                0 0 20px rgba(0, 180, 255, 0.15),
                0 10px 30px rgba(0, 0, 0, 0.35);

            backdrop-filter: blur(10px);

        }


        /* =====================================================
           XP
           ===================================================== */

        .xp {

            background:
                linear-gradient(
                    135deg,
                    #FFD21C,
                    #FF9D00
                );

            color: #111936 !important;

            padding: 10px 20px;

            border-radius: 18px;

            font-weight: 900;

            display: inline-block;

            box-shadow:
                0 0 15px rgba(255, 190, 0, 0.35);

        }


        /* =====================================================
           CABEÇALHO DO EXPLORADOR
           ===================================================== */

        .cabecalho-quest {

            background:
                linear-gradient(
                    135deg,
                    rgba(5, 15, 55, 0.92),
                    rgba(12, 35, 85, 0.82)
                );

            border:
                1px solid rgba(45, 120, 255, 0.35);

            border-radius: 24px;

            padding: 20px 24px;

            margin-bottom: 20px;

            box-shadow:
                0 8px 30px rgba(0, 0, 0, 0.30);

        }


        /* =====================================================
           LOGO
           ===================================================== */

        .logo-quest {

            font-size: 30px;

            font-weight: 900;

            line-height: 1.0;

            color: #FFFFFF;

        }


        .logo-quest .azul {

            color: #72D9FF;

        }


        .logo-quest .amarelo {

            color: #FFD21C;

        }


        .subtitulo-quest {

            color: #D9E8FF;

            font-size: 14px;

            font-weight: 600;

            margin-top: 6px;

        }


        /* =====================================================
           XP E NÍVEL
           ===================================================== */

        .status-quest {

            background:
                rgba(8, 20, 65, 0.85);

            border:
                1px solid rgba(60, 120, 255, 0.35);

            border-radius: 18px;

            padding: 10px 16px;

            text-align: center;

        }


        .status-icone {

            font-size: 25px;

        }


        .status-titulo {

            color: #BFD4FF;

            font-size: 12px;

            font-weight: 700;

        }


        .status-valor {

            color: #FFFFFF;

            font-size: 22px;

            font-weight: 900;

        }


        /* =====================================================
           AVATAR
           ===================================================== */

        .avatar-quest {

            width: 70px;

            height: 70px;

            border-radius: 50%;

            display: flex;

            align-items: center;

            justify-content: center;

            margin: auto;

            background:
                linear-gradient(
                    135deg,
                    #24D7FF,
                    #2878FF
                );

            border:
                3px solid #24D7FF;

            box-shadow:
                0 0 18px rgba(36, 215, 255, 0.45);

            font-size: 42px;

        }


        /* =====================================================
           BOAS-VINDAS
           ===================================================== */

        .boas-vindas {

            background:
                linear-gradient(
                    90deg,
                    rgba(21, 93, 145, 0.55),
                    rgba(18, 67, 110, 0.40)
                );

            border:
                1px solid rgba(50, 180, 255, 0.20);

            border-radius: 15px;

            padding: 12px 18px;

            margin-bottom: 18px;

            color: #FFFFFF;

            font-weight: 700;

        }


        /* =====================================================
           PROGRESSO
           ===================================================== */

        .progresso-titulo {

            color: #FFFFFF;

            font-size: 14px;

            font-weight: 800;

            margin-top: 8px;

            margin-bottom: 6px;

        }


        /* =====================================================
           BOTÕES
           ===================================================== */

        .stButton > button {

            width: 100%;

            min-height: 48px;

            border-radius: 18px;

            border: none;

            font-family:
                'Nunito',
                Arial,
                Helvetica,
                sans-serif !important;

            font-size: 17px;

            font-weight: 900;

            color: #FFFFFF !important;

            background:
                linear-gradient(
                    135deg,
                    #FF4B35,
                    #E91E63
                );

            box-shadow:
                0 6px 15px rgba(0, 0, 0, 0.25);

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease;

        }


        .stButton > button:hover {

            transform:
                translateY(-2px) scale(1.01);

            box-shadow:
                0 10px 24px rgba(0, 0, 0, 0.35);

        }


        .stButton > button:active {

            transform: scale(0.98);

        }


        /* =====================================================
           CAMPOS DE SELEÇÃO
           ===================================================== */

        .stSelectbox label {

            color: #FFFFFF !important;

            font-weight: 800 !important;

        }


        .stSelectbox > div > div {

            border-radius: 14px;

            background:
                rgba(255, 255, 255, 0.96);

        }


        /* =====================================================
           RADIO BUTTONS
           ===================================================== */

        .stRadio label {

            color: #FFFFFF !important;

            font-weight: 700 !important;

        }


        /* =====================================================
           MÉTRICAS
           ===================================================== */

        [data-testid="stMetricLabel"] {

            color: #FFFFFF !important;

            font-family:
                'Nunito',
                Arial,
                Helvetica,
                sans-serif !important;

            font-weight: 800 !important;

        }


        [data-testid="stMetricValue"] {

            color: #FFFFFF !important;

            font-family:
                'Nunito',
                Arial,
                Helvetica,
                sans-serif !important;

            font-weight: 900 !important;

        }


        /* =====================================================
           BARRA DE PROGRESSO
           ===================================================== */

        [data-testid="stProgressBar"] > div {

            background:
                rgba(255, 255, 255, 0.15);

            border-radius: 20px;

        }


        [data-testid="stProgressBar"] > div > div {

            background:
                linear-gradient(
                    90deg,
                    #FFD21C,
                    #FF9D00
                );

            border-radius: 20px;

        }


        /* =====================================================
           ESCONDER ELEMENTOS PADRÃO
           ===================================================== */

        #MainMenu {

            visibility: hidden;

        }


        footer {

            visibility: hidden;

        }


        header {

            visibility: hidden;

        }


        /* =====================================================
           BARRA SUPERIOR DO STREAMLIT
           ===================================================== */

        [data-testid="stHeader"] {

            background: transparent;

        }
/* =====================================================
           ESTILOS PARA A NAVE ESPACIAL E ROBÔ COM IMAGENS PNG
           ===================================================== */

        /* NAVE ESPACIAL */
        .spaceship {
            position: fixed !important;
            top: 10% !important;
            right: 5% !important;
            width: 340px !important;
            max-width: 340px !important;
            height: auto !important;
            z-index: 9999 !important;
            pointer-events: none;
            filter: drop-shadow(0px 0px 25px rgba(0, 220, 255, 0.7)) !important;
            animation: viajarNave 14s ease-in-out infinite alternate !important;
        }

        .spaceship img {
            width: 100% !important;
            height: auto !important;
        }

        /* ROBÔ AVATAR */
        .robo-avatar {
            width: 220px !important;
            height: auto !important;
            display: inline-block;
            animation: flutuarRobo 4s ease-in-out infinite alternate !important;
        }

        .robo-avatar img {
            width: 100% !important;
            max-width: none !important;
            height: auto !important;
            filter: drop-shadow(0px 0px 30px rgba(0, 220, 255, 0.8)) !important;
            transition: transform 0.3s ease;
        }

        .robo-avatar img:hover {
            transform: scale(1.1) rotate(4deg);
        }

       /* BALÃO DE FALA ESTILO QUADRINHOS (HQ) */
        .robo-balao-fala, .robo-mensagem, [class*="robo-texto"] {
            position: relative !important;
            background: #FFFFFF !important; /* Fundo branco estilo HQ */
            color: #1E293B !important; /* Texto escuro e legível */
            border: 3px solid #0F172A !important; /* Borda preta marcada de quadrinho */
            border-radius: 20px !important;
            padding: 14px 18px !important;
            font-weight: 700 !important;
            font-size: 1.05rem !important;
            line-height: 1.4 !important;
            box-shadow: 4px 4px 0px #00D2FF, 6px 6px 15px rgba(0, 0, 0, 0.4) !important; /* Sombra estilo pop-art */
            margin-left: 20px !important; /* Espaço para a ponta não encostar no robô */
            display: inline-block !important;
            z-index: 10 !important;
        }

        /* PONTA DO BALÃO DE FALA (TRIÂNGULO APONTANDO PARA A ESQUERDA / ROBÔ) */
        .robo-balao-fala::before, .robo-mensagem::before, [class*="robo-texto"]::before {
            content: '' !important;
            position: absolute !important;
            top: 50% !important; /* Centraliza a ponta na altura do balão */
            left: -15px !important; /* Posiciona na borda esquerda */
            transform: translateY(-50%) !important;
            border-width: 10px 15px 10px 0 !important;
            border-style: solid !important;
            border-color: transparent #0F172A transparent transparent !important; /* Borda externa da ponta */
            display: block !important;
            width: 0 !important;
        }

        .robo-balao-fala::after, .robo-mensagem::after, [class*="robo-texto"]::after {
            content: '' !important;
            position: absolute !important;
            top: 50% !important;
            left: -10px !important;
            transform: translateY(-50%) !important;
            border-width: 8px 12px 8px 0 !important;
            border-style: solid !important;
            border-color: transparent #FFFFFF transparent transparent !important; /* Preenchimento branco da ponta */
            display: block !important;
            width: 0 !important;
        }

        /* ANIMAÇÃO DA NAVE */
        @keyframes viajarNave {
            0% {
                transform: translate(0px, 0px) rotate(0deg);
            }
            25% {
                transform: translate(-150px, 40px) rotate(-4deg);
            }
            50% {
                transform: translate(-280px, -30px) rotate(3deg);
            }
            75% {
                transform: translate(-120px, 80px) rotate(-2deg);
            }
            100% {
                transform: translate(20px, -20px) rotate(4deg);
            }
        }

        /* ANIMAÇÃO DE FLUTUAÇÃO DO ROBÔ */
        @keyframes flutuarRobo {
            0% {
                transform: translateY(0px) rotate(0deg);
            }
            50% {
                transform: translateY(-12px) rotate(2deg);
            }
            100% {
                transform: translateY(6px) rotate(-1deg);
            }
        }

        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
    """
    <style>
        /* ... outros estilos que você já tem no arquivo ... */

/* ==========================================
           BOTÕES ESTILO HQ (EFEITO DE CLIQUE 3D)
           ========================================== */

        div.stButton > button, 
        .stDownloadButton > button,
        button[kind="primary"], 
        button[kind="secondary"],
        div.stButton > button *,
        .stDownloadButton > button *,
        button[kind="primary"] *,
        button[kind="secondary"] * {
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
        }

        div.stButton > button, 
        .stDownloadButton > button,
        button[kind="primary"], 
        button[kind="secondary"] {
            background: #FFFFFF !important;
            font-weight: 800 !important;
            font-size: 1.05rem !important;
            border: 3px solid #0F172A !important;
            border-radius: 20px !important;
            padding: 12px 24px !important;
            box-shadow: 4px 4px 0px #00D2FF, 6px 6px 15px rgba(0, 0, 0, 0.4) !important;
            transition: all 0.1s ease-in-out !important;
            cursor: pointer !important;
        }

        div.stButton > button:hover,
        .stDownloadButton > button:hover,
        div.stButton > button:hover *,
        .stDownloadButton > button:hover * {
            background: #F8FAFC !important;
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
            border-color: #0F172A !important;
        }

        div.stButton > button:hover,
        .stDownloadButton > button:hover {
            transform: translate(-2px, -2px) !important;
            box-shadow: 6px 6px 0px #00D2FF, 8px 8px 18px rgba(0, 0, 0, 0.5) !important;
        }

        div.stButton > button:active,
        .stDownloadButton > button:active,
        div.stButton > button:active *,
        .stDownloadButton > button:active * {
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
        }

        div.stButton > button:active,
        .stDownloadButton > button:active {
            transform: translate(4px, 4px) !important;
            box-shadow: 0px 0px 0px transparent !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)