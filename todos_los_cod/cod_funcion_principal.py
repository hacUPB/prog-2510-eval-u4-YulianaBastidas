import os
from funciones_txt import contar_palabras_caracteres, reemplazar_palabra, histograma_vocales
from funciones_csv import mostrar_15_filas, calcular_estadisticas, graficar_columna

def listar_archivos(ruta='.'):
    try:
        archivos = os.listdir(ruta)
        print(f"Archivos en {ruta}:")
        for archivo in archivos:
            print(archivo)
    except FileNotFoundError:
        print("Ruta no encontrada.")

def menu_txt():
    while True:
        print("\nSubmenú Archivos TXT:")
        print("1. Contar número de palabras y caracteres")
        print("2. Reemplazar una palabra por otra")
        print("3. Histograma de vocales")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            archivo = input("Ingresa el nombre del archivo .txt: ")
            contar_palabras_caracteres(archivo)
        elif opcion == '2':
            archivo = input("Ingresa el nombre del archivo .txt: ")
            palabra_vieja = input("Palabra a reemplazar: ")
            palabra_nueva = input("Nueva palabra: ")
            reemplazar_palabra(archivo, palabra_vieja, palabra_nueva)
        elif opcion == '3':
            archivo = input("Ingresa el nombre del archivo .txt: ")
            histograma_vocales(archivo)
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")

def menu_csv():
    while True:
        print("\nSubmenú Archivos CSV:")
        print("1. Mostrar las primeras 15 filas")
        print("2. Calcular estadísticas de una columna")
        print("3. Graficar una columna")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            archivo = input("Ingresa el nombre del archivo .csv: ")
            mostrar_15_filas(archivo)
        elif opcion == '2':
            archivo = input("Ingresa el nombre del archivo .csv: ")
            columna = input("Nombre de la columna: ")
            resultado = calcular_estadisticas(archivo, columna)
            if resultado:
                n, promedio, mediana, minimo, maximo = resultado
                print(f"Datos en columna '{columna}':")
                print(f"Número de datos: {n}")
                print(f"Promedio: {promedio}")
                print(f"Mediana: {mediana}")
                print(f"Valor mínimo: {minimo}")
                print(f"Valor máximo: {maximo}")
        elif opcion == '3':
            archivo = input("Ingresa el nombre del archivo .csv: ")
            columna = input("Nombre de la columna: ")
            graficar_columna(archivo, columna)
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")

def main():
    while True:
        print("\nMenú Principal:")
        print("1. Listar archivos en ruta actual o especificar ruta")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            ruta = input("Ingresa la ruta (deja vacío para ruta actual): ")
            if ruta.strip() == '':
                ruta = '.'
            listar_archivos(ruta)
        elif opcion == '2':
            menu_txt()
        elif opcion == '3':
            menu_csv()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()