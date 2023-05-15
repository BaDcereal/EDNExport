import mysql.connector
import pandas as pd
from pandas.api.types import is_float_dtype
import arquivos_config as arqsConfig
from arquivos_config import getIdioma as msgTxt

class Model:
    def __init__(self, parent):
        self.parent = parent
        self.OptionsValue = parent.OptionsValue
        self.tabelas = ('LOG_LOCALIDADE', 'LOG_GRANDE_USUARIO',
                        'LOG_UNID_OPER', 'LOG_CPC', 'LOG_BAIRRO', 'LOG_LOGRADOURO')

    # Verifica se as tabelas padrão estão criadas
    def checkIfTablesExist(self):
        result = True
        tableas_create = []
        conexao = self.getConexao(self.parent)
        sql = 'SHOW TABLES'
        conexao['mycursor'].execute(sql)
        for x in conexao['mycursor']:
            if x[0] in self.tabelas:
                tableas_create.append(True)
            else:
                tableas_create.append(False)
        if False in tableas_create or len(tableas_create) == 0:
            result = False
        conexao['conexao'].close()
        return result

    # Retorna dados da tabela que será apagada
    def getTruncateSQL(self, table):
        if table == 'LOG_LOCALIDADE':
            sql = "TRUNCATE `LOG_LOCALIDADE`"
        elif table == 'LOG_GRANDE_USUARIO':
            sql = "TRUNCATE `LOG_GRANDE_USUARIO`"
        elif table == 'LOG_UNID_OPER':
            sql = "TRUNCATE `LOG_UNID_OPER`"
        elif table == 'LOG_CPC':
            sql = "TRUNCATE `LOG_CPC`"
        elif table == 'LOG_BAIRRO':
            sql = "TRUNCATE `LOG_BAIRRO`"
        elif table == 'LOG_LOGRADOURO':
            sql = "TRUNCATE `LOG_LOGRADOURO`"
        else:
            sql = ''
        return sql
    
    # Cria tabela
    def criaTabela(self):
        conexao = self.getConexao(self.parent)
        result = True
        for x in self.tabelas:
            sql = self.getCreateSQL(x)
            if sql != '':
                try:
                    conexao['mycursor'].execute(sql)
                except:
                    result = False
            else:
                result = False
        conexao['conexao'].close()
        return result
    
