Módulo em Django para o frontend da central de editais

----------------

Testado com:
- Python 3.6.9
- Django 3.0.4 e 3.0.6

----------------

Para executar a aplicação:

1) Verifique se você tem os pré-requisitos mínimos: Python 3.6 e Django 3.0

2) Recomendamos o uso de virtualenv. Após instalar o virtualenv crie um novo virtualenv com o comando:
$ virtualenv ENV
ENV será o diretório do novo virtualenv

3) Se estiver usando o virtualenv faça o carregamento do mesmo com o comando abaixo (ENV é um diretório - indique o caminho se necessário):
$ source ENV/bin/activate

4) Instale as dependências do projeto
pip install -r central_editais/requirements/requirements.txt

5) Execute as migrações da base de dados. Recomendamos o uso do SQLite. Se não for usar o SQLite edite a seção de base de dados no arquivo central_editais/settings.py
$ python manage.py migrate

6) Crie o superusuário
$ python manage.py createsuperuser


7) Execute o servidor web do Django (para testes)
$ python manage.py runserver 
