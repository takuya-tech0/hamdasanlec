from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime
import uvicorn

app = FastAPI()

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

class UserBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True

@app.get("/")
def read_root():
    return {"message": "Hello! Hamada-san!"}

@app.get("/users")
def get_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return users
    finally:
        db.close()

@app.get("/users/{id}")
def get_user(id: int):
    db = SessionLocal()
    try:
        return db.query(User).filter(User.id == id).first()
    finally:
        db.close()

@app.post("/users")
def create_user(user: UserBase):
    db = SessionLocal()
    try:
        db_user = User(name=user.name, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    finally:
        db.close()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
