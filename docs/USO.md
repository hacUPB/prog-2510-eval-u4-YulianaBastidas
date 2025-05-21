Documentación de Uso y Organización del Código

Este proyecto es una **aplicación de línea de comandos (CLI)** que permite al usuario analizar archivos de texto (`archivos.txt`) y archivos CSV (`archivos.csv`). Está pensado para facilitar la manipulación básica de datos con menús simples, estadísticas, reemplazo de texto y gráficos. El archivo principal es `main.py`.

---

## Organización del Código

El código está dividido en bloques funcionales:

1. **Importación de Módulos**
```python
import os
import csv
import matplotlib.pyplot as plt
os: para ver archivos en la carpeta.

csv: para manejar archivos .csv.

matplotlib.pyplot: para mostrar gráficos.

Menús de Navegación

mostrar_menu(): Muestra el menú principal.

menu_texto(): Opciones para analizar archivos de texto.

menu_csv(): Opciones para analizar archivos CSV.

Funciones para analizar archivos de texto (archivos.txt)

contar_palabras_archivo(): Cuenta palabras, caracteres totales y sin espacios.

modificar_texto(): Reemplaza una palabra por otra en el archivo.

grafico_vocales(): Cuenta cuántas veces aparece cada vocal y lo grafica.

Funciones para analizar archivos CSV (archivos.csv)

ver_filas_csv(): Muestra las primeras 15 filas del archivo.

estadisticas_csv(): Calcula promedio, mediana, mínimo, máximo si son números; si no, cuenta repeticiones de palabras.

graficar_csv(): Grafica los valores de una columna numérica.

Función principal main()
Controla la interacción con el usuario y llama los menús y funciones según la opción elegida. Usa un bucle while para repetir hasta que el usuario elija salir.

