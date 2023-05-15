import os
import sys
import tkinter as tk
import arquivos_config as arqsConfig


class imgPath(tk.Tk):
    def __init__(self):
        super().__init__()

    def getIcon(self, name):
        if name == 'redIcon':
            result = os.path.join(arqsConfig.BASEPATHIMGS, 'red.png')
        elif name == 'yellowIcon':
            result = os.path.join(arqsConfig.BASEPATHIMGS, 'yellow.png')
        elif name == 'greenIcon':
            result = os.path.join(arqsConfig.BASEPATHIMGS, 'green.png')
        elif name == 'info':
            result = os.path.join(arqsConfig.BASEPATHIMGS, 'info.png')
        elif name == 'question':
            result = os.path.join(arqsConfig.BASEPATHIMGS, 'question.png')
        elif name == 'warning':
            result = os.path.join(arqsConfig.BASEPATHIMGS, 'warning.png')
        elif name == 'error':
            result = os.path.join(arqsConfig.BASEPATHIMGS, 'error.png')
        elif name == 'app':
            result = os.path.join(arqsConfig.BASEPATHIMGS, 'ednexport.png')
        else:
            result = None        
        return result
