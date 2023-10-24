import pytesseract
import cv2
from gtts import gTTS
import os

# Capturar imagem da webcam
cam = cv2.VideoCapture(0)
resultado, imagem = cam.read()

if resultado:
    # Salvar a imagem capturada como "nova_foto.jpg"
    cv2.imwrite("nova_foto.jpg", imagem)

    # Ler a imagem capturada
    imagem = cv2.imread("nova_foto.jpg")

    # remover a próxima linha para Linux ou encontrar o caminho correto para windows
    caminho_tesseract = r"C:\Program Files\Tesseract-OCR"

    # Extrair o texto
    # remover a próxima linha para Linux ou encontrar o caminho correto para windows
    pytesseract.pytesseract.tesseract_cmd = caminho_tesseract + r"\tesseract.exe"
    texto = pytesseract.image_to_string(imagem, lang="por")

    print("Texto extraído:", texto)

    # Verifica se o texto não está vazio após remoção dos espaços
    if texto.strip():
        # Transformar o texto em voz
        tts = gTTS(texto, lang="pt")
        tts.save("output.mp3")

        # Tocar o arquivo de áudio
        os.system("start output.mp3")
    else:
        mensagem_erro = " Não foi possível identificar a imagem."

        # Transformar a mensagem de erro em voz
        tts_erro = gTTS(mensagem_erro, lang="pt")
        tts_erro.save("erro.mp3")