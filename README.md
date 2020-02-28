# Hello-Django

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
`# ...` はコンテナの中でコマンド実行していることを指す。
1. `$ docker exec -it mysite.web bash`
2. `# python manage.py startapp manager`

## マイグレーション
1. `models.py` を記述する
2. `$ docker exec -it mysite.web bash`
3. `# python manage.py makemigrations`
4. `# python manage.py migrate`

## DBを見たい
1. `$ docker exec -it mysite.db bash`
2. `# mysql -u root -pmysitepass mysite`
3. `mysql> show tables;`
