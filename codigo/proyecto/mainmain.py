import sys
import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli
import curses

def main(pantalla):
    archivo = sys.argv[1]
    #archivo = 'peliculas.txt'

    def accion(lista_peliculas, lista_peliculas_norep, quehacer, data_repeat, data_no_repeat):
        
        
        if quehacer == 1:

            pantalla.clear()
            
            for i, pelis in enumerate(lista_peliculas):
                
                pantalla.addstr(i,  0, opcion)
            while True:
                 if key == 10:  # 10 es el código de Enter
                    break
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






         


def main(pantalla):

    def imprimir_menu(opciones_menu, seleccion_menu, texto):
        pantalla.addstr(0, 0, texto)  # Agregar el texto del menú en la parte superior de la pantalla
        for i, opcion in enumerate(opciones_menu):
            if i == seleccion_menu:
                pantalla.addstr(i+1, 0, opcion, curses.A_REVERSE)
            else:
                pantalla.addstr(i+1, 0, opcion)
    #Inicializamos las listas

    curses.curs_set(0)  # Ocultar el cursor
    pantalla.nodelay(True)  # Configurar para que getch() no bloquee

    opciones_menu_0 = ["(1)Array_ordered_positional_list", '(2)Linked_ordered_positional_list']
    seleccion_menu_0 = 0
    texto_menu_0 = 'Tipo de lista a usar: '

    
    while True:
        #pantalla.clear()  # Limpiar la pantalla antes de imprimir
        pantalla.addstr(0, 0, texto_menu_0)  # Agregar el texto del menú en la parte superior de la pantalla
        imprimir_menu(opciones_menu_0, seleccion_menu_0, texto_menu_0)
        pantalla.refresh()
        key = pantalla.getch()

        # Manejar las teclas de flecha para cambiar la selección del segundo menú
        if key == curses.KEY_UP:
            seleccion_menu_0 = (seleccion_menu_0 - 1) % len(opciones_menu_0)
        elif key == curses.KEY_DOWN:
            seleccion_menu_0 = (seleccion_menu_0 + 1) % len(opciones_menu_0)
        # Volver al primer menú si se presiona Enter en una opción del segundo menú
        elif key == 10:  # 10 es el código de Enter
            tipo_lista = opciones_menu_0[seleccion_menu_0]
        
            break  # Salir del bucle para volver al primer menú
                
        # Imprimir el mensaje
        #pantalla.clear()







    #Elegimos con que tipo de listas queremos hacer la practica
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






    while True:

    









if __name__ == "__main__":
    curses.wrapper(main)
