from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# データベース接続設定
config = {
    'host': 'tech0-db-step4-studentrdb-3.mysql.database.azure.com',
    'user': 'tech0gen7student',
    'password': 'vY7JZNfU',
    'database': 'hamadasan_lec',
    'ssl_ca': 'DigiCertGlobalRootCA.crt.pem'
}

# データベース設定
engine = create_engine(
    f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}",
    connect_args={'ssl_ca': config['ssl_ca']}
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ユーザーモデル
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(100))
    created_at = Column(DateTime, default=datetime.now)

# データベースセットアップ
def setup_database():
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        users = [
            User(name="山田太郎", email="taro@example.com"),
            User(name="鈴木花子", email="hanako@example.com"),
            User(name="佐藤次郎", email="jiro@example.com")
        ]
        db.add_all(users)
        db.commit()
        print("データベースのセットアップが完了しました")
    except Exception as e:
        print(f"エラー: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    setup_database()
