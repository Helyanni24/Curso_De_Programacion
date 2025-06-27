#HELYANNI RODRIGUEZ
def iniciar_juego():
    print("¡Bienvenido a la Aventura de Elara!")
    print("Estás en un bosque oscuro y misterioso. De repente, encuentras dos objetos un FOSFORO y una LINTERNA. ¿Cuál eliges?")
    
    eleccion1 = input("Escribe 'fosforo' o 'linterna': ").strip().lower()

    if eleccion1 == "fosforo":
        escena_fosforo()
    elif eleccion1 == "linterna":
        escena_linterna()
    else:
        print("Opción no válida. Por favor, elige 'fosforo' o 'linterna'.")
        iniciar_juego()

def escena_fosforo():
    print("Coges el fósforo y lo enciendes. Por un instante, el bosque se ilumina y ves un gran oso salvaje.")
    print("El fósforo se apaga rápidamente. ¿Qué haces?")
    
    eleccion2 = input("Escribe 'correr' o 'esconderte': ").strip().lower()

    if eleccion2 == "correr":
        print("Corres tan rápido como puedes, pero el oso te persigue. Te escapas a un claro y encuentras un lago.")
        escena_lago()
    elif eleccion2 == "esconderte":
        print("Te escondes detrás de un árbol. El oso se aleja, pero ahora estás perdido en el bosque.")
        escena_perdido()
    else:
        print("Opción no válida. Por favor, elige 'correr' o 'esconderte'.")
        escena_fosforo()

def escena_linterna():
    print("Coges la linterna y la enciendes. El camino se ilumina frente a ti, pero escuchas un ruido a tu lado.")
    print("¿Qué haces?")
    
    eleccion3 = input("Escribe 'seguir' el camino o 'buscar' en los árboles: ").strip().lower()

    if eleccion3 == "seguir":
        print("Sigues el camino y llegas a una cueva misteriosa. Dentro, encuentras un tesoro escondido.")
        escena_tesoro()
    elif eleccion3 == "buscar":
        print("Buscas entre los árboles y descubres una criatura mágica que te ofrece un deseo.")
        escena_deseo()
    else:
        print("Opción no válida. Por favor, elige 'seguir' o 'buscar'.")
        escena_linterna()

def escena_lago():
    print("En el lago, ves un bote pequeño. ¿Qué decides hacer?")
    
    eleccion4 = input("Escribe 'navegar' en el bote o 'regresar' al bosque: ").strip().lower()

    if eleccion4 == "navegar":
        print("Navegas por el lago y encuentras una isla mágica llena de flores brillantes. ¡Has encontrado un nuevo hogar!")
    elif eleccion4 == "regresar":
        print("Regresas al bosque y te pierdes nuevamente, pero descubres que puedes hablar con los animales.")
    else:
        print("Opción no válida. Por favor, elige 'navegar' o 'regresar'.")
        escena_lago()

def escena_perdido():
    print("Estás perdido en el bosque y comienzas a sentirte asustado. De repente, encuentras un camino iluminado.")
    
    eleccion5 = input("Escribe 'seguir' el camino iluminado o 'gritar' por ayuda: ").strip().lower()

    if eleccion5 == "seguir":
        print("Sigues el camino y llegas a un pueblo donde todos te reciben con alegría. ¡Estás a salvo!")
    elif eleccion5 == "gritar":
        print("Gritas pidiendo ayuda y un grupo de aventureros te encuentra y te lleva de regreso a casa.")
    else:
        print("Opción no válida. Por favor, elige 'seguir' o 'gritar'.")
        escena_perdido()

def escena_tesoro():
    print("Has encontrado un tesoro lleno de oro y joyas. ¿Qué haces?")
    
    eleccion6 = input("Escribe 'tomar' el tesoro o 'compartir' con el pueblo: ").strip().lower()

    if eleccion6 == "tomar":
        print("Tomar el tesoro te hace rico, pero pierdes la amistad de tus vecinos.")
    elif eleccion6 == "compartir":
        print("Compartes el tesoro con el pueblo y todos celebran tu generosidad. ¡Eres un héroe!")
    else:
        print("Opción no válida. Por favor, elige 'tomar' o 'compartir'.")
        escena_tesoro()

def escena_deseo():
    print("La criatura mágica te ofrece un deseo. ¿Qué deseas?")
    eleccion7 = input("Escribe 'riqueza' o 'sabiduria': ").strip().lower()

    if eleccion7 == "riqueza":
        print("Deseas riqueza y te conviertes en la persona más rica del reino, pero te sientes solo.")
    elif eleccion7 == "sabiduria":
        print("Deseas sabiduria y obtienes conocimientos profundos sobre el mundo. Te conviertes en un gran líder.")
    else:
        print("Opción no válida. Por favor, elige 'riqueza' o 'sabiduria'.")
        escena_deseo()


iniciar_juego()


