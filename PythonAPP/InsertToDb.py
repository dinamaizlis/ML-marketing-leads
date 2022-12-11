import sqlalchemy as db
from sqlalchemy import create_engine

 
def connect_and_insert_to_postgres(lead,score):
    engine = create_engine('postgresql+psycopg2://postgres:Dm123456@localhost/postgres')
    connection = engine.connect()
    metadata = db.MetaData()
    lead_score = db.Table('LeadScore', metadata, autoload=True, autoload_with=engine)#, autoload=True
    query = db.insert(lead_score).values(lead_number=int(lead), score=int(score)) 
    ResultProxy = connection.execute(query)

