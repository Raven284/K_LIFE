from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()  # 读取 .env 文件
db_url = os.getenv("DATABASE_URL")

try:
    engine = create_engine(db_url)
    with engine.connect() as conn:
        print("✅ 数据库连接成功！")
except Exception as e:
    print("❌ 数据库连接失败：", e)
