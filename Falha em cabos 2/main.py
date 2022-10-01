import extract as ext
import data as fault

import matplotlib.pyplot as plt


trecho = ext.sep_trecho


#print(trecho[0][1,3:]) #trecho[trecho_desejado][fase_desejada,a partir da 3 coluna

for i in range(ext.n_trechos):

    dim_ph_a = len([x for x in trecho[i][0,3:] if x == x])    # numero de falhas na fase A
    dim_ph_b = len([x for x in trecho[i][1,3:] if x == x])    # numero de falhas na fase B
    dim_ph_c = len([x for x in trecho[i][2,3:] if x == x])    # numero de falhas na fase C
    dim_total = dim_ph_a + dim_ph_b + dim_ph_c
    # Transformando caracter '-' em valor 0 -> Tratar erros de digitação
    for j in range(ext.n_falhas): # varrer todas as falhas
        for x in range(3): # varrer as 3 fases
            if trecho[i][x,j] == "-":
                trecho[i][x,j] = float('nan')
            x=x+1 
    
    ph_a = [int(x) for x in trecho[i][0, 3:] if x == x] # Para retirar o 'nan' do array e transforar em list com valores inteiros (e não char)
    ph_b = [int(x) for x in trecho[i][1, 3:] if x == x] # Para retirar o 'nan' do array e transforar em list com valores inteiros (e não char)
    ph_c = [int(x) for x in trecho[i][2, 3:] if x == x] # Para retirar o 'nan' do array e transforar em list com valores inteiros (e não char)
    dim_ph = len(ph_a)+len(ph_b)+len(ph_c)
    
    # Ordem crescente das falhas
    ph_a.sort()
    ph_b.sort()
    ph_c.sort()
    
    falha = fault.Fault()
    falha.configFault(trecho[i][0,0], trecho[i][0,1])
    falha.phaseFault(ph_a, ph_b, ph_c) 
    falha.nFaults(dim_total, dim_ph)
    falha.plotFault()
    
plt.show()