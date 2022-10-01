import numpy as np
import pandas as pd


df = pd.read_csv("MV_Faults_v2.csv", sep=";") #Arquivo CSV com as informações
# print(df) #Print do arquivo CSV completo
df = df.to_numpy() #transformando para array numpy
layout = df[:,:1] #todas as linhas da 1 coluna = trecho
stretch = df[:,1:2] #todas as linhas da 2 coluna = tamanho
phases = df[:,2:3] #todas as linhas da 3 coluna = fases
#trecho = df
n_trechos = int(len(df)/3)
n_falhas = len(df[1,:])


sep_trecho = np.split(df, n_trechos) # Separando o dataframe por trecho com as 3 fases


