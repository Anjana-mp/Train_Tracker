import json

import sqlalchemy.sql
from sqlalchemy import *
import response

engine = create_engine('postgresql://postgres:password@localhost:5432/Train')
meta = MetaData(engine)
t1 = Table('Train_db', meta, Column('train_no', Integer, primary_key=True), Column('Name', String), Column('Station',String))
output={}
result=['train_no','Name','Station']
class db_connection:


    def insert(self,train_no,name,station):
        try:

            t1.create(checkfirst=True)
            ins = t1.insert().values(train_no=train_no, Name=name, Station=station)
            engine.execute(ins)
            return response.user_created
        except:
            return response.user_notcreated

    def train_byid(self,train_no):
        sel = sqlalchemy.sql.select(['*']).where(t1.columns.train_no == train_no)
        res = engine.execute(sel)
        no = res.rowcount
        try:
            output = {}
            if (no > 0):
                i = 1
                for row in res:
                    output[i] = dict(row)
                    i = i + 1
            return output
        except Exception:
            return response.user_notexists

    def get_all(self):
        sel = t1.select().order_by(asc(t1.columns.train_no))
        res = engine.execute(sel)
        no = res.rowcount
        try:
            if (no > 0):
                i=1
                for row in res:
                    output[i]=dict(row)
                    i=i+1
            return output

        except:
            return response.user_notexists


    def update_train(self,train_no,name,station):
        sel = sqlalchemy.sql.select(['*']).where(t1.columns.train_no == train_no)
        res = engine.execute(sel)
        no = res.rowcount
        print(no)
        try:
            if (no > 0):
                if (name == "name" and station=="station"):
                    update = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name: t1.columns.Name, t1.columns.Station:t1.columns.Station})
                    engine.execute(update)
                elif (station=="station"):
                    update = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name:name, t1.columns.Station:t1.columns.Station})
                    engine.execute(update)

                elif(name=="name"):
                    update = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name:t1.columns.Name, t1.columns.Station:station})
                    engine.execute(update)


                else:
                    update = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name:name, t1.columns.Station:station})
                    engine.execute(update)
                return response.user_updated
            else:
                raise Exception
        except Exception:
            return response.user_notexists

    def delete_train(self,train_no):
        sel = sqlalchemy.sql.select(['*']).where(t1.columns.train_no == train_no)
        res = engine.execute(sel)
        no = res.rowcount
        try:
            if (no > 0):
                delete = t1.delete().where(t1.columns.train_no == train_no)
                engine.execute(delete)
                return response.user_deleted
            else:
                raise Exception
        except Exception:
            return response.user_notexists


