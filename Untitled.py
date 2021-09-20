#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importação das bibliotecas que serão utilizadas
import pandas as pd  
import datetime      
import numpy as np   
import plotly.graph_objects as go


# In[2]:


Q = pd.read_csv(r'C:\Users\Pedro Henrique\OneDrive\Área de Trabalho\UnB\PROGRAMAÇÃO\bases de dados\MGB-IPH_DischargeData_AmazonBasin.txt', delimiter="\s+",engine='python',header=None)
ti='1998-01-01'  # atribui a variavel ti o a data inicial da pesquisa.
tf='2009-12-31'  # atribui a variavel tf o a data final da pesquisa.
date = pd.date_range(start=ti, end=tf, freq='D')  # Cria uma lista com as datas.
Q['date'] = date # Nomeia a coluna das datas.
Q.set_index('date', inplace=True)  # adiciona a lista de datas nos dados das vazões.


# In[3]:


Q # vizualização dos dados


# In[8]:


np_array = Q.to_numpy()  # pega os dados e coloca em um array.
media = 0                # inicia a variavel média.
maior_que_media = 0      # inicia a variavel maior_que_media que armazena a quant. de dias de vazão acima da média.
menor_que_media = 0      # inicia a variavel menor_que_media que armazena a quant. de dias de vazão abaixo da média.
rio = int(input("digite o rio que deseja analisar ")) # variavel rio que recebe um int. do usuario.
for i in range(4383):    # laço de repetição utilizado para percorrer as colunas e calcular a media.
    media += np_array[i][rio]  # armazena a soma na variavel media das vazões de cada coluna.
media = media/4383             # pega a soma e divide pelo total de dias resultando na media.
for i in range(4383):          # laço de repetição para percorrer as colunas e separar os dias das vazões acima e abaixo da média.
    if np_array[i][rio]> media: # condicional para separar os dias de vazão acima da média.
        maior_que_media += 1    # armazena a quantidade de dias que a vazão foi maior que média.
    elif np_array[i][rio]<media: # condicional para separar os dias de vazão abaixo da média.
        menor_que_media +=1      # armazena a quantidade de dias que a vazão foi menor que média.

 

labels = ['Acima da média','Abaixo da média']  # subtítulos do gráfico.
values = [maior_que_media, menor_que_media,]   # armazena na variável values a lista dos valores obtidos.

 

night_colors = ['rgb(0,255,127)', 'rgb(0,191,255)'] # altera as cores do gráfico de pizza de acordo com os parâmetros.

 

fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker_colors=night_colors)]) # armazena na variável fig a configuração do gráfico.
fig.update_layout(                                                         # atualiza o layout do gráfico.
    title_text="Dias em que a vazão foi menor ou maior que a média total", # adiciona título.
    annotations=[dict(text='DVMMM', x=0.5, y=0.5, font_size=20, showarrow=False)]) # adiciona a sigla DVMMM no meio do gráfico. 
fig.update_traces(hole=.4, hoverinfo="label+percent+name")  # configura o tamanho da circunferência no interior do gráfico.
fig.show()  # inicia a plotagem.

        
        


# In[ ]:




