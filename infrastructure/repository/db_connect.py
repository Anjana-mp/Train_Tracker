import sqlalchemy.sql
from sqlalchemy import *
import response
from domain.factory.train_factory import TrainFactory

engine = create_engine('postgresql://postgres:password@localhost:5432/Train')
meta = MetaData(engine)
t1 = Table('Train_db', meta, Column('train_no', Integer, primary_key=True), Column('Name', String),
           Column('Station', String))


class DbConnection:

    @staticmethod
    def insert(train_no, name, station):
        try:
            t1.create(checkfirst=True)
            ins = t1.insert().values(train_no=train_no, Name=name, Station=station)
            engine.execute(ins)
            return response.user_created
        except RuntimeError:
            return response.user_notcreated

    @staticmethod
    def train_byid(train_no):
        sel = sqlalchemy.sql.select(['*']).where(t1.columns.train_no == train_no)
        res = engine.execute(sel)
        no = res.rowcount
        try:
            if no > 0:
                return [TrainFactory.train(train_no=row.train_no, name=row.Name, station=row.Station) for row in res]
            else:
                return response.user_notexists
        except ValueError:
            return response.user_notexists

    @staticmethod
    def get_all():
        sel = t1.select().order_by(asc(t1.columns.train_no))
        res = engine.execute(sel)
        no = res.rowcount
        try:
            if no > 0:
                return [TrainFactory.train(train_no=row.train_no, name=row.Name, station=row.Station) for row in res]
            else:
                return response.user_notexists
        except ValueError:
            return response.user_notexists

    @staticmethod
    def update_train(train_no, name, station):
        sel = sqlalchemy.sql.select(['*']).where(t1.columns.train_no == train_no)
        res = engine.execute(sel)
        no = res.rowcount
        try:
            if no > 0:
                if name == "name" and station == "station":
                    update_details = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name: t1.columns.Name, t1.columns.Station: t1.columns.Station})
                    engine.execute(update_details)
                elif station == "station":
                    update_details = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name: name, t1.columns.Station: t1.columns.Station})
                    engine.execute(update_details)

                elif name == "name":
                    update_details = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name: t1.columns.Name, t1.columns.Station: station})
                    engine.execute(update_details)
                else:
                    update_details = t1.update().where(t1.columns.train_no == train_no).values(
                        {t1.columns.Name: name, t1.columns.Station: station})
                    engine.execute(update_details)
                return response.user_updated
            else:
                return response.user_notexists
        except ValueError:
            return response.user_notexists

    @staticmethod
    def delete_train(train_no):
        sel = sqlalchemy.sql.select(['*']).where(t1.columns.train_no == train_no)
        res = engine.execute(sel)
        no = res.rowcount
        try:
            if no > 0:
                delete_no = t1.delete().where(t1.columns.train_no == train_no)
                engine.execute(delete_no)
                return response.user_deleted
            else:
                raise Exception
        except RuntimeError:
            return response.user_notexists
