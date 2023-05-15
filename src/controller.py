from tkinter import filedialog
from os import path
import threading
import arquivos_func as arqsFunc
from arquivos_config import getIdioma as msgTxt
import banco_dados_config as bd
import options_config as op
import model_func as bdFunc

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.OptionsValue = self.view.parent.OptionsValue

        arqsFunc.Arquivo(self.OptionsValue)

        self.file_names = arqsFunc.Arquivo.getFileNames(self)
        self.arquivos = arqsFunc.Arquivo.getArqNomes(self)
        # self.ufs = arqsFunc.Arquivo.getUfs(self)
        self.arq_data = arqsFunc.Arquivo.getArqData(self)
        self.tasks = {}
        self.tasks_bd = {}
        self.btn_status = {'dir_status': None, 'update': None}

    # Atualiza dados da TreeView
    def updateTreeView(self):
        if self.view.frame_index.get() == 0:
            for child in self.view.tree[self.view.frame_index.get()].get_children():
                dict_index = self.view.tree[self.view.frame_index.get()].item(child)[
                    'values'][0]
                if self.tasks[dict_index] != msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_PROCESS'):
                    self.view.tree[self.view.frame_index.get()].delete(child)
                    self.view.tree[self.view.frame_index.get()].insert('', 'end', values=(
                        dict_index, self.tasks[dict_index]), tags=(self.tasks[dict_index],))
        else:
            for child in self.view.tree[self.view.frame_index.get()].get_children():
                dict_index = self.view.tree[self.view.frame_index.get()].item(child)[
                    'values'][0]
                if self.tasks_bd[dict_index]['status'] != msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_PROCESS'):
                    self.view.tree[self.view.frame_index.get()].delete(child)
                    self.view.tree[self.view.frame_index.get()].insert('', 'end', values=(
                        dict_index, self.tasks_bd[dict_index]['total_add'], self.tasks_bd[dict_index]['total_del'], self.tasks_bd[dict_index]['total_upd'], self.tasks_bd[dict_index]['status']), tags=(self.tasks_bd[dict_index]['status'],))
                else:
                    if dict_index == 'LOG_LOGRADOURO' and self.tasks_bd[dict_index]['total_records'] > 0:
                        self.view.tree[self.view.frame_index.get()].delete(
                            child)
                        self.view.tree[self.view.frame_index.get()].insert('', 'end', values=(dict_index, self.tasks_bd[dict_index]['total_add'], self.tasks_bd[dict_index]
                                                                                              ['total_del'], self.tasks_bd[dict_index]['total_upd'], self.tasks_bd[dict_index]['status']), tags=(self.tasks_bd[dict_index]['status'],))
    # Muda status de diretório e conexão com o Banco de Dados
    def changeStatus(self, tipo):
        if tipo == 'sql':
            if self.view.diretorio_arquivos.get() != '':
                self.view.tree[0].delete(*self.view.tree[0].get_children())
                self.view.label_img_status_dir.configure(
                    image=self.view.greenIcon)
                self.view.label_img_status_dir.image = self.view.greenIcon
                self.view.label_img_status_dir_bd.configure(
                    image=self.view.greenIcon)
                self.view.label_img_status_dir_bd.image = self.view.greenIcon
            else:
                self.view.label_img_status_dir.configure(
                    image=self.view.redIcon)
                self.view.label_img_status_dir.image = self.view.redIcon
                self.view.label_img_status_dir_bd.configure(
                    image=self.view.redIcon)
                self.view.label_img_status_dir_bd.image = self.view.redIcon
        else:
            if self.view.diretorio_arquivos.get() != '':
                self.view.tree[0].delete(*self.view.tree[0].get_children())
                self.view.label_img_status_dir.configure(
                    image=self.view.greenIcon)
                self.view.label_img_status_dir.image = self.view.greenIcon
                self.view.label_img_status_dir_bd.configure(
                    image=self.view.greenIcon)
                self.view.label_img_status_dir_bd.image = self.view.greenIcon
            else:
                self.view.label_img_status_dir.configure(
                    image=self.view.redIcon)
                self.view.label_img_status_dir.image = self.view.redIcon
                self.view.label_img_status_dir_bd.configure(
                    image=self.view.redIcon)
                self.view.label_img_status_dir_bd.image = self.view.redIcon

            if self.view.parent.BDSettingsValue:
                self.view.label_img_status_bd.configure(
                    image=self.view.greenIcon)
                self.view.label_img_status_bd.image = self.view.greenIcon
            else:
                self.view.label_img_status_bd.configure(
                    image=self.view.redIcon)
                self.view.label_img_status_bd.image = self.view.redIcon


