Развёртывание:
1) sudo systemctl start postgresql
2) sudo gitlab-ctl reconfigure
3) Ввести данные для доступа к БД и GitLab CE в backend/.env
4) cd backend uvicorn main:app --reload &
5) cd ../frontend npm start &

Данные .env для доступа к тестовому серверу:

DB_HOST=10.124.243.242
DB_PORT=5433
DB_NAME=xakaton
DB_USER=gitflic
DB_PASS=gitflic

GITLAB_API_URL=http://10.124.243.242:1488
GITLAB_SSH_PORT=2222
GITLAB_APP_ID=51f6d3e1bcc4864ee05cec8b386a6685e4c54989cd6c733a09d858722b4be260
GITLAB_SECRET_KEY=gloas-80260e37fe84d1f9c8e7db6a84f8e98ee024a7603cb85491f62e41e6083f7ec8
GITLAB_GOD_LOGIN=root
GITLAB_GOD_PASSWORD=RrsjdAd3MVcPWJWi08cRPFIWBsVhSTi2ccOfxZV4rDQ=
