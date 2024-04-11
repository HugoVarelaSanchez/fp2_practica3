#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es

#Importamos la libreris sys, y los archivos para implementar el TAD Lista Posicional Ordenada
import sys, time
import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli

def accion(lista_peliculas, lista_peliculas_norep, lista_peliculas_copy, quehacer, data_unorder, data_ordered):
    
    if quehacer == 1:
        print('\nTodas las peliculas:\n')
        for pelicula in lista_peliculas:
            print(pelicula)


    elif quehacer == 2:
        print('\nTodas las peliculas sin repetidos:\n')
        for pelicula in lista_peliculas_norep:
            print(pelicula)


    elif quehacer == 3:

        eleccion = aux_eleccion_number()
        
        if eleccion == 1:
            print('\n Listado de peliculas tabuladas: \n', data_unorder)

        elif eleccion == 2:
            director = menu1(eleccion, data_unorder)

            data_director = data_unorder[data_unorder['Director'] == f'{director}']
            print(f'\nPeliculas de {director}:\n\n', data_director)

        elif eleccion == 3:
            año = menu1(eleccion, data_unorder)

            data_año = data_unorder[data_unorder['Año'] == año]
            print(f'\nPeliculas del año: {año}:\n\n', data_año)



    elif quehacer == 4:
            #1
            print('\nPeliculas creadas por director: \n')
            group_col = 'Director'
            num_peliculas_por_director = data_ordered.groupby(group_col).size()
            print(num_peliculas_por_director, '\n')

            #2
            print('\nPuntuacion media por director: \n')
            group_col = 'Director'
            target_col = 'Puntuacion'
            puntuation_per_director = data_ordered.groupby(group_col).agg({target_col :["mean"]})
            print(puntuation_per_director, '\n')

            #3
            print('\nPuntuacion media por año: \n')
            group_col = 'Año'
            target_col = 'Puntuacion'
            puntuation_per_year = data_ordered.groupby(group_col).agg({target_col :["mean"]})
            print(puntuation_per_year, '\n')







def aux_eleccion_number():
    while True:

        try:
            eleccion = int(input('Que quieres hacer: \n    (1)Ver todas las peliculas\n    (2)Peliculas rodadas por un director\n    (3)Peliculas estrenadas en un año\n\n\tEleccion: '))
            
            if (eleccion<1 or eleccion>3):
                raise peli.NumberNotInMenu
            break

        except ValueError:
            print('\nDebes introducir un número\n')

        except peli.NumberNotInMenu:
            print('\nDebe de ser un número del 1 al 3\n')

    return eleccion




def aux_quehacer():

    while True:

        try:
            quehacer = (input('\n---x---\n\nQue quieres ver:\n1)Lista de peliculas ordenadas\n2)Lista de películas ordenadas sin duplicados\n3)Ver algunos listados tabulados\n4)Mostrar métricas\n\nEleccion: '))
            if quehacer in ('EXIT', 'exit', 'Exit'):
                break
            
            quehacer = int(quehacer)
            if (quehacer<1 or quehacer>4):
                raise peli.NumberNotInMenu
            break
            

        except ValueError:
            print('\nDebes introducir un número\n')

        except peli.NumberNotInMenu:
            print('\nDebe de ser un número del 1 al 4\n')


    return quehacer




def menu1(eleccion, data_unorder): #n va a ser para si es 1 es para elegir cual
    

    if eleccion == 2:

        director = input('\nDeme un nombre del director: ')

        while (director not in data_unorder['Director'].values):
            print('\nNo hay peliculas de este director.Si no es asi, asegurese de escribir el nombre como en la tabla')
            director = input('\nDeme un nombre del director: ')

        return director
    
    elif eleccion == 3:

        año = int(input('\nDeme un año: '))

        while (año not in data_unorder['Año'].values):
            print('\nNo hay peliculas en ese año')
            año = int(input('\nDeme un año de alguna pelicula que se encuentre en la tabla: '))

        return año






def main():

    #archivo = sys.argv[1]
    archivo = 'peliculas.txt'


    #Inicializamos las listas

    lista_peliculas = lop.LinkedOrderedPositionalList()
    lista_peliculas_norep = lop.LinkedOrderedPositionalList()
    lista_peliculas_copy = lop.LinkedOrderedPositionalList()    #Es lo mismo pero se hace un copi para modificar cosas

    #Guardamos el contenido del archivo
    with open(archivo, 'r', encoding='utf-8') as contenido:
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

    data_ordered = pd.DataFrame(aux_data_ordered, columns = ['Titulo', 'Director', 'Año', 'Puntuacion'])

    print('Para salir escribir exit')
    quehacer = aux_quehacer()
    
    while quehacer not in ('EXIT', 'exit', 'Exit'):

        accion(lista_peliculas, lista_peliculas_norep, lista_peliculas_copy, quehacer, data_unorder, data_ordered)
        quehacer = aux_quehacer()
        
main()
