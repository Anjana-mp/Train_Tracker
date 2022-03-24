from domain.entities import train_entities
from infrastructure.repository import db_connect
import response
from functools import wraps
import time
from constants import *
from infrastructure.repository.db_connect import DbConnection


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


class TrainClass:
    def __init__(self):
        self.db = DbConnection()

    @timeit
    def create_train(self, json_file):
        train_no = json_file[TRAIN_NO]
        name = json_file[NAME]
        station = json_file[STATION]
        try:
            train_no = int(train_no)
        except ValueError:
            return response.invalid_trainno
        output = self.db.insert(train_no, name, station)
        return output

    @timeit
    def get_train(self, json_file):
        result = {}
        train_no = json_file[TRAIN_NO]
        try:
            train_no = int(train_no)
            trains = self.db.train_byid(train_no)
            if trains == response.user_notexists:
                return response.user_notexists
            else:
                result['data'] = [train_entities.TrainEntity.to_dict(train) for train in trains]
                return result

        except ValueError:
            return response.invalid_trainno

    @timeit
    def get_trains(self):
        result = {}
        trains = self.db.get_all()
        result['data'] = [train_entities.TrainEntity.to_dict(train) for train in trains]
        return result

    @timeit
    def update_train(self, json_file):
        train_no = json_file[TRAIN_NO]
        name = json_file[NAME]
        station = json_file[STATION]
        try:
            train_no = int(train_no)
            output = self.db.update_train(train_no, name, station)
            return output
        except ValueError:
            return response.invalid_trainno

    @timeit
    def delete_train(self, json_file):
        train_no = json_file[TRAIN_NO]
        try:
            train_no = int(train_no)
            output = self.db.delete_train(train_no)
            return output
        except ValueError:
            return response.invalid_trainno
