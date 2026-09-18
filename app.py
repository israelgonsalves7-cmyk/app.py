import sqlite3
import pandas as pd
import streamlit as st

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Academy Dev: Python, SQL & HTML",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🚀 Academy Dev: Do Básico ao Avançado")
st.caption(
    "Aprenda conceitos fundamentais, intermediários e avançados de Python, SQL e HTML com teoria e prática interativa."
)

# =========================================================
# MENU LATERAL
# =========================================================
tecnologia = st.sidebar.selectbox(
    "1. Escolha a Tecnologia:", ["🐍 Python", "🗄️ SQL", "🌐 HTML & CSS"]
)

nivel = st.sidebar.radio(
    "2. Escolha o Nível:", ["🟢 Básico", "🟡 Intermediário", "🔴 Avançado"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 **Dica:** Altere os parâmetros nos testes práticos para ver os resultados mudando em tempo real!"
)

# =========================================================
# SEÇÃO 1: PYTHON
# =========================================================
if tecnologia == "🐍 Python":
    st.header(f"🐍 Python — Nível {nivel.split(' ')[1]}")

    if nivel == "🟢 Básico":
        st.subheader("📚 Teoria: Tipos de Dados e Controle de Fluxo")
        st.markdown(
            """
        * **Variáveis:** Guardam valores na memória (`x = 10`, `nome = 'Ana'`).
        * **Tipos Básicos:** `int` (inteiros), `float` (decimais), `str` (texto), `bool` (`True`/`False`).
        * **Estrutura Condicional (`if/elif/else`):** Permite que o programa tome decisões com base em condições.
        """
        )

        st.subheader("🛠️ Prática: Calculadora de IMC")
        peso = st.number_input("Peso (kg):", min_value=1.0, value=70.0, step=0.5)
        altura = st.number_input(
            "Altura (m):", min_value=0.5, max_value=2.5, value=1.75, step=0.01
        )

        if st.button("Calcular IMC"):
            imc = peso / (altura**2)
            st.code(
                f"""
peso = {peso}
altura = {altura}
imc = peso / (altura ** 2)

if imc < 18.5:
    status = "Abaixo do peso"
elif imc < 25:
    status = "Peso normal"
else:
    status = "Sobrepeso"
            """,
                language="python",
            )

            if imc < 18.5:
                st.warning(f"Seu IMC é **{imc:.2f}**: Abaixo do peso.")
            elif imc < 25:
                st.success(f"Seu IMC é **{imc:.2f}**: Peso normal.")
            else:
                st.error(f"Seu IMC é **{imc:.2f}**: Sobrepeso.")

    elif nivel == "🟡 Intermediário":
        st.subheader(
            "📚 Teoria: Funções, Manipulação de Listas e Dicionários"
        )
        st.markdown(
            """
        * **Listas (`list`):** Coleções ordenadas e mutáveis de itens (`[1, 2, 3]`).
        * **Dicionários (`dict`):** Coleções de pares `chave: valor` (`{"nome": "Ana", "idade": 25}`).
        * **List Comprehension:** Forma concisa de criar listas (`[x**2 for x in lista]`).
        * **Funções (`def`):** Blocos de código reutilizáveis que podem receber parâmetros e retornar valores.
        """
        )

        st.subheader("🛠️ Prática: Processamento e Filtragem de Dados")
        numeros_texto = st.text_input(
            "Digite números separados por vírgula:", "10, 15, 20, 25, 30, 35, 40"
        )
        fator_multiplicador = st.slider("Multiplicador:", 1, 10, 2)

        try:
            numeros = [
                float(n.strip())
                for n in numeros_texto.split(",")
                if n.strip() != ""
            ]

            if st.button("Processar Dados"):
                multiplicados = [n * fator_multiplicador for n in numeros]
                pares = [n for n in multiplicados if n % 2 == 0]

                st.code(
                    f"""
numeros = {numeros}
multiplicados = [n * {fator_multiplicador} for n in numeros]
pares = [n for n in multiplicados if n % 2 == 0]
                """,
                    language="python",
                )

                st.write("**Lista Multiplicada:**", multiplicados)
                st.write("**Apenas os Números Pares:**", pares)
        except ValueError:
            st.error("Por favor, insira apenas números válidos separados por vírgula.")

    elif nivel == "🔴 Avançado":
        st.subheader(
            "📚 Teoria: Programação Orientada a Objetos (POO) & Decoradores"
        )
        st.markdown(
            """
        * **Classes e Objetos:** Moldes para criar estruturas complexas com atributos e métodos.
        * **Encapsulamento e Propriedades:** Proteção e controle sobre como os dados de um objeto são alterados.
        * **Decoradores (`@`):** Funções que modificam o comportamento de outras funções sem alterar seu código interno.
        """
        )

        st.subheader("🛠️ Prática: Simulação de Conta Bancária (POO)")

        # Exemplo de classe
        class ContaBancaria:

            def __init__(self, titular, saldo_inicial=100.0):
                self.titular = titular
                self._saldo = saldo_inicial  # Atributo "protegido"

            def depositar(self, valor):
                if valor > 0:
                    self._saldo += valor
                    return True
                return False

            def sacar(self, valor):
                if 0 < valor <= self._saldo:
                    self._saldo -= valor
                    return True
                return False

            @property
            def saldo(self):
                return self._saldo

        st.code(
            """
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=100.0):
        self.titular = titular
        self._saldo = saldo_inicial
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        return False

    @property
    def saldo(self):
        return self._saldo
        """,
            language="python",
        )

        titular_nome = st.text_input("Nome do Titular:", "Dev Avançado")
        deposito_val = st.number_input("Valor de Depósito:", min_value=10.0, value=50.0)

        if "conta" not in st.session_state:
            st.session_state.conta = ContaBancaria(titular_nome)

        if st.button("Realizar Depósito"):
            st.session_state.conta.depositar(deposito_val)
            st.success(
                f"Depósito realizado! Saldo atual de {st.session_state.conta.titular}: R$ {st.session_state.conta.saldo:.2f}"
            )


# =========================================================
# SEÇÃO 2: SQL
# =========================================================
elif tecnologia == "🗄️ SQL":
    st.header(f"🗄️ SQL — Nível {nivel.split(' ')[1]}")

    # Criação do banco em memória acessível em todas as sessões do nível
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # População do banco relacional
    cursor.execute(
        "CREATE TABLE departamentos (id INTEGER PRIMARY KEY, nome TEXT)"
    )
    cursor.execute(
        "INSERT INTO departamentos VALUES (1, 'Tecnologia'), (2, 'Vendas'), (3, 'Marketing')"
    )

    cursor.execute(
        "CREATE TABLE funcionarios (id INTEGER PRIMARY KEY, nome TEXT, salario REAL, dept_id INTEGER)"
    )
    cursor.execute(
        "INSERT INTO funcionarios VALUES (1, 'Ana', 7500, 1), (2, 'Carlos', 4500, 2), (3, 'Beatriz', 8200, 1), (4, 'João', 3900, 3), (5, 'Mariana', 6000, 2)"
    )
    conn.commit()

    if nivel == "🟢 Básico":
        st.subheader("📚 Teoria: Comandos `SELECT`, `WHERE` e `ORDER BY`")
        st.markdown(
            """
        * **`SELECT`**: Especifica quais colunas você quer buscar.
        * **`FROM`**: Especifica a tabela de origem.
        * **`WHERE`**: Filtra as linhas com base em condições especificadas.
        * **`ORDER BY`**: Ordena os resultados de forma crescente (`ASC`) ou decrescente (`DESC`).
        """
        )

        st.subheader("🛠️ Prática: Consulta Básica com Filtro")
        salario_min = st.slider("Filtrar funcionários com salário maior que:", 3000, 9000, 5000, 500)

        query = f"SELECT id, nome, salario FROM funcionarios WHERE salario > {salario_min} ORDER BY salario DESC"
        st.code(query, language="sql")

        df = pd.read_sql_query(query, conn)
        st.dataframe(df, use_container_width=True)

    elif nivel == "🟡 Intermediário":
        st.subheader("📚 Teoria: Junções (`JOIN`) e Agregações (`GROUP BY`)")
        st.markdown(
            """
        * **`INNER JOIN`**: Combina linhas de duas ou mais tabelas quando há correspondência entre chaves.
        * **Funções de Agregação**: `SUM()`, `AVG()`, `COUNT()`, `MAX()`, `MIN()`.
        * **`GROUP BY`**: Agrupa os registros com base em uma ou mais colunas para realizar cálculos agregados.
        """
        )

        st.subheader("🛠️ Prática: Relatório de Salários por Departamento")
        query = """
SELECT 
    d.nome AS Departamento,
    COUNT(f.id) AS Total_Funcionarios,
    ROUND(AVG(f.salario), 2) AS Salario_Medio,
    SUM(f.salario) AS Custo_Total
FROM funcionarios f
INNER JOIN departamentos d ON f.dept_id = d.id
GROUP BY d.nome
ORDER BY Salario_Medio DESC;
        """
        st.code(query, language="sql")

        df = pd.read_sql_query(query, conn)
        st.dataframe(df, use_container_width=True)

    elif nivel == "🔴 Avançado":
        st.subheader("📚 Teoria: Subconsultas e Window Functions (`OVER / PARTITION BY`)")
        st.markdown(
            """
        * **Subqueries:** Consultas aninhadas dentro de uma consulta principal.
        * **Window Functions:** Realizam cálculos através de um conjunto de linhas relativas à linha atual sem agrupar as linhas em uma única saída (diferente do `GROUP BY`).
        * **`RANK()` / `DENSE_RANK()`**: Atribui um ranking numérico a cada linha dentro de uma partição.
        """
        )

        st.subheader("🛠️ Prática: Ranking de Salários Dentro do Departamento")
        query = """
SELECT 
    f.nome AS Funcionario,
    f.salario AS Salario,
    d.nome AS Departamento,
    DENSE_RANK() OVER (PARTITION BY f.dept_id ORDER BY f.salario DESC) AS Rank_No_Depto
FROM funcionarios f
INNER JOIN departamentos d ON f.dept_id = d.id;
        """
        st.code(query, language="sql")

        df = pd.read_sql_query(query, conn)
        st.dataframe(df, use_container_width=True)


# =========================================================
# SEÇÃO 3: HTML & CSS
# =========================================================
elif tecnologia == "🌐 HTML & CSS":
    st.header(f"🌐 HTML & CSS — Nível {nivel.split(' ')[1]}")

    if nivel == "🟢 Básico":
        st.subheader("📚 Teoria: Estrutura Semântica e Tags Fundamentais")
        st.markdown(
            """
        * **Tags de Cabeçalho (`<h1>` a `<h6>`):** Definem a hierarquia dos títulos da página.
        * **Parágrafos (`<p>`):** Blocos de texto estruturados.
        * **Links (`<a>`):** Criam hiperlinks para navegação (`href="url"`).
        * **Listas (`<ul>`, `<ol>`, `<li>`):** Listas ordenadas e não ordenadas.
        """
        )

        html_basico = """<div>
  <h1>Meu Primeiro Título</h1>
  <p>Este é um parágrafo que demonstra a estrutura semântica básica do HTML.</p>
  <ul>
    <li>Item da lista 1</li>
    <li>Item da lista 2</li>
  </ul>
  <a href="https://streamlit.io" target="_blank">Link para o Streamlit</a>
</div>"""

        codigo_html = st.text_area("Edite o código HTML abaixo:", value=html_basico, height=200)

        st.subheader("Resultado Renderizado:")
        st.components.v1.html(codigo_html, height=200)

    elif nivel == "🟡 Intermediário":
        st.subheader("📚 Teoria: Estilização com CSS Inline/Block e Formulários")
        st.markdown(
            """
        * **Formulários (`<form>`, `<input>`, `<button>`):** Capturam dados do usuário no front-end.
        * **Propriedades CSS Básicas:** `color`, `background-color`, `padding`, `margin`, `border-radius`.
        * **Estilização com CSS:** Melhora a experiência visual e torna os componentes interativos.
        """
        )

        html_intermediario = """<form style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; font-family: sans-serif;">
  <h3 style="color: #0e1117; margin-top: 0;">Formulário de Contato</h3>
  
  <label for="nome" style="color: #31333F;">Nome:</label><br>
  <input type="text" id="nome" style="width: 100%; padding: 8px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px;"><br>
  
  <label for="email" style="color: #31333F;">E-mail:</label><br>
  <input type="email" id="email" style="width: 100%; padding: 8px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px;"><br><br>
  
  <button type="button" style="background-color: #ff4b4b; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">
    Enviar Dados
  </button>
</form>"""

        codigo_html = st.text_area("Edite o código HTML/CSS abaixo:", value=html_intermediario, height=250)

        st.subheader("Resultado Renderizado:")
        st.components.v1.html(codigo_html, height=260)

    elif nivel == "🔴 Avançado":
        st.subheader("📚 Teoria: Layouts Modernos com CSS Flexbox")
        st.markdown(
            """
        * **CSS Flexbox (`display: flex`):** Sistema unidimensional para alinhar e distribuir espaço entre itens em um contêiner.
        * **`justify-content`**: Controla o alinhamento no eixo principal (ex: `space-between`, `center`).
        * **`align-items`**: Controla o alinhamento no eixo cruzado (ex: `center`, `flex-start`).
        * **Design Responsivo:** Criação de interfaces flexíveis que adaptam seu layout para telas móveis ou desktop.
        """
        )

        html_avancado = """<div style="display: flex; justify-content: space-between; gap: 15px; font-family: sans-serif;">
  <div style="flex: 1; background: #e1f5fe; padding: 15px; border-radius: 8px; border-left: 5px solid #0288d1;">
    <h4 style="margin: 0; color: #01579b;">Cartão 1</h4>
    <p style="color: #0277bd; font-size: 14px;">Utilizando Flexbox para alinhar os elementos lado a lado.</p>
  </div>
  
  <div style="flex: 1; background: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 5px solid #388e3c;">
    <h4 style="margin: 0; color: #1b5e20;">Cartão 2</h4>
    <p style="color: #2e7d32; font-size: 14px;">Cada cartão ocupa um espaço proporcional da tela (`flex: 1`).</p>
  </div>
  
  <div style="flex: 1; background: #fff3e0; padding: 15px; border-radius: 8px; border-left: 5px solid #f57c00;">
    <h4 style="margin: 0; color: #e65100;">Cartão 3</h4>
    <p style="color: #ef6c00; font-size: 14px;">Completamente responsivo e dinâmico.</p>
  </div>
</div>"""

        codigo_html = st.text_area("Edite o layout Flexbox abaixo:", value=html_avancado, height=250)

        st.subheader("Resultado Renderizado:")
        st.components.v1.html(codigo_html, height=200)
