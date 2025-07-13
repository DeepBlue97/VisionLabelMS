from minio import Minio
from minio.error import S3Error

# 初始化 MinIO 客户端
# 替换为你的 MinIO 服务地址、Access Key 和 Secret Key
minio_client = Minio(
    "localhost:9000",  # MinIO 服务地址
    access_key="minioadmin",  # 默认 Access Key（生产环境请修改）
    secret_key="minioadmin",  # 默认 Secret Key（生产环境请修改）
    secure=False  # 如果是 HTTPS 连接，设置为 True
)

# 测试桶（Bucket）操作
bucket_name = "test-bucket"

try:
    # 检查桶是否存在
    found = minio_client.bucket_exists(bucket_name)
    if not found:
        # 创建桶
        print(f"创建桶: {bucket_name}")
        minio_client.make_bucket(bucket_name)
    else:
        print(f"桶 {bucket_name} 已存在")

    # 测试文件上传
    file_path = "testfile.txt"  # 本地测试文件路径
    object_name = "test-object"  # MinIO 中的对象名称

    # 创建一个测试文件（如果不存在）
    with open(file_path, "w") as f:
        f.write("This is a test file for MinIO.")

    # 上传文件
    print(f"上传文件: {file_path} -> {bucket_name}/{object_name}")
    minio_client.fput_object(bucket_name, object_name, file_path)

    # 测试文件下载
    download_path = "downloaded-testfile.txt"  # 下载后的文件路径
    print(f"下载文件: {bucket_name}/{object_name} -> {download_path}")
    minio_client.fget_object(bucket_name, object_name, download_path)

    # 测试文件列表
    print(f"列出桶 {bucket_name} 中的对象:")
    objects = minio_client.list_objects(bucket_name)
    for obj in objects:
        print(f" - {obj.object_name}")

    # 测试文件删除
    print(f"删除对象: {bucket_name}/{object_name}")
    minio_client.remove_object(bucket_name, object_name)

    # 测试桶删除（谨慎操作，会删除所有对象）
    # print(f"删除桶: {bucket_name}")
    # minio_client.remove_bucket(bucket_name)

except S3Error as e:
    print(f"MinIO 操作失败: {e}")

finally:
    print("MinIO 测试完成")
