from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# データベース接続設定
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'test_system'
}

def test_mysql_connection():
    try:
        # 接続文字列を設定から構築
        connection_string = (
            f"mysql+pymysql://{db_config['user']}:{db_config['password']}"
            f"@{db_config['host']}/{db_config['database']}"
        )
        
        # エンジンを作成
        engine = create_engine(connection_string)
        
        # 接続テスト
        with engine.connect() as connection:
            print("MySQLへの接続に成功しました！")
            
    except SQLAlchemyError as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    test_mysql_connection()