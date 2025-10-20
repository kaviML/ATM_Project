#Menu for banking operations
import sys  #To use sys.exit() function, since normal exit gives error cuz of being in local scope
from modules.operations import * 

def showmenu():
    print(' ****** \n Welcome, Select Operation from below: ')
    menu = {1:'Check Balance',2:'Withdraw',3:'Deposite',4:'Transfer', 5:'Check Details',6:'Exit'}
    for key,value in menu.items():  #to get all key and value pair together we use .items() method
        print(f'{key}. {value}')

    option = int(input('\n Your choice: '))
    return option
    

#---
def operation(uid,option):
    if option == 1:
        print(f"Your Balance: {existingusers[uid]['Saving']}")
    elif option == 2:
        withdraw(uid)
    elif option == 3:
        deposit(uid)
    elif option == 4:
        transfer(uid)
    elif option == 5:
        showdetails(uid)
    else:
        #operation.quit()  #to exit of end the code there is no function like this, use exit() instead
        #exit()
        sys.exit()