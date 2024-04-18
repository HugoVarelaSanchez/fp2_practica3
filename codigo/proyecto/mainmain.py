import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop
import pandas as pd
import class_pelicula as peli
import curses, time, sys

#24, 37, 242, 256


def aux_filtro_director(pantalla, lista, dataframe):
	
	pantalla.clear()
	pantalla.addstr(0, 0, 'Nombre del director:')
	pantalla.refresh()
	
	director = pantalla.getstr(1, 0, 20)
	aux = []

	for y in lista:
		aux.append(y.director_name)

	while (director not in aux):

		pantalla.addstr(0, 0, 'No hay peliculas de este director. Si no es asi, asegurese de escribir el nombre como en la tabla')
		pantalla.refresh()


		director = pantalla.getstr(1, 0, 20)

	return director
	
def aux_filtro_año(pantalla, lista, dataframe):
	aux = []
	for y in lista:
		aux.append(y.estreno)

	while True:

		try:

			año = pantalla.getstr(1, 0, 20)

			if (año not in aux):
				raise peli.NumberNotInMenu
			break

		except ValueError:
			print('\nDebes introducir un año\n')

		except peli.NumberNotInMenu:
			print('\nNo se encuentra ninguna peli con ese año, busque otro\n')


	return año
	



def menus(pantalla, menu, seleccion=int, lista_rep=list, lista_norep=list, data=pd.DataFrame, data_norep=pd.DataFrame):
	pantalla.clear()
	seleccion_menu_0 = 0
	if menu == 1:
		texto = '¿Que quieres hacer?'
		opciones = ['Lista peliculas ordenadas', 'Lista peliculas sin duplicados (puede generar archivo)', 'Visualizacion listados tabulados', 'Metricas', 'Exit']
		bombo = [1, 2, 3, 4, 5]
		clat = {'Lista peliculas ordenadas': 1,'Lista peliculas sin duplicados (puede generar archivo)': 2,'Visualizacion listados tabulados': 3,'Metricas': 4,'Exit': 5}
	elif menu == 2:
		texto = 'Que quieres hacer'
		opciones = ['Ver todos los archivos', 'Filtrar por director', 'Filtrar por año', 'Cancelar']
		bombo = [1, 2, 3, 4]
		clat = {'Ver todos los archivos':1, 'Filtrar por director':2, 'Filtrar por año':3, 'Cancelar':4}
	elif menu == 3:
		texto = '¿Quiere generar un archivo nuevo?'
		opciones = ['Si', 'No']
		bombo = [1, 2]
		clat = {'Si':1, 'No':2}
	elif menu == 4:
		texto = '¿Quiere usar repetidos o no?'
		opciones = ['Repetidos', 'Sin repetidos']
		bombo = [1, 2]
		clat = {'Repetidos':1, 'Sin repetidos':2}
	elif menu == 5:
		texto = '¿Quiere representar un dataframe o lista tabulada?'
		opciones = ['Usar DataFrame', 'Usar tabulacion']
		bombo = [1, 2]
		clat = {'Usar DataFrame':1, 'Usar tabulacion':2}
	
	elif menu == 6:
		sys.exit()

	
	while True:
		pantalla.addstr(0, 0, texto)  
		for i, opcion in enumerate(opciones):
			if i == seleccion_menu_0:
				pantalla.addstr(i+1, 0, opcion, curses.A_REVERSE)
			else:
				pantalla.addstr(i+1, 0, opcion)
		
		pantalla.refresh()
		key = pantalla.getch()

		# Manejar las teclas de flecha para cambiar la selección del segundo menú
		if key == curses.KEY_UP:
			seleccion_menu_0 = (seleccion_menu_0 - 1) % len(opciones)

		elif key == curses.KEY_DOWN:
			seleccion_menu_0 = (seleccion_menu_0 + 1) % len(opciones)

		# Volver al primer menú si se presiona Enter en una opción del segundo menú
		elif key == 10:  # 10 es el código de Enter
			saras = opciones[seleccion_menu_0]
			result = clat[saras]
			

			break

	return result



