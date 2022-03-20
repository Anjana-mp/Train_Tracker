import json
import pandas as pd
from Train import Train_class
T1=Train_class()
n=0

while(n!=5):
    print("1.Create Train\n2.Get Train Details\n3.Update Train Details\n4.Delete Train Details\n5.Exit")
    try:
        n=int(input())
        try:
            if (n > 5):
                raise Exception("Value must be below or equal to 5")
        except Exception as e:
            print(e)
    except:
        print("Enter Valid Choice")



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
            print("Invalid train number")
            continue
        #print(train_no)
        T1.get_train(train_no)


    if(n==3):
        try:
            train_no=int(input("Enter the train no:"))
            name = input("Enter the Name:")
            station = input("Enter the station:")
            if(name==""):
                name="name"
            elif(station==""):
                station="station"
            T1.update_train(train_no,name,station)
        except:
            print("Invalid train number")

    if(n==4):
        try:
            train_no=int(input("Enter the train no you want to delete:"))
            T1.delete_train(train_no)
        except:
            print("Invalid Train number")















