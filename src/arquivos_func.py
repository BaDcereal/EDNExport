import os
import pandas as pd
from pandas.api.types import is_float_dtype
from pathlib import Path
import arquivos_config as arqsConfig
from arquivos_config import getIdioma as msgTxt
import threading

class Arquivo:
    def __init__(self, options_value):
        self.OptionsValue = options_value

    # Retorna as configurações das colunas
    def logColumns(self, file_name, file_names):
        if file_name == file_names['log']['localidade'] or file_name == file_names['delta']['localidade']:
            columns = arqsConfig.Configuracoes.columnsLocalidade()

        elif file_name == file_names['log']['grande_usuario'] or file_name == file_names['delta']['grande_usuario']:
            columns = arqsConfig.Configuracoes.columnsGrandeUsuario()

        elif file_name == file_names['log']['unid_oper'] or file_name == file_names['delta']['unid_oper']:
            columns = arqsConfig.Configuracoes.columnsUnidOper()

        elif file_name == file_names['log']['cpc'] or file_name == file_names['delta']['cpc']:
            columns = arqsConfig.Configuracoes.columnsCPC()

        elif file_name == file_names['log']['bairro'] or file_name == file_names['delta']['bairro']:
            columns = arqsConfig.Configuracoes.columnsBairro()

        else:
            columns = arqsConfig.Configuracoes.columnsLogradouro()

        return columns

    # Lê o arquivo delimitado e converte em um DataFrame
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


    # Verifica se no diretório selecionado existe os arquivos delimitados
    def validaDir(self, file_names, arqnomes, arq_data, ufs, caminho, update):
        result = False
        arq_data['geral'].clear()
        arq_data['logradouros'].clear()
        # Verifica se existe os arquivos LOG_LOCALIDADE.TXT, LOG_GRANDE_USUARIO.TXT, LOG_UNID_OPER.TXT, LOG_CPC.TXT e LOG_BAIRRO.TXT
        for x in arqnomes:
            caminho_log_tmp = caminho+x
            caminho_delta_log_tmp = caminho+'DELTA_'+x
            diretorio_log = Path(caminho_log_tmp)
            diretorio_delta = Path(caminho_delta_log_tmp)
            if diretorio_log.is_file() or diretorio_delta.is_file():
                result = True
                if diretorio_log.is_file() and update is False:
                    arq_data['geral'].append(caminho_log_tmp)
                elif diretorio_delta.is_file():
                    arq_data['geral'].append(caminho_delta_log_tmp)                   
            else:
                # No caso de update ignora os arquivos que estão faltando
                if update is False:
                    result = False
                    return result

        # Verifica se existe os arquivos de Logradouro de cada estado
        for x in ufs:
            caminho_log_tmp = caminho+file_names['log']['logradouro']+x+'.TXT'
            caminho_delta_log_tmp = caminho + \
                file_names['delta']['logradouro']+x+'.TXT'
            diretorio_log = Path(caminho_log_tmp)
            diretorio_delta = Path(caminho_delta_log_tmp)
            if diretorio_log.is_file() or diretorio_delta.is_file():
                result = True
                if diretorio_log.is_file() and update is False:
                    arq_data['logradouros'].append(caminho_log_tmp)
                elif diretorio_delta.is_file():
                    arq_data['logradouros'].append(caminho_delta_log_tmp)
            else:
                # No caso de update ignora os arquivos que estão faltando
                if update is False:
                    result = False
                    return result

        if len(arq_data['geral']) == 0 and len(arq_data['logradouros']) == 0:
            result = False

        return result
    
    # Retorna as configurações de nome dos arquivos
    def getFileNames(self):
        return arqsConfig.Configuracoes.fileNames()

    # Retorna as UFS
    def getUfs(self):
        return arqsConfig.Configuracoes.ufNames(self.OptionsValue['TEST_VERSION'])

    # Retorna os nomes dos arquivos
    def getArqNomes(self):
        return arqsConfig.Configuracoes.arqNomes()

    # Retorna dicionario onde sera armazenado as configurações dos arquivos
    def getArqData(self):
        arq_data = {
            'geral': [],
            'logradouros': [],
        }
        return arq_data

    # Cria string sql para remover registros
    def createDelete(self, records, tabela, col_nome, col_data, first_column_name, exp_result):
        if records > 0:
            sql = ''
        else:
            sql = f'DELETE FROM `{tabela}` WHERE `{first_column_name}` IN \n'

        line = ''
        if col_nome == first_column_name and exp_result:
            if records == 0:
                line = '('
            line += "'"+col_data+"'"

        return {'records': records, 'sql': sql, 'lines': line}
    
    # Cria string sql para atualizar registros
    def createUpdate(self, first_column_name, records, tabela, col_nome, col_data, columns, exp_result, tipo_operacao, t_columns):
        sql = f'UPDATE `{tabela}` SET '
        line = ''
        if col_nome in columns['export'] and exp_result: # Deve ser export para retornar as colunas que estao no BD
            if col_nome != first_column_name:
                if columns[tipo_operacao].index(col_nome) < t_columns:
                    if col_data != 'NULL':
                        if "'" not in col_data and '"' not in col_data:
                            line += f'`{col_nome}` = '+"'"+col_data+"'" + ', '
                        else:
                            if "'" not in col_data:
                                line += f'`{col_nome}` = '+"'"+col_data+"'" + ', '
                            else:
                                col_data = col_data.replace('"', "'")
                                line += f'`{col_nome}` = '+'"'+col_data+'"' + ', '
                    else:
                        line += f'`{col_nome}` = '+col_data + ", "
                else:
                    if col_data != 'NULL':
                        if "'" not in col_data and '"' not in col_data:
                            line += f'`{col_nome}` = '+"'"+col_data+"'"
                        else:
                            if "'" not in col_data:
                                line += f'`{col_nome}` = '+"'"+col_data+"'"
                            else:
                                col_data = col_data.replace('"', "'")
                                line += f'`{col_nome}` = '+'"'+col_data+'"'
                    else:
                        line += f'`{col_nome}` = '+col_data
        return {'records': records, 'sql': sql, 'lines': line}

    # Cria string sql para inserir registros
    def createInsert(self, start_line, records, tabela, col_nome, col_data, columns, exp_result, tipo_operacao, t_columns):
        if records > 0:
            sql = ''
        else:
            sql = f'INSERT INTO `{tabela}` {columns["export"]} VALUES \n'

        line = ''    
        if col_nome in columns['export'] and exp_result: # Deve ser export para retornar as colunas que estao no BD
            if start_line:
                line = '('
            if columns[tipo_operacao].index(col_nome) < t_columns:
                if col_data != 'NULL':
                    if "'" not in col_data and '"' not in col_data:
                        line += "'"+col_data+"'" + ', '
                    else:
                        if "'" not in col_data:
                            line += "'"+col_data+"'" + ', '
                        else:
                            col_data = col_data.replace('"', "'")
                            line += '"'+col_data+'"' + ', '
                else:
                    line += col_data + ", "
            else:
                if col_data != 'NULL':
                    if "'" not in col_data and '"' not in col_data:
                        line += "'"+col_data+"'" + ')'
                    else:
                        if "'" not in col_data:
                            line += "'"+col_data+"'" + ')'
                        else:
                            col_data = col_data.replace('"', "'")
                            line += '"'+col_data+'"' + ')'
                else:
                    line += col_data + ')'
        return {'records': records, 'sql': sql, 'lines': line}

