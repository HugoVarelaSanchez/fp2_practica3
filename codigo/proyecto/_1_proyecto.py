import curses, time

def main(pantalla):
    # Configurar curses
    curses.curs_set(0)  # Ocultar el cursor
    pantalla.nodelay(True)  # Configurar para que getch() no bloquee

    # Definir las opciones del menú
    opciones = ["Opción 1", "Opción 2", "Opción 3"]
    seleccion = 0

    # Función para imprimir el menú en la pantalla
    def imprimir_menu():
        #pantalla.clear()
        for i, opcion in enumerate(opciones):
            if i == seleccion:
                pantalla.addstr(i, 0, opcion, curses.A_REVERSE)
            else:
                pantalla.addstr(i, 0, opcion)

    # Loop principal
    while True:
        imprimir_menu()
        key = pantalla.getch()

        # Manejar las teclas de flecha para cambiar la selección
        if key == curses.KEY_UP:
            seleccion = (seleccion - 1) % len(opciones)
        elif key == curses.KEY_DOWN:
            seleccion = (seleccion + 1) % len(opciones)
        # Salir si se presiona Enter
        elif key == 10:  # 10 es el código de Enter
            mensaje = f'Se seleccionó: {opciones[seleccion]}'
            pantalla.addstr(len(opciones), 0, mensaje)
            pantalla.refresh()
            #pantalla.getch()  # Esperar a que el usuario presione una tecla antes de continuar
            time.sleep(2)
            pantalla.clear()

            

if __name__ == "__main__":
    curses.wrapper(main)
