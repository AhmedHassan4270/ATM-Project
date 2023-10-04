status = ""
Balance=0

def User_name():
    while True:    
        try: 
            name = str(input("Please Enter User Name In Five Alphabet: \n").lower())
            global user_name
            if len(name) > 5:
                print("Incorrect Pattern")
            elif len(name) < 5:
                print("Incorrect Pattern")
            else:
                user_name=name
                break
        except ValueError: 
            pass
    import random
    name_number=random.randrange(1000, 9999)
    name_number=str(name_number)
    user_name = name + name_number
    print(f"User Name of Account is: {user_name}")
    return name, user_name

def Account():
    import random
    account=random.randrange(1000000000, 9999999999)
    global User_Account
    User_Account=account
    print(f"Your Account number is:{User_Account}")
    return User_Account

def Pin():
    while True:
        try: 
            pin = int(input("Please Enter Four Digits Pin Code In Numerical: \n"))
            pin=str(pin)
            if len(pin) > 4:
                print("Incorrect")
            elif len(pin) < 4:
                print("Incorrect")
            else:
                global pin_code
                pin_code=pin
                break
        except ValueError: 
            pass
    print(f"Your Pasword is :{pin_code}")
    return  pin_code

def Amount():
    while True:
        try: 
            amount = int(input("Please Enter Deposit Amount in PKR:\n"))
            global Balance
            if amount < 50:
                print("Insufficient Amount You Have To Deposit ")
            if amount > 50:
                Balance +=amount
                break
        except ValueError: 
            pass
    print(f"Your Deposit Amount is: {Balance}PKR")
    return Balance


def data(AccountNumber, name, username, pincode, status, Balance, statement):
    user_dictionary = {}

    new_user = {
        "Name": name,
        "Username": username,
        "Pin": pincode,
        "Status": status,
        "account_detail": {
            "Balance": Balance,
            "Currency": "PKR",
            "statement": [statement]
        }
    }
    user_dictionary[AccountNumber] = new_user
    return user_dictionary


def read_data_from_databasefile(username):
    readuser = ""
    with open("Database.txt", 'r') as f:
        lines = f.readlines()
    for line in lines:
        if username in line:
            readuser = line
            break
    readuser = eval(readuser)
    return readuser

def get_account_number(loginname, readdata):
    for accountnumber, user_db in readdata.items():
        if user_db["Username"] == loginname:
            return accountnumber






# def update_databasefile(x,pincode,current_user_Balance,statement):
#     readuser = ""
#     with open("Database.txt", 'w') as f:
#         lines = f.readlines()
#     for line in lines:
#         if x in line:
#             x = readuser
#             readuser=pincode
#             break
