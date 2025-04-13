import speech_recognition as sr # Importa la librería para reconocimiento de voz
import subprocess # Importa la librería para ejecutar procesos del sistema (como abrir programas)
import pyautogui # Importa la librería para controlar el teclado y mouse automáticamente

recognizer = sr.Recognizer() # Crea un objeto reconocedor de voz
proceso = None # Variable para almacenar el proceso del Notepad (bloc de notas)
saludo = "Hola como estas"

# Función que ejecuta un comando dependiendo de lo que diga el usuario
def ejecutar_comando(comando):
    global proceso # Permite modificar la variable 'proceso' desde dentro de la función
    if "abrir notepad" in comando:
        proceso = subprocess.Popen("notepad.exe")
    elif "saludar a usuario" in comando:
        pyautogui.write(saludo)
    elif "cerrar notepad" in comando:
        proceso.terminate()

# Función que escucha y reconoce el comando de voz        
def escuchar_comando():
    with sr.Microphone() as source: # Usa el micrófono como fuente de entrada
        print("En que puedo ayudarte?")
        recognizer.adjust_for_ambient_noise(source) # Ajusta el ruido ambiente
        audio = recognizer.listen(source) # Escucha lo que diga el usuario

    try:
        # Intenta reconocer lo que se dijo usando Google (en español de España)
        comando = recognizer.recognize_google(audio, language = "es-ES")
        print(f"Comando reconocido: {comando}") # Muestra el comando reconocido
        ejecutar_comando(comando) # Ejecuta el comando
    except sr.UnknownValueError: # Si no se entendió lo que se dijo
        print("No se puede enrtender el comando")
        
    except sr.RequestError as e:  # Si hay un problema con la conexión o solicitud
        print(f"Error al realizar la solicitud: {e}")

while True:
    escuchar_comando()

