from collections import namedtuple

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def leepoblaciones(ruta_fichero):
    registros = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        for linea in f:
            partes = linea.strip().split(',')
            nombre = partes[0]
            codigo = partes[1]
            año = partes [2]
            censo = partes [3]
            registros.append(RegistroPoblacion(nombre, codigo, año, censo))
    return registros

def calcula_paises(poblaciones):
    return sorted(poblaciones)

def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    resultado = []
    
    print (poblaciones[0][0] and paises[0])
    for registro in poblaciones:
        if registro[2] == anyo and registro[0] in paises:
            resultado.append((registro[0], registro[3]))
    return resultado
