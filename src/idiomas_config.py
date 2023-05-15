""" Para adicionar uma tradução para outro idioma, criar uma classe com o idioma desejado
seguindo o mesmo padrão, adicione a classe e o nome do idioma na constante LANGUAGES, 
depois crie uma nova condição no método getIdioma() do arquivo arquivos_config.py em seguida 
para usar esse idioma criado altera a constante IDIOMA do arquivo arquivos_config.py com a 
string criada na condição."""

# Constantes das Mensagens
class ptBR:
    # Para um novo idioma adicionar sigla do idioma e o nome idioma
    LANGUAGES = {'pt-br': 'Português', 'en': 'Inglês'}

    # Titulos e Mensagens de Caixas de Txt
    APP_TITLE = 'EDNExport'
    APP_VERSION = 'beta 0.0.1'
    APP_COPYRIGHT = 'Copyright © 2023 \nFausto Ferreira - BaDcereal \nMIT License'
    APP_AUTHOR = f'{APP_TITLE} {APP_VERSION} \n{APP_COPYRIGHT}'
    CONFIG_INCOMPLETE = 'Configuração Incompleta'
    WARNING_CONFIG_DIR = 'Atenção configure o Diretório Delimitado.'
    WARNING_CONFIG_BD = 'Atenção configure a Conexão Banco Dados.'
    WARNING_TITLE = 'ATENÇÃO'
    WARNING_ERASE_DATA = 'Atenção todos os dados exportados anteriormente serão removidos. Deseja continuar?'
    CONNECTION_ERRO_TITLE = 'Erro na Conexão'
    CONNECTION_ERRO_MSG = 'Erro ao tentar se conectar com o Banco de Dados!'
    INVALID_CONFIG_DIR = 'Diretório Inválido'
    INVALID_CONFIG_DIR_MSG = 'Este diretório não contém os arquivos necessários para executar exportação dos dados. Selecione o diretório Delimitado na pasta eDNE e tente novamente.'
    RUN_FAIL = 'Falha na execução'
    TABLE_CLEAN_FAIL = 'Ocorreu um erro ao tentar limpar a tabela '
    TABLE_CREATE_FAIL = 'Falha da criação das tabelas. Verifique as permissões do usuário no Banco de Dados e tente novamente.'
    BD_ERROR = 'Erro no Banco de Dados'
    BD_CONFIG_TITLE = 'Configuração Banco de Dados'
    ERROR_TITLE = 'Ocorreu um erro'
    ERROR_READ_FILE = 'Falha na leitura do arquivo.\nVerifique se o arquivo Delimitado esta correto e tenta novamente.'
    ERROR_IMG_DIR = 'Diretório de imagens não encontrado. Verifique as configurações e tente novamente.'
    OP_CONFIG_TITLE = 'Configuração das Opções'

    # Texto de Labels
    LABEL_DIR_EXPORT = 'Diretório Delimitado Exportar'
    LABEL_DIR_UPDATE = 'Diretório Delimitado Atualizar'
    LABEL_DIR = 'Diretório Delimitado:'
    LABEL_DIR_STATUS = ' Status do Diretório '
    LABEL_CONNECTION = 'Conexão:'
    LABEL_BD_HOST = 'Endereço Servidor:'
    LABEL_BD_USER = 'Usuário:'
    LABEL_BD_PASSWORD = 'Senha:'
    LABEL_BD_DATABASE = 'Base Dados:'
    LABEL_BD_STATUS = ' Status Conexão '
    LABEL_BD_CONNECT = 'Conexão Banco Dados'
    LABEL_OPTION = 'Configurar Opções'
    LABEL_EXIT = 'Sair'
    LABEL_CONFIG = 'Configurações'
    LABEL_ABOUT = 'Sobre'
    LABEL_HELP = 'Ajuda'
    LABEL_EXPORT_FILE = 'Exporta para arquivo SQL'
    LABEL_EXPORT_BD = 'Exporta para Banco de Dados'
    LABEL_LANGUAGE = 'Idioma:'
    LABEL_TEST_VERSION = 'Versão de Teste:'
    
    # Texto de Botões
    BTN_EXPORT = 'Exportar'
    BTN_UPDATE = 'Atualizar'
    BTN_CLOSE = 'Confirmar'
    BTN_CONNECT = 'Conectar'

    # Headings do TreeView
    HEADING_FILE_NAME = 'Nome do Arquivo'
    HEADING_STATUS = 'Status'
    HEADING_TABLE_NAME = 'Nome da Tabela'
    HEADING_TOTAL_RECORDS = 'Total de Registros'
    HEADING_ADD_RECORDS = 'Adicionado'
    HEADING_DEL_RECORDS = 'Excluído'
    HEADING_UPD_RECORDS = 'Atualizado'
    TAG_PROCESS = 'Processando...'
    TAG_EXPORT = 'Exportado'
    TAG_EMPTY = 'Vazio'
    TAG_ERROR = 'Erro'

    # ComboBox Texto
    VALUE_YES = 'Sim'
    VALUE_NO = 'Não'

    @staticmethod
    def getText(key=None):
        text_dict = {'LANGUAGES': ptBR.LANGUAGES,
                     'APP_TITLE': ptBR.APP_TITLE,
                     'APP_VERSION': ptBR.APP_VERSION,
                     'APP_AUTHOR': ptBR.APP_AUTHOR,
                     'CONFIG_INCOMPLETE': ptBR.CONFIG_INCOMPLETE,
                     'WARNING_CONFIG_DIR': ptBR.WARNING_CONFIG_DIR, 
                     'WARNING_CONFIG_BD': ptBR.WARNING_CONFIG_BD,
                     'WARNING_TITLE': ptBR.WARNING_TITLE,
                     'WARNING_ERASE_DATA': ptBR.WARNING_ERASE_DATA,
                     'CONNECTION_ERRO_TITLE': ptBR.CONNECTION_ERRO_TITLE,
                     'CONNECTION_ERRO_MSG': ptBR.CONNECTION_ERRO_MSG,
                     'INVALID_CONFIG_DIR': ptBR.INVALID_CONFIG_DIR,
                     'INVALID_CONFIG_DIR_MSG': ptBR.INVALID_CONFIG_DIR_MSG,
                     'RUN_FAIL': ptBR.RUN_FAIL,
                     'TABLE_CLEAN_FAIL': ptBR.TABLE_CLEAN_FAIL,
                     'TABLE_CREATE_FAIL': ptBR.TABLE_CREATE_FAIL,
                     'BD_ERROR': ptBR.BD_ERROR,
                     'BD_CONFIG_TITLE': ptBR.BD_CONFIG_TITLE,
                     'ERROR_TITLE': ptBR.ERROR_TITLE,
                     'ERROR_READ_FILE': ptBR.ERROR_READ_FILE,
                     'ERROR_IMG_DIR': ptBR.ERROR_IMG_DIR,
                     'OP_CONFIG_TITLE': ptBR.OP_CONFIG_TITLE,
                     'LABEL_DIR_EXPORT': ptBR.LABEL_DIR_EXPORT,
                     'LABEL_DIR_UPDATE': ptBR.LABEL_DIR_UPDATE,
                     'LABEL_DIR': ptBR.LABEL_DIR,
                     'LABEL_DIR_STATUS': ptBR.LABEL_DIR_STATUS,
                     'LABEL_CONNECTION': ptBR.LABEL_CONNECTION,
                     'LABEL_BD_HOST': ptBR.LABEL_BD_HOST,
                     'LABEL_BD_USER': ptBR.LABEL_BD_USER,
                     'LABEL_BD_PASSWORD': ptBR.LABEL_BD_PASSWORD,
                     'LABEL_BD_DATABASE': ptBR.LABEL_BD_DATABASE,
                     'LABEL_BD_STATUS': ptBR.LABEL_BD_STATUS,
                     'LABEL_BD_CONNECT': ptBR.LABEL_BD_CONNECT,
                     'LABEL_OPTION': ptBR.LABEL_OPTION,
                     'LABEL_EXIT': ptBR.LABEL_EXIT,
                     'LABEL_CONFIG': ptBR.LABEL_CONFIG,
                     'LABEL_ABOUT': ptBR.LABEL_ABOUT,
                     'LABEL_HELP': ptBR.LABEL_HELP,
                     'LABEL_EXPORT_FILE': ptBR.LABEL_EXPORT_FILE,
                     'LABEL_EXPORT_BD': ptBR.LABEL_EXPORT_BD,
                     'LABEL_LANGUAGE': ptBR.LABEL_LANGUAGE,
                     'LABEL_TEST_VERSION': ptBR.LABEL_TEST_VERSION,
                     'BTN_EXPORT': ptBR.BTN_EXPORT,
                     'BTN_UPDATE': ptBR.BTN_UPDATE,
                     'BTN_CLOSE': ptBR.BTN_CLOSE,
                     'BTN_CONNECT': ptBR.BTN_CONNECT,
                     'HEADING_FILE_NAME': ptBR.HEADING_FILE_NAME,
                     'HEADING_STATUS': ptBR.HEADING_STATUS,
                     'HEADING_TABLE_NAME': ptBR.HEADING_TABLE_NAME,
                     'HEADING_TOTAL_RECORDS': ptBR.HEADING_TOTAL_RECORDS,
                     'HEADING_ADD_RECORDS': ptBR.HEADING_ADD_RECORDS,
                     'HEADING_DEL_RECORDS': ptBR.HEADING_DEL_RECORDS,
                     'HEADING_UPD_RECORDS': ptBR.HEADING_UPD_RECORDS,                
                     'TAG_PROCESS': ptBR.TAG_PROCESS,
                     'TAG_EXPORT': ptBR.TAG_EXPORT,
                     'TAG_EMPTY': ptBR.TAG_EMPTY,
                     'TAG_ERROR': ptBR.TAG_ERROR,
                     'VALUE_YES': ptBR.VALUE_YES,
                     'VALUE_NO': ptBR.VALUE_NO                     
                     }
        try:
            return text_dict[key]
        except:
            return ''


