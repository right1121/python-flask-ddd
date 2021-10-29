FROM mysql
EXPOSE 3306

# 設定ファイルの読み込み
ADD ./docker/mysql/my.cnf /etc/mysql/conf.d/my.cnf

CMD ["mysqld"]