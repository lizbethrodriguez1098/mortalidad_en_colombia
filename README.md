# 🩺 Dashboard de Mortalidad en Colombia 2019

## 📘 Introducción del Proyecto

El análisis de datos se ha convertido en una habilidad indispensable en la actualidad ya que hoy en día casi todo genera datos. Saber analizar estos datos permite entender, interpretar y comunicar información valiosa. De esta manera, las visualizaciones de datos cumplen un papel importante en el análisis ya que permiten transformar datos en gráficos que facilitan su interpretación y la comunicación de resultados, haciendo que esta sea accesible y útil para todos.

Por lo anterior esta actividad, tiene como objetivo crear una aplicación web interactiva con Python usando Plotly y Dash. Estas dos herramientas son muy útiles en el análisis y visualización de los datos, la primera permite crear gráficos interactivos y la segunda usa esos gráficos para construir dashboard completos para que los usuarios puedan interactuar fácilmente.

De la misma manera, se busca crear un dashboard interactivo utilizando diferentes tipos de gráficos estructurado por pestañas que permitan analizar y visualizar los datos de mortalidad en Colombia del año 2019. Para ellos, se va a utilizar diferentes tipos de visualizaciones como lo son mapas, gráficos de líneas, barras, diagramas circulares, tablas, histogramas y barras aplicadas que permitirá explorar la información desde diferentes perspectivas con el propósito de identificar patrones, tendencias y correlaciones de los datos.

Igualmente, se va a realizar el despliegue en la web utilizando la plataforma Render, este es un servicio en la nube que permite publicar aplicación web de manera sencilla y automática. Además, esta soporta aplicaciones desarrolladas en Python, por lo que es muy útil para lograr realizar la transición del entorno local hasta un ambiente web accesible desde cualquier parte con conexión a internet.


---

## 🎯 Objetivo

El objetivo principal de la aplicación es **analizar y visualizar los datos de mortalidad en Colombia**, con el fin de identificar **tendencias, patrones y factores predominantes** asociados a las causas de muerte. 
 
El dashboard permite realizar un análisis exploratorio mediante **gráficos interactivos** como mapas, líneas, barras, histogramas y diagramas circulares, ofreciendo una herramienta útil para el estudio y la toma de decisiones en salud pública.

---

## 🗂️ Estructura del Proyecto

```bash
mortalidadColombia/
│
├── callbacks/                  # Callbacks del dashboard (Dash/Plotly)
│   ├── barras_apiladas.py
│   ├── barras.py
│   ├── circular.py
│   ├── histograma.py
│   ├── lineas.py
│   ├── mapa.py
│   └── tabla.py
│
├── data/                       # Datos base
│   ├── Anexo1.NoFetal2019_CE_15-03-23.xlsx
│   ├── Anexo2.CodigosDeMuerte_CE_15-03-23.xlsx
│   └── Divipola_CE_.xlsx
│
├── data_processing/            # Limpieza y transformación de datos
│   └── consolidacion.py
│
├── util/                       # Funciones auxiliares
│   ├── asignar_categoria.py
│   └── filtro_departamento.py
│
├── app.py                      # Script principal del dashboard
├── layout.py                   # Definición del layout del dashboard
├── README.md
└── requirements.txt
```

Con respecto al proyecto, se va a manejar la versión 3.13.5 de Python. En la carpeta *callbacks*, se van a encontrar todas las funciones para la interacción del dashboard, se creó uno para cada tipo de grafica. En *data*, contiene los archivos con los datos de mortalidad del DANE 2019. *Data_processing* contiene el código para realizar la limpieza y transformación de datos. En *útil*, se tienen dos funciones que se van a utilizar en varios gráficos. Por último, se tiene en la raíz del proyecto *app.py* y *layout.py* que definen la estructura y el funcionamiento principal para el dashboard, y *README.md* y *requirements.txt* para documentación del proyecto. 

---

## ⚙️ Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes librerías:

```bash
dash==3.2.0
dash_bootstrap_components==2.0.4
pandas==2.3.3
plotly==6.3.1
openpyxl==3.1.5
gunicorn==23.0.0
```

---

## 🚀 Despliegue en Render

