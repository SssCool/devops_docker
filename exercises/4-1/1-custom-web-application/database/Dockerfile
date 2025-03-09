FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=userdb

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306