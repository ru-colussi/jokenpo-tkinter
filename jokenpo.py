#Ruggero Colussi

import tkinter
from tkinter import *
from tkinter import ttk

#importando o pillow
from PIL import Image, ImageTk

import random

#cores
cor0 = '#ffffff'  #branco
cor1 = '#333333'  #preto
cor2 = '#ffb22e'  #laranja
cor3 = '#fff647'  #amarelo
cor4 = '#2898a6'  #azul
cor6 = '#ffb22e'  #laranja
cor7 = '#ff2626'  #vermelho
cor8 = '#4bde3e'  #verde
fundo = '#3b3b3b'

#configurando a janela
janela = Tk()
janela.title('Jokenpô - Projeto 2')
janela.geometry('260x280')
janela.configure(bg = fundo)


#dividindo a janela
Frame_cima = Frame(janela, width = 260, height = 100, bg = cor1, relief = 'raised')
Frame_cima.grid(row = 0, column = 0, sticky = NW)
Frame_baixo = Frame(janela, width = 260, height = 180, bg = cor0, relief = 'flat')
Frame_baixo.grid(row = 1, column = 0, sticky = NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


#configurando frame cima
app_1 = Label(Frame_cima, text = 'Você', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = cor1, fg = cor0)
app_1.place(x = 25, y = 70)
app_1_linha = Label(Frame_cima, text = '', height = 10, anchor = 'center', font = ('Ivy 10 bold'), bg = cor0, fg = cor0)
app_1_linha.place(x = 0, y = 0)
app_1_pontos = Label(Frame_cima, text = '0', height = 1, anchor = 'center', font = ('Ivy 30 bold'), bg = cor1, fg = cor0)
app_1_pontos.place(x = 50, y = 20)


app_ = Label(Frame_cima, text = ':', height = 1, anchor = 'center', font = ('Ivy 30 bold'), bg = cor1, fg = cor0)
app_.place(x = 125, y = 20)

app_2_pontos = Label(Frame_cima, text = '0', height = 1, anchor = 'center', font = ('Ivy 30 bold'), bg = cor1, fg = cor0)
app_2_pontos.place(x = 170, y = 20)
app_2 = Label(Frame_cima, text = 'PC', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = cor1, fg = cor0)
app_2.place(x = 205, y = 70)
app_2_linha = Label(Frame_cima, text = '', height = 10, anchor = 'center', font = ('Ivy 10 bold'), bg = cor0, fg = cor0)
app_2_linha.place(x = 255, y = 0)

app_linha = Label(Frame_cima, text = '', width = 255, anchor = 'center', font = ('Ivy 1 bold'), bg = cor0, fg = cor0)
app_linha.place(x = 0, y = 95)

app_PC = Label(Frame_baixo, text = '', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = cor0, fg = cor0)
app_PC.place(x = 190, y = 10)


global Você
global PC
global rondas
global pontos_Você
global pontos_PC

pontos_Você = 0
pontos_PC = 0
rondas = 5

#função lógica do jogo
def jogar(i):
    global rondas
    global pontos_Você
    global pontos_PC

    if rondas >0:
        print(rondas)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        PC = random.choice(opcoes)
        Você = i

        app_PC['text'] = PC
        app_PC['fg'] = cor1

        #caso for igual
        if Você == 'Pedra' and PC == 'Pedra':
            print('empate')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor3

        elif Você == 'Papel' and PC == 'Papel':
            print('empate')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor3

        elif Você == 'Tesoura' and PC == 'Tesoura':
            print('empate')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor3

        #movendo para frente
        elif Você == 'Pedra' and PC == 'Papel':
            print('PC ganhou!')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor8
            app_linha['bg'] = cor0
            pontos_PC += 1

        elif Você == 'Pedra' and PC == 'Tesoura':
            print('Você ganhou!')
            app_1_linha['bg'] = cor8
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor0
            pontos_Você += 1

        elif Você == 'Papel' and PC == 'Tesoura':
            print('PC ganhou!')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor8
            app_linha['bg'] = cor0
            pontos_PC += 1

        #movendo para tras
        elif Você == 'Tesoura' and PC == 'Papel':
            print('Você ganhou!')
            app_1_linha['bg'] = cor8
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor0
            pontos_Você += 1

        elif Você == 'Tesoura' and PC == 'Pedra':
            print('PC ganhou!')
            app_1_linha['bg'] = cor0
            app_2_linha['bg'] = cor8
            app_linha['bg'] = cor0
            pontos_PC += 1

        elif Você == 'Papel' and PC == 'Pedra':
            print('Você ganhou!')
            app_1_linha['bg'] = cor8
            app_2_linha['bg'] = cor0
            app_linha['bg'] = cor0
            pontos_Você += 1

        app_1_pontos['text'] = pontos_Você
        app_2_pontos['text'] = pontos_PC

        #atualizando o número de rondas
        rondas -= 1

    else:
        app_1_pontos['text'] = pontos_Você
        app_2_pontos['text'] = pontos_PC

        #chamando a função terminar
        fim_do_jogo()


#criando função - iniciar o jogo

def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('images/pedra.png')
    icon_1 = icon_1.resize((50, 50))
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(Frame_baixo, command = lambda: jogar('Pedra'), width = 50, image = icon_1, compound = CENTER, bg = cor0, fg = cor0, font = ('Ivy 10 bold'), anchor = CENTER, relief = FLAT)
    b_icon_1.place(x = 15, y = 60)

    icon_2 = Image.open('images/papel.png')
    icon_2 = icon_2.resize((50, 50))
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(Frame_baixo, command = lambda: jogar('Papel'), width = 50, image = icon_2, compound = CENTER, bg = cor0, fg = cor0, font = ('Ivy 10 bold'), anchor = CENTER, relief = FLAT)
    b_icon_2.place(x = 95, y = 60)

    icon_3 = Image.open('images/tesoura.png')
    icon_3 = icon_3.resize((50, 50))
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(Frame_baixo, command = lambda: jogar('Tesoura'), width = 50, image = icon_3, compound = CENTER, bg = cor0, fg = cor0, font = ('Ivy 10 bold'), anchor = CENTER, relief = FLAT)
    b_icon_3.place(x = 180, y = 60)


#criando função - terminar o jogo
def fim_do_jogo():
    global rondas
    global pontos_Você
    global pontos_PC

    #reiniciando as variáveis para zero
    pontos_Você = 0
    pontos_PC = 0
    rondas = 5

    #destruindo os botões de opções
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    #desfinindo o vencedor
    jogador_Você = int(app_1_pontos['text'])
    jogador_PC = int(app_2_pontos['text'])

    if jogador_Você > jogador_PC:
        app_vencedor = Label(Frame_baixo, text = 'Parabéns, Você ganhou!!', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = cor0, fg = cor8)
        app_vencedor.place(x = 5, y = 60)
    
    elif jogador_Você < jogador_PC:
        app_vencedor = Label(Frame_baixo, text = 'Infelizmente você perdeu!', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = cor0, fg = cor7)
        app_vencedor.place(x = 5, y = 60)

    else:
        app_vencedor = Label(Frame_baixo, text = 'Foi empate!', height = 1, anchor = 'center', font = ('Ivy 10 bold'), bg = cor0, fg = cor1)
        app_vencedor.place(x = 5, y = 60)

    #Jogar de novo
    def jogar_de_novo():
        app_1_pontos['text'] = 0
        app_2_pontos['text'] = 0
        app_vencedor.destroy()

        b_jogar_de_novo.destroy()

        iniciar_jogo()

    b_jogar_de_novo = Button(Frame_baixo, command = jogar_de_novo, width = 30, text = 'Jogar de novo', bg = fundo, fg = cor0, font = ('Ivy 10 bold'), anchor = CENTER, relief = RAISED, overrelief = RIDGE)
    b_jogar_de_novo.place(x = 5, y = 151)


b_jogar = Button(Frame_baixo, command = iniciar_jogo, width = 30, text = 'Jogar', bg = fundo, fg = cor0, font = ('Ivy 10 bold'), anchor = CENTER, relief = RAISED, overrelief = RIDGE)
b_jogar.place(x = 5, y = 151)

janela.mainloop()
