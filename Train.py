import json
import sqlalchemy.sql
from sqlalchemy import *
from functools import wraps
import time
import pandas as pd
import psycopg2
engine = create_engine('postgresql://postgres:password@localhost:5432/Train')
meta=MetaData(engine)
t1=Table('Train_db',meta,Column('train_no',Integer,primary_key=True),
                 Column('Name',String),Column('Station',String))
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

class Train_class:
    @timeit
    def create_train(self,json_file):
        #print(json_file['Name'])
        try:
            t1.create(checkfirst=True)
            ins=t1.insert().values(train_no=json_file['no'],Name=json_file['Name'],Station=json_file['Station'])
            engine.execute(ins)
        except:
            print("Train no must be unique")
        print("Created Successfully")


    @timeit
    def get_train(self,train_no):
            sel=sqlalchemy.sql.select(['*']).where(t1.columns.train_no==train_no)
            res=engine.execute(sel)
            no=res.rowcount
            try:
                if(no>0):
                    for row in res:
                        result=list((row))
                        json_result=json.dumps(result)
                        print(json_result)
                else:
                    raise Exception("Train Doesnot Exists")
            except Exception as e:
                print(e)


    @timeit
    def update_train(self,train_no,name,station):
        sel = sqlalchemy.sql.select(['*']).where(t1.columns.train_no == train_no)
        res = engine.execute(sel)
        no = res.rowcount
        try:
            if(no>0):
                if(name=="name"):
                    update = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name: t1.columns.Name, t1.columns.Station: station})
                    engine.execute(update)
                elif (name == "station"):
                    update = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name: t1.columns.Name, t1.columns.Station: station})
                    engine.execute(update)
                else:
                    update=t1.update().where(t1.columns.train_no==train_no).values({t1.columns.Name:name,t1.columns.Station:station})
                    engine.execute(update)
                    print("Updated Successfully")
            else:
                raise Exception ("Enter Valid train_no")
        except Exception as e:
            print(e)


    @timeit
    def delete_train(self,train_no):
        sel = sqlalchemy.sql.select(['*']).where(t1.columns.train_no == train_no)
        res = engine.execute(sel)
        no = res.rowcount
        try:
            if(no>0):
                delete=t1.delete().where(t1.columns.train_no==train_no)
                engine.execute(delete)
                print("Deleted Successfully")
            else:
                raise Exception("Train no doesnot exists")
        except Exception as e:
            print(e)





