import json
n=0
import pandas as pd
from Train import Train_class
T1=Train_class()

while(n!=6):
    print("1.Create Train\n2.Get All Trains\n3.Train Details by Id\n4.Update Train Details\n5.Delete Train Details\n6.Exit")
    try:
        n=int(input())
        try:
            if (n > 6):
                raise Exception(json.dumps("Value must be below or equal to 6"))
        except Exception as e:
            print(e)
    except:
        print(json.dumps("Enter Valid Choice"))



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
        T1.get_trains()


    if(n==3):
        print("Train No:")
        try:
            train_no=int(input())
        except:
            print(json.dumps("Invalid train number"))
            continue
        #print(train_no)
        T1.get_train(train_no)


    if(n==4):
        json_inp = {}
        try:
            json_inp['no'] = input('Enter Train No:')
            json_inp['name'] = input('Name:')
            json_inp['station'] = input('Station:')
            if(json_inp['name']==""):
                json_inp['name']="name"
            elif(json_inp['station']==""):
                json_inp['station']="station"
            data = json.dumps(json_inp)
            json_inp = json.loads(data)
            T1.update_train(json_inp)
        except:
            print(json.dumps("Invalid train number"))

    if(n==5):
        try:
            train_no=int(input("Enter the train no you want to delete:"))
            T1.delete_train(train_no)
        except:
            print("Invalid Train number")















