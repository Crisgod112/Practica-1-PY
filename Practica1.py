import numpy as np
import matplotlib.pyplot as plt
import math

def calcular_tabla_frecuencia(datos):
    num_clases = math.ceil(np.log2(len(datos))) + 1
    
    rango = datos.max() - datos.min()
    amplitud_clase = rango / num_clases
    
    limites_inferiores = []
    limites_superiores = []
    marcas_de_clase = []
    frecuencias_absolutas = []
    
    for i in range(num_clases):
        limite_inferior = datos.min() + i * amplitud_clase
        limite_superior = limite_inferior + amplitud_clase
        limites_inferiores.append(limite_inferior)
        limites_superiores.append(limite_superior)
        
        marca_de_clase = (limite_inferior + limite_superior) / 2
        marcas_de_clase.append(marca_de_clase)
        
        frecuencia_absoluta = np.sum((datos >= limite_inferior) & (datos < limite_superior))
        frecuencias_absolutas.append(frecuencia_absoluta)
    
    total_datos = len(datos)
    frecuencias_relativas = [(frecuencia / total_datos) * 100 for frecuencia in frecuencias_absolutas]
    
    frecuencias_relativas_redondeadas = [round(frecuencia, 2) for frecuencia in frecuencias_relativas]
    
    print("\nTabla de Frecuencia")
    print("Clase\tLímite Inferior\tLímite Superior\tMarca de Clase\tFrecuencia Absoluta\tFrecuencia Relativa (%)")
    for i in range(num_clases):
        print(f"{i+1}\t{limites_inferiores[i]:.2f}\t\t{limites_superiores[i]:.2f}\t\t{marcas_de_clase[i]:.2f}\t\t{frecuencias_absolutas[i]}\t\t\t{frecuencias_relativas_redondeadas[i]:.2f}%")
    

def main():
    datos_str = input("Introduce los datos separados por comas: ")
    datos = np.array([float(num) for num in datos_str.split(",")])
    
    calcular_tabla_frecuencia(datos)

if __name__ == "__main__":
    main()
