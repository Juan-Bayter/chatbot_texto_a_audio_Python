import streamlit as st  # construir interfaces aplicaciones web interactivas.
import os # acceder a variables de entorno.
from dotenv import load_dotenv, find_dotenv  # Carga variables de entorno desde un archivo .env
from openai import OpenAI # Biblioteca de OpenAI para interactuar con sus APIs.


# Carga las variables de entornos
load_dotenv(find_dotenv(), override=True)
apiKey = os.environ.get('OPENAI_API_KEY')


# cliente 
client = OpenAI(api_key=apiKey)

# Opciones de voz
voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

# Intefaz gráfica
st.title("Generador de Audio con OpenAI")
text = st.text_area("Ingrese el texto:", height=200)
voice = st.selectbox("Seleccione La voz:", voices)


# Generación de audio 
if st. button("Generar Audio"):
    if text:
        response = client.audio.speech.create( # Llama a la API de OpenAI para generar el audio
            model="tts-1", # Especifica el modelo de texto a voz.
            voice=voice,  # Usa la voz seleccionada.
            input=text, # Texto ingresado por el usuario.
        )
        audio_path = "audio.mp3" # guarda el archivo
        with open(audio_path, "wb") as output_file: 
            for chunk in response.iter_bytes():
                if chunk:
                    output_file.write(chunk)
                    
        st. success ("Audio, generado y guardado en audio.mp3")

        audio_file = open(audio_path, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    else:
        st.error("Por favor, ingrese un texto")

