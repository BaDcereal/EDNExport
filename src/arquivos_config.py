import sys
import os
import idiomas_config


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)


# ******************************* INICIO DAS CONFIGURAÇÕES *******************************
# Para gerar o executavel alterar para False
LOCAL_DEVELOPMENT = True

if LOCAL_DEVELOPMENT:
    # Diretório das imagens
    BASEPATHIMGS = os.path.join(os.getcwd(), 'imgs')

    # Diretório onde serão salvos os arquivos exportados
    DIR_EXPORTADOS = os.path.join(os.getcwd(), 'arquivos_exportados')
    if not os.path.exists(DIR_EXPORTADOS):
        os.makedirs(DIR_EXPORTADOS)
else:
    if sys.platform == 'darwin':
        # Diretório das imagens
        BASEPATHIMGS = os.path.join(os.getcwd(), 'imgs')
        # Diretório onde serão salvos os arquivos exportados
        # No caso será criada a pasta arquivos_exportados no Desktop.
        desktop_path = os.path.abspath(os.path.join(
            os.path.expanduser('~'), 'Desktop', 'arquivos_exportados'))
        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)
        DIR_EXPORTADOS = desktop_path
    else:
        # Diretório das imagens
        BASEPATHIMGS = resource_path('imgs')
        DIR_EXPORTADOS = os.path.join(os.getcwd(), 'arquivos_exportados')
        if not os.path.exists(DIR_EXPORTADOS):
            os.makedirs(DIR_EXPORTADOS)
        # DIR_EXPORTADOS = os.path.join(
        #     os.path.dirname(__file__), 'arquivos_exportados')

# Se EXCLUIRLOGRADOUROS for igual a True, ignora a exportação de Logradouros
EXCLUIRLOGRADOUROS = False

# Idiomas disponíveis: 'pt-br' e 'en'
# Para adicionar novos idiomas verificar o arquivos idiomas_config.py

# Tipo de codificação usada nos arquivos Delimitados
ENCODING_TYPE = 'iso-8859-1'

# Sepadador usado nos arquivos Delimitados
SEPARADOR = '@'

# Máximo de registros processados no Banco de Dados a cada iteração
RECORDS_LIMIT_INSERT = 1000

# Debug Mysql - ativa um print para verificação de possíveis erros.
# Padrão: False
MYSQL_DEBUG = False
# ******************************* FIM DAS CONFIGURAÇÕES *******************************


# Constantes - Caso ocorra mudança de nomes nos arquivos Delimitados,
# alterar os valores abaixo
LOG_LOCALIDADE = 'LOG_LOCALIDADE.TXT'
LOG_GRANDE_USUARIO = 'LOG_GRANDE_USUARIO.TXT'
LOG_UNID_OPER = 'LOG_UNID_OPER.TXT'
LOG_CPC = 'LOG_CPC.TXT'
LOG_BAIRRO = 'LOG_BAIRRO.TXT'
LOG_LOGRADOURO = 'LOG_LOGRADOURO_'
# Arquivos de Update
DELTA_LOG_LOCALIDADE = 'DELTA_LOG_LOCALIDADE.TXT'
DELTA_LOG_GRANDE_USUARIO = 'DELTA_LOG_GRANDE_USUARIO.TXT'
DELTA_LOG_UNID_OPER = 'DELTA_LOG_UNID_OPER.TXT'
DELTA_LOG_CPC = 'DELTA_LOG_CPC.TXT'
DELTA_LOG_BAIRRO = 'DELTA_LOG_BAIRRO.TXT'
DELTA_LOG_LOGRADOURO = 'DELTA_LOG_LOGRADOURO_'


