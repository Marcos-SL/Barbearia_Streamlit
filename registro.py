import streamlit as st
import time
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente

st.markdown("<h1 style='text-align: center; color: white;'>Barbearia Lorem ipsum</h1>", unsafe_allow_html=True)

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.imgur.com/UUKPWO0.jpeg");
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)


with st.form(key="include_cliente"):
    input_name = st.text_input(label="Nome: *", placeholder="Digite seu nome aqui...")
    input_number = st.text_input(label="Telefone: *",max_chars=11, placeholder="(DDD) + Número")
    input_corte = st.selectbox(label="Serviço: *", options=["Cabelo e Barba R$60,00","Barba R$20,00","Sobrancelha R$20,00","Corte de Cabelo Adulto R$45,00","Corte de Cabelo Criança R$40,00"])
    input_data = st.date_input("Data: *", format="DD/MM/YYYY")
    input_time = st.selectbox(label="Horário: *", options=["10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00","14:30", "15:00", "15:30", "16:30", "17:00", "17:30", "18:30" ])
    input_button_submit = st.form_submit_button("Enviar")
    info = st.checkbox("Lembrar dados")


if input_button_submit:
    if input_name == "":
        st.warning("Digite seu nome!",icon="⚠️")
        st.stop()
    if input_number == "":
        st.warning("Digite seu número!", icon="⚠️")
        st.stop()

    cliente.nome = input_name
    cliente.corte = input_corte
    cliente.telefone = input_number
    cliente.data = input_data
    cliente.horario = input_time

    ClienteController.Incluir(cliente)

    with st.spinner('Aguarde...'):
        time.sleep(3)
        st.success("Agendamento realizado com sucesso!", icon="✅")
        st.write(input_corte,",", input_data,"às ", input_time)
