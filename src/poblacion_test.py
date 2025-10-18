from poblacion import leepoblaciones
from poblacion import calcula_paises
from poblacion import filtra_por_paises_y_anyo

def main():
    paises = "Arab World", "Australia"
    print (filtra_por_paises_y_anyo(leepoblaciones("./data/population.csv"), 1960, paises))

if __name__ == '__main__':
    main()