# ./youtube_downloader.py
# Criação: 05/07/2021
# Versão: 1.3
# Descrição: Script criado com a intenção de baixar videos do Youtube
# Modo de uso: python youtube_downloader.py <url_do_video_do_YouTube>

from pytube import YouTube
import sys

if len(sys.argv) != 2:
    print("Modo de uso: python youtube_downloader.py <url_do_video_do_YouTube>")
else:
    # Aqui se define por argumento o link do vídeo do Youtube que será baixado
    video = YouTube(sys.argv[1])

    # Define a qualidade do vídeo na mais alta qualidade
    stream = video.streams.get_highest_resolution()

    # Pasta onde será baixado o conteúdo
    stream.download(output_path='/tmp/')
