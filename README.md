# VisionLabelMS
Vision label manager system


# Create Frontend Project

``` shell

# 全局安装yarn
npm install -g yarn


npm create vite@latest frontend

# 安装依赖
cd frontend
npm install

# 添加常用功能
# Vue Router：
npm install vue-router@4
# Pinia（官方推荐的状态管理库）：
npm install pinia

npm run dev

```


# Create Backend Project

``` shell
# create python env
python -m venv .venv


# Activate the virtual environment
# Windows
.\.venv\Scripts\activate

# install dependencies
pip install fastapi uvicorn

# run dev server, reload when code changes
uvicorn main:app --reload

# install other dependencies
# 安装 Tortoise ORM
pip install tortoise-orm
# 安装 PostgreSQL 异步驱动
pip install asyncpg
# 安装 用于 Tortoise ORM 的数据库迁移工具
pip install aerich
# 安装 MinIO 的 Python 客户端
pip install minio
# 安装 基于 asyncio 的异步 HTTP 客户端/服务端库
pip install aiohttp

# 生成 requirements.txt
pip freeze > requirements.txt
```

# Run Backend DEV Server

``` shell
uvicorn app.main:app --reload
```

# Run Frontend DEV Server 

``` shell
npm run dev
```

# Setup Storage

## Setup PostgreSQL

``` shell

# Pull the latest PostgreSQL image
docker pull postgres:latest
# Create a volume to persist the database data
docker volume create pgdata
# Run the PostgreSQL container
docker run -d --name VisonLabelMS-postgres -e POSTGRES_PASSWORD=123456 -v /home/peter/work/scratch/VisionLabelMS_data/postgre/pgdata:/var/lib/postgresql/data -p 5432:5432 postgres

# compose up
docker-compose -f docker-compose.yaml up -d


# delete container
docker rm -f VisonLabelMS-postgres


# 如果报错 Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:5432 -> 127.0.0.1:0: listen tcp 0.0.0.0:5432: bind: An attempt was made to access a socket in a way forbidden by its access permissions.
# powershell 中 重启 NAT服务，执行 
net stop winnat
net start winnat

```


## Setup MinIO

## Setup Redis

