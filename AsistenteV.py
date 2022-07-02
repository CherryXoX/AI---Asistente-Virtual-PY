import speech_recognition as speech
import pyttsx3
import pywhatkit
import datetime as time
import wikipedia
import chistesESP as chistes
import random

# Aquí va el nombre del Asistente-V
name='Cherry'# Debes ingresar el nombre de tu asistente aqui


#Inicializar el SR y el TTS
listener = speech.Recognizer()

engine = pyttsx3.init()


# Todo esto es la configuración de la voz

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

voice_engine = engine.getProperty('voices')
engine.setProperty('voice', voice_engine[0].id)


# Este es el idioma de la Wikipedia
wikipedia.set_lang('es')

# Traducción de los meses 
spanish_month = {
    'January': 'Enero',
    'February': 'Febrero',
    'March': 'Marzo',
    'April': 'Abril',
    'May': 'Mayo',
    'June': 'Junio',
    'July': 'Julio',
    'August': 'Agosto',
    'September': 'Septiembre',
    'October': 'Octubre',
    'November': 'Noviembre',
    'December': 'Diciembre'
}


def random_choice():
    lista = ['Te escucho', 'Dime tu orden', 'Estoy escuchándote', 'Dime', 'Que desea']
    seleccion = random.choice(lista)
    return seleccion


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with speech.Microphone() as source:
            select = random_choice()
            print('Escuchando...')
            talk(select)
            voice = listener.listen(source)
            recognizer = listener.recognize_google(voice, language='es-MX')
            recognizer = recognizer.lower()

            if name in recognizer:
                recognizer = recognizer.replace(name, '')
    except:
        print('Algo ha salido mal')
        pass
    return recognizer


def run():
    recognizer = listen()

    print(recognizer)


    if 'reproduce' in recognizer:
        music = recognizer.replace('reproduce', '')
        talk('reproduciendo' + music)
        pywhatkit.playonyt(music)


    elif 'hora' in recognizer:
        hora = time.datetime.now().strftime('%I:y%M %p')
        talk('Son las '+hora)


    elif 'fecha' in recognizer:
        fecha = time.datetime.now().strftime('%d-%h-%Y')
        talk('La fecha es: ' + str(fecha))


    elif 'día' in recognizer:
        dia = time.datetime.now().strftime('%d')
        talk('Hoy es el día ' + str(dia))


    elif 'mes' in recognizer:
        mes = time.datetime.now().strftime('%B')
        mes_translate = spanish_month[mes]
        talk('Estamos en el mes de ' + str(mes_translate))


    elif 'año' in recognizer:
        year = time.datetime.now().strftime('%Y')
        talk('Estamos en el ' + str(year))


    elif 'busca en wikipedia' in recognizer:
        consulta = recognizer.replace('busca en wikipedia', '')
        talk('buscando en wikipedia' + consulta)
        resultado = wikipedia.summary(consulta, sentences=3)
        talk(resultado)

 
    elif 'busca en google' in recognizer:
        consulta = recognizer.replace('busca en google', '')
        talk('Buscando en google' + consulta)
        pywhatkit.search(consulta)


    elif 'chiste' in recognizer:
        chiste = chistes.get_random_chiste()
        talk(chiste)

    else:
        talk('Disculpa, no te entiendo, repitelo')

