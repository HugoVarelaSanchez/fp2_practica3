#Hugo Varela Sanchez; hugo.varela.sanchez@udc.es
#David Fernandez Reimundez; david.fernandez.reimundez@udc.es

#Importamos la libreris sys, y los archivos para implementar el TAD Lista Posicional Ordenada
import sys
import array_ordered_positional_list as aop
import linked_ordered_positional_list as lop


#archivo = sys.argv[1]
archivo = 'peliculas.txt'

class Pelicula:
    """Clase que simula un proceso.

    Esta clase crea el proceso que ejecutara una CPU o GPU, los cuales se usaran para 
    simular la ejecucion de estos.

    ----------
    Attributes
    ----------
    
    film_name: str
    Es el nombre del proceso.

    director_name: str
    Es el nombre del usuario que ejecuta el proceso.

    puntuation: int
    Duracion estimada del procesa. (short / long)

    d_real: int
    Duracion real del proceso.

    interaccion: int
    Unidad de tiempo total

    tiempo_inicial: int
    Unidad en la que el proceso entra a ejecutarse

    -------
    Methods
    -------

    def __init__ (self, film_name, director_name, estreno, puntuation, d_real,interaccion, tiempo_inicial)
        Crea los atributos.

    def __str__ (self):
        Muestra por pantalla el proceso.
    
    """ 

    def __init__(self,director_name : str, film_name  : str, estreno : str, puntuation : int):

        """Asigna atributos al objeto.

        
        ----------
        Parameters
        ----------
        film_name: str
            Es el nombre del proceso.

        director_name: str
            Es el nombre del usuario que ejecuta el proceso.

        puntuation: int
            Duracion estimada del procesa. (short / long)

        d_real: int
            Duracion real del proceso.

        interaccion: int
            Unidad de tiempo total

        tiempo_inicial: int
            Unidad en la que el proceso entra a ejecutarse
        
        penalizado: int
            Unidad que indica la penalización del proceso
            0 -> No ha sido penalizado
            1 -> Ha recibido penalización
            
        entrada_cola: int
            Unidad en la que el proceso entra a su respectiva cola de ejecución

        ------- 
        Returns
        -------

        None.

        """

        self._director_name = director_name
        self._film_name = film_name
        self._estreno = estreno
        self._puntuation = puntuation

    def __str__(self) -> str:
        return f'Película: {self.film_name}, Director: {self.director_name}, Estreno: {self.estreno}, Puntuation: {self.puntuation}'


    @property
    def director_name(self):
        return self._director_name
    

    @property
    def film_name(self):
        return self._film_name
    

    @property
    def estreno(self):
        return self._estreno


    @property
    def puntuation(self):
        return self._puntuation


    #Métodos mágicos comparativos
    def __eq__(self, other):
        if self.director_name == other.director_name:
            if self.estreno == other.estreno:
                if self.film_name == other.film_name:
                    return self.film_name == other.film_name
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        if self.director_name == other.director_name:
            if self.estreno == other.estreno:
                return self.film_name >= other.film_name
            else:
                return self.film_name >= other.estreno
        else:
            return self.director_name >= other.director_name
        
    def __gt__(self, other):
        if self.director_name == other.director_name:
            if self.estreno == other.estreno:
                return self.film_name > other.film_name
            else:
                return self.film_name > other.estreno
        else:
            return self.director_name > other.director_name
        
class NumberNotInMenu(Exception):
    pass

       
lista_peliculas = lop.LinkedOrderedPositionalList()

with open(archivo, 'r') as contenido:
        info_procesos = contenido.read()

while True:
    try:
        quehacer = int(input('Que quieres ver:\n1)Lista de peliculas ordenadas\n2)Lista de películas ordenadas sin duplicados\n3)Ver algunos listados tabulados\n4)Mostrar métricas\n'))
        if (quehacer<1 or quehacer>4):
            raise NumberNotInMenu
        break
    except ValueError:
        print('\nDebes introducir un número\n')
    except NumberNotInMenu:
        print('\nDebe de ser un número del 1 al 4\n')

for line in info_procesos.split('\n'):   

    if len(line) != 0 and len(line.split(';')) == 4:

        datos_pelicula = line.split(';')
        director_name, film_name, estreno, puntuation = datos_pelicula 

        pelicula = Pelicula(director_name, film_name, estreno, puntuation)
        
        lista_peliculas.add(pelicula)

if quehacer == 1:
    for pelicula in lista_peliculas:
        print(pelicula)
elif quehacer == 2:
    
elif quehacer == 3:

else:

