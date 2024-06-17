import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis de datos del Titanic")
st.image("images/titanic.jpg", width=700,)
st.sidebar.title("Opciones de la tabla")


data = pd.read_csv("titanic.csv")
st.write(f"Datos Cargados:")
grafico_principal = st.empty()
grafico_principal.write(data)

# Calcular edad maxima y edad minima 
edad_minima = int(data['Age'].min())
edad_maxima= int(data['Age'].max())

# Filtro por edad
enable_age_filter = st.sidebar.checkbox("Habilitar filtro por edad")
age_config = st.sidebar.slider('Edad Mínima', min_value=edad_minima, max_value=edad_maxima, value=edad_minima)
if enable_age_filter:
    filtered_data = data[data['Age'].fillna(-1).astype(int) == age_config]
    st.write(f"Hay {filtered_data.shape[0]} pasajeros con {age_config} años")
    grafico_principal.write(filtered_data)

#Calcula mediana de la edad
mediana = int(data['Age'].median())
st.sidebar.write(f"Mediana de las edades {mediana} años")

# Filtro por mediana de edad
enable_median_filter = st.sidebar.checkbox("Habilitar filtro por mediana de edad")
filtro_mediana = st.sidebar.radio('Filtrar por mediana de edad', ('Todos', 'Menores que la mediana', 'Mayores que la mediana'))
if enable_median_filter:
   if filtro_mediana == 'Menores que la mediana':
      menor_mediana = data[data['Age'] < mediana]
      grafico_principal.write(menor_mediana)
      st.write(f"Hay {menor_mediana.shape[0]} personas menores que {mediana} años")
   elif filtro_mediana == 'Mayores que la mediana':
      mayor_mediana = data[data['Age'] > mediana]
      grafico_principal.write(mayor_mediana)
      st.write(f"Hay {mayor_mediana.shape[0]} personas mayores que {mediana} años")
   else:
      grafico_principal.write(data)
      st.write(f"Hay {data.shape[0]} personas en total")

# Filtro por precio billete
enable_fare_filter = st.sidebar.checkbox("Habilitar filtro por precio del billete")
filtro_billete = st.sidebar.radio('Filtrar por precio Billete', ('Todos', 'Precio mas caro', 'Precio mas barato'))
precio_minimo = data['Fare'].min()
precio_maximo = data['Fare'].max()
def inflation_rate(precio):
   inflation = precio * 143.15
   return round(inflation, 2)
def pounds_to_euros(precio):
   euros = precio * 1.18
   return round(euros, 2)  
if enable_fare_filter:
   if filtro_billete == "Precio mas caro":
      grafico_principal.write(data[data['Fare'] == precio_maximo])
      st.write(f"El precio mas caro es £{precio_maximo.round(2)}")
      st.write(f"Hoy en dia sería £{inflation_rate(precio_maximo)} o {pounds_to_euros(inflation_rate(precio_maximo))}€")
      calculadora = st.checkbox("Habilitar calculadora de inflación", value=False)
      if calculadora:
         number = st.number_input("Introduzca un precio en libras", min_value=0.0, step=0.01, format="%.2f")
         st.write(f"El precio actual es £{inflation_rate(number)} o {pounds_to_euros(inflation_rate(number))}€")
   elif filtro_billete == "Precio mas barato":
      grafico_principal.write(data[data['Fare'] == precio_minimo])
      st.write(f"El precio mas barato es £{precio_minimo.round(2)}")
   else:
      grafico_principal.write(data)

# Filtro titulos
def translate_title(title):
   translations = {
      'Mr': 'Señor',
      'Mrs': 'Señora',
      'Miss': 'Señorita',
      'Master': 'Maestro',
      'Dr': 'Doctor',
      'Rev': 'Reverendo',
      'Col': 'Coronel',
      'Major': 'Mayor',
      'Mlle': 'Señorita',
      'Mme': 'Señora',
      'Sir': 'Señor',
      'Lady': 'Dama',
      'Countess': 'Condesa',
      'Don': 'Don',
      'Jonkheer': 'Jonkheer'
   }
   return translations.get(title, title)
enable_title_filter = st.sidebar.checkbox("Habilitar filtro por título")
data['Title'] = data['Name'].str.extract('([A-Za-z]+)\.', expand=False)
titles = data['Title'].unique()
filtro_titulo = st.sidebar.selectbox("Título para filtrar", titles)
if enable_title_filter:
   if filtro_titulo:
      filtered_data = data[data['Title'] == filtro_titulo]
      st.write(f"Hay {filtered_data.shape[0]} pasajeros con el título {filtro_titulo} ({translate_title(filtro_titulo)})")
      grafico_principal.write(filtered_data)
   else:
      grafico_principal.write(data)



# Gráfico de barras para mostrar el precio medio por billete por cada título
fig_mean_fare = px.bar(data.groupby('Title')['Fare'].mean().reset_index(), x='Title', y='Fare', title='Precio Medio por Billete por Título')
fig_mean_fare.update_layout(xaxis_title='Título', yaxis_title='Precio Medio del Billete')
fig_mean_fare.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5)
st.plotly_chart(fig_mean_fare)

#Configuracion de las graficas
st.sidebar.title("Configuración gráficas")
view_percentage = st.sidebar.checkbox('Mostrar porcentaje de valores nulos', value=False)
emabarked_survived = st.sidebar.checkbox('Mostrar sobrevivientes embarque', value=False, key="emabarked_survived")
sex_survived = st.sidebar.checkbox('Mostrar sobrevivientes por sexo', value=False, key="sex_survived")

