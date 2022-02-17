import os, time
from pathlib import Path
import mysql.connector
import shutil

list_id = list()

def connect():
    com = mysql.connector.connect(host='localhost',database='crachas',user='root',password='', port='3307')
    return com
def view():
    lista = []
    connection = connect()
    cursor = connection.cursor()
    #cursor.select_db('crachas')
    select_requests = "select *from app_servidor;"
    cursor.execute(select_requests)

    request = cursor.fetchall()

    for requests in request:
        view_dict = {'id': requests[0], 'nome':requests[1], 'cpf': requests[2], 'imagem':requests[3] }
        lista.append(view_dict)

    print(lista)
    if lista:
        rename_image(lista)
    else:
        time.sleep(300)
        view()

def rename_image(lista):

    for i in range(len(lista)):
        id = lista[i]['id']   
        cpf = lista[i]['cpf']
        imagem = lista[i]['imagem']
        imagem = imagem[8:]  #pega o nome da foto
        
        addrees =Path(r'C:\Users\Administrador\Desktop\cracha\crachas-hucf-django\imagens')
        new_addrees = Path(r'C:\Users\Administrador\Desktop\cracha\crachas-hucf-django\imagens_renomeadas')
        cpf = '{}.jpg'.format(cpf)
        
        old_name = os.path.join(addrees, imagem) #busco a imagem na pasta nao renomeada 
        new_file = os.path.join(new_addrees, imagem) # preparo para copiar a img pro novo diretorio 
        
        if not os.path.isfile(new_file): #verifico se o dir é existente na maquina 
            if os.path.isfile(old_name):
                shutil.copy(old_name,new_file) #copio o arquivo para a nova pasta mas nao renomeio
                new_name = os.path.join(new_addrees, cpf)  # preparo para renomear o arquivo com o cpf do user
            
                if not os.path.isfile(new_name): #verifico se o arquivo nao existente na pasta 
                    os.rename(new_file, new_name) # renomeio o arquivo 
                    #os.remove(new_file)
                else: 
                    os.remove(new_file) # apago a img antiga no dir deixando so a img docpf
            else:
                print("Arquivo inexistente na pasta {} -- {} -- {}".format(cpf,imagem, id))
        else:
            os.remove(new_file)
        
    time.sleep(300)
    view()

view()