# ------------- Inicio Create -------------
    # Retorna configurações da tabela que será criada
    def getCreateSQL(self, table):
        if table == 'LOG_LOCALIDADE':
            sql = """CREATE TABLE IF NOT EXISTS `LOG_LOCALIDADE` (
                    `LOC_NU` DECIMAL(8) UNSIGNED NOT NULL,
                    `UFE_SG` CHAR(2) NULL DEFAULT NULL,
                    `LOC_NO` VARCHAR(72) NULL DEFAULT NULL,
                    `CEP` CHAR(8) NULL DEFAULT NULL,
                    `LOC_IN_SIT` CHAR(1) NULL DEFAULT NULL,
                    `LOC_IN_TIPO_LOC` CHAR(1) NULL DEFAULT NULL,
                    `LOC_NU_SUB` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `LOC_NO_ABREV` VARCHAR(36) NULL DEFAULT NULL,
                    `MUN_NU` CHAR(7) NULL DEFAULT NULL,
                    PRIMARY KEY (`LOC_NU`))
                    ENGINE = InnoDB
                    DEFAULT CHARACTER SET = utf8mb4
                    COLLATE = utf8mb4_0900_ai_ci"""
        elif table == 'LOG_GRANDE_USUARIO':
            sql = """CREATE TABLE IF NOT EXISTS `LOG_GRANDE_USUARIO` (
                    `GRU_NU` DECIMAL(8) UNSIGNED NOT NULL,
                    `UFE_SG` CHAR(2) NULL DEFAULT NULL,
                    `LOC_NU` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `BAI_NU` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `LOG_NU` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `GRU_NO` VARCHAR(72) NULL DEFAULT NULL,
                    `GRU_ENDERECO` VARCHAR(100) NULL DEFAULT NULL,
                    `CEP` CHAR(8) NULL DEFAULT NULL,
                    `GRU_NO_ABREV` VARCHAR(36) NULL DEFAULT NULL,
                    PRIMARY KEY (`GRU_NU`))
                    ENGINE = InnoDB
                    DEFAULT CHARACTER SET = utf8mb4
                    COLLATE = utf8mb4_0900_ai_ci"""
        elif table == 'LOG_UNID_OPER':
            sql = """CREATE TABLE IF NOT EXISTS `LOG_UNID_OPER` (
                    `UOP_NU` DECIMAL(8) UNSIGNED NOT NULL,
                    `UFE_SG` CHAR(2) NULL DEFAULT NULL,
                    `LOC_NU` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `BAI_NU` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `LOG_NU` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `UOP_NO` VARCHAR(100) NULL DEFAULT NULL,
                    `UOP_ENDERECO` VARCHAR(100) NULL DEFAULT NULL,
                    `CEP` CHAR(8) NULL DEFAULT NULL,
                    `UOP_IN_CP` CHAR(1) NULL DEFAULT NULL,
                    `UOP_NO_ABREV` VARCHAR(36) NULL DEFAULT NULL,
                    PRIMARY KEY (`UOP_NU`))
                    ENGINE = InnoDB
                    DEFAULT CHARACTER SET = utf8mb4
                    COLLATE = utf8mb4_0900_ai_ci"""
        elif table == 'LOG_CPC':
            sql = """CREATE TABLE IF NOT EXISTS `LOG_CPC` (
                    `CPC_NU` DECIMAL(8) UNSIGNED NOT NULL,
                    `UFE_SG` CHAR(2) NULL DEFAULT NULL,
                    `LOC_NU` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `CPC_NO` VARCHAR(72) NULL DEFAULT NULL,
                    `CPC_ENDERECO` VARCHAR(100) NULL DEFAULT NULL,
                    `CEP` CHAR(8) NULL DEFAULT NULL,
                    PRIMARY KEY (`CPC_NU`))
                    ENGINE = InnoDB
                    DEFAULT CHARACTER SET = utf8mb4
                    COLLATE = utf8mb4_0900_ai_ci"""
        elif table == 'LOG_BAIRRO':
            sql = """CREATE TABLE IF NOT EXISTS `LOG_BAIRRO` (
                    `BAI_NU` DECIMAL(8) UNSIGNED NOT NULL,
                    `UFE_SG` CHAR(2) NULL DEFAULT NULL,
                    `LOC_NU` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `BAI_NO` VARCHAR(72) NULL DEFAULT NULL,
                    `BAI_NO_ABREV` VARCHAR(36) NULL DEFAULT NULL,
                    PRIMARY KEY (`BAI_NU`))
                    ENGINE = InnoDB
                    DEFAULT CHARACTER SET = utf8mb4
                    COLLATE = utf8mb4_0900_ai_ci"""
        elif table == 'LOG_LOGRADOURO':
            sql = """CREATE TABLE IF NOT EXISTS `LOG_LOGRADOURO` (
                    `LOG_NU` DECIMAL(8) UNSIGNED NOT NULL,
                    `UFE_SG` CHAR(2) NULL DEFAULT '',
                    `LOC_NU` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `BAI_NU_INI` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `BAI_NU_FIM` DECIMAL(8) UNSIGNED NULL DEFAULT NULL,
                    `LOG_NO` VARCHAR(100) NULL DEFAULT '',
                    `LOG_COMPLEMENTO` VARCHAR(100) NULL DEFAULT NULL,
                    `CEP` CHAR(8) NULL DEFAULT '',
                    `TLO_TX` CHAR(36) NULL DEFAULT '',
                    `LOG_STA_TLO` CHAR(1) NULL DEFAULT NULL,
                    `LOG_NO_ABREV` VARCHAR(36) NULL DEFAULT NULL,
                    PRIMARY KEY (`LOG_NU`))
                    ENGINE = InnoDB
                    DEFAULT CHARACTER SET = utf8mb3"""
        else:
            sql = ''
        return sql
# ------------- Fim Create -------------

