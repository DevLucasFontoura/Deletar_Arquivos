import os
import requests

from tkinter import *
from PIL import Image
from tkinter import filedialog

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


def janelaInicial():
    janela_inicial = Tk()
    janela_inicial.title("Deletar Arquivos Duplicados!")
    # janela_inicial.geometry("560x250")
    height = 250
    width = 560
    x = (janela_inicial.winfo_screenwidth()//2)-(width//2)
    y = (janela_inicial.winfo_screenheight()//2)-(height//2)
    janela_inicial.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    
    texto_orientacao01 = Label(janela_inicial, text="Seja Bem Vindo!", font=("Arial", 15))
    texto_orientacao01.place(x=200, y=10)

    texto_orientacao02 = Label(janela_inicial, text="Este programa irá deletar os arquivos duplicados na pasta indicada por você do seu computador.")
    texto_orientacao02.place(x=30, y=70)

    texto_orientacao02 = Label(janela_inicial, text="Clique no botão se deseja continuar.")
    texto_orientacao02.place(x=185, y=100)

    botao_continuar = Button(janela_inicial, text="Continuar", font=("Arial", 15), command=lambda: janelaCaminhoArquivo(janela_inicial))
    botao_continuar.place(x=230, y=140)

    texto_criador = Label(janela_inicial, text=" © Criado por Lucas Fontora Righi Fontes")
    texto_criador.place(x=170, y=210)

    

    janela_inicial.mainloop()

def janelaCaminhoArquivo(janela_inicial):
    janela_caminho = Tk()
    janela_caminho.title("Indicar Caminho do Arquivo!")
    janela_caminho.geometry("560x250")
    height = 260
    width = 560
    x = (janela_caminho.winfo_screenwidth()//2)-(width//2)
    y = (janela_caminho.winfo_screenheight()//2)-(height//2)
    janela_caminho.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    texto_orientacao01 = Label(janela_caminho, text="Caminho do Arquivo", font=("Arial", 15))
    texto_orientacao01.place(x=190, y=10)

    texto_orientacao02 = Label(janela_caminho, text="Indique Abaixo a Pasta que Deseja Deletar os Arquivos Duplicados", font=("Arial", 12))
    texto_orientacao02.place(x=40, y=70)

    botao_selecionar_pasta = Button(janela_caminho, text="Selecionar pasta", font=("Arial", 15), command=selecionarPasta)
    botao_selecionar_pasta.place(x=200, y=140)

    botao_executar = Button(janela_caminho, text="Executar", font=("Arial", 15), command=lambda: (janelaLoading(janela_caminho), deletarArquivosDuplicados()))
    botao_executar.place(x=240, y=200)

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



