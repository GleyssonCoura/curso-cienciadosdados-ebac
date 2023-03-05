import streamlit as st
import pandas as pd
import numpy as np

#Código 1
st.set_page_config(page_title = 'Exercício 15',
                    page_icon='data:image/png;base64,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',
                    layout='wide')

st.header("Exercício do Módulo 15")

st.subheader("Utilizando três formas de visualização de dataframes")
# Código 2
st.write("Primeira forma: printando o objeto do tipo dataframe")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

# Código 3
st.write("Segunda forma: usando o método write do streamlit")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# Código 4
st.write("Terceira forma: usando o método dataframe do streamlit")
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.dataframe(dataframe)

st.write('---')
st.subheader("Visualização de outras funcionalidades")

# Código 5
st.write('Conhecendo os sliders')
x = st.slider('x') 
st.write(x, 'squared is', x * x)

# Código 6
st.write('Conhecendo a caixa de seleção')
option = st.selectbox(
    'Selecione um número:',
     dataframe['second column'])

#Código 7
st.write('Outras funcionalidades')
left_column, right_column = st.columns(2)
left_column.button('Clique aqui!')
with right_column:
    chosen = st.radio(
        'Chapéu Seletor - escolha sua casa de Harry Potter',
        ("Corvinal", "Grifinória", "Lufa Lufa", "Sonserina"))
    st.write(f"Sua casa é {chosen}!")

# Código 8
add_selectbox = st.sidebar.selectbox(
    'Meio de contato',
    ('Email', 'Telefone residencial', 'Celular')
)

# Código 9
add_slider = st.sidebar.slider(
    'Selecione um intervalo de valores:',
    0.0, 100.0, (25.0, 75.0)
)

st.write('---')
st.subheader("Visualizações gráficas")

# Código 10
st.write('Gráfico de linhas')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# Código 11
st.write('Gráfico de barras')
st.bar_chart(chart_data)

# Código 12
st.write('Gráfico de área')
st.area_chart(chart_data)

# Código 13
st.write('Mapa sobre São Francisco')
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

# Código 14
st.write('---')
st.write('Inserindo uma imagem')
st.image('https://www.simplilearn.com/ice9/free_resources_article_thumb/Data-Science-vs.-Big-Data-vs.jpg')

st.write('---')
st.write('Interações com o usuário')

# Código 15
color = st.color_picker('Selecione uma cor:')

# Código 16
aniversario = st.date_input('Selecione seu aniversário:')

# Código 17
hora = st.time_input('Selecione a hora de acordar:')

# Código 18
arquivo = st.file_uploader('Selecione seu arquivo:')

# Código 19
nome = st.text_input('Qual seu nome?')

# Código 20
idade = st.number_input('Qual sua idade?')