class CreateWorker(threading.Thread):
    def __init__(self, file_location, file_name, columns, tasks, update, options_value, geral):
        super().__init__()
        self.file_location = file_location
        self.file_name = file_name
        self.columns = columns
        self.tasks = tasks
        self.update = update
        self.geral = geral
        self.OptionsValue = options_value

    def run(self):
        if self.update:
            tabela = self.file_name[0:-4].replace("DELTA_", "")
            tipo_operacao = 'update'
            operacoes = ('DEL', 'UPD', 'INS')
        else:
            tabela = self.file_name[0:-4]
            tipo_operacao = 'export'
            operacoes = ('INS',)
            
        colunas = self.columns[tipo_operacao]
        df = Arquivo.readFile(self, self.file_location, colunas)
        if df is None:
            self.tasks[self.file_name] = msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EMPTY')
            return self.tasks[self.file_name]

        c = self.file_name[0:-3] + 'sql'
        t_columns = len(self.columns["export"])-1

        try:            
            fc = open(os.path.join(arqsConfig.DIR_EXPORTADOS, c), 'w', encoding='UTF-8')

            for op in operacoes:

                if self.update is False:
                    if self.geral:
                        t_lines = df.index[-1] # indice do ultimo registro
                        t_lines += 1
                    else:
                        t_lines = df.index[-1] # indice do ultimo registro
                        tabela = 'LOG_LOGRADOURO'
                        t_lines += 1
                else:
                    if self.geral:
                        if op == 'DEL':
                            t_lines = len(df[df[self.columns['col_operacao']]=='DEL'])
                        elif op == 'UPD':
                            t_lines = len(df[df[self.columns['col_operacao']]=='UPD'])
                        else:
                            t_lines = len(df[df[self.columns['col_operacao']]=='INS'])
                    else:
                        tabela = 'LOG_LOGRADOURO'
                        if op == 'DEL':
                            t_lines = len(df[df[self.columns['col_operacao']]=='DEL'])
                        elif op == 'UPD':
                            t_lines = len(df[df[self.columns['col_operacao']]=='UPD'])
                        else:
                            t_lines = len(df[df[self.columns['col_operacao']]=='INS'])

                records = 0
                first_column_name = df.columns[0]
                first_column_value = ''
                for index, row in df.iterrows():
                    start_line = True
                    line = ''
                    for x in self.columns[tipo_operacao]: # x = nome da coluna
                        l = str(row[x]).strip() # l = valor da coluna
                        exp_result = True if self.update is False else op == row[self.columns['col_operacao']]

                        if self.update is False:
                            sql_data = Arquivo.createInsert(self, start_line, records, tabela, x, l, self.columns, exp_result, tipo_operacao, t_columns)
                            if sql_data['lines'] != '':
                                line += sql_data['lines']
                        else:
                            if op == 'DEL':
                                sql_data = Arquivo.createDelete(self, records, tabela, x, l, first_column_name, exp_result)
                                if sql_data['lines'] != '':
                                    line += sql_data['lines']
                            elif op == 'UPD':
                                if x == first_column_name:
                                    first_column_value = l                                
                                sql_data = Arquivo.createUpdate(self, first_column_name, records, tabela, x, l, self.columns, exp_result, tipo_operacao, t_columns)
                                if sql_data['lines'] != '':
                                    line += sql_data['lines']                             
                            else:
                                sql_data = Arquivo.createInsert(self, start_line, records, tabela, x, l, self.columns, exp_result, tipo_operacao, t_columns)
                                if sql_data['lines'] != '':
                                    line += sql_data['lines']

                        start_line = False

                    if op == 'DEL':
                        if line != '':
                            records += 1
                            if records < t_lines:
                                line += ','
                            else:
                                line += ');\n'

                            if sql_data['sql'] != '':
                                sql = sql_data['sql'].replace("'", "`")
                                fc.write(sql)
                            fc.write(line)
                    elif op == 'UPD':
                        if line != '':
                            line += f' WHERE `{first_column_name}` = {first_column_value};\n'

                            if sql_data['sql'] != '':
                                if first_column_value != '':
                                    sql = sql_data['sql'].replace("'", "`")
                                else:
                                    sql = '-- '
                                    sql += sql_data['sql'].replace("'", "`")
                                fc.write(sql)
                                fc.write(line)
                    else:
                        if line != '':
                            records += 1
                            if records < t_lines:
                                line += ',\n'
                            else:
                                line += ';\n'

                            if sql_data['sql'] != '':
                                sql = sql_data['sql'].replace("'", "`")
                                fc.write(sql)
                            fc.write(line)

            fc.close()

            self.tasks[self.file_name] = msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EXPORT')

        except:
            self.tasks[self.file_name] = msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_ERROR')