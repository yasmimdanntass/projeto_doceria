import pickle

def insert(info, users):
  info = open(info, 'wb')
  pickle.dump(users, info)
  info.close()

def read_all(info):
  lista = {}
  try:
    arquivo = open(info, 'rb')
    lista = pickle.load(arquivo)
    arquivo.close()
  except:
    info = open(info, 'wb')
    info.close()
  return lista
