import json
file = open ("Project_1_json.json","r")  # read data
All_List_In_Bank = json.load(file)
file.close()





repeat = True
while repeat:

    print('\n','*'*84 ,"Welcome to SIC bank management",'*'*84,'\n')
    print("If you don't have an account enter [register]")
    print("If you already have an account please enter [login]",'\n')

    user_sign = input('Enter : ').lower().strip()


# login
    if user_sign == 'login':
        print('*'*20 ,"Welcome to login page",'*'*20)



        file = open ("Project_1_json.json","r") 
        data = json.load(file)



        user_logined_id = int(input('Enter your ID : '))
        user_logined_ps = input('Enter your password : ').strip()

        my_index = user_logined_id -1

        # for All_List_In_Bank[my_index] in All_List_In_Bank :
        if len(All_List_In_Bank)>= user_logined_id:
            if All_List_In_Bank[my_index]['ID'] == user_logined_id and All_List_In_Bank[my_index]['Password'] == user_logined_ps:
                repeat = False
                    
                # print(All_List_In_Bank[my_index])
                print('Welcome back' , All_List_In_Bank[my_index]['Name']) 



            else:
                print("Wrong ID or PS")
                repeat = True
                # break

        else:
            print("User not found!  You must register first!")

            
        file.close()

            
        
# register
    elif user_sign == 'register':
        repeat = True

        print('*' * 20, "Welcome to sign up page", '*' * 20)

        file = open('Project_1_json.json' , 'r')
        All_List_In_Bank = json.load(file)
        # print(All_List_In_Bank)


        user_signed_name = input('Please enter your name : ').strip().capitalize()
        user_signed_ps = input('Please enter your password : ').strip()
        user_signed_num = int(input('Please enter your phone number : '))
        user_signed_mail = input('Please enter your mail : ').strip()
        user_signed_gender = input('Please enter your gender : ').strip().capitalize()
        user_signed_age = int(input('Please enter your age : '))
        user_signed_city = input('Please enter your city : ').strip().capitalize()




        ID = All_List_In_Bank[-1]['ID']
        new_ID = ID +1
        User_All_List_In_Bank={"ID": new_ID ,
                               "Name": user_signed_name,
                               "Password": user_signed_ps,
                               "Phone number": user_signed_num,
                               "Mail": user_signed_mail,
                               "Gender": user_signed_gender,
                               "Age": user_signed_age,
                               "City": user_signed_city,
                               "Balance": 0}

        All_List_In_Bank.append(User_All_List_In_Bank)



        file = open("Project_1_json.json", "w")  
        json.dump(All_List_In_Bank,file,indent=2)
        file.close()


        print('sign up successful , your ID is',new_ID)  


# nor
    else:
        repeat = True
        print("Not Avaliable")
        

    continue






# menu 
user_balance = 0
while True:

    print("Please Enter your choice")   

    print('[0]Deposit')  
    print('[1]Withdraw')  
    print('[2]Transfer')  
    print('[3]Check balance & personal info')  
    print('[4]Exit') 

    user_op_num = int(input('Enter operation you want :')) 


#deposite
    if user_op_num == 0:

    
        print("Your balance is " ,All_List_In_Bank[my_index]['Balance'] , "EGP")   
        print("Please enter the amount you want to deposite: ")

        user_deposite = float(input('Enter your amount of money: '))
        currency = input('Enter currency type in this form EGP : ').strip().upper()

        currency_rates = {"USD": 30,
                          "SAR": 9,
                          "EGP": 1}
        


# calculating                 
        if currency in currency_rates:
            print(user_deposite , currency , "was deposited successfully!!" )
            user_deposite *= currency_rates.get(currency)
            user_balance += user_deposite
            user_balance += All_List_In_Bank[my_index]['Balance']
            
            All_List_In_Bank[my_index]['Balance'] += user_deposite
            print("Your balance is " ,All_List_In_Bank[my_index]['Balance'] , "EGP")   #user_balance + user_deposite         

            file = open ('Project_1_json.json','w')
            json.dump(All_List_In_Bank , file , indent=2)

            file.close()


            

        else:
            print("Invalid currency entered")





#withdraw
    elif user_op_num == 1:

        print("Your balance is " ,All_List_In_Bank[my_index]['Balance'] , "EGP")   
        print("Please enter the amount you want to withdraw: ")
        
        user_withdraw = float(input('Enter your amount of money: ')) 
        currency = input('Enter currency type in this form EGP : ').strip().upper() 

        currency_rates = {"USD": 30,
                          "SAR": 9,
                          "EGP": 1}
        


# calculating                 
        if currency in currency_rates:
            if user_withdraw * currency_rates.get(currency) <= All_List_In_Bank[user_logined_id - 1]['Balance']:            
                print(user_withdraw , currency , "was withdrawn successfully!!" )
                user_withdraw *= currency_rates.get(currency)
                user_balance -= user_withdraw
                user_balance -= All_List_In_Bank[my_index]['Balance']
                
                All_List_In_Bank[my_index]['Balance'] -= user_withdraw
                print("Your balance is " ,All_List_In_Bank[my_index]['Balance'] , "EGP")   #user_balance - user_withdraw
            else:
                print("Your money isn't enough!")
        else:
            print("Invalid currency entered")


        file = open ('Project_1_json.json','w')
        json.dump(All_List_In_Bank , file , indent=2)
        file.close()






#transfer
    elif user_op_num == 2:
        # for items in All_List_In_Bank:
        
        user_amount = float(input("please enter the amount.you want to transfer in EGP : "))
        user_id = int(input("please enter the id of the account you want to transfer money to : "))

        
        file = open('Project_1_json.json' , 'r')
        All_List_In_Bank = json.load(file)
        
        # if user_id in All_List_In_Bank:
        if len(All_List_In_Bank)>= user_id:
            if user_amount <= All_List_In_Bank[user_logined_id - 1]['Balance']:

            
                new_balance_1 = All_List_In_Bank[user_logined_id - 1]['Balance'] - user_amount 
                new_balance_2 = All_List_In_Bank[user_id-1]['Balance'] + user_amount 

                All_List_In_Bank[user_logined_id - 1]['Balance'] = new_balance_1
                All_List_In_Bank[user_id - 1]['Balance'] = new_balance_2
                
                print("Done!")
                print("Your balance become " ,new_balance_1 , "EGP")
                print(All_List_In_Bank[user_id - 1]['Name'], "balance become " ,new_balance_2 , "EGP")

            else:
                print("Your money isn't enough!")

        else:
                print("User not found!")


        file = open("Project_1_json.json", "w")  
        json.dump(All_List_In_Bank,file,indent=2)
        file.close()

    
    

# info
    elif user_op_num == 3:
        my_index = user_logined_id -1
        print(All_List_In_Bank[my_index])

        for key in All_List_In_Bank[my_index]:
            print(key ,":", All_List_In_Bank[my_index][key])



#exit
    elif user_op_num == 4:
        print("Program exited")
        break






# wrong operation    
    else:
        print("Invalid operation")
        