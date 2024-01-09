from sqlalchemy import Column, Integer, Text, String, Date, create_engine, inspect
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine


DB_USER = 'crawl_user'
#DB_USER = 'root'
DB_PASSWORD = 'crawl_user_password_01//-_'
DB_HOST = '172.21.0.1'
DB_PORT = '3001'
DB_NAME = 'crawled'

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)


# Define the Crawled model
class Crawled(Base):
    __tablename__ = 'crawled'

    id = Column(Integer, primary_key=True, autoincrement=True)
    site_id = Column(Integer)
    url = Column(String(255))
    date = Column(Date)
    code_status = Column(Integer)
    html = Column(LONGTEXT)


#inspector = inspect(engine)
#existing_tables = inspector.get_table_names()

#if 'crawled' not in existing_tables:
#    Base.metadata.create_all(engine)

if __name__ == '__main__':
    # Create a session
    session = Session()
    # Test 
    try:
        # Perform a sample query (selecting all records)
        all_records = session.query(Crawled).all()
        print("All Crawled records:", all_records)

        # Create an object and add it to the session (for testing insert)
        new_record = Crawled(
            site_id=1,
            url='https://example.com',
            date='2023-12-14',
            code_status=200,
            html='<html><body>Hello, World!</body></html>'
        )
        session.add(new_record)
        session.commit()
        print("New record created:", new_record)

    except Exception as e:
        print(f"Exception: {str(e)}")
        session.rollback()  # Rollback in case of an exception

    finally:
        session.close()