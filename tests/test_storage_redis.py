import redis

# 连接 Redis 服务器
# 如果 Redis 运行在 Docker 容器中且端口映射为 6379，可以直接连接
# 如果 Redis 有密码，需要添加 password='yourpassword' 参数
r = redis.Redis(
    host='localhost',  # Redis 服务器地址
    port=6379,         # Redis 服务器端口
    db=0               # 默认数据库
)

# 测试连接
try:
    r.ping()
    print("成功连接到 Redis 服务器")
except redis.ConnectionError:
    print("无法连接到 Redis 服务器")
    exit(1)

# 设置一个键值对
r.set('test_key', 'Hello, Redis!')

# 获取键值对
value = r.get('test_key')
print(f"获取到的值: {value.decode('utf-8')}")  # 解码字节串为字符串

# 删除键值对
r.delete('test_key')
print("已删除 test_key")

# 检查键是否存在
exists = r.exists('test_key')
print(f"test_key 是否存在: {'是' if exists else '否'}")

# 设置带过期时间的键值对（10秒后过期）
r.setex('temp_key', 10, 'This will expire in 10 seconds')
print("已设置带过期时间的键 temp_key")

# 获取剩余过期时间
ttl = r.ttl('temp_key')
print(f"temp_key 的剩余过期时间: {ttl} 秒")

# 列出所有数据库中的键（注意：生产环境慎用，可能影响性能）
# keys = r.keys('*')
# print(f"所有键: {keys}")

# 关闭连接（redis-py 会自动管理连接池，通常不需要手动关闭）
