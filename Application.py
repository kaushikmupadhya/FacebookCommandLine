import sys
from Facebook import Facebook
from helper import clear
from Database import Database

def home_screen():
    print("|-------------------------------------|")
    print('|      COMMAND LINE FACEBOOK          |')
    print("|-------------------------------------|")
    choice = input('\n 1. Login \n 2. Register \n 3. Exit \n \n Enter your choice: ')
    clear()
    if(choice == '1'):
        current_user = login()
        user_dashboard(current_user)
        home_screen()

    elif(choice == '2'):
        register()
        home_screen()

    elif(choice == '3'):
        exit()

    else:
        print("|-------------------------------------|")
        print("           Invalid Choice!            ")
        print("|-------------------------------------|")
        home_screen()

def login():
    db = Database()
    if(db.count_user() != 0):
        print("|--------------------------------------------------|")
        print("|----------------------LOGIN-----------------------|")
        print("|--------------------------------------------------|")
        email = input('\n Enter Your Email: ')
        password = input('\n Enter Your Password: ')
        if db.validate_credentials(email, password):
            clear()
            print("|-----------------------------------------|")
            print('     Welcome! to command line facebook    ')
            print("|-----------------------------------------|")
            return email
        else:
            clear()
            print("|----------------------|")
            print('   Wrong Credentials!   ')
            print("|----------------------|")
            home_screen()
    else:
        clear()
        print("|----------------------|")
        print("     No user found      ")
        print("|----------------------|")
        home_screen()

def user_dashboard(current_user):
    db = Database()
    user = Facebook()
    print("|-----------------------------|")
    print("|--------USER DASHBOARD-------|")
    print("|-----------------------------|")
    print('\n What Would You Like To Do?')
    choice = input('\n 1. My Timeline \n 2. My Friends \n 3. My Groups \n 4. My Profile \n 0. Log out \n \n Enter your choice: ')
    clear()
    if choice =='1':
        my_timeline(current_user)

    elif choice=='2':
        my_friends(current_user)

    elif choice=='3':
        group_activities(current_user)

    elif choice=='4':
        firstName,lastName,email,dob,bio = db.get_user_node_details(current_user)
        clear()
        print("|-------------------------------------------|")
        print("|----------------MY PROFILE-----------------|")
        print("|-------------------------------------------|")
        print(" First Name : ",firstName)            
        print(" Last Name : ",lastName) 
        print(" Email ID : ",email) 
        print(" Date of Birth : ",dob) 
        print(" Bio : ",bio)
        print("|-------------------------------------------|") 
        input("  Press Enter to go back to your dashboard   ")
        clear()
        user_dashboard(current_user)

    elif choice=='0':
        clear()
        print("|-----------------------------------------|")
        print("     You are logged out of the session     ")
        print("|-----------------------------------------|")
        home_screen()

    else:
        clear()
        print("|-------------------------------------|")
        print("           Invalid Choice!            ")
        print("|-------------------------------------|")
        user_dashboard(current_user)

    return True

def my_timeline(current_user):
    user = Facebook()
    subchoice = input('\n 1. Display my posts \n 2. Create text post \n 0. Back \n \n Enter your choice: ')
    clear()
    if subchoice == '1':
        user.display_user_posts(current_user)
        input("   Press Enter to go back   ")
        clear()
        my_timeline(current_user)
    elif subchoice == '2':
        user.create_post(current_user)
        input("           Press Enter to go back   ")
        clear()
        my_timeline(current_user)
    elif subchoice == '0':
        user_dashboard(current_user)
    else:
        clear()
        print("|-------------------------------------|")
        print("           Invalid Choice!             ")
        print("|-------------------------------------|")
        my_timeline(current_user)

