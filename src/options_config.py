import sys
import os
import tkinter as tk
from tkinter import ttk
from img_configuracoes import imgPath
import arquivos_config as arqsConfig
from arquivos_config import getIdioma as msgTxt

class OpConfig(tk.Toplevel):
    def __init__(self, container, func, options_value, view):
        super().__init__()
        self.container = container
        self.view = view
        self.func = func
        self.OptionsValue = options_value

        self.redIcon = tk.PhotoImage(file=imgPath.getIcon(self,'redIcon'))
        self.yellowIcon = tk.PhotoImage(file=imgPath.getIcon(self,'yellowIcon'))
        self.greenIcon = tk.PhotoImage(file=imgPath.getIcon(self,'greenIcon'))

        # Configuração Tamanho e Posição da janela
        if sys.platform == 'darwin':
            self.geometry("400x170+600+250")
        else:
            self.geometry("400x170+450+250")

        self.iconbitmap(os.path.join(arqsConfig.BASEPATHIMGS, 'favicon.ico'))

        self.resizable(False, False)
        self.title(msgTxt(self.OptionsValue['LANGUAGES'], 'OP_CONFIG_TITLE'))

        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=2)

        # Label Versao de Testes
        self.label_teste = ttk.Label(self, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_TEST_VERSION'))
        self.label_teste.grid(column=0, row=0, padx=5, pady=5, sticky=tk.EW)

        self.teste_value = tk.StringVar()
        self.combobox_teste = ttk.Combobox(self, textvariable=self.teste_value)
        self.combobox_teste.grid(column=1, row=0, padx=5, pady=5, sticky=tk.EW)

        self.combobox_teste['values'] = (msgTxt(self.OptionsValue['LANGUAGES'], 'VALUE_YES'), msgTxt(self.OptionsValue['LANGUAGES'], 'VALUE_NO'))
        self.combobox_teste['state'] = 'readonly'
        
        version = msgTxt(self.OptionsValue['LANGUAGES'], 'VALUE_YES') if self.OptionsValue['TEST_VERSION'] else msgTxt(self.OptionsValue['LANGUAGES'], 'VALUE_NO')
        self.teste_value.set(version)

        # Label Idioma
        self.label_server = ttk.Label(self, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_LANGUAGE'))
        self.label_server.grid(column=0, row=1, padx=5, pady=5, sticky=tk.EW)

        self.language_value = tk.StringVar()
        self.combobox_language = ttk.Combobox(self, textvariable=self.language_value)
        self.combobox_language.grid(column=1, row=1, padx=5, pady=5, sticky=tk.EW)

        languages = msgTxt(self.OptionsValue['LANGUAGES'], 'LANGUAGES')
        self.inverted_dict = {value: key for key, value in languages.items()}

        for options in languages:
            self.combobox_language['values'] = (*self.combobox_language['values'], msgTxt(self.OptionsValue['LANGUAGES'], 'LANGUAGES')[options])
        self.combobox_language['state'] = 'readonly'

        self.language_value.set(msgTxt(self.OptionsValue['LANGUAGES'], 'LANGUAGES')[self.OptionsValue['LANGUAGES']])

        # Botoes
        self.btn_frame = tk.Frame(self)
        self.btn_frame.columnconfigure(index=0, weight=1)
        self.btn_frame.columnconfigure(index=1, weight=1)
        self.btn_frame.columnconfigure(index=2, weight=1)
        self.btn_frame.columnconfigure(index=3, weight=1)
        self.btn_frame.columnconfigure(index=4, weight=1)

        self.btn_frame.grid(column=0, columnspan=2, row=4, padx=5, pady=5, sticky=tk.NSEW)
        # Botão Confirmar
        self.btn_fechar = ttk.Button(self.btn_frame, text=msgTxt(self.OptionsValue['LANGUAGES'], 'BTN_CLOSE'), command=self.fechar)
        self.btn_fechar.grid(column=2, row=0, sticky=tk.EW)

        # Inicio FrameLabel Configuracoes
        label_frame_config = tk.LabelFrame(self, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_CONFIG'), labelanchor=tk.NW)
        label_frame_config.grid(column=0, columnspan=2, row=5, padx=5, pady=5, sticky=tk.NSEW)

        # Label Version
        self.label_txt_version = ttk.Label(
            label_frame_config, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_TEST_VERSION'))
        self.label_txt_version.grid(column=0, row=0, pady=5)

        self.label_img_version = ttk.Label(
            label_frame_config, image=self.redIcon)
        self.label_img_version.grid(column=1, row=0, pady=5)

        # Label Space
        self.label_space = tk.Label(label_frame_config, text=' ')
        self.label_space.grid(column=2, row=0, padx=10, pady=5)
        # Fim Label Space

        # Label Language
        self.label_txt_language = ttk.Label(label_frame_config, text=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_LANGUAGE'))
        self.label_txt_language.grid(column=3, row=0, pady=5)

        self.label_language_value = ttk.Label(
            label_frame_config, text=self.language_value.get(), font=('Arial', 13, 'bold'))
        self.label_language_value.grid(column=4, row=0, pady=5)
        # Fim FrameLabel Configuracoes

        # Evento de fechar a janela
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.changeStatus(self.OptionsValue['TEST_VERSION'])

    # Retorna os dados de configuracao
    def returnSetings(self):
        data_config = {
            'TEST_VERSION': True if self.teste_value.get().strip() == msgTxt(self.OptionsValue['LANGUAGES'], 'VALUE_YES') else False,
            'LANGUAGES': self.inverted_dict[self.language_value.get().strip()]
        }
        self.func(data_config)

    def changeStatus(self, result):
        if result:
            self.label_img_version.configure(image=self.greenIcon)
            self.label_img_version.image=self.greenIcon
        else:   
            self.label_img_version.configure(image=self.redIcon)
            self.label_img_version.image=self.redIcon

    # Fecha a janela de configuracao
    def fechar(self):
        self.returnSetings()
        self.destroy()
        self.container.deiconify()
        self.view.enableMenuBar()

    # Exibe a janela anterior
    def on_closing(self):
        self.destroy()
        self.container.deiconify()
        self.view.enableMenuBar()