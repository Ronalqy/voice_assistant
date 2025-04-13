import speech_recognition as sr
import subprocess
import pyautogui

recognizer = sr.Recognizer()
proceso = None
saludo = "Hola como estas"
def ejecutar_comando(comando):
    global proceso
    if "abrir notepad" in comando:
        proceso = subprocess.Popen("notepad.exe")
    elif "saludar a usuario" in comando:
        pyautogui.write(saludo)
    elif "cerrar notepad" in comando:
        proceso.terminate()
def escuchar_comando():
    with sr.Microphone() as source:
        print("En que puedo ayudarte?")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        comando = recognizer.recognize_google(audio, language = "es-ES")
        print(f"Comando reconocido: {comando}")
        ejecutar_comando(comando)
    except sr.UnknownValueError:
        print("No se puede enrtender el comando")
    except sr.RequestError as e:
        print(f"Error al realizar la solicitud: {e}")

while True:
    escuchar_comando()

