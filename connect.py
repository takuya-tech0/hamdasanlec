from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# データベース接続設定
config = {
    'host': 'tech0-db-step4-studentrdb-3.mysql.database.azure.com',
    'user': 'tech0gen7student',
    'password': '',
    'database': 'sembaapp',
    'ssl_ca': 'DigiCertGlobalRootCA.crt.pem'
}

def test_mysql_connection():
    try:
        # 接続文字列を作成
        connection_string = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
        
        # エンジンを作成（SSL設定付き）
        engine = create_engine(connection_string, connect_args={'ssl_ca': config['ssl_ca']})
        
        # 接続テスト
        with engine.connect() as connection:
            print("データベースへの接続に成功しました！")
            
    except SQLAlchemyError as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    test_mysql_connection()
