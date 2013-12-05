import pilas

pilas.iniciar()
#Definimos la musica
musica_de_fondo = pilas.musica.cargar("musica.mp3")
musica_de_fondo.reproducir()

#Escena de Menu

class EscenaDeMenu(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        menu = pilas.fondos.DesplazamientoHorizontal()
        menu.agregar("FondoMenu.jpg", y=0, velocidad=1000)

#Creamos las opciones que estaran dentro del menu
        opciones = [
		    ('Comenzar a jugar', self.comenzar),('Ayuda', self.ayuda),
		    ('Salir', self.salir)]

        self.menu = pilas.actores.Menu(opciones)

    def comenzar(self):
        pilas.cambiar_escena(EscenaDeJuego())

    def ayuda(self):
        pilas.cambiar_escena(EscenaDeAyuda())

    def salir(self):
        import sys
        sys.exit(0)

#Escena Del Juego

class EscenaDeJuego(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):

# ACA EMPIEZA EL CODIGO DEL JUEGO -----------------------------------------------------------------------------------------------------------------
        import random
        from megaman import Marciano
        from pilas.actores import Bomba

        #Definimos el fondo
        mapa = pilas.actores.MapaTiled("Mapa.tmx")


        fondo = pilas.fondos.DesplazamientoHorizontal()
        fondo.agregar("fondo3.jpg", y=0, velocidad=0.5)

        #Definimos a la bomba 

        class Enemigo(Bomba):
            
            def __init__(self):
                pilas.actores.Bomba.__init__(self)
                self.izquierda = 320
                self.x = m.x+random.randrange(100, 500)
                self.y = random.randrange(-50, 100)
                self.m = m
                self.actualizar()

            def actualizar(self):
                a = self.y
                if a >= 45:
                    a = random.randrange(45, 150)
                elif a <= 45:
                    a = random.randrange(-20, 50)
           
        def bombaexplotar(m, enemigos):
            enemigos.explotar()
            m.eliminar()
            pilas.avisar("Has perdido")

        def cambiar_posicion_camara():
            pilas.escena_actual().camara.x = [m.x], 0.1
            return True   

        pilas.mundo.agregar_tarea(1/10.0, cambiar_posicion_camara)
        enemigos = []


        #Creamos enemigos 
        def crear_enemigo():
            un_enemigo = Enemigo()
            enemigos.append(un_enemigo)
            return True 
            


        #Definimos el actor
        m = Marciano(mapa)


        Bomba = Enemigo()


        pilas.mundo.colisiones.agregar(m, enemigos, bombaexplotar)
        pilas.mundo.agregar_tarea(2, crear_enemigo)

#----------FIN DEL JUEGO---------------------------------------------------------------------------------------------------------------------------


#Con esto al presionar la tecla m regresamos al menu y la r reiniciamos

        pilas.avisar("Pulsa la tecla 'm' para regresar al menu o 'r' para reiniciar")

        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)

    def cuando_pulsa_tecla(self, evento):
        
        if evento.texto == u'm':
            pilas.cambiar_escena(EscenaDeMenu())
        elif evento.texto == u'r':
            pilas.cambiar_escena(EscenaDeJuego2())

class EscenaDeJuego2(pilas.escena.Base):
    def __init__(self):
        pilas.escena.Base.__init__(self)

#Mismo juego pero necesito ponerlo dos veces por que si no daba un bug ----------------------------------------------------------------------------
    def iniciar(self):
        import random
        from megaman import Marciano
        from pilas.actores import Bomba

        #Definimos el fondo
        mapa = pilas.actores.MapaTiled("Mapa.tmx")


        fondo = pilas.fondos.DesplazamientoHorizontal()
        fondo.agregar("fondo3.jpg", y=0, velocidad=0.5)

        #Definimos a la bomba 

        class Enemigo(Bomba):
            
            def __init__(self):
                pilas.actores.Bomba.__init__(self)
                self.izquierda = 320
                self.x = m.x+random.randrange(200, 500)
                self.y = random.randrange(-50, 100)
                self.m = m
                self.actualizar()

            def actualizar(self):
                a = self.y
                if a >= 45:
                    a = random.randrange(45, 150)
                elif a <= 45:
                    a = random.randrange(-20, 50)
            
        def bombaexplotar(m, enemigos):
            enemigos.explotar()
            m.eliminar()
            pilas.avisar("Has perdido")

        def cambiar_posicion_camara():
            pilas.escena_actual().camara.x = [m.x], 0.1
            return True   


        pilas.mundo.agregar_tarea(1/10.0, cambiar_posicion_camara)
        enemigos = []


        #Creamos enemigos 
        def crear_enemigo():
            un_enemigo = Enemigo()
            enemigos.append(un_enemigo)
            return True 
            


        #Definimos el actor
        m = Marciano(mapa)

        #Definimos el enemgio
        Bomba = Enemigo()


        pilas.mundo.colisiones.agregar(m, enemigos, bombaexplotar)
        pilas.mundo.agregar_tarea(2, crear_enemigo)
#--------------------------------FIN DEL SEGUNDO CODIGO DEL MISMO JUEGO----------------------------------------------------------------------------


#Con esto al precionar la tecla m regresamos al menu y con r reiniciamos

        pilas.avisar("Pulsa la tecla 'q' para regresar al menu o 'r' para reiniciar")

        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)

    def cuando_pulsa_tecla(self, evento):
        
        if evento.texto == u'm':
            pilas.cambiar_escena(EscenaDeMenu())
        elif evento.texto == u'r':
            pilas.cambiar_escena(EscenaDeJuego2())

#CLASE DE LA ESCENA AYUDA 
class EscenaDeAyuda(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        ayuda = pilas.fondos.DesplazamientoHorizontal()
        ayuda.agregar("Ayuda.jpg", y=0, velocidad=1000)
        pilas.avisar("Pulsa la tecla 'm' para volver al menu")

#CON ESTO SE VUELVE AL MENU PERO DESDE LA AYUDA

        pilas.eventos.pulsa_tecla.conectar(self.cuando_pulsa_tecla)
    def cuando_pulsa_tecla(self, evento):
        if evento.texto == u'm':
            pilas.cambiar_escena(EscenaDeMenu())

pilas.cambiar_escena(EscenaDeMenu())


pilas.ejecutar()
