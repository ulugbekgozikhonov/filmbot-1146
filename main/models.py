from main.database_set import metadata
import sqlalchemy
from sqlalchemy import Column,Integer,BigInteger,String,DateTime
from datetime import datetime

user = sqlalchemy.Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("chat_id",BigInteger,unique=True)
    
)

move = sqlalchemy.Table(
    "movies",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("title",String(50)),
    Column("format",Integer),
    Column("language",String(50)),
    Column("country",String(55)),
    Column("genre",String(33)),
    Column("file_id",String,unique=True,nullable=False),
    Column("code",Integer,unique=True,nullable=False),
    Column("view",Integer)
)