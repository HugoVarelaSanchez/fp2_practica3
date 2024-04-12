#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es

#Importamos la libreris sys, y los archivos para implementar el TAD Lista Posicional Ordenada
import sys, time
import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli



def aux_quehacer():
    '''
    Funcion que ayuda a poder elegir una opcion correcta del menu de opciones.
    Solo deja escojer numeros entre 1-4, que son las opciones, y la palabra exit, que permite
    finalizar la ejecucion de este programa.

    ---------
    Parameters
    ----------
    None

    -------
    Returns
    -------
    quehacer: int
    except
    '''

    while True:

        try:
            quehacer = (input('\n---x---\n\nQue quieres ver:\n(1)Lista de peliculas ordenadas\n(2)Lista de películas ordenadas sin duplicados\n(3)Ver algunos listados tabulados\n(4)Mostrar métricas\n\nEleccion: '))
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


def aux_eleccion_number():

    '''
    Funcion de ayuda. Esta funcion hace que solo se puedan escojer numeros entre 1-3, para
    el segundo menu de opciones(Si escojes opcion (3) ). Tambien muestara el segundo menu 

    ---------
    Parameters
    ----------

    None
        
    -------
    Returns
    -------

    eleccion : int.
    '''

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





def menu1(eleccion, data_repeat):   #NECESITA CAMBIO  si en año poner algo que no es un int te da un error ya que no peudes poner str, cambiar para que coja str
    '''
    Funcion que nos permite, dependiendo de la eleccion del segundo menu, 
    actuar.
    Si se escoje la opcion 2, conseguiremos director, que solo funcionara si ponemos el 
    nombre exacto del director que queremos ver y esta en la tabla.
    Lo mismo pero para año
    ---------
    Parameters
    ----------
    eleccion : int
        Opcion del segundo menu elegida

    data_repeat: DataFrame
        DataFrame con todos los datos de listas que puede haber repetidos

    -------
    Returns
    -------

    director or año:

    director: str
    año: int
    '''


    if eleccion == 2:

        director = input('\nDeme un nombre del director: ')

        while (director not in data_repeat['Director'].values):
            print('\nNo hay peliculas de este director.Si no es asi, asegurese de escribir el nombre como en la tabla')
            director = input('\nDeme un nombre del director: ')

        return director
    
    elif eleccion == 3:

        #año = int(input('\nDeme un año: '))

        #while (año not in data_repeat['Año'].values):
        #    print('\nNo hay peliculas en ese año')
        #    año = int(input('\nDeme un año de alguna pelicula que se encuentre en la tabla: '))

        #return año
        
        while True:

            try:
                año = int(input('\nDeme un año: '))
                if (año not in data_repeat['Año'].values):
                    raise peli.NumberNotInMenu
                break
            except ValueError:
                print('\nDebes introducir un año\n')
            except peli.NumberNotInMenu:
                print('\nNo se encuentra ninguna peli con ese año, busque otro\n')


        return año




def accion(lista_peliculas, lista_peliculas_norep, quehacer, data_repeat, data_no_repeat):
    '''
    Funcion que ejecuta las acciones del programa. Recibe toda la informacion con la que
    trabajar pero lo que define que hacer es quehacer. 

    ---------
    Parameters
    ----------
    lista_peliculas : list
        Una lista con  peliculas repetidas.

    lista_peliculas_norep: list
        Una pelicula sin  peliculas repetidas

    quehacer : int
        Accion del menu que se debe tomar

    data_repeat: DateFrame
        DataFrame con peliculas repetidas
    
    data_no_repeat: DataFrame
        DataFrame con peliculas sin repetir
        
    -------
    Returns
    -------

    Prints.
    '''

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
            print('\n Listado de peliculas tabuladas: \n', data_repeat)

        elif eleccion == 2:
            director = menu1(eleccion, data_repeat)

            data_director = data_repeat[data_repeat['Director'] == f'{director}']
            print(f'\nPeliculas de {director}:\n\n', data_director)

        elif eleccion == 3:
            año = menu1(eleccion, data_repeat)

            data_año = data_repeat[data_repeat['Año'] == año]
            print(f'\nPeliculas del año: {año}:\n\n', data_año)



    elif quehacer == 4:
            #1
            print('\nPeliculas creadas por director: \n')
            group_col = 'Director'
            num_peliculas_por_director = data_no_repeat.groupby(group_col).size()
            print(num_peliculas_por_director, '\n')

            #2
            print('\nPuntuacion media por director: \n')
            group_col = 'Director'
            target_col = 'Puntuacion'
            puntuation_per_director = data_no_repeat.groupby(group_col).agg({target_col :["mean"]})
            print(puntuation_per_director, '\n')

            #3
            print('\nPuntuacion media por año: \n')
            group_col = 'Año'
            target_col = 'Puntuacion'
            puntuation_per_year = data_no_repeat.groupby(group_col).agg({target_col :["mean"]})
            print(puntuation_per_year, '\n')






def main():
    '''
    Funcion de ejecucion. Al llamarla se ejecuta todo el programa

    ---------
    Parameters
    ----------
    None

    -------
    Returns
    -------
    
    '''

    archivo = sys.argv[1]
    #archivo = 'peliculas.txt'


    #Inicializamos las listas

    lista_peliculas       = lop.LinkedOrderedPositionalList()
    lista_peliculas_norep = lop.LinkedOrderedPositionalList()
    lista_peliculas_copy  = lop.LinkedOrderedPositionalList()    #Es lo mismo pero se hace un copi para modificar cosas

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
    aux_data_repeat = []
    aux_data_no_repeat = []

    for u in lista_peliculas:
        aux_data_repeat.append(u.data_values())

    for u in lista_peliculas_norep:
        aux_data_no_repeat.append(u.data_values())

    data_repeat = pd.DataFrame(aux_data_repeat, columns = ['Titulo', 'Director', 'Año', 'Puntuacion'])

    data_no_repeat = pd.DataFrame(aux_data_no_repeat, columns = ['Titulo', 'Director', 'Año', 'Puntuacion'])

    print('Para salir escribir exit')
    quehacer = aux_quehacer()
    
    while quehacer not in ('EXIT', 'exit', 'Exit'):

        accion(lista_peliculas, lista_peliculas_norep, quehacer, data_repeat, data_no_repeat)
        quehacer = aux_quehacer()
        

if __name__ == "__main__":
    main()
