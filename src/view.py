import tkinter as tk
import sys
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter.messagebox import askyesno
from img_configuracoes import imgPath
from arquivos_config import getIdioma as msgTxt


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.OptionsValue = parent.OptionsValue

        self.frame_index = tk.IntVar()

        self.tree_frame = []
        self.tree = []

        self.progress_frame = []
        self.pb = []

        self.redIcon = tk.PhotoImage(file=imgPath.getIcon(self, 'redIcon'))
        self.yellowIcon = tk.PhotoImage(
            file=imgPath.getIcon(self, 'yellowIcon'))
        self.greenIcon = tk.PhotoImage(file=imgPath.getIcon(self, 'greenIcon'))

        self.infoIcon = tk.PhotoImage(file=imgPath.getIcon(self, 'info'))
        self.questionIcon = tk.PhotoImage(
            file=imgPath.getIcon(self, 'question'))
        self.warningIcon = tk.PhotoImage(file=imgPath.getIcon(self, 'warning'))
        self.errorIcon = tk.PhotoImage(file=imgPath.getIcon(self, 'error'))
        self.appIcon = tk.PhotoImage(file=imgPath.getIcon(self, 'app'))

        # self.createMenus()

        self.export_types = tk.StringVar()
        self.diretorio_arquivos = tk.StringVar()

        # Definir o controlador
        self.controller = None

# ************************************ Inicio Notebook ************************************
        # create a notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        # create frames
        self.frame1 = ttk.Frame(self.notebook, width=650, height=380)
        self.frame2 = ttk.Frame(self.notebook, width=650, height=380)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)

        # Estilo personalizado do TreeView
        style = ttk.Style()
        style.configure("mystyle.Treeview.Heading",
                        font=('Calibri', 13, 'bold'))

# --------------------------------- INICIO FRAME 1 -----------------------------------------
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)

        # # Inicio Barra de Progressso
        self.createProgressBar(self.frame1, 0)
        # # Fim Barra de Progressso

        # Inicio Botao
        # Button frame
        self.button_dir_frame = ttk.Frame(self.frame1)

        self.button_dir_frame.columnconfigure(index=0, weight=1)
        self.button_dir_frame.columnconfigure(index=1, weight=1)
        self.button_dir_frame.columnconfigure(index=2, weight=1)
        self.button_dir_frame.columnconfigure(index=3, weight=1)

        self.button_dir_export = ttk.Button(
            self.button_dir_frame,
            text='',
            command=self.btn_dir_export_click,
            state=tk.NORMAL
        )
        self.button_dir_export.grid(column=1, row=0)
        # Fim Botao

        # Inicio Botao2
        self.button_dir_update = ttk.Button(
            self.button_dir_frame,
            text='',
            command=self.btn_dir_update_click,
            state=tk.NORMAL
        )
        self.button_dir_update.grid(column=2, row=0)

        self.button_dir_frame.grid(
            column=0, columnspan=3, row=3, sticky=tk.NSEW)
        # Fim Botao2

        # Inicio FrameLabel Status Diretorio
        self.label_frame1_status = tk.LabelFrame(
            self.frame1, text='', labelanchor=tk.NW)
        self.label_frame1_status.grid(column=0, columnspan=3,
                                      row=6, pady=5, sticky=tk.NSEW)

        # Label Status Diretorio
        self.label_txt_status_dir = ttk.Label(
            self.label_frame1_status, text='')
        self.label_txt_status_dir.grid(column=0, row=0, pady=5)

        self.label_img_status_dir = ttk.Label(
            self.label_frame1_status, image=self.redIcon)
        self.label_img_status_dir.grid(column=1, row=0, pady=5)
        # Fim FrameLabel Status Diretorio

        # Label Space
        self.label_space = tk.Label(self.label_frame1_status, text=' ')
        self.label_space.grid(column=2, row=0, padx=10, pady=5)
        # Fim Label Space

        # Label Version
        self.label_txt_version = ttk.Label(
            self.label_frame1_status, text='')
        self.label_txt_version.grid(column=3, row=0, pady=5)

        self.label_img_version = ttk.Label(
            self.label_frame1_status, image=self.redIcon)
        self.label_img_version.grid(column=4, row=0, pady=5)

        # Label Space
        self.label_space = tk.Label(self.label_frame1_status, text=' ')
        self.label_space.grid(column=5, row=0, padx=10, pady=5)
        # Fim Label Space

        # Label Language
        self.label_txt_language = ttk.Label(self.label_frame1_status, text='')
        self.label_txt_language.grid(column=6, row=0, pady=5)

        self.label_language_value = ttk.Label(
            self.label_frame1_status, text='', font=('Arial', 13, 'bold'))
        self.label_language_value.grid(column=7, row=0, pady=5)
        # Fim FrameLabel Configuracoes

