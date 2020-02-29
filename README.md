# Hello-Django

※コマンド例のプロンプト  
- `$` => コンテナの外(ホストマシン)で実行している
- `#` => コンテナの中で実行している

## コンテナの作成と起動
`$ docker-compose up -d`

## コンテナの停止と削除
`$ docker-compose down`

## 管理サイトURL
http://localhost:8000/admin/

## コンテナの中に入る
### web
`$ docker exec -it mysite.web bash`

### db
`$ docker exec -it mysite.db bash`

## アプリケーション作成
1. `$ docker exec -it mysite.web bash`
2. `# python manage.py startapp manager`

## マイグレーション
### 通常ケース
1. `models.py` を記述する
2. `$ docker exec -it mysite.web bash`
3. `# python manage.py makemigrations`
4. `# python manage.py migrate`

### 修正する場合
1. `models.py` を修正する
2. `$ docker exec -it mysite.web bash`
3. `# python manage.py showmigrations`
4. `# python manage.py migrate APPLICATION_NAME MIGRATION_NAME`  
=> `MIGRATION_NAME` はその時点まで戻したいマイグレーション名を指定する。
5. 不要なマイグレーションファイルを削除する
6. `# python manage.py makemigrations`
7. `# python manage.py migrate`

参考：[Djangoのマイグレーションをロールバック、元に戻す方法 | Hodalog](https://hodalog.com/how-to-revert-migrations/)

## DBを見たい
1. `$ docker exec -it mysite.db bash`
2. `# mysql -u root -pmysitepass mysite`
3. `mysql> show tables;`

※ホストマシンのGUIクライアントから接続することもできる。  
参考：[Dockerで構築したWordPress環境のMySQLにMySQL Workbenchから接続する - Qiita](https://qiita.com/dnrsm/items/1143517240d178b60d8e)
