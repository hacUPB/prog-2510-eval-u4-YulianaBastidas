import os
import csv
import matplotlib.pyplot as plt

def mostrar_menu():
    print('\nANALIZADOR DE DATOS')
    print('===================')
    print('1. Ver archivos')
    print('2. Analizar texto')
    print('3. Analizar CSV')
    print('4. Salir')
    return input('Elija una opción: ')

def menu_texto():
    print('\nANALIZAR ARCHIVO DE TEXTO')
    print('-------------------------')
    print('1. Contar palabras')
    print('2. Cambiar texto')
    print('3. Ver vocales')
    print('4. Volver')
    return input('Elija una opción: ')

def menu_csv():
    print('\nANALIZAR ARCHIVO CSV')
    print('--------------------')
    print('1. Ver primeras filas')
    print('2. Calcular estadísticas')
    print('3. Hacer gráfico')
    print('4. Volver')
    return input('Elija una opción: ')

def contar_palabras_archivo():
    try:
        with open("archivos.txt") as f:
            texto = f.read()
            palabras = texto.split()
            
            print("\nRESULTADOS:")
            print(f"Palabras: {len(palabras)}")
            print(f"Caracteres (total): {len(texto)}")
            print(f"Caracteres (sin espacios): {len(texto.replace(' ',''))}")
    except:
        print("Error: No se encontró archivos.txt")

def modificar_texto():
    try:
        palabra_vieja = input("Palabra a reemplazar: ")
        palabra_nueva = input("Nueva palabra: ")
        
        with open("archivos.txt", "r") as f:
            texto = f.read()
        
        texto_nuevo = texto.replace(palabra_vieja, palabra_nueva)
        
        with open("archivos.txt", "w") as f:
            f.write(texto_nuevo)
            
        print(f"Se cambió '{palabra_vieja}' por '{palabra_nueva}'")
    except:
        print("Error al modificar el archivo")

def grafico_vocales():
    try:
        vocales = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        
        with open("archivos.txt") as f:
            for letra in f.read().lower():
                if letra in vocales:
                    vocales[letra] += 1
        
        plt.bar(vocales.keys(), vocales.values())
        plt.title('Vocales en el texto')
        plt.show()
    except:
        print("Error al leer el archivo")

def ver_filas_csv():
    try:
        with open('archivos.csv') as f:
            lector = csv.reader(f)
            print("\nPRIMERAS 15 FILAS:")
            
            for i, fila in enumerate(lector):
                if i == 0:
                    print("Columnas:", fila)
                elif i <= 15:
                    print(f"Fila {i}:", fila)
                else:
                    break
    except:
        print("Error al leer archivos.csv")

def estadisticas_csv():
    try:
        with open('archivos.csv') as f:
            lector = csv.reader(f)
            columnas = next(lector)
            
            print("\nCOLUMNAS DISPONIBLES:")
            for i, col in enumerate(columnas):
                print(f"{i}. {col}")
                
            col = int(input("Elija una columna: "))
            
            numeros = []
            textos = []
            
            for fila in lector:
                if len(fila) > col:
                    valor = fila[col].strip()
                    if valor:
                        try:
                            numeros.append(float(valor))
                        except:
                            textos.append(valor)
            
            print(f"\nANÁLISIS DE '{columnas[col]}'")
            print("Registros válidos:", len(numeros) + len(textos))
            
            if numeros:
                numeros.sort()
                prom = sum(numeros)/len(numeros)
                mitad = len(numeros)//2
                mediana = numeros[mitad] if len(numeros)%2 else (numeros[mitad-1]+numeros[mitad])/2
                
                print("\nEstadísticas:")
                print(f"Promedio: {prom:.2f}")
                print(f"Mediana: {mediana:.2f}")
                print(f"Mínimo: {min(numeros):.2f}")
                print(f"Máximo: {max(numeros):.2f}")
            
            if textos:
                conteo = {}
                for t in textos:
                    conteo[t] = conteo.get(t, 0) + 1
                
                print("\nPalabras más usadas:")
                for palabra, cantidad in sorted(conteo.items(), key=lambda x: -x[1]):
                    print(f"'{palabra}': {cantidad}")
    except:
        print("Error en el análisis")

def graficar_csv():
    try:
        with open('archivos.csv') as f:
            lector = csv.reader(f)
            columnas = next(lector)
            
            print("\nCOLUMNAS:")
            for i, col in enumerate(columnas):
                print(f"{i}. {col}")
                
            col = int(input("Columna a graficar: "))
            
            datos = []
            for fila in lector:
                if len(fila) > col:
                    val = fila[col].strip()
                    if val:
                        try:
                            datos.append(float(val))
                        except:
                            pass
            
            plt.plot(datos)
            plt.title(columnas[col])
            plt.show()
    except:
        print("Error al graficar")

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            print("\nARCHIVOS EN CARPETA:")
            for arch in os.listdir():
                print("-", arch)
                
        elif opcion == '2':
            while True:
                op = menu_texto()
                if op == '1':
                    contar_palabras_archivo()
                elif op == '2':
                    modificar_texto()
                elif op == '3':
                    grafico_vocales()
                elif op == '4':
                    break
                else:
                    print("Opción inválida")
        
        elif opcion == '3':
            while True:
                op = menu_csv()
                if op == '1':
                    ver_filas_csv()
                elif op == '2':
                    estadisticas_csv()
                elif op == '3':
                    graficar_csv()
                elif op == '4':
                    break
                else:
                    print("Opción inválida")
        
        elif opcion == '4':
            print("Programa terminado")
            break
            
        else:
            print("Opción incorrecta")

if __name__ == "__main__":
    main()

