from deta import Deta
import streamlit as st

DETA_KEY = st.secrets['DETA_KEY']

deta = Deta(DETA_KEY)

db = deta.Base('lista_compras')

def inserir(item, comentario, comprado = False):
    return db.put({'key': item, 'comentario': comentario, 'comprado': comprado})

def retorna_dados():
    res = db.fetch()
    return res.items

def deleta(item):
    db.delete(item)