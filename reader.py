# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:45:55 2018

@author: tiago
"""
import json #json é um dicionario do python
import random

file=open("dados.json","r") #Abre arquivo...

json_data = file.read() #le arquivo texto... string...

file.close()



data_d = json.loads(json_data) #converte o texto (string) para dicionario

data_d['coisa']=random.randint(1,1000) #adiciona um item no dicionario
data_d['dados'].append(random.randint(1,1000))

print(data_d) #exibe o dicionario





file=open("dados.json","w") #grava arquivo...

file.write(json.dumps(data_d))

file.close()