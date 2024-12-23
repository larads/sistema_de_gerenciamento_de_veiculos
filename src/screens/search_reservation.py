from tkinter import *
from tkinter import ttk
import tkinter as tk

import home

class search_reservation:

    def __init__(self):

        master7=Toplevel()
        master7.title("Buscar Reserva")
        master7.geometry("800x1200")

        # Menu
        self.barra_menu = Label(master7, bg='#c4c4c4')
        self.barra_menu.place(relx=0.0, rely=0.0, relwidth=0.22, relheight=0.999)

        self.bt_sair = Button(master7, text="Sair", font='arial 10')
        self.bt_sair.place(relx=0.06, rely=0.8, relwidth=0.1, relheight=0.03)

        # barra em cima
        self.retangulo = Label(master7, bg='#15803d')
        self.retangulo.place(relx=0.22, rely=0.0, relwidth=0.9999, relheight=0.03)

        self.texto = Label(master7, width=2, height=2, text='Sistema de Gerenciamento de Aluguel de Veículos',
                           fg='#ffffff',font=('Arial 10 bold'), bg='#15803d')
        self.texto.place(relx=0.22, rely=0.0, relwidth=0.78, relheight=0.03)

        # Entradas

        self.buscaReserva= Label(master7, text="Buscar Reserva", font='arial 15 bold')
        self.buscaReserva.place(relx=0.38, rely=0.047,relwidth=0.5, relheight=0.03)

        self.text_cpf = Label(master7, text="CPF", font='arial 9')
        self.text_cpf.place(relx=0.36, rely=0.10, relwidth=0.1, relheight=0.02)
        self.cpf = Entry(master7)
        self.cpf.pack()
        self.cpf.place(relx=0.44, rely=0.10, relwidth=0.25, relheight=0.024)

        self.bt_buscar = Button(master7, text="Buscar", font='arial 9')
        self.bt_buscar.place(relx=0.7, rely=0.10, relwidth=0.1, relheight=0.026)

        self.cliente = Label(master7, width=5, height=5, text='Dados do cliente',
                             font=('Arial 10 bold'), fg='#ffffff',bg='#15803d')
        self.cliente.place(relx=0.222, rely=0.14, relwidth=0.77, relheight=0.026)

        self.text_nome = Label(master7, text="Nome", font='arial 9')
        self.text_nome.place(relx=0.22, rely=0.18, relwidth=0.1, relheight=0.02)
        self.nome = Entry(master7)
        self.nome.pack()
        self.nome.place(relx=0.31, rely=0.18, relwidth=0.25, relheight=0.024)

        self.text_idade = Label(master7, text="Idade", font='arial 9')
        self.text_idade.place(relx=0.587, rely=0.18, relwidth=0.06, relheight=0.019)
        self.idade = Entry(master7)
        self.idade.pack()
        self.idade.place(relx=0.65, rely=0.18, relwidth=0.08, relheight=0.024)

        self.text_cnh = Label(master7, text="CNH", font='arial 9')
        self.text_cnh.place(relx=0.74, rely=0.18, relwidth=0.05, relheight=0.02)
        self.cnh = Entry(master7)
        self.cnh.pack()
        self.cnh.place(relx=0.8, rely=0.18, relwidth=0.17, relheight=0.024)

        self.text_email = Label(master7, text="E-mail", font='arial 9')
        self.text_email.place(relx=0.22, rely=0.22, relwidth=0.1, relheight=0.02)
        self.email = Entry(master7)
        self.email.pack()
        self.email.place(relx=0.31, rely=0.22, relwidth=0.29, relheight=0.024)

        self.text_telefone = Label(master7, text="Telefone", font='arial 9')
        self.text_telefone.place(relx=0.62, rely=0.22, relwidth=0.1, relheight=0.019)
        self.telefone = Entry(master7)
        self.telefone.pack()
        self.telefone.place(relx=0.72, rely=0.22, relwidth=0.18, relheight=0.024)

        self.text_endereco = Label(master7, text="Endereço", font='arial 9')
        self.text_endereco.place(relx=0.231, rely=0.26, relwidth=0.1, relheight=0.02)
        self.endereco = Entry(master7)
        self.endereco.pack()
        self.endereco.place(relx=0.33, rely=0.26, relwidth=0.64, relheight=0.024)

        self.text_estado = Label(master7, text="Estado", font='arial 9')
        self.text_estado.place(relx=0.221, rely=0.3, relwidth=0.1, relheight=0.02)
        self.estado = Entry(master7)
        self.estado.pack()
        self.estado.place(relx=0.314, rely=0.3, relwidth=0.22, relheight=0.024)

        self.text_cidade = Label(master7, text="Cidade", font='arial 9')
        self.text_cidade.place(relx=0.54, rely=0.3, relwidth=0.1, relheight=0.02)
        self.cidade = Entry(master7)
        self.cidade.pack()
        self.cidade.place(relx=0.63, rely=0.3, relwidth=0.34, relheight=0.024)

        self.reserva = Label(master7, width=5, height=5, text='Dados da Reserva',
                             font=('Arial 10 bold'), fg='#ffffff',bg='#15803d')
        self.reserva.place(relx=0.222, rely=0.34, relwidth=0.77, relheight=0.024)

        self.text_numero_reserva = Label(master7, text="Número da reserva", font='arial 9')
        self.text_numero_reserva.place(relx=0.22, rely=0.38, relwidth=0.18,relheight=0.017)
        self.id_reserva = Entry(master7)
        self.id_reserva.pack()
        self.id_reserva.place(relx=0.39, rely=0.38, relwidth=0.2, relheight=0.024)

        self.text_status_reserva = Label(master7, text="Status da reserva", font='arial 9')
        self.text_status_reserva.place(relx=0.6, rely=0.382, relwidth=0.18,relheight=0.017)
        self.status_reserva = Entry(master7)
        self.status_reserva.pack()
        self.status_reserva.place(relx=0.77, rely=0.38, relwidth=0.2, relheight=0.024)

        self.retirada = Label(master7, width=5, height=5, text='DETALHES DA RETIRADA', font=('Arial 9 bold'))
        self.retirada.place(relx=0.239, rely=0.42, relwidth=0.18, relheight=0.016)

        self.devolucao = Label(master7, width=5, height=5, text='DETALHES DA DEVOLUÇÃO', font=('Arial 9 bold'))
        self.devolucao.place(relx=0.62, rely=0.42, relwidth=0.2, relheight=0.015)

        self.text_data_ret = Label(master7, text="Data", font='arial 9')
        self.text_data_ret.place(relx=0.23, rely=0.46, relwidth=0.06, relheight=0.017)
        self.data_retirada = Entry(master7)
        self.data_retirada.pack()
        self.data_retirada.place(relx=0.29, rely=0.46, relwidth=0.12, relheight=0.024)

        self.text_hora_ret = Label(master7, text="Hora", font='arial 9')
        self.text_hora_ret.place(relx=0.42, rely=0.46, relwidth=0.06, relheight=0.017)
        self.hora_retirada = Entry(master7)
        self.hora_retirada.pack()
        self.hora_retirada.place(relx=0.48, rely=0.46, relwidth=0.11, relheight=0.024)

        self.text_sede_ret = Label(master7, text="Sede", font='arial 9')
        self.text_sede_ret.place(relx=0.23, rely=0.5, relwidth=0.06, relheight=0.017)
        self.sede_retirada = Entry(master7)
        self.sede_retirada.pack()
        self.sede_retirada.place(relx=0.29, rely=0.5, relwidth=0.3, relheight=0.024)

        self.text_endereco_ret =Label(master7, text="Endereço", font='arial 9')
        self.text_endereco_ret.place(relx=0.224, rely=0.54, relwidth=0.1, relheight=0.02)
        self.endereco_retirada = Entry(master7)
        self.endereco_retirada.pack()
        self.endereco_retirada.place(relx=0.32, rely=0.54, relwidth=0.27, relheight=0.024)

        self.text_estado_ret = Label(master7, text="Estado", font='arial 9')
        self.text_estado_ret.place(relx=0.224, rely=0.58, relwidth=0.08, relheight=0.02)
        self.estado_retirada = Entry(master7)
        self.estado_retirada.pack()
        self.estado_retirada.place(relx=0.31, rely=0.58, relwidth=0.28, relheight=0.024)

        self.text_cidade_ret = Label(master7, text="Cidade", font='arial 9')
        self.text_cidade_ret.place(relx=0.234, rely=0.62, relwidth=0.06, relheight=0.02)
        self.cidade_retirada = Entry(master7)
        self.cidade_retirada.pack()
        self.cidade_retirada.place(relx=0.31, rely=0.62, relwidth=0.28, relheight=0.024)

        self.text_data_dev = Label(master7, text="Data", font='arial 9')
        self.text_data_dev.place(relx=0.61, rely=0.46, relwidth=0.06, relheight=0.017)
        self.data_devolucao = Entry(master7)
        self.data_devolucao.pack()
        self.data_devolucao.place(relx=0.67, rely=0.46, relwidth=0.12, relheight=0.024)

        self.text_hora_dev = Label(master7, text="Hora", font='arial 9')
        self.text_hora_dev.place(relx=0.8, rely=0.46, relwidth=0.06, relheight=0.017)
        self.hora_devolucao = Entry(master7)
        self.hora_devolucao.pack()
        self.hora_devolucao.place(relx=0.86, rely=0.46, relwidth=0.11, relheight=0.024)

        self.text_sede_dev = Label(master7, text="Sede", font='arial 9')
        self.text_sede_dev.place(relx=0.61, rely=0.5, relwidth=0.06, relheight=0.017)
        self.sede_devolucao = Entry(master7)
        self.sede_devolucao.pack()
        self.sede_devolucao.place(relx=0.67, rely=0.5, relwidth=0.3, relheight=0.024)

        self.text_endereco_dev = Label(master7, text="Endereço", font='arial 9')
        self.text_endereco_dev.place(relx=0.606, rely=0.54, relwidth=0.1, relheight=0.02)
        self.endereco_devolucao = Entry(master7)
        self.endereco_devolucao.pack()
        self.endereco_devolucao.place(relx=0.71, rely=0.54, relwidth=0.26, relheight=0.024)

        self.text_estado_dev = Label(master7, text="Estado", font='arial 9')
        self.text_estado_dev.place(relx=0.598, rely=0.58, relwidth=0.1, relheight=0.02)
        self.estado_devolucao = Entry(master7)
        self.estado_devolucao.pack()
        self.estado_devolucao.place(relx=0.69, rely=0.58, relwidth=0.28, relheight=0.024)

        self.text_cidade_dev = Label(master7, text="Cidade", font='arial 9')
        self.text_cidade_dev.place(relx=0.615, rely=0.62, relwidth=0.06, relheight=0.02)
        self.cidade_devolucao = Entry(master7)
        self.cidade_devolucao.pack()
        self.cidade_devolucao.place(relx=0.69, rely=0.62, relwidth=0.28, relheight=0.024)

        self.text_categoria = Label(master7, text="Categoria", font='arial 9')
        self.text_categoria.place(relx=0.22, rely=0.66, relwidth=0.1, relheight=0.02)
        self.categoria = Entry(master7)
        self.categoria.pack()
        self.categoria.place(relx=0.32, rely=0.66, relwidth=0.12, relheight=0.024)

        self.text_modelo = Label(master7, text="Modelo", font='arial 9')
        self.text_modelo.place(relx=0.46, rely=0.66, relwidth=0.06, relheight=0.02)
        self.modelo = Entry(master7)
        self.modelo.pack()
        self.modelo.place(relx=0.53, rely=0.66, relwidth=0.2, relheight=0.024)

        self.text_ano = Label(master7, text="Ano", font='arial 9')
        self.text_ano.place(relx=0.74, rely=0.66, relwidth=0.06, relheight=0.02)
        self.ano = Entry(master7)
        self.ano.pack()
        self.ano.place(relx=0.8, rely=0.66, relwidth=0.17, relheight=0.024)

        self.text_veiculo = Label(master7, text="Nome do Veículo", font='arial 9')
        self.text_veiculo.place(relx=0.224, rely=0.7, relwidth=0.14, relheight=0.02)
        self.nome_veiculo = Entry(master7)
        self.nome_veiculo.pack()
        self.nome_veiculo.place(relx=0.36, rely=0.7, relwidth=0.23, relheight=0.024)

        self.text_placa = Label(master7, text="Placa", font='arial 9')
        self.text_placa.place(relx=0.6, rely=0.7, relwidth=0.06, relheight=0.02)
        self.placa = Entry(master7)
        self.placa.pack()
        self.placa.place(relx=0.66, rely=0.7, relwidth=0.1, relheight=0.024)

        self.text_portas = Label(master7, text="Qutda. de Portas", font='arial 9')
        self.text_portas.place(relx=0.78, rely=0.7, relwidth=0.12, relheight=0.02)
        self.portas = Entry(master7)
        self.portas.pack()
        self.portas.place(relx=0.91, rely=0.7, relwidth=0.06, relheight=0.024)

        self.text_combustivel = Label(master7, text="Combustível", font='arial 9')
        self.text_combustivel.place(relx=0.226, rely=0.74, relwidth=0.1, relheight=0.02)
        self.combustivel = Entry(master7)
        self.combustivel.pack()
        self.combustivel.place(relx=0.33, rely=0.74, relwidth=0.15, relheight=0.024)

        self.text_transmissao = Label(master7, text="Transmissão", font='arial 9')
        self.text_transmissao.place(relx=0.49, rely=0.74, relwidth=0.1, relheight=0.02)
        self.transmissao = Entry(master7)
        self.transmissao.pack()
        self.transmissao.place(relx=0.6, rely=0.74, relwidth=0.17, relheight=0.024)

        self.text_km = Label(master7, text="KM/L", font='arial 9')
        self.text_km.place(relx=0.78, rely=0.74, relwidth=0.06, relheight=0.02)
        self.quilometragem = Entry(master7)
        self.quilometragem.pack()
        self.quilometragem.place(relx=0.84, rely=0.74, relwidth=0.13, relheight=0.024)

        self.text_diarias = Label(master7, text="Diárias", font='arial 9')
        self.text_diarias.place(relx=0.227, rely=0.78, relwidth=0.06, relheight=0.02)
        self.diaria = Entry(master7)
        self.diaria.pack()
        self.diaria.place(relx=0.3, rely=0.78, relwidth=0.06, relheight=0.024)

        self.text_valorDiaria = Label(master7, text="Valor da Diária", font='arial 9')
        self.text_valorDiaria.place(relx=0.37, rely=0.78, relwidth=0.12, relheight=0.02)
        self.valor_diaria = Entry(master7)
        self.valor_diaria.pack()
        self.valor_diaria.place(relx=0.49, rely=0.78, relwidth=0.07, relheight=0.024)

        self.text_pagamento = Label(master7, text="Pagamento", font='arial 9')
        self.text_pagamento.place(relx=0.57, rely=0.78, relwidth=0.08, relheight=0.02)
        self.box = ttk.Combobox(master7, values=[ "Cartão de Crédito", "Cartão de Débito","Dinheiro"])
        self.box.place(relx=0.66, rely=0.78, relwidth=0.13, relheight=0.024)

        self.text_valorTotal = Label(master7, text="Valor Total", font='arial 9')
        self.text_valorTotal.place(relx=0.8, rely=0.782, relwidth=0.08, relheight=0.02)
        self.valor_total = Entry(master7)
        self.valor_total.pack()
        self.valor_total.place(relx=0.89, rely=0.78, relwidth=0.08, relheight=0.024)

        #Botão de Check

        self.chkValue1 = tk.BooleanVar()
        self.chkValue1.set(True)

        self.chkValue2 = tk.BooleanVar()
        self.chkValue2.set(True)

        self.chkValue3 = tk.BooleanVar()
        self.chkValue3.set(True)

        self.chkValue4 = tk.BooleanVar()
        self.chkValue4.set(True)

        self.chkValue5 = tk.BooleanVar()
        self.chkValue5.set(True)

        self.chkValue6 = tk.BooleanVar()
        self.chkValue6.set(True)

        self.chkValue7 = tk.BooleanVar()
        self.chkValue7.set(True)

        self.chkValue8 = tk.BooleanVar()
        self.chkValue8.set(True)

        self.chkValue9 = tk.BooleanVar()
        self.chkValue9.set(True)

        self.chkValue10 = tk.BooleanVar()
        self.chkValue10.set(True)

        self.chkValue11 = tk.BooleanVar()
        self.chkValue11.set(True)

        self.serv_adicional = Label(master7, text="Serviço Adicional", font='arial 9')
        self.serv_adicional.place(relx=0.224, rely=0.82, relwidth=0.13, relheight=0.02)

        self.servico_adicional1 = tk.Checkbutton(master7, font= 'arial 6',
                                                 text='Seguro Veicular Acidente  R$30,00', var=self.chkValue1)
        self.servico_adicional1.place(relx=0.35, rely=0.82, relwidth=0.19, relheight=0.02)

        self.servico_adicional2 = tk.Checkbutton(master7, font= 'arial 6',
                                                 text='Seguro Veicular Roubo e furto  R$40,00', var=self.chkValue2)
        self.servico_adicional2.place(relx=0.75, rely=0.82, relwidth=0.22, relheight=0.02)

        self.servico_adicional3 = tk.Checkbutton(master7, font= 'arial 6',
                                                 text='Seguro Veicular Completo  R$50,00', var=self.chkValue3)
        self.servico_adicional3.place(relx=0.55, rely=0.82, relwidth=0.2, relheight=0.02)

        self.servico_adicional4 = tk.Checkbutton(master7, font= 'arial 6',
                                                 text='Cadeira de bebê  R$20,00', var=self.chkValue4)
        self.servico_adicional4.place(relx=0.37, rely=0.84, relwidth=0.13, relheight=0.02)

        self.servico_adicional5 = tk.Checkbutton(master7, font= 'arial 6',
                                                 text='Bebê conforto  R$20,00', var=self.chkValue5)
        self.servico_adicional5.place(relx=0.224, rely=0.84, relwidth=0.14, relheight=0.02)

        self.servico_adicional6 = tk.Checkbutton(master7, font= 'arial 6',
                                                 text='Condutor extra  R$40,00', var=self.chkValue6)
        self.servico_adicional6.place(relx=0.51, rely=0.84, relwidth=0.14, relheight=0.02)

        self.servico_adicional7 = tk.Checkbutton(master7, font= 'arial 6',
                                                 text='Limpeza Simples  R$40,00', var=self.chkValue7)
        self.servico_adicional7.place(relx=0.65, rely=0.84, relwidth=0.14, relheight=0.02)

        self.servico_adicional8 = tk.Checkbutton(master7, font= 'arial 6',
                                                 text='Limpeza Completa  R$150,00', var=self.chkValue8)
        self.servico_adicional8.place(relx=0.8, rely=0.84, relwidth=0.15, relheight=0.02)

        self.ocorrencias = Label(master7, text="Ocorrências", font='arial 9')
        self.ocorrencias.place(relx=0.226, rely=0.87, relwidth=0.09, relheight=0.02)

        self.ocorrencias1 = tk.Checkbutton(master7, font= 'arial 6',text='Acidente de Carro', var=self.chkValue9)
        self.ocorrencias1.place(relx=0.33, rely=0.87, relwidth=0.13, relheight=0.02)

        self.ocorrencias2 = tk.Checkbutton(master7, font= 'arial 6',text='Furto/Roubo', var=self.chkValue10)
        self.ocorrencias2.place(relx=0.47, rely=0.87, relwidth=0.12, relheight=0.02)

        self.ocorrencias3 = tk.Checkbutton(master7, font= 'arial 6',text='Outros', var=self.chkValue11)
        self.ocorrencias3.place(relx=0.58, rely=0.87, relwidth=0.1, relheight=0.02)

        #Botões

        self.bt_salvar = Button(master7, text="Salvar", font='arial 10', bg='#15803d', fg="#ffffff")
        self.bt_salvar.place(relx=0.82, rely=0.91, relwidth=0.14, relheight=0.038)

        self.bt_cancelar = Button(master7, text="Cancelar", font='arial 10', bg="#70706e", fg="#ffffff",
                                  command=home.tela_inicial)
        self.bt_cancelar.place(relx=0.25, rely=0.91, relwidth=0.14, relheight=0.038)