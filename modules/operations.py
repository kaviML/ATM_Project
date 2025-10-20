from data.userdata import existingusers

def withdraw(uid):
    outamount = int(input('Enter withdrawl amount: '))
    totalamount = existingusers[uid]['Saving']
    remainingamount = totalamount - outamount
    existingusers[uid]['Saving'] = remainingamount
    print(f'\nAvailable Balance after withdrawl: {remainingamount}')

def deposit(uid):
    inamount = int(input('Enter deposit amount: '))
    totalamount = existingusers[uid]['Saving']
    updatedtotal = totalamount + inamount
    existingusers[uid]['Saving'] = updatedtotal
    print(f'\nAvailable Balance after withdrawl: {updatedtotal}')

def transfer(uid):
    sendamount = int(input('\nEnter amount to transfer: '))
    totalamount = existingusers[uid]['Saving']
    leftamount = totalamount - sendamount
    reciever = input('Enter the name of reciever: ')
    moneysent = False
    #for uid, credentials in existingusers.items():  ##here uid is conflicting with the transfering users uid, so rename it to rid etc
    for rid, credentials in existingusers.items():
        if credentials['name'] == reciever:
            existingusers[rid]['Saving'] = existingusers[rid]['Saving'] + sendamount
            moneysent = True
        
    if moneysent:
        existingusers[uid]['Saving'] = leftamount
        
        print(f'\nMoney Transfered... Remaing Balance is: {leftamount} \n Thank you!')
    else:
        print('Transfer failed! Receiver not found.')

def showdetails(uid):
    print(' *** Your Account Details are: ***')
    for key, details in existingusers[uid].items():
        print(key,':',details)
