import pygame as pg
import PySimpleGUI as sg
from utils import directories
import os
from random import shuffle

directories = directories

sg.theme('Reddit')
atual = 0
pg.mixer.init()
pg.mixer.music.load(directories[atual])
pg.mixer.music.play()

next_image = 'Imagens\\next.png'
back_image = 'Imagens\\back.png'
play_image = 'Imagens\\play.png'
pause_image = 'Imagens\\pause.png'
random_image = 'Imagens\\random.png'
fundo = 'Imagens\\marshmallow.png'


coluna = [
    [sg.Text(os.path.basename(directories[atual]).replace('.mp3', ''), background_color='black', text_color='white', font='Tahoma 12', key='musica')],
    [sg.Text('_'*70, background_color='black', text_color='white')],
    [sg.Image(filename=back_image, background_color='black', key='back', enable_events=True),
     sg.Image(filename=random_image, background_color='black', key='random', enable_events=True),
     sg.Image(filename=play_image, background_color='black', key='play', enable_events=True),
     sg.Image(filename=pause_image, background_color='black', key='pause', enable_events=True),
     sg.Image(filename=next_image, background_color='black', key='next', enable_events=True)]
]

layout = [
    [sg.Text('MP3 Player - By Davi de Alcantara dos Santos', background_color='black', text_color='white', font='arial 5')],
    [
        sg.Image(filename=fundo, background_color='black',
                 size=(350, 350), pad=None),
    ],
    [
        sg.Column(layout=coluna, background_color='black', justification='c', element_justification='c',)
    ]
]

root = sg.Window('teste', layout=layout, size=(370, 550), background_color='black', resizable=False)


def atualizar_musica():
    nome_musica = os.path.basename(directories[atual]).replace('.mp3', '')
    root['musica'].update(nome_musica)


while True:
    event, values = root.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'pause':
        pg.mixer.music.pause()

    if event == 'play':
        pg.mixer.music.unpause()

    if event == 'back':
        if directories.index(directories[atual]) == 0:
            pass
        else:
            atual -= 1
            pg.mixer.music.load(directories[atual])
            pg.mixer.music.play()
            atualizar_musica()

    if event == 'next':
        if directories.index(directories[atual]) == len(directories) - 1:
            pass
        else:
            atual += 1
            pg.mixer.music.load(directories[atual])
            pg.mixer.music.play()
            atualizar_musica()

    if event == 'random':
        musica_atual = directories[atual]
        shuffle(directories)
        while directories[atual] == musica_atual:
            shuffle(directories)
        atual = 0
        pg.mixer.music.load(directories[atual])
        pg.mixer.music.play()
        atualizar_musica()
