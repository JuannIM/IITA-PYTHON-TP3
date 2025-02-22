class FuenteSonido:
    """Base class for sound sources."""
    def reproducir(self) -> str:
        raise NotImplementedError("This method should be implemented in subclasses.")

class MP3(FuenteSonido):
    def reproducir(self) -> str:
        return "Sonando MP3"

class CD(FuenteSonido):
    def reproducir(self) -> str:
        return "Sonando CD"

class Consola(FuenteSonido):
    def reproducir(self) -> str:
        return "Sonando Consola"

class Reproductor:
    """
    Music player that can switch between different sound sources dynamically,
    without using conditional structures (if, elif, else, match-case).
    """

    fuentes_disponibles = {
        "MP3": MP3,
        "CD": CD,
        "Consola": Consola
    }

    def __init__(self, fuente: FuenteSonido = None) -> None:
        """Initializes the player with a default sound source (MP3)."""
        self.fuente = fuente if fuente else MP3()
    
    def reproducir(self) -> None:
        """Plays the current sound source."""
        print(self.fuente.reproducir())

    def cambiar_fuente(self, nueva_fuente: str) -> None:
        """
        Changes the sound source dynamically without conditionals.
        
        Args:
            nueva_fuente (str): The name of the new sound source.
        """
        self.fuente = self.fuentes_disponibles.get(nueva_fuente, lambda: self.fuente)()

def main():
    """
    Handles user interaction for selecting and switching sound sources
    without using conditionals.
    """
    reproductor = Reproductor()
    
    try:
        while True:
            reproductor.reproducir()
            nueva_fuente = input("Ingrese nueva fuente (MP3, CD, Consola): ").strip()
            
            # Attempt to switch the source, fallback to the same source if invalid
            reproductor.cambiar_fuente(nueva_fuente)
    
    except KeyboardInterrupt:
        print("\nSaliendo del reproductor...")

# Run the program
if __name__ == "__main__":
    main()
