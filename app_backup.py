import streamlit as st
import pandas as pd

# Configuração
st.set_page_config(
    page_title="EduMetrics Quest",
    page_icon="🚀",
    layout="wide"
)

# Carregar alunos
@st.cache_data
def carregar_alunos():
    return pd.read_csv("dados/alunos.csv")


alunos = carregar_alunos()


# Título
st.title("🚀 EduMetrics Quest")

st.subheader("Jornada de Aprendizagem - Ensino Fundamental I")


st.write(
    """
    Uma plataforma gamificada baseada nas habilidades da BNCC,
    preparada para desenvolver competências do SAEB e SARESP.
    """
)


st.divider()


st.header("Escolha seu perfil")


col1, col2 = st.columns(2)


with col1:

    st.subheader("👨‍🎓 Aluno")

    st.write(
        """
        Entre na sua jornada de desafios,
        conquiste XP e desenvolva habilidades.
        """
    )


    if st.button("🎮 Entrar como aluno"):

        st.session_state.modo = "aluno"


with col2:

    st.subheader("👨‍🏫 Professor")

    st.write(
        """
        Acompanhe sua turma,
        habilidades e evolução.
        """
    )


    if st.button("📊 Entrar como professor"):

        st.session_state.modo = "professor"



# Área do aluno

if st.session_state.get("modo") == "aluno":

    st.divider()

    st.header("🎮 Área do Aluno")


    nome = st.selectbox(
        "Escolha seu nome:",
        alunos["Nome"]
    )


    aluno = alunos[alunos["Nome"] == nome].iloc[0]


    st.success(f"Bem-vindo, {nome}! 🚀")


    col1, col2 = st.columns(2)


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


    st.subheader("📚 Sua primeira missão")


    st.info(
        """
        Desafio Matemático

        Habilidade:
        EF05MA07

        Resolver problemas envolvendo adição e subtração.
        """
    )


    if st.button("🚀 Iniciar desafio"):

        st.success(
            "Missão iniciada! Em breve teremos os desafios."
        )