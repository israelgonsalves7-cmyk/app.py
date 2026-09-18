import sqlite3
import pandas as pd
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Dev Diário: Aprenda na Prática", page_icon="📅", layout="wide"
)

st.title("📅 Dev Diário: Um Desafio Prático Por Dia")
st.caption(
    "Aprenda Python, SQL e HTML sem teoria longa — resolva o desafio e veja o resultado na hora!"
)

# Inicializar progresso do usuário no session_state
if "dias_concluidos" not in st.session_state:
    st.session_state.dias_concluidos = set()

# Barra lateral para seleção do dia
dias_disponiveis = [f"Dia {i}" for i in range(1, 6)]
dia_selecionado = st.sidebar.selectbox("Escolha o Dia:", dias_disponiveis)

# Barra de Progresso
progresso = len(st.session_state.dias_concluidos) / len(dias_disponiveis)
st.sidebar.markdown("---")
st.sidebar.write(f"**Seu Progresso:** {len(st.session_state.dias_concluidos)}/5 Dias")
st.sidebar.progress(progresso)

# =========================================================
# DIA 1: PYTHON - CONCATENAÇÃO DE STRINGS
# =========================================================
if dia_selecionado == "Dia 1":
    st.header("🐍 Dia 1: Criador de Mensagens Automáticas (Python)")
    st.markdown(
        "**Objetivo Prático:** Crie uma função que receba o nome de um cliente e o status do pedido, retornando uma mensagem formatada."
    )

    col1, col2 = st.columns(2)
    with col1:
        nome_cliente = st.text_input("Nome do Cliente:", "Carlos")
        status_pedido = st.selectbox(
            "Status do Pedido:", ["Enviado", "Processando", "Entregue"]
        )

    with col2:
        st.write("**Desafio:**")
        st.code(
            """
# Complete o código montando a string formatada:
def gerar_mensagem(nome, status):
    return f"Olá {nome}, seu pedido está: {status}!"
""",
            language="python",
        )

    if st.button("Executar Código do Dia 1"):
        mensagem = f"Olá {nome_cliente}, seu pedido está: {status_pedido}!"
        st.success(f"**Resultado do seu código:** {mensagem}")
        st.session_state.dias_concluidos.add("Dia 1")

# =========================================================
# DIA 2: SQL - FILTRAGEM COM WHERE
# =========================================================
elif dia_selecionado == "Dia 2":
    st.header("🗄️ Dia 2: Filtrando Produtos em Promoção (SQL)")
    st.markdown(
        "**Objetivo Prático:** Escreva uma consulta SQL para listar apenas os produtos com preço menor que o limite definido."
    )

    # Configuração do Banco de Dados
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE produtos (id INT, nome TEXT, preco REAL, categoria TEXT)"
    )
    cursor.execute(
        """INSERT INTO produtos VALUES 
        (1, 'Teclado Mecânico', 250.0, 'Periféricos'),
        (2, 'Mouse Gamer', 120.0, 'Periféricos'),
        (3, 'Monitor 24', 850.0, 'Monitores'),
        (4, 'Mousepad XL', 60.0, 'Acessórios')"""
    )
    conn.commit()

    preco_max = st.slider("Selecione o preço máximo desejado:", 50, 900, 200, 10)

    query = f"SELECT nome, preco, categoria FROM produtos WHERE preco <= {preco_max} ORDER BY preco ASC;"
    st.code(query, language="sql")

    df = pd.read_sql_query(query, conn)
    st.write("**Resultado da Consulta:**")
    st.dataframe(df, use_container_width=True)

    if not df.empty:
        st.session_state.dias_concluidos.add("Dia 2")

# =========================================================
# DIA 3: HTML/CSS - CRIAÇÃO DE UM CARD DE PRODUTO
# =========================================================
elif dia_selecionado == "Dia 3":
    st.header("🌐 Dia 3: Construindo um Componente de Interface (HTML/CSS)")
    st.markdown(
        "**Objetivo Prático:** Altere os valores de CSS no código abaixo para personalizar o visual do cartão de compras."
    )

    cor_fundo = st.color_picker("Escolha a cor do botão:", "#28a745")
    titulo_prod = st.text_input("Nome do Produto:", "Fone Bluetooth Pro")

    codigo_html = f"""
    <div style="border: 1px solid #ddd; padding: 20px; border-radius: 12px; max-width: 300px; font-family: sans-serif; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
        <h3 style="margin-top: 0; color: #333;">{titulo_prod}</h3>
        <p style="color: #666; font-size: 14px;">Som de alta fidelidade com cancelamento de ruído.</p>
        <p style="font-weight: bold; color: #111; font-size: 18px;">R$ 299,00</p>
        <button style="background-color: {cor_fundo}; color: white; border: none; padding: 10px 15px; border-radius: 6px; cursor: pointer; width: 100%;">
            Comprar Agora
        </button>
    </div>
    """

    st.code(codigo_html, language="html")
    st.subheader("Visualização em Tempo Real:")
    st.components.v1.html(codigo_html, height=230)

    st.session_state.dias_concluidos.add("Dia 3")

# =========================================================
# DIA 4: PYTHON - ESTRUTURAS DE REPETIÇÃO (FOR LOOP)
# =========================================================
elif dia_selecionado == "Dia 4":
    st.header("🐍 Dia 4: Automação com Loops (Python)")
    st.markdown(
        "**Objetivo Prático:** Aplique um desconto automático em uma lista de preços utilizando o laço `for`."
    )

    desconto = st.slider("Desconto (%):", 5, 50, 10)
    precos_originais = [100.0, 250.0, 400.0, 50.0]

    precos_com_desconto = [p * (1 - desconto / 100) for p in precos_originais]

    st.code(
        f"""
precos = {precos_originais}
desconto = {desconto / 100}

# Aplicando o desconto em cada item:
precos_finais = [p * (1 - desconto) for p in precos]
""",
        language="python",
    )

    df_precos = pd.DataFrame(
        {"Preço Original (R$)": precos_originais, "Preço Final (R$)": precos_com_desconto}
    )

    st.table(df_precos)
    st.session_state.dias_concluidos.add("Dia 4")

# =========================================================
# DIA 5: SQL - AGREGAÇÃO DE DADOS (SUM & GROUP BY)
# =========================================================
elif dia_selecionado == "Dia 5":
    st.header("🗄️ Dia 5: Relatório Financeiro (SQL)")
    st.markdown(
        "**Objetivo Prático:** Agrupe as vendas por vendedor para calcular o total faturado por cada um."
    )

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE vendas (id INT, vendedor TEXT, valor REAL)")
    cursor.execute(
        """INSERT INTO vendas VALUES 
        (1, 'Ana', 1500.0), (2, 'Carlos', 2300.0), 
        (3, 'Ana', 800.0), (4, 'Carlos', 1200.0), (5, 'Beatriz', 3100.0)"""
    )
    conn.commit()

    query = """SELECT vendedor, SUM(valor) AS total_vendas 
FROM vendas 
GROUP BY vendedor 
ORDER BY total_vendas DESC;"""

    st.code(query, language="sql")

    df_vendas = pd.read_sql_query(query, conn)
    st.dataframe(df_vendas, use_container_width=True)

    st.session_state.dias_concluidos.add("Dia 5")
