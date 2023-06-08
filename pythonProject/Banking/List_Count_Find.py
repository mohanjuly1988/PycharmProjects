from pythonProject.Banking.Source2 import *


def List_Count():
    global To_Count
    global Con_Cast
    global l1
    l1=List_Display()
    print("********** Count a particular object in the List **********")
    To_Count=input("Enter the object to count: ")
    Con_Cast = input("Do you need the type casting: ")

    if Con_Cast.capitalize()=='Yes':
        print(l1.count(TypeCasting(globals()['To_Count'])))
    else:
        print(l1.count(To_Count))

def List_Index():
    global To_Find
    print("******* Finding a value ********")
    To_Find=input("Enter a value to find: ")
    Find_Cast=input("Do you need the type casting: ")

    l1=globals()['l1']
    if Find_Cast.capitalize()=='Yes':
        print(l1.index(TypeCasting(globals()['To_Find'])))

    else:
        print(l1.index(To_Find))