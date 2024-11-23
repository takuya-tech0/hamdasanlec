# setup_db.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# データベース接続設定
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'test_system'
}

# データベース接続URL
DATABASE_URL = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"

# SQLAlchemyの設定
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ユーザーモデル定義
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

def create_tables():
    """テーブルを作成する"""
    Base.metadata.create_all(bind=engine)
    print("テーブルを作成しました")

def insert_sample_data():
    """サンプルデータを挿入する"""
    db = SessionLocal()
    try:
        sample_users = [
            User(name="山田太郎", email="taro@example.com"),
            User(name="鈴木花子", email="hanako@example.com"),
            User(name="佐藤次郎", email="jiro@example.com")
        ]
        db.add_all(sample_users)
        db.commit()
        print("サンプルデータを挿入しました")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    # コマンドライン引数で処理を選択できるようにする
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "create":
            create_tables()
        elif sys.argv[1] == "insert":
            insert_sample_data()
        elif sys.argv[1] == "all":
            create_tables()
            insert_sample_data()
    else:
        print("使用方法:")
        print("テーブル作成: python setup_db.py create")
        print("データ挿入: python setup_db.py insert")
        print("両方実行: python setup_db.py all")