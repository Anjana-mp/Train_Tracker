import json
import pandas as pd
from Train import Train_class
T1=Train_class()
n=0

while(n!=5):
    print("1.Create Train\n2.Get Train Details\n3.Update Train Details\n4.Delete Train Details\n5.Exit")
    try:
        try:
            n=int(input())
        except:
            print("Enter valid choice")
        if(n>5):
            raise Exception("Value must be below or equal to 5")
    except Exception as e:
        print(e)
    if(n==1):
        print("Enter Train Details")
        json_inp={}
        try:
            json_inp['no']=input('Enter Train id:')
            json_inp['Name']=input('Name:')
            json_inp['Station']=input('Station:')
            if(json_inp['no']=="" or json_inp['Name']=="" or json_inp['Station']==""):
                raise Exception("Empty Values are not allowed")
        except Exception as e:
            print(e)
            continue
        data=json.dumps(json_inp)
        json_inp=json.loads(data)
        T1.create_train(json_inp)

    if(n==2):
        print("Train No:")
        try:
            train_no=int(input())
        except:
            print("Train No must be integer")
            continue
        #print(train_no)
        T1.get_train(train_no)


    if(n==3):
        train_no=input("Enter the train no:")
        name=input("Enter the Name:")
        station=input("Enter the station:")
        try:
            if (train_no== ""):
                raise Exception("Train no Must not be empty")
        except Exception as e:
            print(e)
            continue
        if(name==""):
            name="name"
        elif(station==""):
            station="station"
        T1.update_train(train_no,name,station)

    if(n==4):
        train_no=input("Enter the train no you want to delete:")
        try:
            if (train_no== ""):
                raise Exception("Train no Must not be empty")
        except Exception as e:
            print(e)
            continue
        T1.delete_train(train_no)













