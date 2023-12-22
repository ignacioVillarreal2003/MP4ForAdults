from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox
import os
import sys


descargas_path = os.path.join(os.path.expanduser("~"), "Downloads")

def resourcePath(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def descargar():
    try:
        enlace = videoURL.get()
        opcion = opc.get()
        if (len(enlace) == 0):
            MessageBox.showinfo('Error', 'Verifique la URL')
        else:
            if (opcion == 1):
                descargarVideo(enlace)
            elif (opcion == 2):
                descargarAudio(enlace)
            elif (opcion != 1 | opcion != 2):
                MessageBox.showinfo('Error', 'Seleccione un tipo')
    except Exception:
        MessageBox.showinfo('Error', 'Verifique la URL')

def descargarVideo(enlace):
    try:
        videoProcesado = YouTube(enlace)
        video = videoProcesado.streams.get_highest_resolution()
        video.download(output_path=descargas_path)
        MessageBox.showinfo('Correcto', f'Video descargado')
    except Exception as e:
        MessageBox.showinfo('Error', f'Error desconocido: {e}')

def descargarAudio(enlace):
    try:
        videoProcesado = YouTube(enlace)
        audio = videoProcesado.streams.filter(only_audio=True).first()
        audio.download(output_path=descargas_path)
        MessageBox.showinfo('Correcto', f'Audio descargado')
    except Exception as e:
        MessageBox.showinfo('Error', f'Error desconocido: {e}')
def desplegarInformacion():
    MessageBox.showinfo('Sobre mí', 'Enlace a mi perfil de LinkedIn: https://www.linkedin.com/in/ignacio-villarreal-518804267/')

# Cuadro principal
root = Tk()
ancho = 700
alto = 500
root.geometry(f"{ancho}x{alto}")
root.config(bd=25)
root.title('Descargar videos para viejos.')

# Logo
logo = PhotoImage(file=resourcePath("youtube.png"))
nuevo_ancho = 160
nuevo_alto = 160
logo = logo.subsample(int(logo.width() / nuevo_ancho), int(logo.height() / nuevo_alto))
foto = Label(root, image=logo, bd=0)
foto.grid(row=0, column=0, padx=(0, 40))

# Menu de opciones
menuBar = Menu(root)
root.config(menu=menuBar)
helpMenu = Menu(menuBar, tearoff=0)

menuBar.add_cascade(label='Más información', menu=helpMenu)
helpMenu.add_command(label='Autor', command=desplegarInformacion)
menuBar.add_command(label='Salir', command=root.destroy)

# Descripcion
custom_font = ("Helvetica", 14)
instrucciones = Label(root, text='Programa para descargar videos de YouTube.\n Ingrese la URL.\n', font=custom_font)
instrucciones.grid(row=0, column=1)

# Input URL
videoURL = Entry(root, width=30, font=("Helvetica", 12))
videoURL.grid(row=1, column=1, pady=(0, 20))

boton = Button(root, text='Descargar', command=descargar)
boton.grid(row=2, column=1)

# Tipo descarga
tipo = LabelFrame(root, text='Tipo descarga')
tipo.grid(row=3, column=1, pady=(20, 0))
opc = IntVar()

video = Radiobutton(tipo, text='Video', value=1, variable=opc)
video.grid(row=0, column=0)
audio = Radiobutton(tipo, text='Audio', value=2, variable=opc)
audio.grid(row=0, column=1)


root.mainloop()

#   pyinstaller --onefile -w --hidden-import=pytube --hidden-import=PIL main.py       ---- No funciona por la imagen
#   python -m auto_py_to_exe

