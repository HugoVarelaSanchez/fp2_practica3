#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es

#Hay que filtrar el apartado 2-3 por listas en vez del dataframe
#En una clase un profesor dice que el apartado 3 no se puede hacer de x manera y manda un correo y en otra dice  que si que vale, y en una dicen que el apartado 4 es de una y en otra que es de otra, lo hacemos con tantas opciones para que digan lo que digan este la opcion

#Importamos la libreris sys, y los archivos para implementar el TAD Lista Posicional Ordenada
import sys
import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli
<<<<<<< HEAD
import curses


#---------------------------------------------------------------------------------------------------------------



=======
>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020


#---------------------------------------------------------------------------------------------------------------

def menus(menu,  eleccion = int, data_repeat = pd.DataFrame, lista = list):
    
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

<<<<<<< HEAD
        eleccion = int(input(salida))
                
=======

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


>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020
        if eleccion == 1:
            opcion  = True

        else:
            opcion = False

        return opcion
     
<<<<<<< HEAD
#---------------------------------------------------------------------------

    elif menu ==1:
           
            quehacer = int(input('\n---x---\n\nQue quieres ver:\n(1)Lista de peliculas ordenadas\n(2)Lista de películas ordenadas sin duplicados (devuelve un archivo txt con las peliculas)\n(3)Ver algunos listados tabulados\n(4)Mostrar métricas\n(5)Cerrar programa\n\nEleccion: '))
            if quehacer == 5:
                sys.exit()
    
            if quehacer == 1:
                quehacer  = True

            else:
                quehacer = False

            return quehacer
    
            

#---------------------------------------------------------------------------

    elif menu == 2:

        
        eleccion = int(input('Que quieres hacer: \n    (1)Ver todas las peliculas\n    (2)Peliculas rodadas por un director\n    (3)Peliculas estrenadas en un año \n    (4)Cancelar\n\n\tEleccion: '))
                
                
        if eleccion == 1:
                eleccion  = True

        else:
                eleccion = False

        return eleccion
     
#---------------------------------------------------------------------------

    elif menu == 3:
         

         #-----------------------------------------------------------------------------
=======
    
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
         
>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020
         if eleccion == 2:

            director = input('\nDeme un nombre del director: ')

            while (director not in data_repeat['Director'].values):

                print('\nNo hay peliculas de este director.Si no es asi, asegurese de escribir el nombre como en la tabla')
                director = input('\nDeme un nombre del director: ')

            return director
        
<<<<<<< HEAD
            #-----------------------------------------------------------------------------
=======

>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020


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
         
<<<<<<< HEAD
         #-----------------------------------------------------------------------------
=======

>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020

         elif eleccion == 4:
             
             director = input('\nDeme un nombre del director: ')
             aux = []

             for y in lista:
                 aux.append(y.director_name)

             while (director not in aux):

                print('\nNo hay peliculas de este director. Si no es asi, asegurese de escribir el nombre como en la tabla')
                director = input('\nDeme un nombre del director: ')

             return director
         
<<<<<<< HEAD
         #-----------------------------------------------------------------------------
=======

>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020
         elif eleccion == 5:
            aux = []
            for y in lista:
                 aux.append(y.estreno)

            while True:

                try:
                    año = int(input('\nDeme un año: '))

                    if (año not in aux):
                        raise peli.NumberNotInMenu
                    break

                except ValueError:
                    print('\nDebes introducir un año\n')

                except peli.NumberNotInMenu:
                    print('\nNo se encuentra ninguna peli con ese año, busque otro\n')


            return año




<<<<<<< HEAD








