# -*- coding: UTF-8 -*-
import urllib
import json
import pprint
import sys

token = 

def writefile(nome, foto):
    arquivo = nome + '.jpg'
    try:
        f = open ('fotos/'+arquivo, 'wb')
        f.write(foto)
        f.close()
        print ("Arquivo gravado com sucesso "+arquivo)
    except:
        print ("Arquivo não foi gravado Erro: " )
        print (sys.exc_info()[0])

def getIdAmigos(token):
    url = 'https://graph.facebook.com/100000902608740?fields=friends&access_token=' + token
    resp = urllib.urlopen(url).read()
    data = json.loads(resp.decode('utf-8'))
    amigos = list()
    for amigo in data['friends']['data']:
        amigos.append(amigo['id'])
    print ('Número de amigos encontrados: '+str( len(amigos)))
    return amigos


def getProfileFoto(users):
    for user in users:
        try:
            url = 'http://graph.facebook.com/'+user+'/picture?type=large'
            foto = urllib.urlopen(url).read()
            writefile(user,foto)
        except:
            print ("Erro: " )
            print (sys.exc_info()[0])            

def getIdGarotas(amigos):
    idgarotas = list()
    for amigo in amigos:
        try:
            url = "http://graph.facebook.com/"+amigo
            resp = urllib.urlopen(url).read()
            data = json.loads(resp.decode('utf-8'))
            if (data['gender'])=='female':
                idgarotas.append(amigo)
        except:
            print ("Erro: " )
            print (sys.exc_info()[0])
    print (len(idgarotas))
    return idgarotas
        
#print(idamigos(token)[0])
getProfileFoto(getIdGarotas(getIdAmigos(token)))


