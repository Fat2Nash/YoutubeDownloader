#essayer d'importer pytube sinon l'installer
try:
    import pytube
except ImportError:
    print("pytube n'est pas installé")
    print("installez pytube avec pip install pytube")
    exit()
#essayer d'importer ffmpeg-python sinon l'installer
try:
    import ffmpeg
except ImportError:
    print("ffmpeg-python n'est pas installé")
    print("installez ffmpeg-python avec pip install ffmpeg-python")
    exit()


#import module couleur*
from termcolor import colored
from colorama import init, Fore, Back, Style
from pystyle import *
#importation des librairie 
from pytube import YouTube, Playlist
import os
import time

#import sys
import sys


def download_video(path):
    path = "../YoutubeDownloader/video"
    #choisir le lien de la video
    link = input("choisir le lien de la video : ")
    #choisir la resolution de la video
    reso = input("choisir la resolution de la video (360p, 480p, 720p) : ")
    #telecharger la video dans le repertoir choisi, avec la resolution choisi
    yt = YouTube(link)
    yt.streams.filter(resolution=reso).first().download(path)
    print(f"{yt.title} téléchargée avec succès !")
    print("La video se trouve : " + path)

def download_playlist(path):
    path = "../YoutubeDownloader/video"
    #choisir le lien de la playlist
    link = input("choisir le lien de la playlist : ")
    reso = input("choisir la resolution de la video (360p, 480p, 720p) : ")
    p = Playlist(link)
    print(f"Telechargement de la playlist {p.title}")
    for video in p.videos:
        print(f"Telechargement de la video {video.title}")
        video.streams.filter(resolution=reso).first().download(path)
    print("Toutes les videos ont été téléchargées avec succès !")
    print("Les videos se trouvent dans : " + path)


def download_mp3(path):
    path = "../YoutubeDownloader/musique"
    link = input("choisir le lien de la musique : ")
    yt= YouTube(link)
    #telecharger la musique en mp3
    try:
        if yt.streams.filter(only_audio=True).first().download(path):
            print(f"{yt.title} téléchargée avec succès !") #afficher le titre de la musique
            print("La musique se trouve : " + path)
    except:
        print("Erreur lors du téléchargement, veuillez rééssayer  ")
    convertisseur(path)


def download_playlist_mp3(path):
    path = "../YoutubeDownloader/musique"
    link = input("choisir le lien de la playlist : ")
    p = Playlist(link)
    print(f"Telechargement de la playlist {p.title}")
    for musique in p.videos:
        print(f"telechargement de la musique {musique.title}")
        musique.streams.filter(only_audio=True,).first().download(path)
        #renomer le fichier mp4 en mp3
        if os.rename(os.path.join(path,musique.title+".mp4"), os.path.join(path,musique.title+".mp3")) == True:
            print(f"{musique.title} renommée avec succès !")
        else:
            continue    
        print("La Playliste est disponible dans le dossier :" + path)

        convertisseur()

def convertisseur (path):
    path = ("../YoutubeDownloader/musique")
    files = os.listdir(path)
    
    for file in files:

        str =  file
        str_list = str.split(".")
        #print(str_list)
        str_list[len(str_list)-1] = "mp3"
        #print(str_list)
        new_str = ".".join(str_list)
        #print(new_str)
        os.rename(os.path.join(path, file), os.path.join(path, new_str))
        
    print("Toute les fichier du dossier : [" + path + "] sont convertis en mp3")









text = '''

    __   _______            _   _ _     _             ______                    _                     _           
    \ \ / /_   _|          | | | (_)   | |            |  _  \                  | |                   | |
     \ V /  | |    ______  | | | |_  __| | ___  ___   | | | |_____      ___ __ | |     ___   __ _  __| | ___ _ __ 
      \ /   | |   |______| | | | | |/ _` |/ _ \/ _ \  | | | / _ \ \ /\ / / '_ \| |    / _ \ / _` |/ _` |/ _ \ '__| 
      | |   | |            \ \_/ / | (_| |  __/ (_) | | |/ / (_) \ V  V /| | | | |___| (_) | (_| | (_| |  __/ |   
      \_/   \_/             \___/|_|\__,_|\___|\___/  |___/ \___/ \_/\_/ |_| |_\_____/\___/ \__,_|\__,_|\___|_|

'''
print(Colorate.Horizontal(Colors.blue_to_cyan, text))
print()
print()

textligne = "--------------------------------------------------------------------------------------------------------------------"
print(Colors.blue + textligne )
print()
print()

credit = Fore.LIGHTBLUE_EX + "[" + Fore.LIGHTCYAN_EX + "!" + Fore.LIGHTBLUE_EX + "] " + "Développer par : fat 2 nash#9413\n"
for char in credit:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

print()
print()
print()
print()


#menu des choix
premier = Fore.BLUE + "[" + Fore.CYAN + "1" + Fore.BLUE+ "] : " + Fore.BLUE + "Telecharger une video\n"
for char in premier:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0)

deuxieme = Fore.BLUE + "[" + Fore.CYAN + "2" + Fore.BLUE+ "] : " + Fore.BLUE+ "Telecharger une playlist\n"
for char in deuxieme:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0)

troisieme = Fore.BLUE+ "[" + Fore.CYAN + "3" + Fore.BLUE+ "] : " + Fore.BLUE + "Telecharger une musique\n"
for char in troisieme:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0)

quatrieme = Fore.BLUE + "[" + Fore.CYAN + "4" + Fore.BLUE+ "] : " + Fore.BLUE + "Telecharger une playlist de musique\n"
for char in quatrieme:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0)

cinquieme = Fore.BLUE + "[" + Fore.CYAN + "5" + Fore.BLUE+ "] : " + Fore.BLUE + "Convertisseur de MP4 en MP3\n"
for char in cinquieme:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0)

sixieme = Fore.BLUE + "[" + Fore.CYAN + "6" + Fore.BLUE+ "] : " + Fore.BLUE + "Quitter\n " + Fore.CYAN 
for char in sixieme:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0)
print()
print()
print()
print()

while True:
    try:
        choix = input(Colorate.Horizontal(Colors.blue_to_cyan, "Choisir une option : ", 1))
    except:
        print("erreur de saisie")
        continue
    if choix == "1":
        download_video("")
    elif choix == "2":
        download_playlist("")
    elif choix == "3":
        download_mp3("")
    elif choix == "4":
        download_playlist_mp3
    elif choix == "5":
        convertisseur("")
    elif choix == "6":
        choix = input("choisir une option : y / n")
        if choix == "y":
            break
        else:
            continue
    else:
        print("choix invalide, veuillez réessayer")