# ------------- Inicio Insert Update -------------
    # Cria um dicionário com os dados para inserir ou atualizar
    def createInsertOrUpdate(self, col_nome, col_data, columns, exp_result, tipo_operacao, t_columns):
        line = ''
        if col_nome in columns['export'] and exp_result: # Deve ser export para retornar as colunas que estao no BD
            if columns[tipo_operacao].index(col_nome) < t_columns:
                if "'" not in col_data and '"' not in col_data:
                    line += "'"+col_nome+"': '"+col_data+"'" + ', '
                else:
                    if "'" not in col_data:
                        line += "'"+col_nome+"': '"+col_data+"'" + ', '
                    else:
                        col_data = col_data.replace('"', "'")
                        line += '"'+col_nome+'": "'+col_data+'"' + ', '
            else:
                if "'" not in col_data and '"' not in col_data:
                    line += "'"+col_nome+"': '"+col_data+"'" + ', '
                else:
                    if "'" not in col_data:
                        line += "'"+col_nome+"': '"+col_data+"'" + ', '
                    else:
                        col_data = col_data.replace('"', "'")
                        line += '"'+col_nome+'": "'+col_data+'"' + ', '

        return {'lines': line}

    # Insere dados no Banco de Dados, se o ID já existir atualiza o registro
    def insertOrUpdateMany(self, data_connection, data_list=None, mysql_table=None):
        conexao = Model.getConexao(self, data_connection)

        query = ""
        values = []
        result = {'total_records': 0, 'status': False}

        for data_dict in data_list:
            if not query:
                columns = ', '.join(f'`{k}`' for k in data_dict)
                duplicates = ', '.join(f'{k}=VALUES({k})' for k in data_dict)
                place_holders = ', '.join('%s' for k in data_dict)
                query = f"INSERT INTO {mysql_table} ({columns}) VALUES ({place_holders})"
                query = f"{query} ON DUPLICATE KEY UPDATE {duplicates}"

            v = list(data_dict.values())
            values.append(v)
        total = len(values)
        try:
            conexao['mycursor'].executemany(query, values)
            conexao['conexao'].commit()
            if conexao['mycursor'].rowcount >= total:
                result['total_records'] = total
            else:
                result['total_records'] = conexao['mycursor'].rowcount
            conexao['mycursor'].close()
            conexao['conexao'].close()
            result['status'] = True
            return result
        except mysql.connector.Error as err:
            if arqsConfig.MYSQL_DEBUG:
                try:
                    print("MySQL Error [%d]: %s" % (err.args[0], err.args[1]))
                except IndexError:
                    print("MySQL Error: %s" % str(err))

            conexao['conexao'].rollback()
            conexao['mycursor'].close()
            conexao['conexao'].close()
            return result
# ------------- Fim Insert Update -------------

# ------------- Inicio Delete -------------
    def getDeleteSQL(self, table):
        if table == 'LOG_LOCALIDADE':
            sql = """DELETE FROM `LOG_LOCALIDADE`
                    WHERE `LOC_NU` = %s"""
            sql_total = "SELECT COUNT(`LOC_NU`) from `LOG_LOCALIDADE`"
        elif table == 'LOG_GRANDE_USUARIO':
            sql = """DELETE FROM `LOG_GRANDE_USUARIO`
                    WHERE `GRU_NU` = %s"""
            sql_total = "SELECT COUNT(`GRU_NU`) from `LOG_GRANDE_USUARIO`"
        elif table == 'LOG_UNID_OPER':
            sql = """DELETE FROM `LOG_UNID_OPER`
                    WHERE `UOP_NU` = %s"""
            sql_total = "SELECT COUNT(`UOP_NU`) from `LOG_UNID_OPER`"
        elif table == 'LOG_CPC':
            sql = """DELETE FROM `LOG_CPC`
                    WHERE `CPC_NU` = %s"""
            sql_total = "SELECT COUNT(`CPC_NU`) from `LOG_CPC`"
        elif table == 'LOG_BAIRRO':
            sql = """DELETE FROM `LOG_BAIRRO`
                    WHERE `BAI_NU` = %s"""
            sql_total = "SELECT COUNT(`BAI_NU`) from `LOG_BAIRRO`"
        elif table == 'LOG_LOGRADOURO':
            sql = """DELETE FROM `LOG_LOGRADOURO`
                    WHERE `LOG_NU` = %s"""
            sql_total = "SELECT COUNT(`LOG_NU`) from `LOG_LOGRADOURO`"
        else:
            sql = ''
            sql_total = ''
        return {'sql': sql, 'sql_total': sql_total}
    
    def createDelete(self, col_nome, col_data, first_column_name, exp_result):
        line = ''
        if col_nome == first_column_name and exp_result:
            line += "'"+col_data+",'"

        return {'lines': line}
    
    def deleteMany(self, data_connection, data_list=None, mysql_table=None):
        conexao = Model.getConexao(self, data_connection)
        query = Model.getDeleteSQL(self, mysql_table)

        result = {'total_records': 0, 'status': True}

        try:
            conexao['mycursor'].execute(query['sql_total'])
            total_before = conexao['mycursor'].fetchone()
            conexao['mycursor'].executemany(query['sql'], data_list)
            conexao['conexao'].commit()
            conexao['mycursor'].execute(query['sql_total'])
            total_after = conexao['mycursor'].fetchone()
            try:
                result['total_records'] = total_before[0] - total_after[0]
                result['status'] = True
            except:
                result['total_records'] = 0
                result['status'] = False
            conexao['mycursor'].close()
            conexao['conexao'].close()            
            return result
        except mysql.connector.Error as err:
            if arqsConfig.MYSQL_DEBUG:
                try:
                    print("MySQL Error [%d]: %s" % (err.args[0], err.args[1]))
                except IndexError:
                    print("MySQL Error: %s" % str(err))

            conexao['conexao'].rollback()
            conexao['mycursor'].close()
            conexao['conexao'].close()
            result['status'] = False
            return result