=======
>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020
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

    #---------------------------------------------------------------------------------






    elif quehacer == 2:
        print('\nTodas las peliculas sin repetidos:\n')
        for pelicula in lista_peliculas_norep:
            print(pelicula)

        aux_eleccion = menus(6)

        if aux_eleccion == True:

            nombre_archivo = input('\n¿Como quieres que se llame el archivo?: ')

            with open(f'{nombre_archivo}', 'w', encoding='utf-8') as archivo:
                for pelii in lista_peliculas_norep:
                    archivo.write(f'{pelii.director_name}; {pelii.film_name}; {pelii.estreno}; {pelii.puntuation}\n')

        else:
            pass




    #------------------------------------------------------------------------------


    elif quehacer == 3:





        eleccion = menus(2)
        





        if eleccion == 1:

            opcion = menus(5)

            if opcion == True:
                    conclusion = lista_peliculas
                    conclusion_data = data_repeat
            else:
                    conclusion = lista_peliculas_norep
                    conclusion_data = data_no_repeat

            opcion = menus(4)

            if opcion == True:
                print('\n Listado de peliculas tabuladas: \n', conclusion_data)
            else:
                new_aux_list = ['Título', 'Director', 'Año','Puntuación']
                cadena_sup = ''
                for i in new_aux_list:
                    columna =  f"{i: ^37}"
                    cadena_sup = cadena_sup + f'\t{columna}'

                

                print('\n',cadena_sup)

                separador = '-'*37
                lineas = f'\t{separador}'*4
                print(lineas)
                
                for i in conclusion:
                    film_name = f"{i.film_name: ^37}" 
                    director_name = f"{i.director_name: ^37}" 
                    estreno =  f"{i.estreno: ^37}" 
                    puntuation = f"{i.puntuation: ^37}"
                    print(f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

                separador = '-'*37
                lineas = f'\t{separador}'*4
                print(lineas)

               


    #-------------------------------------------------------------------------------




        elif eleccion == 2:

            
            
            opcion = menus(5)
            
            if opcion == True:
                    conclusion = lista_peliculas
                    conclusion_data = data_repeat
            else:
    
                    conclusion = lista_peliculas_norep
                    conclusion_data = data_no_repeat
            
            opcion = menus(4)

            if opcion == True:
                
                director = menus(3, eleccion, data_repeat)

                data_director = conclusion_data[conclusion_data['Director'] == director]
                print(f'\nPeliculas de {director}:\n\n', data_director)


            else:
                

                director = menus(3, 4, data_repeat, conclusion)

                new_aux_list = ['Título', 'Director', 'Año','Puntuación']
                cadena_sup = ''
                for i in new_aux_list:
                    columna =  f"{i: ^37}"
                    cadena_sup = cadena_sup + f'\t{columna}'

                

                print('\n',cadena_sup)

                separador = '-'*37
                lineas = f'\t{separador}'*4
                print(lineas)
                
                aux = []
                for y in conclusion:
                    if director == y.director_name:
                        aux.append(y)

                for i in aux:
                    
                    film_name = f"{i.film_name: ^37}" 
                    director_name = f"{i.director_name: ^37}" 
                    estreno =  f"{i.estreno: ^37}" 
                    puntuation = f"{i.puntuation: ^37}"
                    print(f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

                separador = '-'*37
                lineas = f'\t{separador}'*4
                print(lineas)

    #-------------------------------------------------------------------------------



        elif eleccion == 3:
            

            opcion = menus(5)
            print(opcion)
            if opcion:
                conclusion = lista_peliculas
                conclusion_data = data_repeat
            else:
                conclusion = lista_peliculas_norep
                conclusion_data = data_no_repeat


            opcion = menus(4)

            if opcion==True:
                año = menus(3, eleccion, data_repeat)
                data_año = conclusion_data[conclusion_data['Año'] == año]
                print(f'\nPeliculas del año: {año}:\n\n', data_año)

            else:
                
                año = menus(3, 5, data_repeat, conclusion)


                new_aux_list = ['Título', 'Director', 'Año','Puntuación']
                cadena_sup = ''

                for i in new_aux_list:
                    columna =  f"{i: ^37}"
                    cadena_sup = cadena_sup + f'\t{columna}'

                print('\n',cadena_sup)

                separador = '-'*37
                lineas = f'\t{separador}'*4
                print(lineas)
                
                aux = []

                for y in conclusion:
                    if año == y.estreno:
                        aux.append(y)

                for i in aux:
                    
                    film_name = f"{i.film_name: ^37}" 
                    director_name = f"{i.director_name: ^37}" 
                    estreno =  f"{i.estreno: ^37}" 
                    puntuation = f"{i.puntuation: ^37}"
                    print(f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

                separador = '-'*37
                lineas = f'\t{separador}'*4
                print(lineas)
    
    



    #-------------------------------------------------------------------------------

    elif quehacer == 4:
            
            opcion = menus(5)

            if opcion == True:
                    conclusion = lista_peliculas
                    conclusion_data = data_repeat
            else:
                    conclusion = lista_peliculas_norep
                    conclusion_data = data_no_repeat
            
            #1
            print('\nPeliculas creadas por director: \n')
            group_col = 'Director'
            num_peliculas_por_director = conclusion_data.groupby(group_col).size()
            print(num_peliculas_por_director, '\n')

            #2
            print('\nPuntuacion media por director: \n')
            group_col = 'Director'
            target_col = 'Puntuacion'
            puntuation_per_director = conclusion_data.groupby(group_col).agg({target_col :["mean"]})
            print(puntuation_per_director, '\n')

            #3
            print('\nPuntuacion media por año: \n')
            group_col = 'Año'
            target_col = 'Puntuacion'
            puntuation_per_year = conclusion_data.groupby(group_col).agg({target_col :["mean"]})
            print(puntuation_per_year, '\n')


            
#-----------------------------------------------------------------------------------------------------------------------------------



<<<<<<< HEAD
def main(pantalla):
=======
def main():
>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020
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

    #Elegimos con que tipo de listas queremos hacer la practica

    tipo_lista = menus(0)


    if tipo_lista == 1:
        lista_peliculas       = aop.ArrayOrderedPositionalList()
        lista_peliculas_norep = aop.ArrayOrderedPositionalList()
        lista_peliculas_copy  = aop.ArrayOrderedPositionalList()  

    else:
        lista_peliculas       = lop.LinkedOrderedPositionalList()
        lista_peliculas_norep = lop.LinkedOrderedPositionalList()
        lista_peliculas_copy  = lop.LinkedOrderedPositionalList()
    #Hacemos esto ya que en el pdf especfica que se pueden usar ambas implementaciones.
    #Al poder definir que lista creas, se ve que uses la que uses, al usar metodos comunes
    #Puedes usar un tipo o otro indiferentemente



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

    quehacer = menus(1)
    
<<<<<<< HEAD


    curses.curs_set(0)  # Ocultar el cursor
    pantalla.nodelay(True)

    def imprimir_menu_1(opciones, elejida):
        for i, opcion in enumerate(opciones):

            if i == elejida:
                pantalla.addstr(i, 0, opcion, curses.A_REVERSE)
            else:
                pantalla.addstr(i, 0, opcion)






















=======
>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020
    while True:

        accion(lista_peliculas, lista_peliculas_norep, quehacer, data_repeat, data_no_repeat)
        quehacer = menus(1)
        

if __name__ == "__main__":
<<<<<<< HEAD
    curses.wrapper(main)
=======
    main()
>>>>>>> e63efdf92a085ed199d31d2d999eb80f94a9c020
