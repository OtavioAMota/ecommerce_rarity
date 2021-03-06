# ecommerce

Este repositorio tem o intuito de estudo das principais tecnologias utilizadas, que são o Django, python, git e docker.

### Inicialização

Inicie o projeto abrindo o terminal na pasta escolhida e inicie um repositorio git.
```
git init
```
Crie um ambiente controlado, para manter o versionamento.
```
python -m venv venv
```
Entre no ambiente controlado.
```
.\venv\scripts\activate
```
Atualize o comando pip dentro da sua venv.
```
python -m pip install --upgrade pip
```
Crie um arquivo com o nome de "requirements" com o tipo .txt para instalar de forma rapida as dependencias. Copie o arquivo requirements.txt deste repositorio.
```
pip install -r .\requirements.txt 
```
Utilize a linha de comando abaixo para iniciar um projeto django. O formato desta linha de comando é "django-admin startproject [Nome do projeto] [local de criação do projeto]. No local da criação do projeto eu utilizei o "." (ponto) para criar na mesma pasta.
```
django-admin startproject raritydisc .
```
Para testar se o server esta funcionando. Apos rodar o comando, caso queira utilize 127.0.0.1:8000/
```
python .\manage.py runserver
```
Para desligar o servidor pelo terminal.
```
No terminal pressione "Ctrl + C" para "matar" (desligar) o servidor.
```
Verificando o que não foi salvo em seu repositorio git. 
```
git status
```
Utilize este comando para adicionar todas as modificações em seu repositorio. O formado do comando é "git add [local/arquivo]", no meu caso eu utilizei o "." (ponto) para adicionar todos os arquivos pendentes dentro do meu projeto.
```
git add .
```
Utilize este comando para declarar suas informações com um breve comentario. O formato do comando é "git commit -m "[comentario]" ", utilizei o comentario "first commit" como padrão, porem pode ser mais especifico para saber em poucas linhas o que se trata das modificações do arquivo.
```
git commit -m "first commit"
```
### Docker

https://docs.docker.com/get-docker/

Utilize o arquivo "Dockerfile" e "docker-compose.yml" deste repositorio como base.

Primeira inicialização no sistema para buildar a imagem do servidor.
```
docker-compose up --build
```
Apos a primeira inicialização voce pode usar o comando normal para "deploy" local do server. Caso não queira que fique aparecendo informações do servidor em seu terminal utilize o prefixo -d.
```
docker-compose up
```

### pytest

Comando para testes. Dentro do seu terminal com a aplicação ligada no docker, utilize o comando a seguir para testar todos(-x) os arquivos e tambem cobri-los (--cov):
```
docker-compose exec web pytest -x --cov
```