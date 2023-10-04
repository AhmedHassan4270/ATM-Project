from ATMFuntionDefine import *
import datetime
realtime = datetime.datetime.now()
realtime=realtime.strftime("%c")


print("*******WELCOME TO THE BANK OF MAH*******")
print("\n")
print("""
            TRANSACTION 
        *********************
            MAIN MENU:
            1. Create Account
            2. Sub Menu
            3. Exit
        *********************
        """)

while True:
    try:
        option = int(input("Select 1, 2 or 3\n"))
        if option == 1:
            name,username = User_name()
            pincode = Pin()
            account = Account()
            amount = Amount()
            Balance = amount
            status = "Active"
            balncestatment = f"You Initial deposited {Balance}Rs on {realtime}"
            my_data = data(account, name, username, pincode, status, Balance, balncestatment)
            with open("Database.txt", 'a') as file:
                file.write(str(my_data)+"\n")
            print(f"Congratulations! Account Created Successfully & status:{status}.....\n")

        elif option == 2:
            loginname = input("Enter your username to login: ")
            readdata = read_data_from_databasefile(loginname)
            getAccountNumber = get_account_number(loginname, readdata)
            
            current_user_name=(readdata[getAccountNumber]["Name"])
            current_user_Balance = readdata[getAccountNumber]["account_detail"]["Balance"]
            current_user_status = readdata[getAccountNumber]["Status"]
            current_user_pin = readdata[getAccountNumber]["Pin"]
            current_user_statement = readdata[getAccountNumber]["account_detail"]["statement"]

            if getAccountNumber != None:
                print("""
                    TRANSACTION 
                *********************
                    SUB MENU:
                    1. Account Detail
                    2. Deposit
                    3. Withdraw
                    4. Update Pin
                    5. Check Statement
                    6. Logout
                *********************
                """)
                while True:
                    try:
                        option = int(input("Please Select 1, 2, 3, 4, 5, or 6\n"))

                        if option == 1:
                            chances=0
                            while chances<3:
                                x=int(input("Enter Pin Code: "))
                                x=str(x)
                                if x == current_user_pin:
                                    print(f"User Name is : {current_user_name}")
                                    print(f"Balance is : {current_user_Balance}PKR")
                                    print(f"Account number is:{getAccountNumber}")
                                    print(f"Your Account Status is {current_user_status}")
                                    break
                                if chances==3:
                                    current_user_status="Block"
                                    break
                                else:
                                    print("****Invalid Password****")
                                    chances +=1
                        elif option == 2:
                            deposit=Amount()
                            b = current_user_Balance + deposit
                            current_user_Balance= int(b)
                            print(f"Your Current User Balance is {current_user_Balance}PKR")
                            statement= f"You deposited {deposit}Rs on {realtime}"                           
                            status == "Active"
                            # my_data = data(account, name, username, pincode,status, current_user_Balance, statement )
                            # with open("Database.txt", 'w') as file:
                            #     file.write(str(my_data))
                        elif option == 3:
                            print(f"Your Current status is {current_user_status}")
                            if current_user_status == "Active":
                                Withdraw=int(input("Enter amount to withdraw:"))
                                if Withdraw < current_user_Balance:
                                    print("withdraw successful")
                                    Tax = round(Withdraw * .01)
                                    a=current_user_Balance -int(Withdraw +Tax)
                                    current_user_Balance=a
                                    print(f"Your current Balance is {current_user_Balance}PKR")
                                    statement= f"Your Withdraw Amount is {Withdraw}Rs on {realtime}"
                                else:
                                    print("insufficient funds")
                            else:
                                print("Your Account is Blocked. Please Call On Helpline Number For More Detail")
                        elif option == 4:
                            x = int(input("Enter Pin Code: "))
                            x = str(x)
                            if x == current_user_pin:
                                pincode=Pin()
                                # my_data = data(account, name, username, pincode,amount, status)
                                # with open("Database.txt", 'w') as file:
                                #    file.write(str(my_data))
                            else:
                                print("****Invalid Password****")
                        elif option == 5:
                            print(current_user_statement)
                        elif option == 6:
                            print("""
                             -------------------------------------
                            | Thanks for choosing us as your bank |
                            | Visit us again!                     |
                             -------------------------------------
                            """)
                            break
                        else:
                            print("Wrong command! Please Select 1, 2, 3, 4, 5, or 6\n")
                            continue
                    except:
                            pass
            else:
                print("user data not found.please create account first then login")
        elif option == 3:
            print("""
             -------------------------------------
            | Thanks for choosing us as your bank |
            | Visit us again!                     |
             -------------------------------------
            """)
            break
        else:
            print("Wrong command! Please Select 1, 2 or 3 only!\n")
            continue
    except Exception as e:
        print("Error ", e)