def accion(pantalla, accion, lista_rep=list, lista_norep=list, data=pd.DataFrame, data_norep=pd.DataFrame):

	if accion == 5:
		sys.exit()



	elif accion == 1:
		pantalla.clear()
		pantalla.addstr(0, 0, 'Lista de todas las peliculas:')
		for i, pelis in enumerate(lista_rep): 
			pantalla.addstr(i+1, 0, f'Director: {pelis.director_name}, Pelicula: {pelis.film_name} Estreno: {pelis.estreno}, Puntuation: {pelis.puntuation}')
			if i == len(lista_rep)-1:
				pantalla.addstr(i+2, 0, 'Pulse enter para continuar.')


		pantalla.addstr('Pulse enter para continuar.')

		while True:
			pantalla.refresh()
			key = pantalla.getch()
			
			if key == 10:
				break




	if accion == 2:

		pantalla.clear()
		pantalla.refresh()

		pantalla.addstr(0, 0, 'Lista de todas las peliculas sin repetidos:')

		for i, pelis in enumerate(lista_norep): 
			pantalla.addstr(i+1, 0, f'Director: {pelis.director_name}, Pelicula: {pelis.film_name} Estreno: {pelis.estreno}, Puntuation: {pelis.puntuation}')
			ultimo = i
		
		pantalla.addstr(i+2, 0, 'Pulse enter para continuar.')
		pantalla.refresh()
		while True:
			pantalla.refresh()
			key = pantalla.getch()

			if key == 10:
				break

		
		pantalla.refresh()

		guardar = menus(pantalla, 3)
		

		if guardar == 1:
			nombre_archivo = 'Peliculas_sin_repetir.txt'
			with open(f'{nombre_archivo}', 'w', encoding='utf-8') as archivo:
				for pelii in lista_norep:
					archivo.write(f'{pelii.director_name}; {pelii.film_name}; {pelii.estreno}; {pelii.puntuation}\n')

			pantalla.clear()
			pantalla.addstr(0, 0, 'Lista guardada')
			pantalla.addstr(1, 0, 'Presione enter para continuar')
			pantalla.refresh()
			while True:
				pantalla.refresh()
				key = pantalla.getch()
				
				if key == 10:
					break


              # Salir del bucle cuando se haya hecho una selección




	if accion == 3:
		siguiente = menus(pantalla, 2)
		
		if siguiente in (1, 2, 3):
			rep = menus(pantalla, 4)
			pri = menus(pantalla, 5)



			if rep == 1:
					conclusion = lista_rep
					conclusion_data = data
					tx = 'con'
			else:
					conclusion = lista_norep
					conclusion_data = data_norep
					tx = 'sin'



			if siguiente == 1:
				if pri == 1:
					pantalla.clear()

					pantalla.addstr(0, 0, f'Todas las peliculas tabuladas y ordenadas en formato DataFrame {tx} repetidos')
					pantalla.addstr(1, 0, conclusion_data.to_string())
					long = (len(conclusion_data))
					pantalla.addstr(long+6, 0, 'Pulse enter para continuar')

					pantalla.refresh()

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break


				else:
					pantalla.clear()
					pantalla.addstr(0, 0, f'Todas las peliculas tabuladas y ordenadas en formato lista tabulada {tx} repetidos')

					new_aux_list = ['Título', 'Director', 'Año','Puntuación']
					cadena_sup = ''

					for i in new_aux_list:
						columna =  f"{i: ^37}"
						cadena_sup = cadena_sup + f'\t{columna}'
					
					pantalla.addstr(2, 0, cadena_sup)


					separador = '-'*37
					lineas = f'\t{separador}'*4

					pantalla.addstr(3, 0, lineas)
					
					for lo, i in enumerate(conclusion):
						film_name = f"{i.film_name: ^37}" 
						director_name = f"{i.director_name: ^37}" 
						estreno =  f"{i.estreno: ^37}" 
						puntuation = f"{i.puntuation: ^37}"
						pantalla.addstr(lo+4, 0, f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")
						iii = lo

					separador = '-'*37
					lineas = f'\t{separador}'*4
					pantalla.addstr(int(lo+6), 0, lineas)
					pantalla.refresh()

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break








			elif siguiente == 2:
				
					
					
				if pri == 1:
					
					#------------------------------
					director = aux_filtro_director(pantalla, conclusion, conclusion_data)
					#------------------------------


					data_director = conclusion_data[conclusion_data['Director'] == director]
					print(f'\nPeliculas de {director}:\n\n', data_director)


				else:
					

					director = aux_filtro_director(pantalla, conclusion, conclusion_data)

					pantalla.clear()
					pantalla.addstr(0, 0, f'Todas las peliculas de {director} tabuladas y ordenadas en formato lista tabulada {tx} repetidos')

					new_aux_list = ['Título', 'Director', 'Año','Puntuación']
					cadena_sup = ''
					for i in new_aux_list:
						columna =  f"{i: ^37}"
						cadena_sup = cadena_sup + f'\t{columna}'

					
					pantalla.addstr(2, 0, cadena_sup)

					separador = '-'*37
					lineas = f'\t{separador}'*4
					pantalla.addstr(3, 0, lineas)

					aux = []
					for y in conclusion:
						if director == y.director_name:
							aux.append(y)

					for i in aux:
						
						film_name = f"{i.film_name: ^37}" 
						director_name = f"{i.director_name: ^37}" 
						estreno =  f"{i.estreno: ^37}" 
						puntuation = f"{i.puntuation: ^37}"
						pantalla.addstr(lo+4, 0, f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

					separador = '-'*37
					lineas = f'\t{separador}'*4
					pantalla.addstr(int(lo+6), 0, lineas)
					pantalla.refresh()

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break


				






			elif siguiente == 3:
				if pri == 1:
					
					#------------------------------
					año = aux_filtro_año(pantalla, conclusion, conclusion_data)
					#------------------------------


					data_año = conclusion_data[conclusion_data['Año'] == año]
					print(f'\nPeliculas de {año}:\n\n', data_año)


				else:
					

					año = aux_filtro_año(pantalla, conclusion, conclusion_data)

					pantalla.clear()
					pantalla.addstr(0, 0, f'Todas las peliculas de {año} tabuladas y ordenadas en formato lista tabulada {tx} repetidos')

					new_aux_list = ['Título', 'Director', 'Año','Puntuación']
					cadena_sup = ''

					for i in new_aux_list:
						columna =  f"{i: ^37}"
						cadena_sup = cadena_sup + f'\t{columna}'

					
					pantalla.addstr(2, 0, cadena_sup)

					separador = '-'*37
					lineas = f'\t{separador}'*4
					pantalla.addstr(3, 0, lineas)

					aux = []
					for y in conclusion:
						if año == y.estreno:
							aux.append(y)

					for i in aux:
						
						film_name = f"{i.film_name: ^37}" 
						director_name = f"{i.director_name: ^37}" 
						estreno =  f"{i.estreno: ^37}" 
						puntuation = f"{i.puntuation: ^37}"
						pantalla.addstr(lo+4, 0, f"\t{film_name}\t{director_name}\t{estreno}\t{puntuation}")

					separador = '-'*37
					lineas = f'\t{separador}'*4
					pantalla.addstr(int(lo+6), 0, lineas)
					pantalla.refresh()

					while True:
						pantalla.refresh()
						key = pantalla.getch()

						if key == 10:
							pantalla.clear()
							break






	






	if accion == 4:
		rep = menus(pantalla, 4)

		if rep == 1:
					conclusion = lista_rep
					conclusion_data = data
		else:
					conclusion = lista_norep
					conclusion_data = data_norep

	#--------------------------------------------------------------

		pantalla.clear()
		
		pantalla.addstr(0, 0, 'Peliculas creadas por director: ')
		
		group_col = 'Director'
		num_peliculas_por_director = conclusion_data.groupby(group_col).size()
		pantalla.addstr(2, 0, num_peliculas_por_director.to_string())
		long = len(num_peliculas_por_director)
		
    
		pantalla.refresh()

		pantalla.addstr(long+4, 0, 'Pulse enter para continuar')

		while True:
				pantalla.refresh()
				key = pantalla.getch()
			
				if key == 10:
					pantalla.clear()
					break
		
#-----------------------------------------------------------------

		pantalla.addstr(0, 0, 'Peliculas creadas por director: ')
		
		group_col = 'Director'
		target_col = 'Puntuacion'
		puntuation_per_director = conclusion_data.groupby(group_col).agg({target_col :["mean"]})
		pantalla.addstr(2, 0, puntuation_per_director.to_string())
		long = len(puntuation_per_director)
		
    
		pantalla.refresh()

		pantalla.addstr(long+6, 0, 'Pulse enter para continuar')

		while True:
				pantalla.refresh()
				key = pantalla.getch()
			
				if key == 10:
					pantalla.clear()
					break
	#----------------------------------------------------------
		pantalla.clear()
		
		pantalla.addstr(0, 0, 'Puntuacion media por director: ')
		
		group_col = 'Año'
		target_col = 'Puntuacion'
		puntuation_per_year = conclusion_data.groupby(group_col).agg({target_col :["mean"]})
		pantalla.addstr(2, 0, puntuation_per_year.to_string())
		long = len(puntuation_per_year)
		
    
		pantalla.refresh()

		pantalla.addstr(long+6, 0, 'Pulse enter para continuar')

		while True:
				pantalla.refresh()
				key = pantalla.getch()
			
				if key == 10:
					pantalla.clear()
					break
		

	#----------------------------------------------------

		





def main():
	#archivo = sys.argv[1]
	archivo = 'peliculas.txt'
	pantalla = curses.initscr()
			


	def imprimir_menu(opciones_menu, seleccion_menu, texto):

		pantalla.addstr(0, 0, texto)  # Agregar el texto del menú en la parte superior de la pantalla

		for i, opcion in enumerate(opciones_menu):

			if i == seleccion_menu:
				pantalla.addstr(i+1, 0, opcion, curses.A_REVERSE)
			else:
				pantalla.addstr(i+1, 0, opcion)


	curses.curs_set(0)  # Ocultar el cursor
	pantalla.nodelay(True)  # Configurar para que getch() no bloquee
	pantalla.keypad(True) #Activa el poder pasar valores por teclado


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
			pantalla.clear()
			
			break  # Salir del bucle para volver al primer menú
				
		# Imprimir el mensaje
		#pantalla.clear()






	#Elegimos con que tipo de listas queremos hacer la practica
	if tipo_lista == "(1)Array_ordered_positional_list":
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
		siguiente = menus(pantalla, 1, lista_rep=lista_peliculas, lista_norep=lista_peliculas_norep, data=data_repeat, data_norep=data_no_repeat )

		pantalla.clear()
		pantalla.refresh()
		pantalla.clear()
		pantalla.refresh()
		
		

		if siguiente == 5:
			accion(pantalla, 5)
			
		elif siguiente == 1:
			accion(pantalla, 1, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)

		elif siguiente == 2:
			accion(pantalla, 2, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)
		
		elif siguiente == 3:
			accion(pantalla, 3, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)
		
		elif siguiente == 4:
			accion(pantalla, 4, lista_peliculas, lista_peliculas_norep, data_repeat, data_no_repeat)
		
		




if __name__ == "__main__":
	main()
