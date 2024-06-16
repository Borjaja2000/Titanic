# Aplicación de Análisis de Datos del Titanic

Esta aplicación de Streamlit realiza un análisis exhaustivo del conjunto de datos del Titanic. Proporciona visualizaciones interactivas y opciones de filtrado de datos para explorar varios aspectos de los datos de los pasajeros del Titanic.

## Características

- **Carga y visualización del conjunto de datos del Titanic**: La aplicación carga el conjunto de datos del Titanic y muestra los datos en una tabla.
- **Filtro por edad**: Filtra pasajeros por edad.
- **Filtro por mediana de edad**: Filtra pasajeros según si su edad está por debajo o por encima de la mediana.
- **Filtro por precio del billete**: Filtra pasajeros por el precio del billete (más barato o más caro).
- **Visualización de valores nulos**: Muestra el porcentaje o la cantidad de valores nulos en cada columna.
- **Distribución de precios**: Histograma que muestra la distribución de los precios de los billetes.
- **Distribución por lugar de embarque**: Histograma que muestra la distribución de los pasajeros según su lugar de embarque.
- **Distribución por sexo**: Histograma que muestra la distribución de los pasajeros según su sexo.
- **Distribución de edades**: Diagrama de caja que muestra la distribución de las edades de los pasajeros.
- **Relación entre edad y precio del billete**: Diagrama de dispersión que muestra la relación entre la edad de los pasajeros, el precio del billete y su estado de supervivencia.
- **Distribución por clase**: Gráfico de pastel que muestra la distribución de los pasajeros según su clase.
- **Distribución de la supervivencia por clase**: Histograma que muestra la distribución de la supervivencia según la clase de los pasajeros.
- **Distribución de la supervivencia por lugar de embarque**: Histograma que muestra la distribución de la supervivencia según el lugar de embarque.
- **Distribución de la supervivencia por sexo y clase**: Histograma que muestra la distribución de la supervivencia según el sexo y la clase de los pasajeros.

## Instalación

1. **Clona el repositorio**:
    ```sh
    git clone https://github.com/Borjaja2000/Titanic
    cd Titanic
    ```

2. **Crea un entorno virtual y actívalo**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instala los paquetes requeridos**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Ejecuta la aplicación de Streamlit**:
    ```sh
    streamlit run app.py
    ```

## Uso

1. **Carga el conjunto de datos del Titanic**:
    - Asegúrate de que el archivo `titanic.csv` esté en el mismo directorio que `app.py`.

2. **Lanza la aplicación**:
    - La aplicación estará disponible en `http://localhost:8501`.

3. **Interactúa con la barra lateral**:
    - Utiliza la barra lateral para habilitar o deshabilitar varios filtros y configuraciones para las visualizaciones.

## Archivos

- `app.py`: Script principal de la aplicación.
- `requirements.txt`: Lista de paquetes de Python necesarios para la aplicación.
- `titanic.csv`: Conjunto de datos que contiene los datos de los pasajeros del Titanic.
- `images/titanic.jpg`: Imagen mostrada en la aplicación.

## Capturas de Pantalla

### Interfaz Principal
![Interfaz Principal](images/titanic.jpg)


## Dependencias

- `streamlit`
- `pandas`
- `plotly`

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.

## Agradecimientos

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)




