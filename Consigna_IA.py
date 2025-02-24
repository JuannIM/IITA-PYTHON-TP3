class FuenteSonido:
    """Base class for all sound sources."""
    
    def reproducir(self) -> str:
        """Should be implemented by subclasses."""
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
    Music player that dynamically switches between sound sources
    without using conditional statements.
    """

    def __init__(self) -> None:
        """Initializes the player with MP3 as the default source."""
        self.fuente: FuenteSonido = MP3()

    @staticmethod
    def obtener_fuentes() -> dict[str, type[FuenteSonido]]:
        """
        Returns a dictionary mapping source names to their corresponding classes.
        """
        return {cls.__name__: cls for cls in FuenteSonido.__subclasses__()}

    def reproducir(self) -> None:
        """Plays the current sound source."""
        print(self.fuente.reproducir())

    def cambiar_fuente(self, nueva_fuente: str) -> None:
        """
        Changes the sound source dynamically without conditionals.
        
        Args:
            nueva_fuente (str): The name of the new sound source.
        """
        self.fuente = self.obtener_fuentes().get(nueva_fuente, lambda: self.fuente)()

    def iniciar(self) -> None:
        """Handles user interaction for selecting and switching sound sources."""
        print("\n🎵 Bienvenido al Reproductor de Música 🎵\n")
        
        while True:
            self.reproducir()
            nueva_fuente = input(f"Ingrese nueva fuente {list(self.obtener_fuentes().keys())} o 'salir': ").strip()
            
            if nueva_fuente.lower() == "salir":
                print("\n🎧 Saliendo del reproductor... ¡Hasta luego! 🎧")
                break

            self.cambiar_fuente(nueva_fuente)

# Run the program
if __name__ == "__main__":
    Reproductor().iniciar()