1. Crear una cuenta en [Render](https://render.com).  
2. Subir el repositorio del proyecto a **GitHub**.  
3. En Render, seleccionar **New Web Service → Connect GitHub**.  
4. Elegir el repositorio del proyecto.  
5. Configurar los siguientes parámetros:

   - **Start Command:** `gunicorn app:server`  
   - **Environment:** `Python`  
   - **Build Command:** `pip install -r requirements.txt`

6. Hacer clic en **Deploy** para publicar la aplicación.  
7. Render generará un **enlace público** para acceder al dashboard.

![Image](https://github.com/faridbaron/prueba/blob/824f4f4033cbdf3ccd5211482c3c1a638ab6598e/imagenes/render1.jpeg)


![Image](https://github.com/faridbaron/prueba/blob/824f4f4033cbdf3ccd5211482c3c1a638ab6598e/imagenes/render2.jpeg)



Link público: [Mortalidad en Colombia 2019](https://mortalidad-en-colombia.onrender.com/)

---

## 🧰 Software Utilizado

* Python 3.13.5
* Dash → para el desarrollo del dashboard interactivo.
* Plotly → para la creación de gráficos dinámicos.
* Pandas y NumPy → para la manipulación y análisis de datos.
* Render → para el despliegue web de la aplicación.

## 💻 Instalación local

Para ejecutar el proyecto localmente, sigue estos pasos:

#### 1. Clonar el repositorio

git clone https://github.com/lizbethrodriguez1098/mortalidad_en_colombia.git

#### 2. Posicionarse en la carpeta

cd mortalidad_colombia_2019

#### 2. Instalar dependencias
pip install -r requirements.txt

#### 4. Ejecutar la aplicación
python app.py

---

## 📈 Visualizaciones y resultados

**Visualización 1. Mapa geográfico de la mortalidad en Colombia:** 

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Mapa.png)

En esta visualización encontramos un mapa de Colombia interactivo donde se representa la cantidad de muertes registradas por departamento en Colombia durante el año 2019. Cada departamento tiene un color según el número de muertes, usando una escala de colores desde tonos claros (baja mortalidad) a tono oscuros (alta mortalidad).  Cuando el usuario pase el cursor sobre el mapa en cada uno de las correspondientes regiones, muestra el nombre del departamento y la cantidad de muertes. 

Se observa una mayor concentración de mortalidad en los departamentos del centro y norte del país, principalmente en Bogotá DC con 11,184K, Antioquia con 34,451K y Valle del cauca con 28,438K, al ser los tonos mas oscuros del mapa. En contraste, los departamentos con menos cantidad de muertes, denotados por tener los tonos más claros del mapa al sur del país son Vaupés con 87, Guainía con 115 y Vichada con 188 y Amazonas con 190. Esta información del mapa permite identificar patrones regionales que puede ayudar a tomar decisiones en diferentes situaciones sociales. 

**Visualización 2 Tendencias mensuales de mortalidad:**

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/lineas_Colombia.png)

En esta visualización de gráfico de líneas se representa el número total de muertes registradas por mes en Colombia durante el año 2019; en cada punto de la línea se muestra el valor total de muertes junto con el número del mes del año, que permite apreciar la evolución temporal de la mortalidad a lo largo del año 2019. 

Para el mes de febrero se evidencia una caída significativa de muertes para Colombia con 17,965K, siendo el menor número de muertes en el año. Después se observa que a partir del mes de marzo la cantidad de muertes comienza a tener una tendencia ascendente y alcanza su punto máximo en los meses de julio con 21,361K y agosto con 21,154K; posteriormente, se observa una caída para el mes de septiembre con 19.773K y luego vuelve aumentar hasta el mes de diciembre con 21,67K que es el pico mas alto en el año. Este análisis mensual permite la identificación de patrones de riesgos que pueden ser útiles para las planeaciones. 

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Lineas_Boyaca.png)

Así mismo, para este grafico se pueden hacer filtros por departamento, por ejemplo, para el análisis del departamento de Boyacá, también se evidencia para el mes de febrero una disminución con 399 muertes y el pico más alto en el mes julio con 572 muertes. 

**Visualización 3. Ciudades con mayor índice de homicidios:**

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Barras_Colombia.png)

En esta visualización encontramos el grafico de barras donde se muestra el Top 5 de las ciudades con mayor número de homicidios en Colombia durante el año 2019, teniendo en cuenta la causa con el código X95 (agresión con disparo de armas de fuego y casos no especificados); cada barra representa el número total de homicidios registrados por cada ciudad organizada de mayor a menor, lo que permite comparar visualmente los lugares con mayor incidencia de muertes en esta categoría. 

Se evidencia que la ciudad Santiago de Cali cuneta con la mayor cantidad de muertes de la lista con 971 homicidios; luego le siguen Bogotá DC con 601 homicidios y Medellín con 428 homicidios, que son cifras representativas debido a su gran población; después se continua con las ciudades de Barranquilla con 260 homicidios y San José de Cúcuta con 206 homicidios, son niveles mas moderados, pero siguen siendo representativas dentro del contexto nacional.

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Barras_Boyaca.png)

A nivel regional, al aplicar el filtro a nivel de Boyacá se observa que la mayor cantidad de muertes por homicidios corresponde a Puerto Boyacá con 12 casos, seguido de Chiquinquirá y Tunja con 4 cada uno, luego La Victoria y Paipa con 2. Al comparar esta región con las demás ciudades del Top 5 a nivel de Colombia, se evidencia que en Boyacá presenta una baja cantidad de homicidios, lo cual sugiere que es uno de los departamentos más tranquilos en este aspecto 

**Visualización 4. Ciudades con menor índice de mortalidad en Colombia:**

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Circular_Colombia.png)

