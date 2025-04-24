

from sqlalchemy  import create_engine, MetaData, Table, Column, String, Integer, insert

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

conn = engine.connect()

#insert_statement = people.insert().values(name='Mike', age=30)

insert_statement = insert(people.values('name='))
result = conn.execute(insert_statement)
conn.commit()