class enUS:
    # Para um novo idioma adicionar sigla do idioma e o nome idioma
    LANGUAGES = {'pt-br': 'Portuguese', 'en': 'English'}

    # Txt Box Titles and Messages
    APP_TITLE = 'EDNExport'
    APP_VERSION = 'beta 0.0.1'
    APP_COPYRIGHT = 'Copyright © 2023 \nFausto Ferreira - BaDcereal \nMIT License'
    APP_AUTHOR = f'{APP_TITLE} {APP_VERSION} \n{APP_COPYRIGHT}'
    CONFIG_INCOMPLETE = 'Incomplete Configuration'
    WARNING_CONFIG_DIR = 'Attention configure the Delimited Directory.'
    WARNING_CONFIG_BD = 'Attention configure the Database Connection.'
    WARNING_TITLE = 'ATTENTION'
    WARNING_ERASE_DATA = 'Attention all previously exported data will be removed. Do you wish to continue?'
    CONNECTION_ERRO_TITLE = 'Connection Error'
    CONNECTION_ERRO_MSG = 'Error when trying to connect to the Database!'
    INVALID_CONFIG_DIR = 'Invalid Directory'
    INVALID_CONFIG_DIR_MSG = 'This directory does not contain the files needed to perform data export. Select the Delimited directory under the eDNE folder and try again.'
    RUN_FAIL = 'Execution failure'
    TABLE_CLEAN_FAIL = 'An error occurred while trying to clear the table '
    TABLE_CREATE_FAIL = "Table creation failed. Check the user's permissions on the Database and try again."
    BD_ERROR = 'Database Error'
    BD_CONFIG_TITLE = 'Database Configuration'
    ERROR_TITLE = 'An error has occurred'
    ERROR_READ_FILE = 'Failed to read the file.\nCheck if the Delimited file is correct and try again.'
    ERROR_IMG_DIR = 'Image directory not found. Check the settings and try again.'
    OP_CONFIG_TITLE = 'Options Configuration'

    # Labels Text
    LABEL_DIR_EXPORT = 'Delimited Directory Export'
    LABEL_DIR_UPDATE = 'Delimited Directory Update'
    LABEL_DIR = 'Delimited Directory:'
    LABEL_DIR_STATUS = ' Directory Status '
    LABEL_CONNECTION = 'Connection:'
    LABEL_BD_HOST = 'Server Address:'
    LABEL_BD_USER = 'User:'
    LABEL_BD_PASSWORD = 'Password:'
    LABEL_BD_DATABASE = 'Database:'
    LABEL_BD_STATUS = 'Connection Status'
    LABEL_BD_CONNECT = 'Database connection'
    LABEL_OPTION = 'Configure Options'
    LABEL_EXIT = 'Exit'
    LABEL_CONFIG = 'Settings'
    LABEL_ABOUT = 'About'
    LABEL_HELP = 'Help'
    LABEL_EXPORT_FILE = 'Export to SQL file'
    LABEL_EXPORT_BD = 'Export to Database'
    LABEL_LANGUAGE = 'Language:'
    LABEL_TEST_VERSION = 'Trial version:'

    #Buttons Text
    BTN_EXPORT = 'Export'
    BTN_UPDATE = 'Update'
    BTN_CLOSE = 'Confirm'
    BTN_CONNECT = 'Connect'

    # Headings TreeView
    HEADING_FILE_NAME = 'File Name'
    HEADING_STATUS = 'Status'
    HEADING_TABLE_NAME = 'Table Name'
    HEADING_TOTAL_RECORDS = 'Total Records'
    HEADING_ADD_RECORDS = 'Added'
    HEADING_DEL_RECORDS = 'Deleted'
    HEADING_UPD_RECORDS = 'Updated'
    TAG_PROCESS = 'Processing...'
    TAG_EXPORT = 'Exported'
    TAG_EMPTY = 'Empty'
    TAG_ERROR = 'Error'

    # ComboBox Text
    VALUE_YES = 'Yes'
    VALUE_NO = 'No'

    @staticmethod
    def getText(key=None):
        text_dict = {'LANGUAGES': enUS.LANGUAGES,
                     'APP_TITLE': enUS.APP_TITLE,
                     'APP_VERSION': enUS.APP_VERSION,
                     'APP_AUTHOR': enUS.APP_AUTHOR,                     
                     'CONFIG_INCOMPLETE': enUS.CONFIG_INCOMPLETE,
                     'WARNING_CONFIG_DIR': enUS.WARNING_CONFIG_DIR, 
                     'WARNING_CONFIG_BD': enUS.WARNING_CONFIG_BD,
                     'WARNING_TITLE': enUS.WARNING_TITLE,
                     'WARNING_ERASE_DATA': enUS.WARNING_ERASE_DATA,
                     'CONNECTION_ERRO_TITLE': enUS.CONNECTION_ERRO_TITLE,
                     'CONNECTION_ERRO_MSG': enUS.CONNECTION_ERRO_MSG,
                     'INVALID_CONFIG_DIR': enUS.INVALID_CONFIG_DIR,
                     'INVALID_CONFIG_DIR_MSG': enUS.INVALID_CONFIG_DIR_MSG,
                     'RUN_FAIL': enUS.RUN_FAIL,
                     'TABLE_CLEAN_FAIL': enUS.TABLE_CLEAN_FAIL,
                     'TABLE_CREATE_FAIL': enUS.TABLE_CREATE_FAIL,
                     'BD_ERROR': enUS.BD_ERROR,
                     'BD_CONFIG_TITLE': enUS.BD_CONFIG_TITLE,
                     'ERROR_TITLE': enUS.ERROR_TITLE,
                     'ERROR_READ_FILE': enUS.ERROR_READ_FILE,
                     'ERROR_IMG_DIR': enUS.ERROR_IMG_DIR,
                     'OP_CONFIG_TITLE': enUS.OP_CONFIG_TITLE,
                     'LABEL_DIR_EXPORT': enUS.LABEL_DIR_EXPORT,
                     'LABEL_DIR_UPDATE': enUS.LABEL_DIR_UPDATE,
                     'LABEL_DIR': enUS.LABEL_DIR,
                     'LABEL_DIR_STATUS': enUS.LABEL_DIR_STATUS,
                     'LABEL_CONNECTION': enUS.LABEL_CONNECTION,
                     'LABEL_BD_HOST': enUS.LABEL_BD_HOST,
                     'LABEL_BD_USER': enUS.LABEL_BD_USER,
                     'LABEL_BD_PASSWORD': enUS.LABEL_BD_PASSWORD,
                     'LABEL_BD_DATABASE': enUS.LABEL_BD_DATABASE,
                     'LABEL_BD_STATUS': enUS.LABEL_BD_STATUS,
                     'LABEL_BD_CONNECT': enUS.LABEL_BD_CONNECT,
                     'LABEL_OPTION': enUS.LABEL_OPTION,
                     'LABEL_EXIT': enUS.LABEL_EXIT,
                     'LABEL_CONFIG': enUS.LABEL_CONFIG,
                     'LABEL_ABOUT': enUS.LABEL_ABOUT,
                     'LABEL_HELP': enUS.LABEL_HELP,
                     'LABEL_EXPORT_FILE': enUS.LABEL_EXPORT_FILE,
                     'LABEL_EXPORT_BD': enUS.LABEL_EXPORT_BD,
                     'LABEL_LANGUAGE': enUS.LABEL_LANGUAGE,
                     'LABEL_TEST_VERSION': enUS.LABEL_TEST_VERSION,
                     'BTN_EXPORT': enUS.BTN_EXPORT,
                     'BTN_UPDATE': enUS.BTN_UPDATE,
                     'BTN_CLOSE': enUS.BTN_CLOSE,
                     'BTN_CONNECT': enUS.BTN_CONNECT,
                     'HEADING_FILE_NAME': enUS.HEADING_FILE_NAME,
                     'HEADING_STATUS': enUS.HEADING_STATUS,
                     'HEADING_TABLE_NAME': enUS.HEADING_TABLE_NAME,
                     'HEADING_TOTAL_RECORDS': enUS.HEADING_TOTAL_RECORDS,
                     'HEADING_ADD_RECORDS': enUS.HEADING_ADD_RECORDS,
                     'HEADING_DEL_RECORDS': enUS.HEADING_DEL_RECORDS,
                     'HEADING_UPD_RECORDS': enUS.HEADING_UPD_RECORDS,             
                     'TAG_PROCESS': enUS.TAG_PROCESS,
                     'TAG_EXPORT': enUS.TAG_EXPORT,
                     'TAG_EMPTY': enUS.TAG_EMPTY,
                     'TAG_ERROR': enUS.TAG_ERROR,
                     'VALUE_YES': enUS.VALUE_YES,
                     'VALUE_NO': enUS.VALUE_NO
                     }
        try:
            return text_dict[key]
        except:
            return ''