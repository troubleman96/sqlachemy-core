

from sqlalchemy  import create_engine, MetaData, Table, Column, String, Integer, TEXT

#engine = create_engine('sqlite:///mydatabase.db', echo=True)

engine  = create_engine("postgresql+psycopg2://postgres:darkknight@localhost/satutorialdb", echo=True)

meta = MetaData()

people = Table(
    "people", 
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer)
)

meta.create_all(engine)

