##Autor bl4c4lv##
##Fecha: 01/05/2021##
#Script para obtener los correos comprometidos de la cooperativa#
#Para correr el exploit, debemos obtener el csrf y cookie de firefox monitor#
#Hay dos métodos disponibles la opción p va a have i been pwned y cualquier otra opción va a firefox monitor#

import hashlib
import sys
import requests
import time
import json

def pwned():
    if __name__ == "__main__":
        f = open("usuarios.txt")
        s = open("cuentasFiltradas.txt",'a')
        for linea in f:
            texto = "@dominio.com"
            correo = linea.rstrip('\n') + texto
            print(correo)
            consumirWSGet(correo,s)
        f.close()
        s.close()

def firefox(type):
    if __name__ == "__main__":
        f = open("usuarios.txt")
        s = open("cuentasFiltradas.txt",'a')
        for linea in f:
            texto = "@dominio.com"
            correo = linea.rstrip('\n') + texto
            print(correo)
            consumirWSPost("hX1df9vx-nCrticG9-fBttEb1-WEBkiPGaew", encrypt(correo,type),correo,s) #aquì va el csrf
        f.close()
        s.close()

def encrypt(text, type):
    key = hashlib.sha1(text.encode())
    return key.hexdigest()

def consumirWSGet(correo,archivo):
    url = 'https://haveibeenpwned.com/unifiedsearch/' + correo
    cabecera = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'es-ES,es;q=0.9', 
    'Connection': 'keep-alive', 'DNT': '1', 'Sec-GPC': '1', 'TE': 'Trailers',
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    time.sleep(2)
    solicitud = requests.get(url, headers = cabecera)
    print(solicitud.status_code)
    if solicitud.status_code == 200:
        obtenRespuestaPwned(solicitud.text,correo,archivo)

def consumirWSPost(csrf,hash,correo,archivo):
    url = 'https://monitor.firefox.com/scan'
    cookies = {'connect.sid' : 's:CEI8WSaIJ_VHJ-Url79hAUOoBkkfIOg8.v64CADgJyVaAq3ktBhqLZc5UhaBMCiIKER11SaQjUbQ', 'vpnBannerDismissed' : 'true'} #, 'ga':'GA1.3.1252200155.1620401849', 'gid':'GA1.3.1533905843.1620401849', 'gat':'1'
    cabecera = {'Content-type': 'application/x-www-form-urlencoded', 'Origin' : 'https://monitor.firefox.com', 'Referer': 'https://monitor.firefox.com/', 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Connection' : 'keep-alive', 'Content-Length': '128', 'Upgrade-Insecure-Requests': '1', 'DNT' : '1'}
    datos = {'_csrf':csrf, 'pageToken':'', 'scannedEmailId':'1', 'email':'', 'emailHash':hash}
    time.sleep(5)
    solicitud = requests.post(url, headers = cabecera, data = datos, cookies = cookies)
    print(solicitud.status_code)
    if solicitud.status_code == 200:
        obtenRespuestaFirefox(solicitud.text,correo,archivo)

def obtenRespuestaPwned(text,correo,archivo):
    jsonResp = json.loads(text)
    for (k,v) in jsonResp.items():
        for (key,value) in v[0].items():
            if key in ('Name','BreachDate','DataClasses'):
                print(correo+" ==> "+key+" ==> "+str(value)+"\n")
                archivo.write(correo+" ==> "+key+" ==> "+str(value)+"\n")
        archivo.write("\n")
        print('\n')        

def obtenRespuestaFirefox(text,correo,archivo):
    inicio = text.find("Esta dirección de correo aparece en")
    resultado = text[inicio:inicio+100].replace('Esta dirección de correo aparece en <span class="bold">','').replace('</span>','').replace('</h2>','')
    print(int(resultado[0:1]))
    if int(resultado[0:1])>0:
        archivo.write(correo+'  ==>  '+resultado+'\n')



while True:
    if sys.argv[1] == 'p':
        print("aki")
        print(pwned())
    else:
        print("aca")
        print(firefox('sha1'))
