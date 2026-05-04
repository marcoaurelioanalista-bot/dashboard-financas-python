%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configurações Iniciais
st.set_page_config(page_title="Finanças Pro", layout="wide", page_icon="💰")

# Custom CSS para melhorar o visual
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. Dados Fictícios (Simulando um Banco de Dados)
df = pd.DataFrame({
    'Data': pd.date_range(start='2023-01-01', periods=12, freq='M'),
    'Receita': [5000, 5200, 4800, 6000, 6500, 7000, 6800, 7200, 8000, 8500, 9000, 9500],
    'Despesas': [3000, 3100, 2900, 3200, 3500, 4000, 3800, 4100, 4300, 4500, 4700, 4900]
})
df['Lucro'] = df['Receita'] - df['Despesas']

# 3. Sidebar (Filtros - Recrutadores amam interatividade)
st.sidebar.header("⚙️ Filtros do Dashboard")
mes_selecionado = st.sidebar.select_slider("Selecione o período", options=df['Data'].dt.strftime('%b/%y'))

# 4. Cabeçalho
st.title("🚀 Business Intelligence Dashboard")
st.subheader("Análise de Performance Mensal")

# 5. Métricas Principais (Cards)
col1, col2, col3 = st.columns(3)
receita_total = df['Receita'].sum()
lucro_total = df['Lucro'].sum()
margem = (lucro_total / receita_total) * 100

col1.metric("Receita Acumulada", f"R$ {receita_total:,.2f}", "+8%")
col2.metric("Lucro Líquido", f"R$ {lucro_total:,.2f}", "+12%")
col3.metric("Margem de Lucro", f"{margem:.1f}%", "稳定")

# 6. Gráficos Interativos
st.markdown("### 📈 Tendências Financeiras")
c1, c2 = st.columns([2, 1])

with c1:
    fig_linha = px.line(df, x='Data', y=['Receita', 'Despesas'], 
                        title="Evolução Mensal", template="plotly_white",
                        color_discrete_map={"Receita": "#00d1b2", "Despesas": "#ff3860"})
    st.plotly_chart(fig_linha, use_container_width=True)

with c2:
    fig_pizza = px.pie(values=[receita_total, lucro_total], names=['Custos', 'Lucro'],
                       title="Distribuição de Valor", hole=0.5,
                       color_discrete_sequence=["#f1f3f5", "#007bff"])
    st.plotly_chart(fig_pizza, use_container_width=True)

# 7. Tabela de Dados (Mostra que você entende de estruturação)
with st.expander("📂 Visualizar dados brutos"):
    st.dataframe(df.style.format({'Receita': 'R$ {:.2f}', 'Despesas': 'R$ {:.2f}', 'Lucro': 'R$ {:.2f}'}))