def my_friends(current_user):
    db = Database()
    user = Facebook()
    subchoice = input('\n 1. Add friends \n 2. Display friends \n 3. Display friend\'s posts \n 0. Back \n \n Enter your choice: ')
    clear()
    if subchoice == '1':
        user.showUsers()
        friend_name = input("\n Enter the first name of the user you want to add as a friend from the users list: ")
        user.addFriend(current_user,friend_name)
        input("           Press Enter to go back   ")
        clear()
        my_friends(current_user)

    elif subchoice == '2':
        user.showFriends(current_user)
        input("           Press Enter to go back   ")
        clear()
        my_friends(current_user)
    
    elif subchoice == '3':
        user.showFriends(current_user)
        friend_name = input("\n Enter the first name of your friend, to view their posts: ")
        user.showFriendsPost(current_user, friend_name)
        input("           Press Enter to go back   ")
        clear()
        my_friends(current_user)

    elif subchoice == '0':
        user_dashboard(current_user)
    else:
        clear()
        print("|-------------------------------------|")
        print("           Invalid Choice!             ")
        print("|-------------------------------------|")
        my_friends(current_user)

def group_activities(current_user):
    user = Facebook()
    subchoice = input('\n 1. Create new group \n 2. Show groups \n 3. Join group \n 4. Leave group \n 5. My groups \n 6. Post in a group \n 7. Display group posts \n 8. Chat room \n 0. Back \n \n Enter your choice: ')
    clear()
    if subchoice == '1':
        user.createGroup(current_user)
        input("           Press Enter to go back   ")
        clear()
        group_activities(current_user)

    elif subchoice == '2':
        user.showGroups()
        input("           Press Enter to go back   ")
        clear()
        group_activities(current_user)
    
    elif subchoice == '3':
        user.joinGroup(current_user)
        input("           Press Enter to go back   ")
        clear()
        group_activities(current_user)

    elif subchoice == '4':
        user.leaveGroup(current_user)
        input("           Press Enter to go back   ")
        clear()
        group_activities(current_user)

    elif subchoice == '5':
        user.showMyGroups(current_user)
        input("           Press Enter to go back   ")
        clear()
        group_activities(current_user)

    elif subchoice == '6':
        user.post_in_group(current_user)
        input("           Press Enter to go back   ")
        clear()
        group_activities(current_user)

    elif subchoice == '7':
        user.showGroupPosts(current_user)
        input("           Press Enter to go back   ")
        clear()
        group_activities(current_user)

    elif subchoice == '8':
        user.chatRoom(current_user)
        input("           Press Enter to go back   ")
        clear()
        group_activities(current_user)

    elif subchoice == '0':
        user_dashboard(current_user)
    else:
        clear()
        print("|-------------------------------------|")
        print("           Invalid Choice!             ")
        print("|-------------------------------------|")
        group_activities(current_user)

def register():
    user = Facebook()
    db = Database()
    print("|--------------------------------------------------|")
    print("|--------------------REGISTER----------------------|")
    print("|--------------------------------------------------|")
    email = input('\nPlease provide an unique email id to register : ')
    flag = db.exist_user(email)
    if not user.user_exists(email) and flag == None:
        firstName = input("\nPlease enter your first name: ")
        lastName = input("\nPlease enter your last name: ")
        dob = input("\nPlease enter your date of birth: ")
        bio = input("\nPlease enter few lines about yourself: ")
        password = input("\nPlease enter your password: ")
        user.add_user(firstName, lastName, email, password, dob, bio)
        db.create_user_node(firstName, lastName, email, password, dob, bio)
        db.get_user_node_details(email)
        print("|--------------------------------------------------------------------|")
        print("     You've been successfully signed up! Please login to continue... ")
        print("|--------------------------------------------------------------------|")
        print("\n")
    else:
        clear()
        print("|--------------------------|")
        print("    User already exists     ")
        print("|--------------------------|")
        print("\n")
    return

def exit():
    print("|-------------------------------------|")
    print("   Closing the program...Good Bye ")
    print("|-------------------------------------|")
    sys.exit()

if __name__=='__main__':
    home_screen()
