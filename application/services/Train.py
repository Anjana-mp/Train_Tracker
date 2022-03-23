from infrastructure.repository import db_connect
import response

d1= db_connect.db_connection()
from functools import wraps
import time



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
        train_no=json_file['no']
        name=json_file['name']
        station=json_file['station']
        try:
            train_no=int(train_no)
            if (name== "" or station== ""):
                return response.empty_values
            else:
                output = d1.insert(train_no, name, station)
                return output
        except:
            return response.invalid_trainno




    @timeit
    def get_train(self,json_file):
        train_no=json_file['no']
        try:
            train_no=int(train_no)
            output = d1.train_byid(train_no)
            if(output== response.user_notexists):
                return response.user_notexists
            else:
                response.user_retrieved['body']={}
                response.user_retrieved['body']=output
                return response.user_retrieved

        except:
            return response.invalid_trainno

    @timeit
    def get_trains(self):
        output=d1.get_all()
        response.user_retrieved['body'] =''
        response.user_retrieved['body'] = output
        return response.user_retrieved




    @timeit
    def update_train(self,json_file):
        train_no=json_file['no']
        name = json_file['name']
        station = json_file['station']
        if (name == ""):
            name = "name"
            #print(name)
        if (station == ""):
            station = "station"
            #print(station)
        try:
            train_no=int(train_no)
            output = d1.update_train(train_no, name, station)
            return output
        except:
            return response.invalid_trainno



    @timeit
    def delete_train(self,json_file):
        train_no=json_file['no']
        try:
            train_no=int(train_no)
            output = d1.delete_train(train_no)
            return output
        except:
            return response.invalid_trainno







