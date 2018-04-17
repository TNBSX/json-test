# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 17:45:55 2018

@author: tiago
"""
import json #json é um dicionario do python

json_data=open("dados.json").read() #Le arquivo texto...

data_d = json.loads(json_data) #converte o texto (string) para dicionario

data_d['coisa']=100 #adiciona um item no dicionario

print(data_d) #exibe o dicionario