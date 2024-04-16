#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es

#Preguntas: Se asumen repetidos en el apartado 4? Asumimos no repetidos
#Recordar: implementar opcion de cancelar y volver menu principal
#Implementar poder elegir por que las quieres ordenar
#Implementar si en el apartado 3-4 se trate con las listas con/sin repetidas


#Importamos la libreris sys, y los archivos para implementar el TAD Lista Posicional Ordenada
import sys, time
import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli


#---------------------------------------------------------------------------------------------------------------

def menus(menu, eleccion = int, data_repeat = pd.DataFrame):
    '''
    Funcion de ayuda. Esta funcion lo que hace gestionar los 4 menus de la practica:
        El menu de eleccion de tipo de lista
        El menu de eleccion entre los 4 puntos de la practica.
        El menu de eleccion entre los puntos del punto 3
        Un menu para poder elegir (sin tener opcion a poner algo que no debes) director y año
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


    #Menu 1 (Eleccion de tipo de listas) (1-2)
    if menu == 0:

        while True:

            try:
                tipo_lista = int(input('Tipo de lista a usar: \n  (1)Array_ordered_positional_list\n  (2)Linked_ordered_positional_list\n\n  Eleccion: '))
            
                if (tipo_lista<1 or tipo_lista>2):
                    raise peli.NumberNotInMenu
                break
            

            except ValueError:
                print('\nDebes introducir un número\n')

            except peli.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 2\n')


        return tipo_lista
    




    #Menu principal (1-4)
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




    #Menu del apartado 2 (Eleccion de peliculas del apartado 3) (1-3)
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
    



    #Eleccion correcta de año o director apartado 3.2 - 3.3
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


    elif menu == 4:
        rescata = bool
        while True:

            try:
                opcion = int(input('\nForma de visualizar listas: \n  (1)DataFrame\n  (2)Tabulacion\n\n  Eleccion: '))
            
                if (opcion<1 or opcion>2):
                    raise peli.NumberNotInMenu
                break
            

            except ValueError:
                print('\nDebes introducir un número\n')

            except peli.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 2\n')

        if opcion == 1:
            rescata = True
        else:
            rescata = False
        return rescata
    



    elif menu == 5:
        
        while True:

            try:
                opcion = int(input('\nQuieres usar repetidos, ¿si o no?: \n  (1)SI usar repetidos\n  (2)NO usar repetidos\n\n  Eleccion: '))
            
                if (opcion<1 or opcion>2):
                    raise peli.NumberNotInMenu
                break
            

            except ValueError:
                print('\nDebes introducir un número\n')

            except peli.NumberNotInMenu:
                print('\nDebe de ser un número del 1 al 2\n')

        if opcion == 1:
            rescata = True
        else:
            rescata = False
        return rescata





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

        nombre_archivo = input('\n¿Como quieres que se llame el archivo?: ')

        with open(f'{nombre_archivo}', 'w', encoding='utf-8') as archivo:
            for pelii in lista_peliculas_norep:
                archivo.write(f'{pelii.director_name}; {pelii.film_name}; {pelii.estreno}; {pelii.puntuation}\n')






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

                # if opcion == True:
                    
                #     print('\n', new_aux_list[0])
                #     for i in lista_peliculas:
                #         print(f'\t{i.film_name}\t\t{i.director_name}\t\t{i.estreno}\t{i.puntuation}')
                
                # else:
                #     print('\n', new_aux_list[0])
                #     for i in lista_peliculas_norep:
                #         print(f'\t{i.film_name}\t\t{i.director_name}\t\t{i.estreno}\t{i.puntuation}')







        elif eleccion == 2:

            director = menus(3, eleccion, data_repeat)
            
            opcion = menus(5)
            
            if opcion == True:
                    conclusion = lista_peliculas
                    conclusion_data = data_repeat
            else:
    
                    conclusion = lista_peliculas_norep
                    conclusion_data = data_no_repeat
            
            opcion = menus(4)

            if opcion == True:
                
                
                data_director = conclusion_data[conclusion_data['Director'] == director]
                print(f'\nPeliculas de {director}:\n\n', data_director)

            else:
                

                new_aux_list = [f'\tTitulo \t\tDirector \tFecha Estreno \tPuntuacion\n']


                new_aux_list = [f'\tTitulo \t\tDirector \tFecha Estreno \tPuntuacion\n']
                lista_de_autores = []
                for i in conclusion:
                    if i.director_name == director:
                        lista_de_autores.append(i)

                if len(lista_de_autores) >= 1:
                    print(new_aux_list[0])
                    for i in lista_de_autores:
                        print(f'{i.film_name}\t{i.director_name}\t{i.estreno}\t{i.puntuation}')


        elif eleccion == 3:
            año = menus(3, eleccion, data_repeat)

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
                data_año = conclusion_data[conclusion_data['Año'] == año]
                print(f'\nPeliculas del año: {año}:\n\n', data_año)

            else:
                
                new_aux_list = [f'\tTitulo \t\tDirector \tFecha Estreno \tPuntuacion\n']
                lista_de_estrenos = []
                for i in conclusion:
                    if i.estreno == año:
                        lista_de_estrenos.append(i)

                if len(lista_de_estrenos) >= 1:
                    print(new_aux_list[0])
                    for i in lista_de_estrenos:
                        print(f'{i.film_name}\t{i.director_name}\t{i.estreno}\t{i.puntuation}')
    
    



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
    
    while True:

        accion(lista_peliculas, lista_peliculas_norep, quehacer, data_repeat, data_no_repeat)
        quehacer = menus(1)
        

if __name__ == "__main__":
    main()
