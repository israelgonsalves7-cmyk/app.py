import sqlite3
import streamlit as st

# Configuração inicial da página
st.set_page_config(
    page_title="Jornada Dev: Python, SQL & HTML",
    page_icon="💻",
    layout="wide",
)

st.title("💻 Jornada Dev: Aprenda do Zero")
st.write(
    "Aprenda a teoria e pratique **Python**, **SQL** e **HTML** em um só lugar."
)

# Menu Lateral para Navegação
modulo = st.sidebar.radio(
    "Escolha o Módulo:", ["1. Python Básico", "2. Banco de Dados com SQL", "3. Estrutura Web com HTML"]
)

# ---------------------------------------------------------
# MÓDULO 1: PYTHON BÁSICO
# ---------------------------------------------------------
if modulo == "1. Python Básico":
    st.header("🐍 Módulo 1: Python Básico")

    st.subheader("📚 Teoria")
    st.markdown(
        """
    **O que é Python?**  
    Python é uma linguagem de programação simples e poderosa. Ela usa **variáveis** para armazenar dados e **estruturas condicionais** para tomar decisões.

    * **Variáveis:** Guardam informações (ex: `nome = "Maria"`, `idade = 25`).
    * **Condicionais (`if/else`):** Executam blocos de código com base em uma condição.
    """
    )

    st.subheader("🛠️ Prática Interativa")
    st.write("Teste o funcionamento de uma estrutura condicional em Python:")

    nome = st.text_input("Digite seu nome:", "Dev")
    idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, value=18)

    if st.button("Executar Código Python"):
        st.code(
            f"""
# Código executado:
nome = "{nome}"
idade = {idade}

if idade >= 18:
    print(f"Olá {{nome}}, você é maior de idade!")
else:
    print(f"Olá {{nome}}, você é menor de idade.")
        """,
            language="python",
        )

        if idade >= 18:
            st.success(f"Olá {nome}, você é maior de idade!")
        else:
            st.info(f"Olá {nome}, você é menor de idade.")

# ---------------------------------------------------------
# MÓDULO 2: BANCO DE DADOS COM SQL
# ---------------------------------------------------------
elif modulo == "2. Banco de Dados com SQL":
    st.header("🗄️ Módulo 2: Banco de Dados com SQL")

    st.subheader("📚 Teoria")
    st.markdown(
        """
    **O que é SQL?**  
    SQL (Structured Query Language) é a linguagemusada para se comunicar com bancos de dados relacionais.

    * **CREATE TABLE:** Cria uma tabela para guardar dados.
    * **INSERT INTO:** Insere registros na tabela.
    * **SELECT:** Consulta e filtra os dados salvos.
    """
    )

    st.subheader("🛠️ Prática Interativa")
    st.write("Execute comandos SQL em um banco de dados SQLite temporário:")

    # Criar banco SQLite em memória
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nome TEXT, cargo TEXT)"
    )
    cursor.execute(
        "INSERT INTO usuarios (nome, cargo) VALUES ('Ana', 'Desenvolvedora'), ('Carlos', 'Designer')"
    )
    conn.commit()

    novo_nome = st.text_input("Nome do novo usuário:", "Beatriz")
    novo_cargo = st.text_input("Cargo do novo usuário:", "Analista de Dados")

    if st.button("Inserir e Consultar (SQL)"):
        cursor.execute(
            "INSERT INTO usuarios (nome, cargo) VALUES (?, ?)",
            (novo_nome, novo_cargo),
        )
        conn.commit()

        st.code(
            f"""
-- Comando executado:
INSERT INTO usuarios (nome, cargo) VALUES ('{novo_nome}', '{novo_cargo}');
SELECT * FROM usuarios;
        """,
            language="sql",
        )

        # Exibir resultado da consulta
        res = cursor.execute("SELECT * FROM usuarios").fetchall()
        st.write("**Resultado da Tabela `usuarios`:**")
        st.dataframe(res, column_config={"0": "ID", "1": "Nome", "2": "Cargo"})

# ---------------------------------------------------------
# MÓDULO 3: ESTRUTURA WEB COM HTML
# ---------------------------------------------------------
elif modulo == "3. Estrutura Web com HTML":
    st.header("🌐 Módulo 3: Estrutura Web com HTML")

    st.subheader("📚 Teoria")
    st.markdown(
        """
    **O que é HTML?**  
    HTML (HyperText Markup Language) é a linguagem de marcação usada para estruturar páginas web através de **tags**.

    * `<h1>`: Título principal.
    * `<p>`: Parágrafo de texto.
    * `<button>`: Botão clicável.
    """
    )

    st.subheader("🛠️ Prática Interativa")
    st.write("Edite o código HTML abaixo e veja a renderização em tempo real:")

    codigo_html_padrao = """<div style='padding: 15px; border: 2px solid #4CAF50; border-radius: 8px;'>
  <h2 style='color: #4CAF50;'>Meu Primeiros Passos no HTML</h2>
  <p>Este é um parágrafo estilizado dentro do Streamlit.</p>

</div>"""

    codigo_usuario = st.text_area("Código HTML:", value=codigo_html_padrao, height=150)

    st.subheader("Resultado Renderizado:")
    st.components.v1.html(codigo_usuario, height=200)
