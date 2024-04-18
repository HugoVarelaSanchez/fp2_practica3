import curses

def main(pantalla):
    # Configurar curses
    curses.curs_set(0)  # Ocultar el cursor
    pantalla.nodelay(True)  # Configurar para que getch() no bloquee

    # Definir las opciones del primer menú
    opciones_menu_1 = ["Opción 1", "Opción 2", "Opción 3"]
    seleccion_menu_1 = 0

    # Función para imprimir el primer menú en la pantalla
    def imprimir_menu_1():
        for i, opcion in enumerate(opciones_menu_1):
            if i == seleccion_menu_1:
                pantalla.addstr(i, 0, opcion, curses.A_REVERSE)
            else:
                pantalla.addstr(i, 0, opcion)

    # Loop principal del primer menú
    while True:
        #pantalla.clear()  # Borra la pantalla antes de imprimir el menú
        imprimir_menu_1()
        pantalla.refresh()
        key = pantalla.getch()

        # Manejar las teclas de flecha para cambiar la selección del primer menú
        if key == curses.KEY_UP:
            seleccion_menu_1 = (seleccion_menu_1 - 1) % len(opciones_menu_1)
        elif key == curses.KEY_DOWN:
            seleccion_menu_1 = (seleccion_menu_1 + 1) % len(opciones_menu_1)
        # Abrir el segundo menú si se presiona Enter en una opción del primer menú
        elif key == 10:  # 10 es el código de Enter
            pantalla.clear()  # Borra la pantalla antes de imprimir el segundo menú
            break  # Salir del bucle para abrir el segundo menú

    # Definir las opciones del segundo menú
    opciones_menu_2 = ["Subopción 1", "Subopción 2", "Subopción 3"]
    seleccion_menu_2 = 0

    # Función para imprimir el segundo menú en la pantalla
    def imprimir_menu_2():
        for i, opcion in enumerate(opciones_menu_2):
            if i == seleccion_menu_2:
                pantalla.addstr(i, 0, opcion, curses.A_REVERSE)
            else:
                pantalla.addstr(i, 0, opcion)

    # Loop principal del segundo menú
    while True:
        imprimir_menu_2()
        pantalla.refresh()
        key = pantalla.getch()

        # Manejar las teclas de flecha para cambiar la selección del segundo menú
        if key == curses.KEY_UP:
            seleccion_menu_2 = (seleccion_menu_2 - 1) % len(opciones_menu_2)
        elif key == curses.KEY_DOWN:
            seleccion_menu_2 = (seleccion_menu_2 + 1) % len(opciones_menu_2)
        # Volver al primer menú si se presiona Enter en una opción del segundo menú
        elif key == 10:  # 10 es el código de Enter
            break  # Salir del bucle para volver al primer menú

if __name__ == "__main__":
    curses.wrapper(main)
