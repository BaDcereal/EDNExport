import sys
import os
import tkinter as tk
import model
import view
import controller
import arquivos_config as arqsConfig
from arquivos_config import getIdioma as msgTxt

OPTIONS_VALUE = {'TEST_VERSION': False, 'LANGUAGES': 'pt-br'}


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuracao das Opcoes padrao
        self.op_settings = None
        self.OptionsValue = OPTIONS_VALUE

        self.title(msgTxt(self.OptionsValue['LANGUAGES'], 'APP_TITLE'))

        # Configuração Tamanho e Posição da janela
        if sys.platform == 'darwin':
            self.geometry('650x400+500+200')
        else:
            self.geometry('620x400+350+200')
        self.resizable(False, False)

        self.iconbitmap(os.path.join(arqsConfig.BASEPATHIMGS, 'favicon.ico'))

        # Dados da Conexao
        self.bd_settings = None
        self.BDSettingsValue = None

        # Criar modelo
        modelo = model.Model(self)

        # Criar um view e definir seu container
        visualizador = view.View(self)
        visualizador.grid(column=0, row=0, padx=10, pady=10)

        # Criar o controlador
        controlador = controller.Controller(modelo, visualizador)

        # Definir o controlador para o view
        visualizador.set_controller(controlador)


if __name__ == '__main__':
    try:
        app = App()
        app.mainloop()
    except:
        view.showerror(msgTxt(OPTIONS_VALUE['LANGUAGES'], 'INVALID_CONFIG_DIR'), msgTxt(
            'pt-br', 'ERROR_IMG_DIR'))
