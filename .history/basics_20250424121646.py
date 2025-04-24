from sqlalchemy import create_engine, text

engine  = create_engine('sqlite:///mydatabase.db', echo=True)

conn = engine.connect()

conn.execute(text("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTERGER)"))

conn.commit()


from sqlalchemy .orm import create_engine, MetaData, Table, Column, String, Integer, TEXT

engine = create_engine('sqlite:///mydatabase.db', echo=True)

meta = MetaData()

people = Table(
    "people", 
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer)
)

meta.create_all(engine)

