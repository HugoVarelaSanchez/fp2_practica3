import sys, time
import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli



def menus(menu,  eleccion = int, data_repeat = pd.DataFrame):
    
    '''
    Funcion de ayuda muy extensa. 
    Esta funcion lo que hace gestionar los 'menus' de la practica:

        El menu == 0 Es el primero que aparece, y aparece siempre. 
            Elige si quieres usar lop o aop

        El menu == 1 Es el menu principal.
            Te da a cual de los 4 puntos principales de la practica quieres usar

        El menu == 2 Menu del apartado 3
            Submenu para elegir cual de las 3 opciones del apartado 3 quieres realizar

        El menu == 3 no es un menu pero se usa para que no puedas introducir un valor
            que no debas en la eleccion de director o año de los subpuntos del apartado 3
        
        El menu == 4 Dada la primera implementacion de visualizar listas 
            tabuladas con pandas, implementamos otra opcion para verlas a traves de 
            bucles y tabulacion. Puedes elegir cual de las dos formas las quieres 
            visualizar en el apartado 3
        
        El menu == 5 Como el pdf no viene bien explicado, y para dar mas variedad
            de opcion, tambien se implemento que se pueda elegir si se quiere las
            tablas con o sin peliculas repetidas en el apartado 3-4

        El menu == 6 Es simplemente un 'Menu' Donde te restringe poner algo
            distinto de 1 o 0, con las opciones llamadas si/no. Principalmente 
            se implementa para el punto 2, ya que se le puede dar al 2 sin querer 
            en el menu principal y no gusta si se le da sin querer tener que cerrar
            el programa o guardar un archivo obligatoriamente.

    ---------
    Parameters
    ----------

    menu: int
        Eliges que a que menu quieres acceder
    eleccion = int
        variable para elegir el menu del apartado 3
    data_repeat: pd.DataFrame
        dataframe de las peliculas. Lo usamos para ver si poodemos filtrar por año o director 
        sin poner algo que no se debe

        
    -------
    Returns
    -------

    tipo_lista : int.
    quehacer : int
    eleccion : int
    director : str
    año : int
    '''

    
    if menu in (0, 4, 5, 6):
          

        
        if menu == 0:
            salida = 'Tipo de lista a usar: \n  (1)Array_ordered_positional_list\n  (2)Linked_ordered_positional_list\n\n  Eleccion: '

        elif menu == 4:
            salida = '\nForma de visualizar listas: \n  (1)DataFrame\n  (2)Tabulacion\n\n  Eleccion: '

        elif menu == 5:
            salida = '\nQuieres usar repetidos, ¿si o no?: \n  (1)SI usar repetidos\n  (2)NO usar repetidos\n\n  Eleccion: '
        
        elif menu == 6:
               salida = '\n¿Quieres guardar la nueva lista?: \n    (1)SI\n    (2)NO\n\n\tEleccion: '


        while True:

            try:
                eleccion = int(input(salida))
                
                if (eleccion<1 or eleccion>2):
                    raise peli.NumberNotInMenu
                break

            except ValueError:
                print('\nDebes introducir un número\n')

            except peli.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 2\n')


        if eleccion == 1:
            opcion  = True

        else:
            opcion = False

        return opcion
     
    
    elif menu ==1:
        while True:

            try:
                quehacer = int(input('\n---x---\n\nQue quieres ver:\n(1)Lista de peliculas ordenadas\n(2)Lista de películas ordenadas sin duplicados (devuelve un archivo txt con las peliculas)\n(3)Ver algunos listados tabulados\n(4)Mostrar métricas\n(5)Cerrar programa\n\nEleccion: '))
                if quehacer == 5:
                    sys.exit()
                
                
                if (quehacer<1 or quehacer>4):
                    raise peli.NumberNotInMenu
                break
                

            except ValueError:
                print('\nDebes introducir un número\n')

            except peli.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 4\n')


        return quehacer

    elif menu == 2:

        while True:

            try:
                eleccion = int(input('Que quieres hacer: \n    (1)Ver todas las peliculas\n    (2)Peliculas rodadas por un director\n    (3)Peliculas estrenadas en un año \n    (4)Cancelar\n\n\tEleccion: '))
                
                if (eleccion<1 or eleccion>4):
                    raise peli.NumberNotInMenu
                break

            except ValueError:
                print('\nDebes introducir un número\n')

            except peli.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 3\n')

        return eleccion
     
    elif menu == 3:
         
         if eleccion == 2:

            director = input('\nDeme un nombre del director: ')

            while (director not in data_repeat['Director'].values):

                print('\nNo hay peliculas de este director.Si no es asi, asegurese de escribir el nombre como en la tabla')
                director = input('\nDeme un nombre del director: ')

            return director
        



         elif eleccion == 3:

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