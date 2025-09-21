import streamlit as st

st.title("Minha Primeira Aplicação Streamlit!")
st.header("Uma jornada para surpreender o mercado.")
st.write("Olá comunidade! Estamos começando.")

if st.button("Clique em mim!"):
	st.balloons()
	st.success("Você está no caminho certo!")
