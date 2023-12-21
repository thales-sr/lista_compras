import streamlit as st
import database
import pandas as pd

st.title('Lista de compras')

with st.expander('Cadastro'):
    with st.form('Cadastro itens', clear_on_submit=True):
        item = st.text_input('Item')
        comentario = st.text_input('Comentário')
        submitted = st.form_submit_button('Cadastrar item')
        
        if submitted:
            database.inserir(item, comentario)
    
dados = database.retorna_dados()

df_dados = pd.DataFrame(dados)
df_dados = df_dados[['comprado', 'key', 'comentario']]

dados_editados = st.data_editor(df_dados)

# st.write(dados_editados.to_dict(orient='records'))

atualizar = st.button('Atualizar dados')
if atualizar:
    for index, value in dados_editados.iterrows():
        database.inserir(item = value['key'], comentario = value['comentario'], comprado = value['comprado'])