import streamlit as st
import time
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente

st.markdown("<h1 style='text-align: center; color: white;'>Cadastro de pessoas</h1>", unsafe_allow_html=True)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://wallpapercave.com/wp/wp3493594.png");
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Nome:", placeholder="Digite seu nome aqui...")
    input_pw = st.text_input(label="Senha:", type="password", max_chars=10, placeholder="Digite sua senha aqui...")
    input_age = st.number_input(label="Idade:", step=1, min_value=1)
    input_occupation = st.selectbox(label="Profissão:", options=["Garçom", "Advogado", "Médico", "Analista de Sistemas", "Designer", "Músico", "Dentista", "Veterinário", "Segurança","Motorista", "Professor" ])
    input_button_submit = st.form_submit_button("Enviar")
    info = st.checkbox("Concordo com os termos de cadastro")

if info:
    st.write()
else:
    st.warning("Você precisa concordar com os termos para continuar")
    st.stop()

if input_button_submit:
    if input_name == "":
        st.warning("Informe um nome válido!",icon="⚠️")
        st.stop()
    if input_pw == "":
        st.warning("Digite uma senha!", icon="⚠️")
        st.stop()
    else:
         cliente.nome = input_name
         cliente.idade = input_age
         cliente.profissao = input_occupation
         cliente.senha = input_pw

         ClienteController.Incluir(cliente)

         with st.spinner('Aguarde...'):
                time.sleep(3)
                st.success("Cadastro realizado com sucesso!", icon="✅")