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

![Image](https://github.com/faridbaron/prueba/blob/34ab17f2e6f524cfeb1ff1f371283b37254efa66/mapa.jpeg)

---

## 🧠 Conclusiones

Se logró desarrollar una interfaz web interactiva aplicando un caso práctico en Python mediante el uso de Dash y Plotly, consolidando conceptos de la programación como la creación de callbacks reactivos, uso de funciones para realizar la transformación de los datos de entrada consolidándolos en un solo para optimizar su uso, siguiendo las buenas prácticas para el desarrollo de software. Además, se obtuvo una integración entre la lógica de programación y la visualización de datos para lograr un dashboard interactivo para el análisis de datos.

El uso de Dash y Plotly, permitió crear fácilmente dashboard dinámicos, ya que fue posible combinarlo con la programación en Python. Esto permitió crear diferentes tipos de gráficos que contribuyeron a mejorar el análisis de datos, facilitando identificar patrones, tendencias y comportamientos relacionados con la mortalidad en Colombia. Lo anterior, favorece a la interpretación que ayuda a sacar conclusiones relevantes.

Por último, la transición del entorno local al web por medio de Render permitió publicar el dashboard para acceder remotamente, facilitando la disponibilidad para cualquier usuario que posea una conexión a internet. Esta implementación amplia los conocimientos sobre el uso de las herramientas para el análisis de datos, fomentando el aprendizaje practico y la capacidad de transmitir resultados de una manera efectiva y agradable.

---

## 👤 Autores

Desarrollado por Lizbeth Natalia Rodriguez & Farid Steven Baron.