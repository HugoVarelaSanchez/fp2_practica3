class Pelicula:


    """Clase que almacena los datos de una pelicula.

    Esta clase crea una pelicula la cual contiene los datos de esta.

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


    -------
    Methods
    -------

    def __init__ (self, film_name, director_name, estreno, puntuation, d_real,interaccion, tiempo_inicial)
        Crea los atributos.

    def __str__ (self):
        Muestra por pantalla el proceso.
    
    """ 

    def __init__(self,director_name : str, film_name  : str, estreno : str, puntuation : float):

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

        ------- 
        Returns
        -------

        None.

        """

        self._director_name = director_name
        self._film_name = film_name
        self._estreno = int(estreno)
        self._puntuation = float(puntuation)

    #Atributos

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
    

    #Metodos magicos:
    def __str__(self) -> str:
        return f'Película: {self.film_name}, Director: {self.director_name}, Estreno: {self.estreno}, Puntuation: {self.puntuation}'


    #Metodos magicos comparativos

    #Comparamos si es igual
    def __eq__(self, other):

        if self.director_name == other.director_name:

            if self.estreno == other.estreno:

                if self.film_name == other.film_name:
                    return self.film_name == other.film_name
                
            else:
                return False
        else:
            return False

    #Mayor o igual
    def __ge__(self, other):

        if self.director_name == other.director_name:

            if self.estreno == other.estreno:
                return self.film_name >= other.film_name
            
            else:
                return self.estreno >= other.estreno
            
        else:
            return self.director_name >= other.director_name

    #Mayor
    def __gt__(self, other):
    
        if self.director_name == other.director_name:

            if self.estreno == other.estreno:
                return self.film_name > other.film_name
            
            else:
                return self.estreno > other.estreno
            
        else:
            return self.director_name > other.director_name
        

    #Metodos de ayuda

    def data_values(self):
        lista = [self.film_name, self.director_name, self.estreno, self.puntuation]
        return lista
    


class NumberNotInMenu(Exception):
    pass