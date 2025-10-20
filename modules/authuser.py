##VERIFY/Authenticate user:
from data.userdata import existingusers

def authuser(): #No parameters need since we are assigning the entered values via userinput function made above
    entername = input('Your name: ')
    enterpin = input('Pin: ')
    validuser = False

    for uid, credential in existingusers.items(): #this ensure the details are compared with right credentials, its important 
                                                  #to consider key for verification along with its corresponding details
        #now to compare credentials of user
        if credential['name'] == entername  and credential['pin'] == enterpin :
            validuser = True
            print(f'Hey {entername}, You are Logged in now...')
            validuser = uid
            break
        #else:
            #print('Incorrect details! Try again...') ;; this code line will iterate and check for each entry which is not right due to
            #privacy and optimization concerns. Right place to write this code is shown below!!
    
    if validuser:
        return validuser       #if you wanna get value/access this anywhere in code for Verification and process
        # option = showmenu()          #this will show the menu as well as store the input from user in variable 'option'
        #                              #to get/access this value anywhere in code
        # operation(validuser,option)       
    else:
        print('\nIncorrect details! Try again...')
        
