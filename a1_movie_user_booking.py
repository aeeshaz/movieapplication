"""
Assessment 1: A user login function for the online movie ticket booth

Description: Combine m61 and m62 to create an advanced online ticketing system
that can allow members to login. Since we need to check their age for the movie,
make sure age is also part of the user dictionary! Users should only be allowed 
to buy a movie ticket after they have signed up for an account.
Hint: You can create a switch that is "off" and is turned on when a users successfully
signs in. And the movie showings segment should only run IF the switch is "on".
"""

acc_user = {'jay':{'username':'jay01','password':'jy00001','age':16},'kate':{'username':'kate769','password':'kate40002','age':23},'wendy':{'username':'wen39','password':'dy40','age':12}}


# Part 2: Get user's info
name = input('What is your name?')
login = False
    
# Part 3: Check if user is a registered user and if details are accurate
while True : 
    #when user exist
    if name in acc_user.keys():
        actual_username = acc_user[name]['username']
        actual_password = acc_user[name]['password']
        #ask for username and password
        log_in_user = input('what is your username?')
        log_in_password = input ('what is your password?')
        #check if its correct or not
        #if correct password, stop the while loop and allow them to log in (break)
        if actual_username == log_in_user and actual_password == log_in_password:
            print('you have succesfully logged in')
            login = True
            break
        #if its not correct, ask to log in again (continue)
        else:
            print('username or password is wrong')
            print('please log in again')
            continue
        
    
    #if user doesnt exist
    else:
        #ask them if they want to create a new account
        new_acc = input('do you want to create a new account?')
        #if they want it, ask for username and password, ask if they want to be log in immedietly (continue / break)
        if new_acc == 'yes':
            new_log_in_user = input('what is your new username?')
            new_log_in_password = input ('what is your new password?')
            age = int(input('whats your age?'))
            acc_user[name] = {'username': new_log_in_user,'password': new_log_in_password,'age': age}
            print('succesfully created')
            answer = input('do you want to be log in?')
            if answer == 'yes':
                continue
            else:
                break
        #if they doesnt, exit (break)
        else:
            print('thank you, have a good day')
            break
############################################################################################################
# Part 1: Create the movie list
movie_age = {'harry potter': 16, 'the bees': 7, 'jaws': 18, 'spiderman': 13}
if login:
# Part 2: As user for their details
    age = acc_user[name] ['age']
    movie = input("What movie do you want to watch?")
        
     # Part 3: Check if they are old enough to watch the movie
    while age < (movie_age[movie]):
       movie = input(f"The age doesnt match,choose another movie")
        
    print("You can have the ticket")