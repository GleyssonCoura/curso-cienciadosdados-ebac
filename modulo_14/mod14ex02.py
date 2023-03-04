import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

sns.set()  

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).unstack().plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None

print ('Quantidade de argumentos:', len(sys.argv), 'argumentos.')
print ('Lista de argumentos:', sys.argv)

for i in range(0,len(sys.argv)):
    print ('Argumento '+str(i)+' sys.argv['+str(i)+']:', sys.argv[i])

for i in range(1,len(sys.argv)):
    sinasc = pd.read_csv('SINASC_RO_2019_'+sys.argv[i]+'.csv')  #Arquivo dos dados

    max_data = sinasc.DTNASC.max()[:7]
    print(max_data)

    os.makedirs('./ImagensTarefa02/'+max_data, exist_ok=True)

    plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'mean', 'média idade mãe por data', 'data nascimento')
    plt.savefig('./ImagensTarefa02/'+max_data+'/media idade mae por data.png')

    plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae','data de nascimento','unstack')
    plt.savefig('./ImagensTarefa02/'+max_data+'/media idade mae por sexo.png')

    plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')
    plt.savefig('./ImagensTarefa02/'+max_data+'/media peso bebe por sexo.png')

    plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'PESO mediano','escolaridade mae','sort')
    plt.savefig('./ImagensTarefa02/'+max_data+'/PESO mediano por escolaridade mae.png')

    plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')
    plt.savefig('./ImagensTarefa02/'+max_data+'/media apgar1 por gestacao.png')