import json
from textwrap import indent

import response
from application.services.Train import Train_class
T1=Train_class()


def setup():
    n = 0
    while (n != 6):
        print(
            "1.Create Train\n2.Get All Trains\n3.Train Details by Id\n4.Update Train Details\n5.Delete Train Details\n6.Exit")
        try:
            n = int(input())
            if (n > 6):
                raise Exception
        except Exception:
            print(response.invalid_choice)
            continue
        if (n == 1):
            create_details()
        if (n == 2):
            get()
        if (n == 3):
            id()
        if (n == 4):
            up_details()
        if (n == 5):
            del_details()


def create_details():
    print("Enter Train Details")
    json_inp = {}
    json_inp['no'] = input('Enter Train no:')
    if (json_inp['no'] == ""):
        print(json.dumps(response.empty_values))
    else:
        json_inp['name'] = input('Name:')
        json_inp['station'] = input('Station:')
        data = json.dumps(json_inp)
        json_inp = json.loads(data)
        result = T1.create_train(json_inp)
        print(json.dumps(result,indent=4))


def get():
    result = T1.get_trains()
    print(json.dumps(result,indent=4))


def id():
    json_inp = {}
    json_inp['no'] = input('Enter Train no:')
    if (json_inp['no'] == ""):
        print(json.dumps(response.empty_train))
    else:
        data = json.dumps(json_inp)
        json_inp = json.loads(data)
        result = T1.get_train(json_inp)
        print(json.dumps((result),indent=4))



def up_details():
    json_inp = {}
    json_inp['no'] = input('Enter Train No:')
    if (json_inp['no'] == ""):
        print(json.dumps(response.empty_train))
    else:
        json_inp['name'] = input('Name:')
        json_inp['station'] = input('Station:')
        data = json.dumps(json_inp)
        json_inp = json.loads(data)
        result = T1.update_train(json_inp)
        print(json.dumps(result,indent=4))



def del_details():
    json_inp = {}
    json_inp['no'] = input('Enter Train no:')
    if (json_inp['no'] == ""):
        print(json.dumps(response.empty_train))
    else:
        data = json.dumps(json_inp)
        json_inp = json.loads(data)
        result = T1.delete_train(json_inp)
        print(json.dumps(result,indent=4))
if __name__=='__main__':
    setup()


























