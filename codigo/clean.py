#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es

#Importamos la libreris sys, y los archivos para implementar el TAD Lista Posicional Ordenada
import sys, time
import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli

def accion(lista_peliculas, lista_peliculas_norep, lista_peliculas_copy, quehacer):
    
    if quehacer == 1:
        for pelicula in lista_peliculas:
            print(pelicula)

    elif quehacer == 2:
        for i in lista_peliculas_norep:
            print(i)

    elif quehacer == 3:
        print(data_unorder)



def aux_quehacer():
    while True:

        try:
            quehacer = int(input('Que quieres ver:\n1)Lista de peliculas ordenadas\n2)Lista de películas ordenadas sin duplicados\n3)Ver algunos listados tabulados\n4)Mostrar métricas\n'))
            
            if (quehacer<1 or quehacer>4):
                raise peli.NumberNotInMenu
            break

        except ValueError:
            print('\nDebes introducir un número\n')

        except peli.NumberNotInMenu:
            print('\nDebe de ser un número del 1 al 4\n')

    return quehacer

def

def main():

    #archivo = sys.argv[1]
    archivo = 'peliculas.txt'


    #Inicializamos las listas

    lista_peliculas = lop.LinkedOrderedPositionalList()
    lista_peliculas_norep = lop.LinkedOrderedPositionalList()
    lista_peliculas_copy = lop.LinkedOrderedPositionalList()    #Es lo mismo pero se hace un copi para modificar cosas

    #Guardamos el contenido del archivo
    with open(archivo, 'r') as contenido:
        info_procesos = contenido.read()

    #Rellenamos las listas

    for line in info_procesos.split('\n'):   

        if len(line) != 0 and len(line.split(';')) == 4:

            datos_pelicula = line.split(';')
            director_name, film_name, estreno, puntuation = datos_pelicula 

            pelicula = peli.Pelicula(director_name, film_name, estreno, puntuation)
            
            lista_peliculas.add(pelicula)
            lista_peliculas_copy.add(pelicula)
    

    #Rellenamos lista_peliculas_norep

    
    while True:
        
        primero   = lista_peliculas_copy.get_element(lista_peliculas_copy.first())
        siguiente = lista_peliculas_copy.get_element(lista_peliculas_copy.after(lista_peliculas_copy.first()))
        ultima    = lista_peliculas_copy.get_element(lista_peliculas_copy.last())

        if (primero.director_name == siguiente.director_name) and (primero.film_name == siguiente.film_name):
                
                lista_peliculas_copy.delete(lista_peliculas_copy.first())

        else:
            

            if siguiente == ultima:

                lista_peliculas_norep.add(lista_peliculas_copy.delete(lista_peliculas_copy.first()))
                lista_peliculas_norep.add(lista_peliculas_copy.delete(lista_peliculas_copy.last()))
                break

            lista_peliculas_norep.add(lista_peliculas_copy.delete(lista_peliculas_copy.first()))

    #Creamos los dataframes con peliculas repetidas y no repetidas
    aux_data_unorder = []
    aux_data_ordered = []

    for u in lista_peliculas:
        aux_data_unorder.append(u.data_values())

    for u in lista_peliculas_norep:
        aux_data_ordered.append(u.data_values())

    data_unorder = pd.DataFrame(aux_data_unorder, columns = ['Titulo', 'Director', 'Año', 'Puntuacion'])

    aux_data_ordered = pd.DataFrame(aux_data_ordered, columns = ['Titulo', 'Director', 'Año', 'Puntuacion'])


    quehacer = aux_quehacer()

    while quehacer != 'exit':

        accion(lista_peliculas, lista_peliculas_norep, lista_peliculas_copy, quehacer)
        
        

