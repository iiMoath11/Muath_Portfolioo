from sqlalchemy import create_engine,text

engine = create_engine(
    "mysql+pymysql://admin:1234admin@database-1.c5yecsksg66z.eu-north-1.rds.amazonaws.com/projects?charset=utf8mb4"
)
with engine.connect() as conn:
    result = conn.execute(text("select * from trial1"))
    print(result.all())
  #interaction between mysql and python