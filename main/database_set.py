import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL="postgresql://postgres:root_123@localhost:5432/filmbot"

database = databases.Database(url=DATABASE_URL)
Base = declarative_base()
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