# -------------------- Inicio Funcoes Arquivo  --------------------
    # Verifica dados do diretório e armazena em variável
    def setDirectory(self, update):
        self.view.diretorio_arquivos.set(filedialog.askdirectory())
        caminho = self.view.diretorio_arquivos.get()+'/'
        if arqsFunc.Arquivo.validaDir(self, self.file_names, self.arquivos, self.arq_data, arqsFunc.Arquivo.getUfs(self), caminho, update) is False:
            self.view.show_error(msgTxt(self.OptionsValue['LANGUAGES'], 'INVALID_CONFIG_DIR'),
                                 msgTxt(self.OptionsValue['LANGUAGES'], 'INVALID_CONFIG_DIR_MSG'))
            if update is self.view.updateOFF():
                self.view.button_dir_export['state'] = 'disabled'
                self.view.button_bd_export['state'] = 'disabled'
            else:
                self.view.button_dir_update['state'] = 'disabled'
                self.view.button_bd_update['state'] = 'disabled'
            self.view.diretorio_arquivos.set('')
            self.btn_status['dir_status'] = False
            self.btn_status['update'] = update
            self.changeStatus('sql')
        else:
            self.btn_status['dir_status'] = True
            self.btn_status['update'] = update
            self.changeStatus('sql')
            if update is self.view.updateOFF():
                self.view.button_dir_export['state'] = 'normal'
                self.view.button_bd_export['state'] = 'normal'
                self.view.button_dir_update['state'] = 'disabled'
                self.view.button_bd_update['state'] = 'disabled'
            else:
                self.view.button_dir_export['state'] = 'disabled'
                self.view.button_bd_export['state'] = 'disabled'
                self.view.button_dir_update['state'] = 'normal'
                self.view.button_bd_update['state'] = 'normal'
        self.view.focusRoot()

    # Incia processo de exportação de dados para arquivo
    def start_export_dir(self, update):
        if self.view.diretorio_arquivos.get() == '':
            if update is self.view.updateOFF():
                self.view.button_dir_export['state'] = 'disabled'
            else:
                self.view.button_dir_update['state'] = 'disabled'
            self.view.show_info(msgTxt(self.OptionsValue['LANGUAGES'], 'CONFIG_INCOMPLETE'),
                                msgTxt(self.OptionsValue['LANGUAGES'], 'WARNING_CONFIG_DIR'))
            return False
        else:
            self.view.progress_frame[self.view.frame_index.get()].tkraise()
            self.view.pb[self.view.frame_index.get()].start(20)
            return True

    # Finaliza o processo de exportação de dados para arquivo
    def stop_export_dir(self):
        self.updateTreeView()
        self.view.button_dir_frame.tkraise()
        self.view.pb[self.view.frame_index.get()].stop()
        self.view.nome_arquivos.clear()
        self.tasks.clear()
        self.arq_data['geral'].clear()
        self.arq_data['logradouros'].clear()
        self.view.diretorio_arquivos.set('')
        self.btn_status['dir_status'] = None
        self.btn_status['update'] = None
        self.changeStatus(self.view.export_types.get())
        self.view.enableTabs()
        self.view.enableMenuBar()

    # Cria tarefa para exportar dados para arquivo
    def handle_export_dir(self, update):
        estado = msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_PROCESS')
        if self.start_export_dir(update):
            self.view.disableTabs()
            self.view.disableMenuBar()

            for file_location in self.arq_data['geral']:
                file_name = path.basename(file_location)
                columns = arqsFunc.Arquivo.logColumns(
                    self, file_name, self.file_names)
                self.view.nome_arquivos.append((f'{file_name}', f'{estado}'))
                export_thread = arqsFunc.CreateWorker(
                    file_location, file_name, columns, self.tasks, update, self.OptionsValue, geral=True)

                export_thread.daemon = True
                export_thread.start()
                self.tasks[file_name] = estado

            if arqsFunc.arqsConfig.EXCLUIRLOGRADOUROS is False:
                columns = ''
                for file_location in self.arq_data['logradouros']:
                    file_name = path.basename(file_location)
                    if (columns == ''):
                        columns = arqsFunc.Arquivo.logColumns(
                            self, file_name, self.file_names)
                    self.view.nome_arquivos.append(
                        (f'{file_name}', f'{estado}'))
                    export_thread = arqsFunc.CreateWorker(
                        file_location, file_name, columns, self.tasks, update, self.OptionsValue, geral=False)

                    export_thread.daemon = True
                    export_thread.start()
                    self.tasks[file_name] = estado

            for arqs in self.view.nome_arquivos:
                self.view.tree[self.view.frame_index.get()].insert(
                    '', 'end', values=arqs, tags=(estado,))

            self.monitor_tasks_dir()

    # Monitora as tarefas criadas e verifica se a execusão foi terminada
    def monitor_tasks_dir(self):
        self.updateTreeView()

        def is_main_thread_active():
            return any((i.name != "MainThread") and i.is_alive() for i in threading.enumerate())
        if is_main_thread_active():
            self.view.after(100, lambda: self.monitor_tasks_dir())
        else:
            self.stop_export_dir()
