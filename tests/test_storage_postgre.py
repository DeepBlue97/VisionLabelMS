import psycopg2

def test_postgres_connection():
    try:
        # 连接到PostgreSQL数据库
        conn = psycopg2.connect(
            host="127.0.0.1", 
            database="vlms", 
            user="postgres", 
            password="123456"
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        if cursor.fetchone() is not None:
            print("PostgreSQL connection is successful.")
        else:
            print("Failed to connect or no data received.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error connecting to PostgreSQL: {error}")
    finally:
        if 'conn' in locals():
            conn.close()

# 调用函数进行测试
test_postgres_connection()