# Grafica de datos y porcentaje de valores nulos 
if view_percentage: 
    y_label = "Porcentaje de valores nulos (%)"
    title = "Porcentaje de Valores Nulos por Columna"
    null = data.isnull().mean()*100
    null = null.reset_index().round(2)
    null.columns = ['Columnas', 'Porcentaje']
    y_data = 'Porcentaje'
else:
    y_label = "Cantidad de Valores Nulos"
    title = "Cantidad de Valores Nulos por Columna"
    null = data.isnull().sum().reset_index()
    null.columns = ['Columnas', 'Cantidad']
    y_data = 'Cantidad'
fig = px.bar(null, x='Columnas', y=y_data, title=title, labels={y_data: y_label})
st.plotly_chart(fig)

# Gráfica distribución de precios
st.write("Distribución de Precios de Billetes")
fig_fare = px.histogram(data, x='Fare', nbins=30, title='Distribución de Precios de Billetes', range_x=[0, precio_maximo])
fig_fare.add_vline(x=precio_minimo, line_dash="dash", line_color="blue", annotation_text="Mínimo", annotation_position="top right")
fig_fare.add_vline(x=precio_maximo, line_dash="dash", line_color="green", annotation_text="Máximo", annotation_position="top right")
fig_fare.update_layout(xaxis_title='Precio del Billete', yaxis_title='Total pasajeros', showlegend=False)

st.plotly_chart(fig_fare)

# Gráfico de barras para mostrar la distribución de los lugares de embarque
if emabarked_survived:
   color = 'Survived'
   title = 'Distribución de la Supervivencia por Puerto de Embarque'
else:
   color = 'Embarked'
   title = 'Distribución de Lugares de Embarque'
   
data['Embarked'] = data['Embarked'].map({'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'})
fig_embarked = px.histogram(data, x='Embarked', title=title, color=color)
fig_embarked.update_layout(xaxis_title='Puerto de embarque',yaxis_title="Total pasajeros", showlegend=True)
fig_embarked.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, selector=dict(type='bar'))
st.plotly_chart(fig_embarked)

# Gráfico de barras para mostrar la distribución de sexos en las personas embarcadas
if sex_survived:
   color = 'Survived'
   title = 'Distribución de la Supervivencia por Género'
else:
   color = 'Sex'
   title = 'Distribución de Sexo'
data['Sex'] = data['Sex'].map({'male': 'Hombres', 'female': 'Mujeres'})
fig = px.histogram(data, x='Sex', title=title, color=color)
fig.update_layout(xaxis_title='Sexo', yaxis_title='Total pasajeros', showlegend=False)
fig.update_traces(marker_color=['rgb(158,202,225)', 'rgb(255,87,87)'], marker_line_color='rgb(8,48,107)', marker_line_width=1.5, selector=dict(type='bar'))
st.plotly_chart(fig)


# Gráfico de barras para mostrar la distribución de la edad de los pasajeros
fig_age = px.box(data, x='Age', title='Distribución de la Edad de los Pasajeros')
fig_age.update_layout(xaxis_title='Edad', yaxis_title='Total pasajeros', showlegend=False)
fig_age.update_traces(marker_color='rgb(144, 238, 144)', marker_line_color='white', marker_line_width=1.5)
st.plotly_chart(fig_age)

# Gráfico de dispersión para mostrar la relación entre la edad y el precio del billete
fig_scatter = px.scatter(data, x='Age', y='Fare', title='Relación entre Edad, Precio del Billete y Sobrevivientes', color='Survived', color_continuous_scale='agsunset')
fig_scatter.update_layout(xaxis_title='Edad', yaxis_title='Precio del Billete')
st.plotly_chart(fig_scatter)

# Gráfico de pastel para mostrar la distribución de la clase de pasajeros
fig_pie = px.pie(data, names='Pclass', title='Distribución de la Clase de Pasajeros')
st.plotly_chart(fig_pie)

# Gráfico de barras para mostrar la distribución de la supervivencia por clase de pasajeros
fig_survived_class = px.histogram(data, x='Pclass', color='Survived', barmode='group', title='Distribución de la Supervivencia por Clase de Pasajeros')
fig_survived_class.update_layout(xaxis_title='Clase de Pasajeros', yaxis_title='Total pasajeros', showlegend=True)
fig_survived_class.update_traces(marker_color=['rgb(158,202,225)', 'rgb(255,87,87)'], marker_line_color='rgb(8,48,107)', marker_line_width=1.5, selector=dict(type='bar'))
st.plotly_chart(fig_survived_class)

# Gráfico de barras para mostrar la distribución de la supervivencia por sexo y clase de pasajeros
fig_survived_sex_class = px.histogram(data, x='Sex', color='Survived', facet_col='Pclass', barmode='group', title='Distribución de la Supervivencia por Sexo y Clase de Pasajeros')
fig_survived_sex_class.update_layout(xaxis_title='Sexo', yaxis_title='Total pasajeros', showlegend=True)
fig_survived_sex_class.update_traces(marker_color=['rgb(158,202,225)', 'rgb(255,87,87)'], marker_line_color='rgb(8,48,107)', marker_line_width=1.5, selector=dict(type='bar'))
st.plotly_chart(fig_survived_sex_class)

# Gráfico de dispersión para mostrar la relación entre la cabina, el precio y la clase
fig_cabin = px.scatter(data, x='Cabin', y='Fare', color='Pclass', title='Relación entre Cabina, Precio del Billete y Clase', color_continuous_scale='emrld')
fig_cabin.update_layout(xaxis_title='Cabina', yaxis_title='Precio del Billete')
st.plotly_chart(fig_cabin)

