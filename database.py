from deta import Deta

DETA_KEY = 'e05tk7pvmwm_oYyv95xX692hVNP2J9L4rEBYH1YsncWm'

deta = Deta(DETA_KEY)

db = deta.Base('lista_compras')

def inserir(item, comentario, comprado = False):
    return db.put({'key': item, 'comentario': comentario, 'comprado': comprado})

def retorna_dados():
    res = db.fetch()
    return res.items