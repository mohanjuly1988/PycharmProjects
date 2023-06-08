from pythonProject.Banking.TypeCast import *

def List_Creation():
    global l1
    print("******* List Creation *********")
    l1=eval(input("Enter your list: "))

def List_Append():
    global To_Append
    print("******* Appending the List *********")
    To_Append=input("Enter the value to append: ")
    Append_Cast=input("Do you need the type casting: ")

    if Append_Cast.capitalize()=='Yes':
        l1.append(TypeCasting(globals()['To_Append']))

    else:
        l1.append(To_Append)

def List_Extend():
    print("******* Extending the List *********")
    l2=eval(input("Enter a list to extend: "))
    l1.extend(l2)

def List_Insert():
    global To_Insert
    print("******* Insert an object into the List *********")
    To_Insert=input(": ")
    index_value=eval(input("Enter the index value: "))
    Ins_Cast = input("Do you need the type casting: ")

    if Ins_Cast.capitalize()=='Yes':
        l1.insert(index_value, TypeCasting(globals()['To_Insert']))
    else:
        print(l1.insert(index_value,To_Insert))

def List_Display():
    print("******* Current list now ********")
    return l1

