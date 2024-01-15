from sqlalchemy import Column, Integer, String, Date, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = 'user003'
DB_PASSWORD = 'user_password_01//-_'
DB_HOST = '127.0.0.1'
DB_PORT = '3002'
DB_NAME = 'extracted'

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#print(DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define the articles model
class articles(Base):
    __tablename__ = 'extracted'

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_id = Column(Integer)
    url = Column(String(255))
    extracted_date = Column(Date)
    title = Column(String(255))
    author = Column(String(255))
    body = Column(Text) 
    date = Column(String(50))

existing_tables = Base.metadata.tables


def getArticles(siteID):
    session = Session()
    data = session.query(articles).filter(articles.site_id == siteID).all()    
    return data