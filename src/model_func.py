import threading
import ast
import model
from arquivos_config import getIdioma as msgTxt

class CreateWorker(threading.Thread):
    def __init__(self, bd_setings, file_location, file_name, table_name, columns, tasks_bd, tasks, options_value, update):
        super().__init__()
        self.bd_setings = bd_setings
        self.file_location = file_location
        self.file_name = file_name
        self.table_name = table_name
        self.columns = columns
        self.tasks_bd = tasks_bd
        self.tasks = tasks
        self.OptionsValue = options_value
        self.update = update

    def run(self):
        if self.update:
            tipo_operacao = 'update'
            operacoes = ('DEL', 'UPD', 'INS')
        else:
            tipo_operacao = 'export'
            operacoes = ('INS',)

        colunas = self.columns[tipo_operacao]
        df = model.Model.readFile(self, self.file_location, colunas)
        if df is None:
            self.tasks_bd[self.table_name] = {'status': msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_EMPTY'), 'total_add': 0, 'total_del': 0, 'total_upd': 0, 'total_records': 0}
            return self.tasks_bd[self.table_name]

        t_columns = len(self.columns)-1
        total_add = 0
        total_del = 0
        total_upd = 0
        total_records = 0

        try:
            linha_del = []
            linha_upd = []
            linha_ins = []
            result_sql = {'total_records': 0, 'status': True}
            for op in operacoes:
                first_column_name = df.columns[0]
                for index, row in df.iterrows():
                    line = ''
                    for x in self.columns[tipo_operacao]:
                        l = str(row[x]).strip()
                        exp_result = True if self.update is False else op == row[self.columns['col_operacao']]

                        if self.update is False:
                            sql_data = model.Model.createInsertOrUpdate(self, x, l, self.columns, exp_result, tipo_operacao, t_columns)
                            if sql_data['lines'] != '':
                                line += sql_data['lines']
                        else:
                            if op == 'DEL':
                                sql_data = model.Model.createDelete(self, x, l, first_column_name, exp_result)
                                if sql_data['lines'] != '':
                                    line += sql_data['lines']
                            else:
                                sql_data = model.Model.createInsertOrUpdate(self, x, l, self.columns, exp_result, tipo_operacao, t_columns)
                                if sql_data['lines'] != '':
                                    line += sql_data['lines']

                    if line != '':
                        if op == 'DEL':
                            line_tmp = line.replace("'",'')
                            line = line_tmp.split(',')
                            for y in line:
                                if y != '':
                                    linha_del.append(tuple([y]))
                        elif op == 'UPD':
                            line_tmp = '{' + line[:-2] + '}'
                            line = ast.literal_eval(line_tmp)
                            for d in line:
                                if line[d] == 'NULL':
                                    line[d] = None
                            linha_upd.append(line)
                        else:
                            line_tmp = '{' + line[:-2] + '}'
                            line = ast.literal_eval(line_tmp)
                            for d in line:
                                if line[d] == 'NULL':
                                    line[d] = None
                            linha_ins.append(line)

                    if op == 'DEL':
                        if len(linha_del) >= model.arqsConfig.RECORDS_LIMIT_INSERT:
                            result_sql = model.Model.deleteMany(self, self.bd_setings, linha_del, self.table_name)
                            if result_sql['status']:
                                total_del += result_sql['total_records']
                            linha_del.clear()
                    elif op == 'UPD':
                        if len(linha_upd) >= model.arqsConfig.RECORDS_LIMIT_INSERT:
                            result_sql = model.Model.insertOrUpdateMany(self, self.bd_setings, linha_upd, self.table_name)
                            if result_sql['status']:
                                total_upd += result_sql['total_records']
                            linha_upd.clear()
                    else:
                        if len(linha_ins) >= model.arqsConfig.RECORDS_LIMIT_INSERT:
                            result_sql = model.Model.insertOrUpdateMany(self, self.bd_setings, linha_ins, self.table_name)
                            if result_sql['status']:
                                total_records += result_sql['total_records']
                                total_add += result_sql['total_records']
                            linha_ins.clear()

                if op == 'DEL':
                    if len(linha_del) > 0:
                        result_sql = model.Model.deleteMany(self, self.bd_setings, linha_del, self.table_name)
                        if result_sql['status']:
                            total_del += result_sql['total_records']
                        linha_del.clear()
                elif op == 'UPD':
                    if len(linha_upd) > 0:
                        result_sql = model.Model.insertOrUpdateMany(self, self.bd_setings, linha_upd, self.table_name)
                        if result_sql['status']:
                            total_upd += result_sql['total_records']
                        linha_upd.clear()
                else:
                    if len(linha_ins) > 0:
                        result_sql = model.Model.insertOrUpdateMany(self, self.bd_setings, linha_ins, self.table_name)
                        if result_sql['status']:
                            total_records += result_sql['total_records']
                            total_add += result_sql['total_records']
                        linha_ins.clear()

                self.tasks_bd[self.table_name] = {'status': msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_ERROR'), 'total_add': total_add, 'total_del': total_del, 'total_upd': total_upd, 'total_records': total_records}

                if result_sql['status']:
                    process_data = model.Model.getProcessStatus(self, self.tasks, self.table_name, self.file_name, op, total_add, total_del, total_upd, total_records)
                    self.tasks[self.file_name] = process_data['tasks']
                    self.tasks_bd[self.table_name] = process_data['tasks_bd']
        except:
            self.tasks_bd[self.table_name] = {'status': msgTxt(self.OptionsValue['LANGUAGES'], 'TAG_ERROR'), 'total_add': total_add, 'total_del': total_del, 'total_upd': total_upd, 'total_records': total_records}