# -------------------- Fim Funcoes Arquivo  --------------------


# -------------------- Inicio Funcoes BD --------------------
    # Retorna dados de conexão do Banco de Dados
    def mysql_conf(self):
        self.view.parent.withdraw()
        self.view.parent.bd_settings = bd.BDConfig(
            self.view.parent, self.updateBDConfig, self.view.parent.BDSettingsValue, self.view, self.OptionsValue)

    # Atualiza configurações de conexão do Banco de Dados
    def updateBDConfig(self, n):
        self.view.parent.BDSettingsValue = n
        if self.view.parent.BDSettingsValue:
            if self.btn_status['dir_status'] and self.btn_status['update'] is False:
                self.view.button_bd_export['state'] = 'normal'
                self.view.button_bd_update['state'] = 'disabled'
            elif self.btn_status['dir_status'] and self.btn_status['update']:
                self.view.button_bd_export['state'] = 'disabled'
                self.view.button_bd_update['state'] = 'normal'
            else:
                self.view.button_bd_export['state'] = 'normal'
                self.view.button_bd_update['state'] = 'normal'
        else:
            self.view.button_bd_export['state'] = 'disabled'
            self.view.button_bd_update['state'] = 'disabled'
        self.changeStatus('bd')

    # Apaga todos os dados das tabelas
    def truncateTable(self, table_name):
        try:
            conexao = self.model.getConexao(self.view.parent)
            sql = self.model.getTruncateSQL(table_name)
            conexao['mycursor'].execute(sql)
            conexao['conexao'].commit()
            conexao['mycursor'].close()
            conexao['conexao'].close()
        except:
            self.view.show_error(msgTxt(self.OptionsValue['LANGUAGES'], 'RUN_FAIL'), msgTxt(self.OptionsValue['LANGUAGES'], 'TABLE_CLEAN_FAIL') + table_name)

    # Incia processo de exportação de dados para o Banco de Dados
    def start_export_bd(self, update):
        if self.view.diretorio_arquivos.get() == '':
            if update is self.view.updateOFF():
                self.view.button_bd_export['state'] = 'disabled'
            else:
                self.view.button_bd_update['state'] = 'disabled'
            self.view.show_info(msgTxt(self.OptionsValue['LANGUAGES'], 'CONFIG_INCOMPLETE'),
                                msgTxt(self.OptionsValue['LANGUAGES'], 'WARNING_CONFIG_DIR'))
            return False
        elif self.view.parent.BDSettingsValue is None:
            if update is self.view.updateOFF():
                self.view.button_bd_export['state'] = 'disabled'
            else:
                self.view.button_bd_update['state'] = 'disabled'
            self.view.show_info(msgTxt(self.OptionsValue['LANGUAGES'], 'CONFIG_INCOMPLETE'),
                                msgTxt(self.OptionsValue['LANGUAGES'], 'WARNING_CONFIG_BD'))
            return False
        else:
            if self.model.checkIfTablesExist() is False:
                if self.model.criaTabela() is False:
                    self.view.show_error(
                        msgTxt(self.OptionsValue['LANGUAGES'], 'BD_ERROR'), msgTxt(self.OptionsValue['LANGUAGES'], 'TABLE_CREATE_FAIL'))
                    return False
            else:
                if update is False:
                    if self.view.show_confirm(msgTxt(self.OptionsValue['LANGUAGES'], 'WARNING_TITLE'), msgTxt(self.OptionsValue['LANGUAGES'], 'WARNING_ERASE_DATA')):
                        self.view.progress_frame[self.view.frame_index.get(
                        )].tkraise()
                        self.view.pb[self.view.frame_index.get()].start(20)
                        return True
                    else:
                        return False
                else:
                    self.view.progress_frame[self.view.frame_index.get(
                    )].tkraise()
                    self.view.pb[self.view.frame_index.get()].start(20)
                    return True
            self.view.progress_frame[self.view.frame_index.get()].tkraise()
            self.view.pb[self.view.frame_index.get()].start(20)
            return True

    # Finaliza o processo de exportação de dados para o Banco de Dados
    def stop_export_bd(self):
        self.updateTreeView()
        self.view.button_bd_frame.tkraise()
        self.view.pb[self.view.frame_index.get()].stop()
        self.view.nome_arquivos.clear()
        self.tasks.clear()
        self.tasks_bd.clear()
        self.view.diretorio_arquivos.set('')
        self.btn_status['dir_status'] = None
        self.btn_status['update'] = None
        self.changeStatus(self.view.export_types.get())
        self.view.enableTabs()
        self.view.enableMenuBar()

    # Cria tarefa para exportar dados para o Banco de Dados
    def handle_export_bd(self, update):
        estado = msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_PROCESS')
        self.view.tree[1].delete(*self.view.tree[1].get_children())
        if self.start_export_bd(update):
            self.view.disableTabs()
            self.view.disableMenuBar()

            for file_location in self.arq_data['geral']:
                file_name = path.basename(file_location)
                if update is False:
                    tabela = file_name[0:-4]
                    self.truncateTable(tabela)
                else:
                    tabela = file_name[0:-4].replace("DELTA_", "")
                columns = arqsFunc.Arquivo.logColumns(
                    self, file_name, self.file_names)
                self.view.nome_arquivos.append(
                    (f'{tabela}', 0, 0, 0, f'{estado}'))
                export_thread = bdFunc.CreateWorker(
                    self.view.parent, file_location, file_name, tabela, columns, self.tasks_bd, self.tasks, self.OptionsValue, update)

                export_thread.daemon = True
                export_thread.start()
                self.tasks_bd[tabela] = {
                    'status': estado, 'total_add': 0, 'total_del': 0, 'total_upd': 0, 'total_records': 0}

            if arqsFunc.arqsConfig.EXCLUIRLOGRADOUROS is False:
                columns = ''
                tabela = 'LOG_LOGRADOURO'
                if update is False:
                    self.truncateTable(tabela)
                for file_location in self.arq_data['logradouros']:
                    file_name = path.basename(file_location)
                    if (columns == ''):
                        columns = arqsFunc.Arquivo.logColumns(
                            self, file_name, self.file_names)
                        self.view.nome_arquivos.append(
                            (f'{tabela}', 0, 0, 0, f'{estado}'))
                        self.tasks_bd[tabela] = {
                            'status': estado, 'total_add': 0, 'total_del': 0, 'total_upd': 0, 'total_records': 0}
                    export_thread = bdFunc.CreateWorker(
                        self.view.parent, file_location, file_name, tabela, columns, self.tasks_bd, self.tasks, self.OptionsValue, update)

                    export_thread.daemon = True
                    export_thread.start()
                    self.tasks[file_name] = {
                        'status': estado, 'total_add': 0, 'total_del': 0, 'total_upd': 0, 'total_records': 0}

            for arqs in self.view.nome_arquivos:
                self.view.tree[self.view.frame_index.get()].insert(
                    '', 'end', values=arqs, tags=(estado,))

            self.monitor_tasks_bd()

    # Monitora as tarefas criadas e verifica se a execusão foi terminada
    def monitor_tasks_bd(self):
        self.updateTreeView()
        def is_main_thread_active():
            return any((i.name != "MainThread") and i.is_alive() for i in threading.enumerate())
        if is_main_thread_active():
            self.view.after(100, lambda: self.monitor_tasks_bd())
        else:
            self.stop_export_bd()
# -------------------- Fim Funcoes BD --------------------


# -------------------- Inicio Funcoes Opcoes --------------------
    # Retorna dados de configurações
    def option_conf(self):
        self.view.parent.withdraw()
        self.view.parent.op_settings = op.OpConfig(
            self.view.parent, self.updateOpConfig, self.OptionsValue, self.view)

    # Atualiza configurações
    def updateOpConfig(self, n):
        self.OptionsValue = n
        self.view.setTextLanguages(self.OptionsValue)
# -------------------- Fim Funcoes Opcoes --------------------