# Music Player using Object-Oriented Programming (OOP)

## 🎵 Overview
This project implements a music player using **Object-Oriented Programming (OOP)** in Python. It allows switching between different sound sources dynamically **without using conditional statements** (`if, elif, else, match-case`).

## 📌 Features
- **Polymorphism-based switching** between different sound sources.
- **Encapsulation**: Clean separation of logic using OOP principles.
- **Automatic source detection**: Uses Python's `__subclasses__()` to register new sources dynamically.
- **User interaction**: The player allows users to change the music source interactively.

## 🔧 How It Works
The player starts with **MP3** as the default sound source. Users can switch to:
- **MP3** (`"Sonando MP3"`)
- **CD** (`"Sonando CD"`)
- **Consola** (`"Sonando Consola"`)

### Example Usage
```python
reproductor = Reproductor()
reproductor.reproducir()  # Output: "Sonando MP3"

reproductor.cambiar_fuente("CD")
reproductor.reproducir()  # Output: "Sonando CD"
```

## 📜 Classes & Structure
### 1. `FuenteSonido`
Base class for all sound sources.

### 2. `MP3`, `CD`, `Consola`
Each subclass implements the `reproducir()` method with its own message.

### 3. `Reproductor`
- Initializes with **MP3** as the default source.
- Uses **polymorphism** to switch sources dynamically.
- No conditionals for selecting sources.
- Handles user input via `iniciar()` method.

## 🚀 Running the Program
1. **Clone this repository**:
   ```sh
   git clone https://github.com/your-repo/music-player-POO.git
   ```
2. **Navigate to the project folder**:
   ```sh
   cd music-player-POO
   ```
3. **Run the script**:
   ```sh
   python main.py
   ```
4. **Follow the on-screen instructions to switch sources** or exit.

## 🛠 Adding a New Sound Source
Simply create a new class inheriting from `FuenteSonido`:
```python
class Radio(FuenteSonido):
    def reproducir(self):
        return "Sonando Radio"
```
It will **automatically** be registered without modifying any existing code.

## 📌 Key Takeaways
✅ **No conditionals** for switching sources.
✅ **Scalable & Maintainable** with automatic source detection.
✅ **Encapsulated logic** with clear separation of concerns.

🏆 Author
Juan Ignacio Mora

