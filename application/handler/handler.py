import json
import logging
import response
from application.services.Train import TrainClass
from constants import *

t_obj = TrainClass()


def setup():
    n = 0
    while n != 6:
        print(
            "1.Create Train\n"
            "2.Get All Trains\n"
            "3.Train Details by Id\n"
            "4.Update Train Details\n"
            "5.Delete Train Details\n"
            "6.Exit")
        try:
            n = int(input())
            try:
                if n > 6:
                    raise ValueError('Invalid Option')
            except ValueError as e:
                logging.error(e)
        except ValueError:
            logging.error('Wrong Input')

        if n == 1:
            create_details()
        if n == 2:
            get_all_trains()
        if n == 3:
            get_by_id()
        if n == 4:
            update_train_details()
        if n == 5:
            del_details()


def create_details():
    print("Enter Train Details")
    json_input = {TRAIN_NO: input('Enter Train no:'),
                  NAME: input('Name:'),
                  STATION: input('Station:')}
    if json_input[TRAIN_NO] is None:
        print(json.dumps(response.empty_values))
    else:
        if json_input[NAME] is None or json_input[STATION] is None:
            print(response.empty_values)
        data = json.dumps(json_input)
        json_data = json.loads(data)
        result = t_obj.create_train(json_data)
        print(json.dumps(result, indent=4))


def get_all_trains():
    result = t_obj.get_trains()
    print(json.dumps(result, indent=4))


def get_by_id():
    json_input = {TRAIN_NO: input("Enter Train no:")}
    if json_input[TRAIN_NO] is None:
        print(json.dumps(response.empty_train))
    else:
        data = json.dumps(json_input)
        json_inp = json.loads(data)
        result = t_obj.get_train(json_inp)
        print(json.dumps(result, indent=4))


def update_train_details():
    json_input = {TRAIN_NO: input('Enter Train no:'),
                  NAME: input('Name:'),
                  STATION: input('Station:')}
    if json_input[TRAIN_NO] is None:
        print(json.dumps(response.empty_train))
    else:
        if json_input[NAME] == "":
            json_input[NAME] = "name"
        if json_input[STATION] == "":
            json_input[STATION] = "station"
        data = json.dumps(json_input)
        json_inp = json.loads(data)
        result = t_obj.update_train(json_inp)
        print(json.dumps(result, indent=4))


def del_details():
    json_input = {TRAIN_NO: input("Enter Train no:")}
    if json_input[TRAIN_NO] is None:
        print(json.dumps(response.empty_train))
    else:
        data = json.dumps(json_input)
        json_inp = json.loads(data)
        result = t_obj.delete_train(json_inp)
        print(json.dumps(result, indent=4))


if __name__ == '__main__':
    setup()
