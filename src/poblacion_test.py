from poblacion import *

def test_lee_poblaciones(ruta):
    print("TESTEANDO: test_lee_poblaciones")
    print(leepoblaciones(ruta))

def test_calcula_paises(poblaciones):
    print("TESTEANDO: test_calcula_paises")
    print(calcula_paises(poblaciones))
    
def test_filtra_por_pais(poblaciones, nombre_o_codigo):
    print("TESTEANDO: test_filtra_por_pais")
    print(filtra_por_pais(poblaciones, nombre_o_codigo))
    
def test_filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    print("TESTEANDO: test_filtra_por_paises_y_anyo")
    print(filtra_por_paises_y_anyo(poblaciones, anyo, paises))

def test_muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    print("TESTEANDO: test_muestra_evolucion_poblacion")
    muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)
    
def test_muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    print("TESTEANDO: test_muestra_comparativa_paises_anyo")
    muestra_comparativa_paises_anyo(poblaciones, anyo, paises)

def main():
    #test_lee_poblaciones("./data/population.csv")
    #test_calcula_paises(leepoblaciones("./data/population.csv"))
    #test_filtra_por_pais(leepoblaciones("./data/population.csv"), "Canada")
    #test_filtra_por_pais(leepoblaciones("./data/population.csv"), "CAN")
    #paises = ("Canada", "Cameroon")
    #test_filtra_por_paises_y_anyo(leepoblaciones("./data/population.csv"), 1984, paises)
    #test_muestra_evolucion_poblacion(leepoblaciones("./data/population.csv"), "Canada")
    paises = ("Canada", "Cameroon")
    test_muestra_comparativa_paises_anyo(leepoblaciones("./data/population.csv"), 1984, paises)
    pass

if __name__ == '__main__':
    main()