# ============== ATENÇÃO NÃO ALTERAR OS CODIGOS ABAIXO ==============
# ============== A MENOS QUE SAIBA O QUE ESTA FAZENDO. ==============
class Configuracoes:
    # Configuração dos nomes das colunas das tabelas SQL,
    # usadas também como headers do DataFrame do Pandas
    @staticmethod
    def columnsLocalidade():
        columns = {'export': ('LOC_NU', 'UFE_SG', 'LOC_NO', 'CEP', 'LOC_IN_SIT',
                              'LOC_IN_TIPO_LOC', 'LOC_NU_SUB', 'LOC_NO_ABREV', 'MUN_NU'),
                   'update': ('LOC_NU', 'UFE_SG', 'LOC_NO', 'CEP', 'LOC_IN_SIT',
                              'LOC_IN_TIPO_LOC', 'LOC_NU_SUB', 'LOC_NO_ABREV', 'MUN_NU', 'LOC_OPERACAO', 'CEP_ANT'),
                   'col_operacao': 'LOC_OPERACAO'}

        # LOC_OPERACAO CHAR(3)
        # Operação: DEL = Delete, INS  = Insert, UPD = Update.
        # CEP_ANT CHAR(8)
        # CEP anterior da localidade. Campo informado para LOC_OPERACAO =UPD
        return columns

    @staticmethod
    def columnsGrandeUsuario():
        columns = {'export': ('GRU_NU', 'UFE_SG', 'LOC_NU', 'BAI_NU', 'LOG_NU',
                              'GRU_NO', 'GRU_ENDERECO', 'CEP', 'GRU_NO_ABREV'),
                   'update': ('GRU_NU', 'UFE_SG', 'LOC_NU', 'BAI_NU', 'LOG_NU',
                              'GRU_NO', 'GRU_ENDERECO', 'CEP', 'GRU_NO_ABREV', 'GRU_OPERACAO', 'CEP_ANT'),
                   'col_operacao': 'GRU_OPERACAO'}

        # GRU_OPERACAO CHAR(3)
        # Operação: DEL = Delete, INS  = Insert, UPD = Update.
        # CEP_ANT CHAR(8)
        # CEP anterior da localidade. Campo informado para LOC_OPERACAO =UPD.
        return columns

    @staticmethod
    def columnsUnidOper():
        columns = {'export': ('UOP_NU', 'UFE_SG', 'LOC_NU', 'BAI_NU', 'LOG_NU',
                              'UOP_NO', 'UOP_ENDERECO', 'CEP', 'UOP_IN_CP', 'UOP_NO_ABREV'),
                   'update': ('UOP_NU', 'UFE_SG', 'LOC_NU', 'BAI_NU', 'LOG_NU', 'UOP_NO',
                              'UOP_ENDERECO', 'CEP', 'UOP_IN_CP', 'UOP_NO_ABREV', 'UOP_OPERACAO', 'CEP_ANT'),
                   'col_operacao': 'UOP_OPERACAO'}

        # UOP_OPERACAO CHAR(3)
        # Operação: DEL = Delete, INS  = Insert, UPD = Update.
        # CEP_ANT CHAR(8)
        # CEP anterior da localidade. Campo informado para LOC_OPERACAO =UPD.
        return columns

    @staticmethod
    def columnsCPC():
        columns = {'export': ('CPC_NU', 'UFE_SG', 'LOC_NU',
                              'CPC_NO', 'CPC_ENDERECO', 'CEP'),
                   'update': ('CPC_NU', 'UFE_SG', 'LOC_NU',
                              'CPC_NO', 'CPC_ENDERECO', 'CEP', 'CPC_OPERACAO', 'CEP_ANT'),
                   'col_operacao': 'CPC_OPERACAO'}

        # CPC_OPERACAO CHAR(3)
        # Operação: DEL = Delete, INS  = Insert, UPD = Update.
        # CEP_ANT CHAR(8)
        # CEP anterior da localidade. Campo informado para LOC_OPERACAO =UPD.
        return columns

    @staticmethod
    def columnsBairro():
        columns = {'export': ('BAI_NU', 'UFE_SG', 'LOC_NU', 'BAI_NO', 'BAI_NO_ABREV'),
                   'update': ('BAI_NU', 'UFE_SG', 'LOC_NU', 'BAI_NO', 'BAI_NO_ABREV', 'BAI_OPERACAO'),
                   'col_operacao': 'BAI_OPERACAO'}

        # BAI_OPERACAO CHAR(3)
        # Operação: DEL = Delete, INS  = Insert, UPD = Update.
        return columns

    @staticmethod
    def columnsLogradouro():
        columns = {'export': ('LOG_NU', 'UFE_SG', 'LOC_NU', 'BAI_NU_INI', 'BAI_NU_FIM',
                              'LOG_NO', 'LOG_COMPLEMENTO', 'CEP', 'TLO_TX', 'LOG_STA_TLO', 'LOG_NO_ABREV'),
                   'update': ('LOG_NU', 'UFE_SG', 'LOC_NU', 'BAI_NU_INI', 'BAI_NU_FIM', 'LOG_NO',
                              'LOG_COMPLEMENTO', 'CEP', 'TLO_TX', 'LOG_STA_TLO', 'LOG_NO_ABREV',
                              'LOG_OPERACAO', 'CEP_ANT'),
                   'col_operacao': 'LOG_OPERACAO'}

        # LOG_OPERACAO
        # Operação: DEL = Delete, INS  = Insert, UPD = Update.
        # CEP_ANT CHAR(8)
        # CEP anterior da localidade. Campo informado para LOC_OPERACAO =UPD.
        return columns

    # Nome dos arquivos Delimitados
    @staticmethod
    def arqNomes():
        arquivos = (LOG_LOCALIDADE, LOG_GRANDE_USUARIO,
                    LOG_UNID_OPER, LOG_CPC, LOG_BAIRRO)
        return arquivos

    @staticmethod
    def fileNames():
        arquivos = {
            'log': {
                'localidade': LOG_LOCALIDADE,
                'grande_usuario': LOG_GRANDE_USUARIO,
                'unid_oper': LOG_UNID_OPER,
                'cpc': LOG_CPC,
                'bairro': LOG_BAIRRO,
                'logradouro': LOG_LOGRADOURO
            },
            'delta': {
                'localidade': DELTA_LOG_LOCALIDADE,
                'grande_usuario': DELTA_LOG_GRANDE_USUARIO,
                'unid_oper': DELTA_LOG_UNID_OPER,
                'cpc': DELTA_LOG_CPC,
                'bairro': DELTA_LOG_BAIRRO,
                'logradouro': DELTA_LOG_LOGRADOURO
            }
        }
        return arquivos

    # UFS
    @staticmethod
    def ufNames(version):
        if version is False:
            ufs = ('AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT',
                   'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO')
        else:
            ufs = ('AC', 'DF', 'ES')
        return ufs

# Método para retornar as configurações de idioma
# Para adicionar um novo idioma use o exemplo abaixo:
# Exp: Espanhol
#
#    elif language == 'esp':
#        return idiomas_config.ESP.getText(key)
#


@staticmethod
def getIdioma(language='pt-br', key=None):
    if language == 'en':
        return idiomas_config.enUS.getText(key)
    # Novo idioma
    # -------- Inicio --------

    # --------- Fim ----------
    else:
        return idiomas_config.ptBR.getText(key)
