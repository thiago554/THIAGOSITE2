import streamlit as st

# =========================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================
st.set_page_config(
    page_title="Empresas Parceiras",
    page_icon="🌐",
    layout="wide"
)

# =========================================
# TÍTULO
# =========================================
st.title("🌎 Empresas Parceiras")
st.write("Confira algumas empresas incríveis abaixo.")

# =========================================
# COLUNAS
# =========================================
col1, col2, col3 = st.columns(3)

# =========================================
# EMPRESA 1
# =========================================
with col1:
    st.image("Palmeiras.png", use_container_width=True)
    st.subheader("Palmeiras")
    st.write("Empresa de tecnologia espacial fundada por Abel ferreira.")
    st.link_button(
        "Acessar Site",
        "https://www.palmeiras.com"
    )

# =========================================
# EMPRESA 2
# =========================================
with col2:
    st.image("Flamengo.png", use_container_width=True)
    st.subheader("Flamengo")
    st.write("Empresa mundialmente conhecida por jogar muito.")
    st.link_button(
        "Acessar Site",
        "https://www.flamengo.com"
    )

# =========================================
# EMPRESA 3
# =========================================
with col3:
    st.image("Remo.png", use_container_width=True)
    st.subheader("Remo")
    st.write("Time em ascenção.")
    st.link_button(
        "Acessar Site",
        "https://clubedoremo.com.br/"
    )

# =========================================
# RODAPÉ
# =========================================
st.write("---")
st.write("Desenvolvido por Thiago Paulino")
