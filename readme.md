# Simple Microsservices Machine Learning App (Rest API)
> Este repositório implementa uma aplicação simples que segue a arquitetura de micro-serviços, expondo uma API REST auto-documentada para realizar inferências em um modelo de machine learning.
> Pode ser usada como blueprint para teste rápido de projetos.

* Usa flask para rotas e endpoints.
* API REST auto-documentada (Swagger) utilizando flask_restx.
* Log simplificado de requisições armazenados banco Mysql (serviço rodando separado).
* Uso de docker-compose para facilitar desenvolvimento e comunicação entre serviços.
* Auto-update restart do serviço ao atualizar diretorio local

> Montando o diretorio do projeto no diretorio /app do container utilizando volumes, conseguimos 
> editar facilmente o código no host e essas alterações são refletidas no container executando.


## Comandos básicos para execução
**Criando rede interna**
> docker network create mysqlnet

**Subindo serviço mysql**
> docker run --rm -d -v mysql:/var/lib/mysql  -v mysql_config:/etc/mysql -p 3306:3306 --network mysqlnet  --name mysqldb -e MYSQL_ROOT_PASSWORD=p@ssw0rd1  mysql

**Compilando e subindo serviço endpoint**
>  docker build -t app . && docker run -p 5000:5000 --name flask --network mysqlnet app

**Acessando terminal do serviço mysql**
>  docker exec -it mysqldb mysql -u root -p





## Comandos Úteis:
**Removendo todos so containeres:**
> docker rm -f $(docker container ls -aq)

**Build & Up**
> docker-compose up --build


# Referências:
* https://flask-restx.readthedocs.io/en/latest/quickstart.html
* https://docs.docker.com/language/python/develop/
* https://realpython.com/python-logging/
* https://www.datadoghq.com/blog/python-logging-best-practices/

 