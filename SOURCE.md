# Crie e execute a partir do código

EDNExport é um aplicativo GUI (aplicativo baseado em gráficos) baseado em Python. 

Para desenvolvedores que desejam alterar as configurações de diretório de arquivos exportados devem ler atentamente as instruções abaixo:

Os usuários que executam novas compilações do projeto sem entender o que mudou correm o risco de perda de dados. Queremos minimizar ao máximo essas situações.

----------

## Começando

Para começar, certifique-se de ter o Python 3.11.1 ou mais recente instalado. Além disso, verifique se ele foi baixado da fonte oficial, [python.org](https://www.python.org/downloads/macos/).

* As instalações do Python pré-instaladas ou fornecidas com o Xcode ou as ferramentas de linha de comando do Xcode não são suportadas devido a problemas de confiabilidade.

Depois que o Python estiver instalado, abra o Terminal e execute o seguinte:

# MacOSX
```sh
# Mover para um diretório para armazenar o projeto, aqui estou usando o projetos
cd 
mkdir projetos
cd ./projetos
# Clonar projeto
git clone https://github.com/BaDcereal/EDNExport
# Mover para o diretório do projeto
cd ./EDNExport
# Crie seu ambiente virtual
# Mais detalhes aqui => https://docs.python.org/3/library/venv.html
python -m venv .venv
# Ative seu ambiente virtual
source .venv/bin/activate
# Instale as dependências do Python usadas pelo projeto
pip3 install -r requirements.txt
```

# Windows
```powershell
# Mover para um diretório para armazenar o projeto, aqui estou usando o projetos
cd \
mkdir projetos
cd projetos
# Clonar projeto
git clone https://github.com/BaDcereal/EDNExport
# Mover para o diretório do projeto
cd EDNExport
# Crie seu ambiente virtual
# Mais detalhes aqui => https://docs.python.org/3/library/venv.html
python -m venv .venv
# Ative seu ambiente virtual
.\.venv\Scripts\activate
# Instale as dependências do Python usadas pelo projeto
pip3 install -r requirements.txt
```

Se você tiver algum erro de instalação, consulte as seguintes opções de solução de problemas:

* Usar Python 3.11.1
  * Nosso servidor de compilação atualmente usa Python 3.11.1 para gerar binários.
  * **Windows** problemas de permissão para executar scripts no powershell, usar o comando abaixo

  ```powershell
  # Verifica a permissão
  Get-ExecutionPolicy
  # Se retornar
  Restricted
  # Você deve alterar a permissão. Use o comando abaixo e pressione Enter
  # e depois digite "S" para confirmar.
  Set-ExecutionPolicy Unrestricted
  ```
----------

## Executando EDNExport

Antes de executar o projeto a partir do código-fonte verifique as configurações no arquivo
[arquivos_config.py](./src/arquivos_config.py):

***Configuração de ambiente de desenvolvimento. Para gerar o executavel alterar para False O Padrão: True***
- LOCAL_DEVELOPMENT = True

***Diretório onde serão salvos os arquivos exportados. Padrão: arquivos_exportados***
- DIR_EXPORTADOS = 'arquivos_exportados'

***Diretório das imagens. Padrão: imgs***
- BASEPATHIMGS = 'imgs'

***Se EXCLUIRLOGRADOUROS for igual a True, ignora a exportação de Logradouros. Padrão: False***
- EXCLUIRLOGRADOUROS = False

***Idiomas disponíveis: 'pt-br' e 'en'. Para adicionar novos idiomas verificar o arquivos [idiomas_config.py](./src/idiomas_config.py). Padrão: pt-br***

***Tipo de codificação usada nos arquivos Delimitados. Padrão: iso-8859-1***
- ENCODING_TYPE = 'iso-8859-1'

***Sepadador usado nos arquivos Delimitados. Padrão: @***
- SEPARADOR = '@'

***Máximo de registros processados no Banco de Dados a cada iteração. Padrão: 1000***
- RECORDS_LIMIT_INSERT = 1000

***Debug Mysql - ativa um print para verificação de possíveis erros. Padrão: False***
- MYSQL_DEBUG = False

Para executar o projeto a partir do código-fonte, basta invocar via python3:

```sh
# Inicialização GUI
python3 -u "./src/ednexport.pyw"
```

----------
# MacOSX

## Gerando binários pré-construídos para teste

```sh
# Mova para o diretório do projeto
cd ~/projetos/EDNExport
# Instale o py2app no seu ambiente virtual
# Se você não está em um ambiente virtual recomendamos que verifique os passos acima e ative o ambiente virtual
pip3 install -U py2app
# Execute o py2app no modo alias e verifique se nenhum erro ocorreu
python setup.py py2app -A
# Executando seu aplicativo
./dist/EDNExport.app/Contents/MacOS/EDNExport 
```

----------

## Gerando binários para distribuição
Depois de fazer seu aplicativo funcionar sem problemas no modo de alias, é hora de começar a criar uma versão redistribuível. Como estamos mudando do modo de alias para o modo normal, você deve remover suas pastas build e dist como mostrado abaixo.

```sh
# Mova para o diretório do projeto
cd ~/projetos/EDNExport
# Remova as pastas dist e build criadas no modo alias
rm -rf dist build
# Execute o py2app
# Certifique que a configuração LOCAL_DEVELOPMENT está com o valor False 
# Isso montará seu aplicativo em ./dist/EDNExport.app. Como esse aplicativo é independente, você terá que executar o comando py2app novamente sempre que alterar qualquer código-fonte, arquivos de dados, opções etc.
python setup.py py2app
# Executando seu aplicativo.
./dist/EDNExport.app/Contents/MacOS/EDNExport 
```

Agora vc pode copiar o [EDNExport.zip](./dist/MacOSX/EDNExport.zip) para sua pasta de Aplicativos e usar ele sem precisar do Python.

----------

# Windows

## Gerando binários para distribuição
Depois de fazer seu aplicativo funcionar sem problemas no modo de alias, é hora de começar a criar uma versão redistribuível. Como estamos mudando do modo de alias para o modo normal, você deve remover suas pastas build e dist como mostrado abaixo.

```powershell
# Mova para o diretório do projeto
cd \projetos\EDNExport
# Instale o PyInstaller no seu ambiente virtual
# Se você não está em um ambiente virtual recomendamos que verifique os passos acima e ative o ambiente virtual
pip3 install pyinstaller
# Execute o pyinstaller
# Certifique que a configuração LOCAL_DEVELOPMENT está com o valor False 
# Isso montará seu aplicativo em dist\ednexport.exe ou output\ednexport.exe vai depender da configuração do pyinstaller. Como esse aplicativo é independente, você terá que executar o comando abaixo novamente sempre que alterar qualquer código-fonte, arquivos de dados, opções etc.
pyinstaller --noconfirm --onefile --windowed --icon "C:/projetos/ednexport/imgs/favicon.ico" --no-embed-manifest --add-data "C:/projetos/ednexport/imgs/ednexport.png;imgs/" --add-data "C:/projetos/ednexport/imgs/error.png;imgs/" --add-data "C:/projetos/ednexport/imgs/favicon.ico;imgs/" --add-data "C:/projetos/ednexport/imgs/green.png;imgs/" --add-data "C:/projetos/ednexport/imgs/info.png;imgs/" --add-data "C:/projetos/ednexport/imgs/question.png;imgs/" --add-data "C:/projetos/ednexport/imgs/red.png;imgs/" --add-data "C:/projetos/ednexport/imgs/warning.png;imgs/" --add-data "C:/projetos/ednexport/imgs/yellow.png;imgs/"  "C:/projetos/ednexport/src/ednexport.pyw"
# Executando seu aplicativo.
cd output
ednexport
```

Agora vc pode copiar o [ednexport.zip](./dist/Windows/ednexport.zip) para sua pasta de Aplicativos e usar ele sem precisar do Python.
