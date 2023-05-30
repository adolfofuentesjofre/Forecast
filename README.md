# Capston Project Forecast

- Adolfo Ignacio Fuentes Jofré

Repositorio creado en Python 3.9.13 

## Estructura

- **Data:** Datos utilizados por el proyecto. La sub carpeta raw  Contiene el archivo contiene la BBDD que se utilizará. Por otra parte la sub carpeta processed tienes los datos ya procesados que serán importados posteriormente para entrenar los modelos.

- **Notebooks:** Notebooks del proyecto que dividen en 3 secciones: Limpieza, Analisis y Reporte.La carpeta llamda **Funciones:** contiene una librería llamada "Funciones_feriados_semana" con las funciones para evaluar dias feriados, dias antes de feriados y número de la semana del mes

- **Output:** Html final de los 3 notebooks ya ejecutados


## Descripción

Capston Project Analisis de Datos, este repositorio de Series de Tiempo creado en Python 3.9.13 Se utilizará un dataset del consumo de productos de una empresa en Chile durante el año 2022, identificaremos patrones de uso e de implementaremos predicciones respecto al consumo futuro. Base de Datos corresponde a datos internos deuna compañía privada que registra la cantidad de bienes en uso en un momento especifico del día. La BBDD tiene 347.863 registros.

## Guía de ejecución

- Primero se debe ejecutar el notebook llamado Limpieza, el cual ejecutará el preprocesamiento de los datos y se podrá observar el analisis descriptivo de la serie de tiempo. Este Notebook generará un dataset y limpio y con el nivel de granularidad adecuado para entrenar los modelos.
- Segundo se debe ejecutar el Notebook llamado Analisis el cual importará los datos ya procesados por el script Limpieza.
- El notebook Reporte finalmente resume, discute y concluye todos los resultados de este proyecto.