# ------------- Fim Delete -------------


    def readFile(self, file_location, columns):
        try:
            df = pd.read_csv(file_location, sep=arqsConfig.SEPARADOR, encoding=arqsConfig.ENCODING_TYPE, header=None)
            # Se o número de colunas do DataFrame for diferente das
            # colunas do arquivo de configuração, adiciona as colunas
            # que faltam com valor NULL
            if len(df.columns) == len(columns):
                df.columns = columns
            else:
                for index, x in enumerate(columns):
                    if index >= len(df.columns):
                        df.insert(index, x, 0.0)
                df.columns = columns

            for x in columns:
                if is_float_dtype(df[x]):
                    df[x] = df[x].fillna(0).astype(int)
                    df[x] = df[x].astype(str)
                    df[x] = df[x].replace('0', 'NULL')
            df.fillna('NULL', inplace=True)

            return df
        except:
            return None

    def getConexao(self, data_connection):
        conexao = mysql.connector.connect(
            host=data_connection.BDSettingsValue['host'],
            user=data_connection.BDSettingsValue['user'],
            password=data_connection.BDSettingsValue['password'],
            database=data_connection.BDSettingsValue['database']
        )
        mycursor = conexao.cursor()
        return {'conexao': conexao, 'mycursor': mycursor}
    
    # Retorna status das tarefas
    def getProcessStatus(self, tasks, table_name, file_name,  op, total_add, total_del, total_upd, total_records):
        process_data = {'tasks': {'status': '', 'total_add': total_add, 'total_del': total_del, 'total_upd': total_upd, 'total_records': 0}, 'tasks_bd': {'status': '', 'total_add': total_add, 'total_del': total_del, 'total_upd': total_upd, 'total_records': 0}}
        if table_name != 'LOG_LOGRADOURO':
            process_data['tasks_bd']['status'] = msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EXPORT')
            if op == 'DEL':
                process_data['tasks_bd']['total_del'] = total_del
            elif op == 'UPD':
                process_data['tasks_bd']['total_upd'] = total_upd
            else:
                process_data['tasks_bd']['total_add'] = total_add
                process_data['tasks_bd']['total_records'] = total_records
        else:
            process_data['tasks']['status'] = msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EXPORT')
            if op == 'DEL':
                process_data['tasks']['total_del'] = total_del
            elif op == 'UPD':
                process_data['tasks']['total_upd'] = total_upd
            else:
                process_data['tasks']['total_add'] = total_add
                process_data['tasks']['total_records'] = total_records
            tasks[file_name] = {'status': msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EXPORT'), 'total_records': total_records}
            t_records = 0
            process_finish = True
            for x in tasks:
                if tasks[x]['status'] == msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_PROCESS'):
                    process_finish = False
                    break
                else:
                    t_records += tasks[x]['total_records']
            process_data['tasks_bd']['total_records'] = t_records
            process_data['tasks_bd']['total_add'] = t_records
            if process_finish:
                process_data['tasks_bd']['status'] = msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EXPORT')
            else:
                process_data['tasks_bd']['status'] = msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_PROCESS')

        return process_data
