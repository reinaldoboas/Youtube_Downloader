# youtube_downloader.py
# Data: 05/07/2021
# Descrição: Script criado com a intenção de baixar videos do Youtube

from pytube import YouTube

# Aqui se define o link do vídeo do Youtube que será baixado
video  = YouTube('https://www.youtube.com/watch?v=wLeCegZPM9M&list=PLDaam_oLGwaqUs-r0Sn0Bl70oNLMK2aUW&index=464')

# Define a qualidade do vídeo na mais alta qualidade
stream = video.streams.get_highest_resolution()

# Pasta onde será baixado o conteúdo
stream.download(output_path='C:/Users/reinaldo/Documents/Scripts/downloads')