# ----------------------------------- FIM FRAME 1 ------------------------------------------


# --------------------------------- INICIO FRAME 2 -----------------------------------------
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.columnconfigure(index=3, weight=1)

        # # Inicio Barra de Progressso

        self.createProgressBar(self.frame2, 1)

        # # Fim Barra de Progressso

        # Inicio Botao
        # Button frame
        self.button_bd_frame = ttk.Frame(self.frame2)

        self.button_bd_frame.columnconfigure(index=0, weight=1)
        self.button_bd_frame.columnconfigure(index=1, weight=1)
        self.button_bd_frame.columnconfigure(index=2, weight=1)
        self.button_bd_frame.columnconfigure(index=3, weight=1)

        self.button_bd_export = ttk.Button(
            self.button_bd_frame,
            text='',
            command=self.btn_bd_export_click,
            state=tk.NORMAL
        )
        self.button_bd_export.grid(column=1, row=0)
        # Fim Botao

        # Inicio Botao2
        self.button_bd_update = ttk.Button(
            self.button_bd_frame,
            text='',
            command=self.btn_bd_update_click,
            state=tk.NORMAL
        )
        self.button_bd_update.grid(column=2, row=0)

        self.button_bd_frame.grid(
            column=0, columnspan=3, row=3, sticky=tk.NSEW)
        # Fim Botao2

        # Inicio FrameLabel Status da Conexao
        self.label_frame2_status = tk.LabelFrame(
            self.frame2, text='', labelanchor=tk.NW)
        self.label_frame2_status.grid(column=0, columnspan=3,
                                      row=6, pady=5, sticky=tk.NSEW)

        # Label Status Diretorio BD
        self.label_txt_status_dir_bd = ttk.Label(
            self.label_frame2_status, text='')
        self.label_txt_status_dir_bd.grid(column=0, row=0, pady=5)

        self.label_img_status_dir_bd = ttk.Label(
            self.label_frame2_status, image=self.redIcon)
        self.label_img_status_dir_bd.grid(column=1, row=0, pady=5)
        # Fim Label Status Diretorio BD

        # Label Space
        self.label_frame2_space = tk.Label(self.label_frame2_status, text=' ')
        self.label_frame2_space.grid(column=2, row=0, padx=10, pady=5)
        # Fim Label Space

        # Label Status Conexao
        self.label_txt_status_bd = ttk.Label(
            self.label_frame2_status, text='')
        self.label_txt_status_bd.grid(column=3, row=0, pady=5)

        self.label_img_status_bd = ttk.Label(
            self.label_frame2_status, image=self.redIcon)
        self.label_img_status_bd.grid(column=4, row=0, pady=5)

        # Label Space
        self.label_frame2_space = tk.Label(self.label_frame2_status, text=' ')
        self.label_frame2_space.grid(column=5, row=0, padx=10, pady=5)
        # Fim Label Space

        # Label Version
        self.label_txt_version_bd = ttk.Label(
            self.label_frame2_status, text='')
        self.label_txt_version_bd.grid(column=6, row=0, pady=5)

        self.label_img_version_bd = ttk.Label(
            self.label_frame2_status, image=self.redIcon)
        self.label_img_version_bd.grid(column=7, row=0, pady=5)

        # Label Space
        self.label_frame2_space = tk.Label(self.label_frame2_status, text=' ')
        self.label_frame2_space.grid(column=8, row=0, padx=10, pady=5)
        # Fim Label Space

        # Label Language
        self.label_txt_language_bd = ttk.Label(
            self.label_frame2_status, text='')
        self.label_txt_language_bd.grid(column=9, row=0, pady=5)

        self.label_language_value_bd = ttk.Label(
            self.label_frame2_status, text='', font=('Arial', 13, 'bold'))
        self.label_language_value_bd.grid(column=10, row=0, pady=5)
        # Fim FrameLabel Configuracoes

        # Fim FrameLabel Status da Conexao

