# Generador de Audio con OpenAI y Streamlit

Este proyecto utiliza **Streamlit** y la **API de OpenAI** para crear una aplicación web interactiva que convierte texto a voz. Los usuarios pueden ingresar texto, seleccionar una voz y generar un archivo de audio en formato `.mp3`. Este audio se guarda en el servidor y se reproduce en la interfaz web.

## Requisitos

- Python 3.x
- Bibliotecas necesarias:
  - `streamlit`
  - `openai`
  - `dotenv`
  
## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Juan-Bayter/chatbot_texto_a_audio_Python.git
   cd https://github.com/Juan-Bayter/chatbot_texto_a_audio_Python.git
   
2. Es importante crear un archivo .env en la raíz del proyecto, ya que este archivo contiene la clave de la API de OpenAI necesaria para interactuar con sus servicios. En el archivo .env, agrega lo siguiente:

   ```bash
   OPENAI_API_KEY=tu_clave_de_api

   