En esta visualización, tenemos un grafico circular que representa las 10 cuidades con menos índice de mortalidad. Teniendo el filtro de todos los departamentos muestras que a nivel nacional las cuidades con menor índice se dividen equitativamente el 10% que equivale a una muerte, entre las que se encuentra. Bituma, Taraira, Margarita, Hato, Mapiripana, Nuquí, San Fernando, Puerto Alegría, El Calvario y El Encanto.

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Circular_Boyaca.png)

Siguiendo con la línea de análisis filtrando por el departamento de Boyacá, se observa que la menores ciudad con menor índice de mortalidad son Iza, Paqueba y Guacamayas con 5,88% que equivalen 2 muertes cada una.  Seguido de Tununguá y La Victoria con 8,82% (3 muertes), Posteriormente se tiene con 11,8% que representa 4 muertes a Sáchica, Paya y Pisba. Por último, se tiene a Cuítiva y Caldas con 14,7% que equivalen a 5 muertes. Las grafica reflejan que estas ciudades con menor índice de mortalidad puede estar relacionados a factores como su baja densidad poblacional.

**Visualización 5. Causas de muertes más comunes:**

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Tabla_Colombia.png)

En esta visualización, se tiene una tabla con el listado de las 10 principales causas de muerte, que incluye su código, nombre y total de casos.  En Colombia la enfermedad cardiovascular causado por infarto agudo de miocardio es la causa más común con un poco más de 35 mil casos, que representa más del doble de los casos que la segunda causa que es las enfermedades pulmonares obstructivas crónicas, la tercera causa más común es la relacionada a violencia que puede reflejar un problema social y de seguridad pública con 9273 casos. La neumonía aparece como la cuarta causa con una cantidad considerable que puede ser por impactos de los factores ambientes. De la misma manera en el listado aparecen la diabetes y canceres frecuentes como lo es de estómago, pulmón, mama y próstata.

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Tabla_Boyaca.png)

A nivel de Boyacá, el panorama es similar en cuanto a las principales causas, donde también se encuentra como causa primaria el infarto agudo del miocardio. Sin embargo, en Boyacá destacan con más fuerza las enfermedades relacionadas con el corazón y la circulación, como la enfermedad cardiaca, la hipertensión, la hemorragia intracerebral y la insuficiencia cardíaca. Esto sugiere que en la población en la región es más envejecida y con mayor prevalencia de factores de riesgo cardiovascular. 

**Visualización 6. Comparación de muerte por sexo**

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Barras_Apiladas_Colombia.png)

El grafico de barras apiladas representa la distribución del número total de muertes por sexo masculino, femenino e indeterminado,	por cada departamento de Colombia para el año 2019. Cada barra representa el total de fallecimientos por departamento y se representa con colores para los grupos de cada sexo; esta visualización permite observar tanto el volumen total de muertes por región como las diferencias de magnitud entre hombres, mujeres e indeterminado dentro de cada región. 

Se observa que en la mayoría de los departamentos, la mayor proporción de muertes se centra en el sexo masculino comparándolo con el sexo femenino, lo que refleja una tendencia general de las estadísticas del país.

**Visualización 7. Histograma de las distribución de muertes por grupo de edad:**

![Image](https://github.com/faridbaron/prueba/blob/20cf950ea905b4e20556d0465ecbbc4e873edc81/imagenes/Histograma_Colombia.png)

En esta visualización, se tiene un histograma con la distribución de muertes por grupo de edad. En Colombia permite observar cómo la mortalidad aumenta de forma progresiva con la edad. El numero de muertes empieza a aumentar de manera significativa en el rango de la juventud de 20-29 años, y llega al pico de casos en el rango de la vejez que esta comprendida entre el rango de los 60 y 84 años, esto se puede relacionar que a esta edad es más común que se presenten las enfermades cardiovasculares y respiratorias que son causas comunes de muertes en el país.

---

## 🧠 Conclusiones

Se logró desarrollar una interfaz web interactiva aplicando un caso práctico en Python mediante el uso de Dash y Plotly, consolidando conceptos de la programación como la creación de callbacks reactivos, uso de funciones para realizar la transformación de los datos de entrada consolidándolos en un solo para optimizar su uso, siguiendo las buenas prácticas para el desarrollo de software. Además, se obtuvo una integración entre la lógica de programación y la visualización de datos para lograr un dashboard interactivo para el análisis de datos.

El uso de Dash y Plotly, permitió crear fácilmente dashboard dinámicos, ya que fue posible combinarlo con la programación en Python. Esto permitió crear diferentes tipos de gráficos que contribuyeron a mejorar el análisis de datos, facilitando identificar patrones, tendencias y comportamientos relacionados con la mortalidad en Colombia. Lo anterior, favorece a la interpretación que ayuda a sacar conclusiones relevantes.

Por último, la transición del entorno local al web por medio de Render permitió publicar el dashboard para acceder remotamente, facilitando la disponibilidad para cualquier usuario que posea una conexión a internet. Esta implementación amplia los conocimientos sobre el uso de las herramientas para el análisis de datos, fomentando el aprendizaje practico y la capacidad de transmitir resultados de una manera efectiva y agradable.

---

## 👤 Autores

Desarrollado por Lizbeth Natalia Rodriguez & Farid Steven Baron.