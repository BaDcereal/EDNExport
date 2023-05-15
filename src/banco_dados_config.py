import sys
import os
import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter.messagebox import showerror
from img_configuracoes import imgPath
import arquivos_config as arqsConfig
from arquivos_config import getIdioma as msgTxt

class BDConfig(tk.Toplevel):
    def __init__(self, container, func, dados_conexao, view, options_value):
        super().__init__()
        self.container = container
        self.view = view
        self.func = func
        self.dados_conexao = dados_conexao
        self.OptionsValue = options_value

        # Configuração Tamanho e Posição da janela
        if sys.platform == 'darwin':
            self.geometry("400x250+600+250")
        else:
            self.geometry("400x250+450+250")

        self.iconbitmap(os.path.join(arqsConfig.BASEPATHIMGS, 'favicon.ico'))

        self.resizable(False, False)
        self.title(msgTxt(self.OptionsValue['LANGUAGES'], 'BD_CONFIG_TITLE'))

        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=2)

        self.redIcon = tk.PhotoImage(file=imgPath.getIcon(self,'redIcon'))
        self.yellowIcon = tk.PhotoImage(file=imgPath.getIcon(self,'yellowIcon'))
        self.greenIcon = tk.PhotoImage(file=imgPath.getIcon(self,'greenIcon'))

        self.errorIcon = tk.PhotoImage(file=imgPath.getIcon(self,'error'))
        self.appIcon = tk.PhotoImage(file=imgPath.getIcon(self,'app'))

        # Label Servidor
        self.label_server = ttk.Label(self, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_BD_HOST'))
        self.label_server.grid(column=0, row=0, padx=5, pady=5, sticky=tk.EW)

        self.server_value = tk.StringVar()
        self.entry_server = ttk.Entry(self, textvariable=self.server_value)
        self.entry_server.grid(column=1, row=0, padx=5, pady=5, sticky=tk.EW)

        # Label Usuario
        self.label_user = ttk.Label(self, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_BD_USER'))
        self.label_user.grid(column=0, row=1, padx=5, pady=5, sticky=tk.EW)

        self.user_value = tk.StringVar()
        self.entry_user = ttk.Entry(self, textvariable=self.user_value)
        self.entry_user.grid(column=1, row=1, padx=5, pady=5, sticky=tk.EW)

        # Label Senha
        self.label_password = ttk.Label(self, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_BD_PASSWORD'))
        self.label_password.grid(column=0, row=2, padx=5, pady=5, sticky=tk.EW)

        self.password_value = tk.StringVar()
        self.entry_password = ttk.Entry(self, textvariable=self.password_value, show='*')
        self.entry_password.grid(column=1, row=2, padx=5, pady=5, sticky=tk.EW)

        # Label Base de Dados
        self.label_base_dados = ttk.Label(self, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_BD_DATABASE'))
        self.label_base_dados.grid(column=0, row=3, padx=5, pady=5, sticky=tk.EW)

        self.base_dados_value = tk.StringVar()
        self.entry_base_dados = ttk.Entry(self, textvariable=self.base_dados_value)
        self.entry_base_dados.grid(column=1, row=3, padx=5, pady=5, sticky=tk.EW)

        # Botoes
        self.btn_frame = tk.Frame(self)
        self.btn_frame.columnconfigure(index=0, weight=1)
        self.btn_frame.columnconfigure(index=1, weight=1)
        self.btn_frame.columnconfigure(index=2, weight=1)
        self.btn_frame.columnconfigure(index=3, weight=1)

        self.btn_frame.grid(column=0, columnspan=2, row=4, padx=5, pady=5, sticky=tk.NSEW)
        # Botão Confirmar
        self.btn_fechar = ttk.Button(self.btn_frame, text=msgTxt(self.OptionsValue['LANGUAGES'], 'BTN_CLOSE'), command=self.fechar)
        self.btn_fechar.grid(column=1, row=0, sticky=tk.W)

        # Botao Conectar
        self.btn_conexao = ttk.Button(self.btn_frame, text=msgTxt(self.OptionsValue['LANGUAGES'], 'BTN_CONNECT'), command=self.conectar)
        self.btn_conexao.grid(column=2, row=0, sticky=tk.E)

        # FrameLabel
        label_frame_status = tk.LabelFrame(self, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_BD_STATUS'), labelanchor=tk.NW)
        label_frame_status.grid(column=0, columnspan=2, row=5, padx=5, pady=5, sticky=tk.NSEW)

        # Label Status Conexao
        self.txt_status_value = tk.StringVar()
        self.txt_status_value.set(msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_CONNECTION'))
        self.label_txt_status = ttk.Label(label_frame_status, textvariable=self.txt_status_value)
        self.label_txt_status.grid(column=0, row=0, pady=5)

        self.label_img_status = ttk.Label(label_frame_status, image=self.redIcon)
        self.label_img_status.grid(column=1, row=0, pady=5)

        # Evento de fechar a janela
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        if dados_conexao is not None:
            self.recoverData()

    # Preenche os campos de login no caso dos dados de conexão já terem sidos informados
    def recoverData(self):
        self.server_value.set(self.dados_conexao['host'])
        self.user_value.set(self.dados_conexao['user'])
        self.password_value.set(self.dados_conexao['password'])
        self.base_dados_value.set(self.dados_conexao['database'])
        self.changeStatus(True)

    # Cria uma conexão com o Banco de Dados
    def conectar(self):
        try:
            conexao = mysql.connector.connect(
                host=self.server_value.get().strip(),
                user=self.user_value.get().strip(),
                password=self.password_value.get().strip()
            )

            mycursor = conexao.cursor()
            sql = 'SHOW DATABASES where `Database` = %s'
            var = (self.base_dados_value.get().strip(),)
            mycursor.execute(sql, var)
            records = mycursor.fetchall()

            if records:
                self.changeStatus(True)
            else:
                sql = 'CREATE DATABASE IF NOT EXISTS %s'
                mycursor.execute(sql, var)

            conexao.close()

            self.returnSetings()
        except:
            self.changeStatus(False)
            self.show_error(msgTxt(self.OptionsValue['LANGUAGES'], 'CONNECTION_ERRO_TITLE'), msgTxt(self.OptionsValue['LANGUAGES'], 'CONNECTION_ERRO_MSG'))

    # Retorna os dados da conexão
    def returnSetings(self):
        data_conection = {
            'host': self.server_value.get().strip(),
            'user': self.user_value.get().strip(),
            'password': self.password_value.get().strip(),
            'database': self.base_dados_value.get().strip()
        }
        self.func(data_conection)

    # Altera o status da conexão
    def changeStatus(self, result):
        if result:
            self.label_img_status.configure(image=self.greenIcon)
            self.label_img_status.image=self.greenIcon
        else:   
            self.label_img_status.configure(image=self.redIcon)
            self.label_img_status.image=self.redIcon

    # Fecha a janela de conexão
    def fechar(self):
        self.destroy()
        self.container.deiconify()
        self.view.enableMenuBar()

    # Exibe a janela anterior 
    def on_closing(self):
        self.destroy()
        self.container.deiconify()
        self.view.enableMenuBar()

    def set_icon(self, icon):
        if sys.platform == "darwin":
            self.iconphoto(False, icon)
            
    # Exibe mensagem de erro
    def show_error(self, titulo, msg):
        self.set_icon(self.errorIcon)
        showerror(parent=self, title=titulo, message=msg)
        self.set_icon(self.appIcon)