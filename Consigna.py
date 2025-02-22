class FuenteSonido:
    """
    Base class for sound sources.
    """
    def reproducir(self):
        raise NotImplementedError("This method should be implemented in subclasses.")

class MP3(FuenteSonido):
    def reproducir(self):
        return "Sonando MP3"

class CD(FuenteSonido):
    def reproducir(self):
        return "Sonando CD"

class Consola(FuenteSonido):
    def reproducir(self):
        return "Sonando Consola"

class Reproductor:
    """
    Music player that can switch between different sound sources dynamically.
    """
    def __init__(self, fuente=MP3()):
        self.fuente = fuente
    
    def reproducir(self):
        print(self.fuente.reproducir())
    
    def cambiar_fuente(self, nueva_fuente):
        self.fuente = nueva_fuente

# Dictionary to map user input to classes
fuentes_disponibles = {
    "MP3": MP3,
    "CD": CD,
    "Consola": Consola
}

# Main loop for user interaction
reproductor = Reproductor()
while True:
    reproductor.reproducir()
    try:
        nueva_fuente = input("Ingrese nueva fuente (MP3, CD, Consola) o 'salir' para terminar: ")
        reproductor.cambiar_fuente(fuentes_disponibles[nueva_fuente]())
    except (KeyError, TypeError):
        print("Fuente no válida o salida del programa.")
        break

