import os
import requests

from tkinter import *
from PIL import Image
from tkinter import filedialog
from tkinter import PhotoImage

global imagem_de_fundo

caminho_arquivo = 'C:\\Users\\Usuario\\Downloads\\'
imageObject = ''
gif_Label = ''
frames = ''
showAnimation = None

def selecionarPasta():
    caminho = filedialog.askdirectory()
    if caminho:
        global caminho_arquivo
        caminho_arquivo = caminho
        

def deletarArquivosDuplicados():
    print('OS ARQUIVOS FORAM DELETADOS COM SUCESSO!')
    for filename in os.listdir(caminho_arquivo):
        for i in range(1, 101):
            if  f'({i})' in filename:
                file_path = os.path.join(caminho_arquivo, filename)
                os.remove(file_path)
                # print("O arquivo", filename, "foi excluído com sucesso.")
                print("OS ARQUIVOS FORAM DELETADOS COM SUCESSO!")

def atualizarCaminhoSelecionado(caminho, caminho_selecionado):
    caminho_selecionado.config(text=caminho)

def selecionarPastaCaminho(caminho_selecionado):
    caminho = filedialog.askdirectory()
    atualizarCaminhoSelecionado(caminho, caminho_selecionado)

def janelaInicial():
    global imagem_de_fundo
    janela_inicial = Tk()
    janela_inicial.title("Deletar Arquivos Duplicados!")
    janela_inicial.configure(background='#1F41A9')
    height = 500
    width = 500

    x = (janela_inicial.winfo_screenwidth()//2)-(width//2)
    y = (janela_inicial.winfo_screenheight()//2)-(height//2)
    janela_inicial.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    
    texto_orientacao01 = Label(janela_inicial, text="Seja Bem Vindo!", font=("Arial", 25), bg='#1F41A9', fg='white')
    texto_orientacao01.place(x=130, y=80)

    texto_orientacao02 = Label(janela_inicial, text="Este programa irá deletar os arquivos duplicados na pasta indicada", font=("Arial", 12), bg='#1F41A9', fg='white')
    texto_orientacao02.place(x=10, y=180)

    texto_orientacao03 = Label(janela_inicial, text="por você do seu computador.", font=("Arial", 12), bg='#1F41A9', fg='white')
    texto_orientacao03.place(x=140, y=210)

    texto_orientacao04 = Label(janela_inicial, text="Clique no botão se deseja continuar.", font=("Arial", 12), bg='#1F41A9', fg='white')
    texto_orientacao04.place(x=120, y=300)

    botao_continuar = Button(janela_inicial, text="Continuar", font=("Arial", 15), command=lambda: janelaCaminhoArquivo(janela_inicial), bg='#1F41A9', fg='white')
    botao_continuar.place(x=190, y=370)

    texto_criador = Label(janela_inicial, text=" © Criado por Lucas Fontora Righi Fontes", bg='#1F41A9', fg='white')
    texto_criador.place(x=140, y=470)

    

    janela_inicial.mainloop()


def janelaCaminhoArquivo(janela_inicial):
    janela_caminho = Tk()
    janela_caminho.title("Indicar Caminho do Arquivo!")
    janela_caminho.geometry("560x250")
    janela_caminho.configure(background='#1F41A9')
    height = 500
    width = 500


    x = (janela_caminho.winfo_screenwidth()//2)-(width//2)
    y = (janela_caminho.winfo_screenheight()//2)-(height//2)
    janela_caminho.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    texto_orientacao01 = Label(janela_caminho, text="Caminho do Arquivo", font=("Arial", 25), bg='#1F41A9', fg='white')
    texto_orientacao01.place(x=120, y=20)

    texto_orientacao02 = Label(janela_caminho, text="Indique abaixo a pasta que deseja deletar os arquivos duplicados:", font=("Arial", 12), bg='#1F41A9', fg='white')
    texto_orientacao02.place(x=20, y=110)

    botao_selecionar_pasta = Button(janela_caminho, text="Selecionar pasta", font=("Arial", 15), bg='#1F41A9', fg='white', command=selecionarPasta)
    botao_selecionar_pasta.place(x=170, y=180)

    texto_orientacao03 = Label(janela_caminho, text="Clique no botão abaixo para executar o programa:", font=("Arial", 12), bg='#1F41A9', fg='white')
    texto_orientacao03.place(x=60, y=280)

    botao_executar = Button(janela_caminho, text="Executar", font=("Arial", 15), bg='#1F41A9', fg='white', command=lambda: (janelaLoading(janela_caminho), deletarArquivosDuplicados()))
    botao_executar.place(x=210, y=330)

    caminho_selecionado = Label(janela_caminho, text="", font=("Arial", 12), bg='#1F41A9', fg='white')
    caminho_selecionado.place(x=20, y=380)

    janela_inicial.destroy()
    janela_caminho.mainloop()

def janelaLoading(janela_caminho):
    splash = Tk()
    height = 500
    width = 500
    x = (splash.winfo_screenwidth()//2)-(width//2)
    y = (splash.winfo_screenheight()//2)-(height//2)
    splash.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    backgroundImage = PhotoImage(file="Background.png")
    bg_image = Label(
        splash,
        image=backgroundImage
    )
    bg_image.pack()

    gifImage = "load.gif"
    openImage = Image.open(gifImage)
    frames = openImage.n_frames
    imageObject = [PhotoImage(file=gifImage, format=f"gif -index {i}") for i in range(frames)]
    count = 0
      
    splash.overrideredirect(True)
    splash.after(3000, lambda: (splash.destroy(), janela_final()))

    gif_Label = Label(splash, image="")
    gif_Label.place(x=200, y=220, width=100, height=100)

    animation(count, imageObject, gif_Label, splash)
    janela_caminho.destroy()
    splash.mainloop()

def animation(count, imgObject, gif, splash):

    global showAnimation
        
    newImage = imgObject[count]

    gif.configure(image=newImage)
    count +=1
    if count == frames:
        count = 0
    showAnimation = splash.after(50, lambda: animation(count, imgObject, gif, splash))
    

def janela_final():
    janela_final = Tk()
    janela_final.title("Programa Finalizado!")
    janela_final.geometry("560x250")
    janela_final.configure(background='#1F41A9')
    height = 260
    width = 560

    x = (janela_final.winfo_screenwidth()//2)-(width//2)
    y = (janela_final.winfo_screenheight()//2)-(height//2)
    janela_final.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    texto_orientacao01 = Label(janela_final, text="Arquivos Duplicados Deletados Com Sucesso!", font=("Arial", 15))
    texto_orientacao01.place(x=100, y=50)

    texto_orientacao02 = Label(janela_final, text="Você já pode fechar essa janela.", font=("Arial", 12))
    texto_orientacao02.place(x=170, y=110)

    janela_final.mainloop()

def main():
    janelaInicial()

main()



