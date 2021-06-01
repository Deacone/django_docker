# 注意这里的数据库名django_docker和用户名admin和密码password必需和docker-compose.yml里与MySQL相关的环境变量保持一致

GRANT ALL PRIVILEGES ON xiaoe_testing_platform.* TO admin@"%" IDENTIFIED BY "xiaoe@123";
FLUSH PRIVILEGES;
