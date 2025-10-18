from collections import namedtuple
import csv
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def leepoblaciones(ruta_fichero):
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        
        lista_registro = []
        
        for pais, codigo, anyo, censo in lector:
            anyo = int(anyo)
            censo = int(censo)
            
            registro = (pais, codigo, anyo, censo)
            lista_registro.append(registro)
        
        return lista_registro     
    return

def calcula_paises(poblaciones):
    return sorted(poblaciones)

def filtra_por_pais(poblaciones, nombre_o_codigo):
    resultado = []
    
    for registro in poblaciones:
        if registro[0] == nombre_o_codigo or registro[1] == nombre_o_codigo:
            datos = (registro[2], registro[3])
            resultado.append(datos)
    return resultado

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    resultado = []
    
    for registro in poblaciones:
        if registro[2] == anyo and registro[0] in paises:
            datos = (registro[0], registro[3])
            resultado.append(datos)
    return resultado

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    registro_pais = filtra_por_pais(poblaciones, nombre_o_codigo)
    
    lista_anyos = registro_pais[0]
    lista_habitantes = registro_pais[1]
    
    plt.title("lista_años")
    plt.plot(lista_anyos, lista_habitantes)
    plt.show()
    
def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    registro = filtra_por_paises_y_anyo(poblaciones, anyo, paises)
    
    lista_habitantes = []
    for i in registro:
        lista_habitantes.append(i[1])

    plt.title("Comparativa: Paises/Año")
    plt.bar(paises, lista_habitantes)
    plt.show()