# ----------------------------------- FIM FRAME 2 ------------------------------------------

        self.notebook.add(self.frame1, text='')
        self.notebook.add(self.frame2, text='')
        self.notebook_tabs = (0, 1)

        self.notebook.bind('<<NotebookTabChanged>>', self.setTipo)

        self.setTextLanguages(self.OptionsValue)
# ************************************ Fim Notebook ************************************

    def createMenus(self):
        # Cria MenuBar
        self.menubar = tk.Menu(self)
        self.parent.config(menu=self.menubar)

        # Cria menu Configuracoes
        self.config_menu = tk.Menu(self.menubar, tearoff=False)

        # Cria itens do menu Configuracoes
        self.config_menu.add_command(
            label=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_DIR_EXPORT'), command=self.menu_click_diretorio_export)
        self.config_menu.add_command(
            label=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_DIR_UPDATE'), command=self.menu_click_diretorio_update)
        self.config_menu.add_command(
            label=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_BD_CONNECT'), command=self.menu_click_banco_dados)
        self.config_menu.add_separator()
        self.config_menu.add_command(
            label=msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_OPTION'), command=self.menu_click_opcoes)
        self.config_menu.add_separator()
        self.config_menu.add_command(label=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_EXIT'), command=self.parent.destroy)

        # Adiciona o menu Configuracoes no MenuBar
        self.menubar.add_cascade(label=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_CONFIG'), menu=self.config_menu, underline=0)

        # Cria o menu Ajuda
        self.help_menu = tk.Menu(self.menubar, tearoff=False)

        # Cria itens do menu Ajuda
        self.help_menu.add_command(label=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_ABOUT'), command=self.menu_click_sobre)

        # Adiciona o menu Ajuda no MenuBar
        self.menubar.add_cascade(label=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_ABOUT'), menu=self.help_menu, underline=0)

    def set_controller(self, controller):
        self.controller = controller

    def setTipo(self, *args):
        frame = self.notebook.index(self.notebook.select())
        self.frame_index.set(frame)
        if frame == 0:
            self.export_types.set('sql')
        else:
            self.export_types.set('bd')

    def set_icon(self, icon):
        if sys.platform == "darwin":
            self.parent.iconphoto(False, icon)

    def show_info(self, titulo, msg):
        self.set_icon(self.infoIcon)
        showinfo(parent=self, title=titulo, message=msg)
        self.set_icon(self.appIcon)

    def show_warning(self, titulo, msg):
        self.set_icon(self.warningIcon)
        showwarning(parent=self, title=titulo, message=msg)
        self.set_icon(self.appIcon)

    def show_error(self, titulo, msg):
        self.set_icon(self.errorIcon)
        showerror(parent=self, title=titulo, message=msg)
        self.set_icon(self.appIcon)

    def show_confirm(self, titulo, msg):
        self.set_icon(self.questionIcon)
        result = askyesno(parent=self, title=titulo, message=msg)
        self.set_icon(self.appIcon)
        return result

    def focusRoot(self):
        self.focus_force()
        self.lift()
        self.update()

    def disableTabs(self):
        for x in self.notebook_tabs:
            if self.frame_index.get() != x:
                if x == 0:
                    self.notebook.tab(self.frame1, state='disabled')
                else:
                    self.notebook.tab(self.frame2, state='disabled')

    def enableTabs(self):
        self.notebook.tab(self.frame1, state='normal')
        self.notebook.tab(self.frame2, state='normal')

    def disableMenuBar(self):
        self.menubar.entryconfig(0, state='disabled')
        self.menubar.entryconfig(1, state='disabled')

    def enableMenuBar(self):
        self.parent.update()
        self.menubar.entryconfig(0, state='normal')
        self.menubar.entryconfig(1, state='normal')

    def updateON(self):
        return True

    def updateOFF(self):
        return False

    def changeStatus(self, result):
        if result:
            self.label_img_version.configure(image=self.greenIcon)
            self.label_img_version.image = self.greenIcon
            self.label_img_version_bd.configure(image=self.greenIcon)
            self.label_img_version_bd.image = self.greenIcon
        else:
            self.label_img_version.configure(image=self.redIcon)
            self.label_img_version.image = self.redIcon
            self.label_img_version_bd.configure(image=self.redIcon)
            self.label_img_version_bd.image = self.redIcon

    def setTextLanguages(self, options_value):
        self.OptionsValue = options_value
        # --- Inicio Menu ---
        self.createMenus()
        # --- Fim Menu ---

        # --- Inicio Frame 1 ---
        self.button_dir_export.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'BTN_EXPORT'))
        self.button_dir_update.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'BTN_UPDATE'))

        # # Inicio TreeView
        frame1_colunas = {
            'columns': ('nome', 'estado'),
            'anchor': ('', ''),
            'headings': (msgTxt(self.OptionsValue['LANGUAGES'], 'HEADING_FILE_NAME'), msgTxt(self.OptionsValue['LANGUAGES'], 'HEADING_STATUS')),
            'minsize': (0, 0),
            'maxsize': (380, 0),
            'tags': {
                'name': (msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_PROCESS'), msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EXPORT'), msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EMPTY'), msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_ERROR')),
                'foreground': ('blue', 'green', 'goldenrod', 'red')
            }
        }
        self.createTreeView(self.frame1, 0, **frame1_colunas)
        # # Fim TreeView

        self.label_frame1_status.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_DIR_STATUS'))

        self.label_txt_status_dir.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_DIR'))

        # Label Version
        self.label_txt_version.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_TEST_VERSION'))
        self.changeStatus(self.OptionsValue['TEST_VERSION'])

        self.label_txt_language.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_LANGUAGE'))
        self.label_language_value.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LANGUAGES')[self.OptionsValue['LANGUAGES']])
        # --- Fim Frame 1 ---

        # --- Inicio Frame 2 ---
        self.button_bd_export.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'BTN_EXPORT'))
        self.button_bd_update.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'BTN_UPDATE'))
        # # Inicio TreeView
        frame2_colunas = {
            # 'columns': ('nome', 'records', 'estado'),
            'columns': ('nome', 'add', 'del', 'upd', 'estado'),
            'anchor': ('', 'center', 'center', 'center', ''),
            'headings': (msgTxt(self.OptionsValue['LANGUAGES'], 'HEADING_TABLE_NAME'), msgTxt(self.OptionsValue['LANGUAGES'], 'HEADING_ADD_RECORDS'), msgTxt(self.OptionsValue['LANGUAGES'], 'HEADING_DEL_RECORDS'), msgTxt(self.OptionsValue['LANGUAGES'], 'HEADING_UPD_RECORDS'), msgTxt(self.OptionsValue['LANGUAGES'], 'HEADING_STATUS')),
            'minsize': (0, 0, 0, 0, 0),
            'maxsize': (215, 100, 75, 90, 100),
            'tags': {
                'name': (msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_PROCESS'), msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EXPORT'), msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EMPTY'), msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_ERROR')),
                'foreground': ('blue', 'green', 'goldenrod', 'red')
            }
        }
        self.createTreeView(self.frame2, 1, **frame2_colunas)
        # # Fim TreeView
        self.label_frame2_status.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_BD_STATUS'))

        self.label_txt_status_dir_bd.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_DIR_STATUS'))
        self.label_txt_status_bd.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_CONNECTION'))

        # Label Version
        self.label_txt_version_bd.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_TEST_VERSION'))

        self.label_txt_language_bd.config(text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_LANGUAGE'))
        self.label_language_value_bd.config(text=msgTxt(self.OptionsValue['LANGUAGES'], 'LANGUAGES')[
                                            self.OptionsValue['LANGUAGES']], font=('Arial', 13, 'bold'))
        # --- Fim Frame 2 ---

        self.notebook.tab(0, text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_EXPORT_FILE'))
        self.notebook.tab(1, text=msgTxt(
            self.OptionsValue['LANGUAGES'], 'LABEL_EXPORT_BD'))

# -------------------- Inicio Widget dos Frames --------------------
    def createProgressBar(self, frame, frame_index):
        # Inicio Barra de Progressso
        # Progress frame
        progress_frame = ttk.Frame(frame)
        self.progress_frame.append(progress_frame)

        # configure the grid to place the progress bar is at the center
        self.progress_frame[frame_index].columnconfigure(index=0, weight=1)
        self.progress_frame[frame_index].rowconfigure(index=3, weight=1)

        # progressbar
        progressbar = ttk.Progressbar(
            self.progress_frame[frame_index], orient=tk.HORIZONTAL, mode='indeterminate')
        self.pb.append(progressbar)
        self.pb[frame_index].grid(
            column=0, columnspan=3, row=3, pady=15, sticky=tk.EW)

        # place the progress frame
        self.progress_frame[frame_index].grid(
            column=0, columnspan=3, row=3, sticky=tk.NSEW)
        # Fim Barra de Progressso

    def createTreeView(self, frame, frame_index, **colunas):
        # Inicio TreeView
        tree_frame = ttk.Frame(frame)
        self.tree_frame.append(tree_frame)
        # Definir as colunas
        columns = colunas['columns']

        # Definir a tabela
        treeview = ttk.Treeview(
            self.tree_frame[frame_index], columns=columns, show='headings', style='mystyle.Treeview')
        self.tree.append(treeview)

        # Definir os cabeçalhos
        x = 0
        for headings in colunas['headings']:
            self.tree[frame_index].heading(
                colunas['columns'][x], text=headings)
            x += 1

        self.nome_arquivos = []

        # Posiciona tree na janela
        self.tree[frame_index].grid(column=0, row=5, sticky=tk.NSEW)

        # Cria barra de rolagem
        scrollbar = ttk.Scrollbar(
            self.tree_frame[frame_index], orient='vertical', command=self.tree[frame_index].yview)
        # Associa ao objeto tree
        self.tree[frame_index].configure(yscrollcommand=scrollbar.set)
        # Posiciona a barra de rolagem
        scrollbar.grid(column=1, row=5, sticky='ns')

        x = 0
        for sizes in colunas['maxsize']:
            if sizes != 0:
                self.tree[frame_index].column(
                    colunas['columns'][x], minwidth=0, width=sizes, stretch=tk.NO)
            x += 1

        # Define Alinhamento
        x = 0
        for anchor_value in colunas['anchor']:
            if anchor_value != '':
                self.tree[frame_index].column(
                    colunas['columns'][x], anchor=anchor_value)
            x += 1

        self.tree_frame[frame_index].grid(column=0, columnspan=3, row=5)

        x = 0
        for tag_config in colunas['tags']['name']:
            self.tree[frame_index].tag_configure(
                tag_config, foreground=colunas['tags']['foreground'][x])
            x += 1
        # Fim TreeView

# -------------------- Fim Widget dos Frames --------------------


# -------------------- Inicio Funcoes do Menu --------------------

    def menu_click_diretorio_export(self):
        if self.controller:
            self.controller.setDirectory(self.updateOFF())

    def menu_click_diretorio_update(self):
        if self.controller:
            self.controller.setDirectory(self.updateON())

    def menu_click_banco_dados(self):
        if self.controller:
            self.disableMenuBar()
            self.controller.mysql_conf()

    def menu_click_opcoes(self):
        if self.controller:
            self.disableMenuBar()
            self.controller.option_conf()

    def menu_click_sobre(self):
        self.show_info(msgTxt(self.OptionsValue['LANGUAGES'], 'LABEL_ABOUT'), msgTxt(
            self.OptionsValue['LANGUAGES'], 'APP_AUTHOR'))

# -------------------- Fim Funcoes do Menu --------------------


# -------------------- Inicio Funcoes dos Botoes --------------------

    def btn_dir_export_click(self):
        if self.controller:
            self.controller.handle_export_dir(self.updateOFF())

    def btn_dir_update_click(self):
        if self.controller:
            self.controller.handle_export_dir(self.updateON())

    def btn_bd_export_click(self):
        if self.controller:
            self.controller.handle_export_bd(self.updateOFF())

    def btn_bd_update_click(self):
        if self.controller:
            self.controller.handle_export_bd(self.updateON())
# -------------------- Fim Funcoes dos Botoes --------------------
