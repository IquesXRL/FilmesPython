import streamlit as st
import dados

st.title("Filmes")

nome = st.text_input("Nome do filme")
ano = st.number_input("Ano",min_value=2010)
nota = st.slider("Nota do filme",min_value=0.0,max_value=10.0)

if st.button('Adicionar'):
    dados.insere_dados(nome,ano,nota)
    st.success("Filme cadastrado!")

st.header("Lista de Filmes")
filmes = dados.obter_dados()

if filmes.empty:
    st.info("Nenhum filme cadastrado.")
else:
    for index, row in filmes.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])

        col1.write(f"🎬 **{row['nome']}**")
        col2.write(row['ano'])
        col3.write(row['nota'])

        # Botão VIEW
        if col5.button("👁️ Ver", key=f"view_{row['id']}"):
            filme = dados.view_dados(row['id'])
            st.subheader("🔎 Detalhes do Filme")
            st.write(f"**ID:** {filme['id']}")
            st.write(f"**Nome:** {filme['nome']}")
            st.write(f"**Ano:** {filme['ano']}")
            st.write(f"**Nota:** {filme['nota']}")

        # Botão DELETE
        if col6.button("🗑️ Deletar", key=f"del_{row['id']}"):
            dados.deletar_dados(row['id'])
            st.success(f"Filme '{row['nome']}' deletado!")
            st.rerun()
