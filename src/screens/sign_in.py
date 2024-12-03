from tkinter import *
from PIL import Image, ImageTk
import home

class sign_in:
    def __init__(self, master=None):
        master.title("Tela de Login")
        master.geometry("500x700")
        master.resizable(True, True)

        self.login = Label(master, width=5, height=5, text='Login', font=('Arial 18 bold'), fg='#000000')
        self.login.place(relx=0.27, rely=0.22)

        self.retangulo = Label(master, width=5, height=5, text='', font=('Arial 18 bold'), bg='#15803d')
        self.retangulo.place(relx=0.27, rely=0.38, relwidth=0.45, relheight=0.01)

        # Criação de imagens
        self.image = Image.open("../assets/logo.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.imagem = Label(master, image=self.photo)
        self.imagem.image = self.photo
        self.imagem.place(relx=0.5, rely=0.1, anchor='center')

        # Entradas
        self.text_nome = Label(master, text="Nome", font='arial,3')
        self.text_nome.place(relx=0.21, rely=0.43, relwidth=0.2, relheight=0.05)
        self.nome = Entry(master)
        self.nome.place(relx=0.27, rely=0.5, relwidth=0.45, relheight=0.05)

        self.text_senha = Label(master, text="Senha", font='arial,3')
        self.text_senha.place(relx=0.21, rely=0.58, relwidth=0.2, relheight=0.05)
        self.senha = Entry(master)
        self.senha.place(relx=0.27, rely=0.65, relwidth=0.45, relheight=0.05)

        # Botão
        self.bt_entrar = Button(master, text="Entrar", fg='#fffcfc', bg='#15803d', font=('15'),
                                command=lambda: home())
        self.bt_entrar.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)


root = Tk()
sign_in(root)
root.mainloop()