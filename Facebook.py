import sys
from User import User 
from Group import Group
from helper import clear
from Database import Database
import client

usersList = []
groupsList = []
class Facebook:
    def __init__(self):
        self.usersList = usersList
        self.groupsList = groupsList

    def get_usersList(self):
        return(self.usersList)

    def get_groupsList(self):
        return(self.groupsList)

    def add_user(self, firstName, lastName, email, password, dob, bio):
        user = User(firstName, lastName, email, password, dob, bio, "","","")
        self.usersList.append(user)
        return user

    def addgroup(self,groupName):
        self.groupsList.append(groupName)

    def user_exists(self, email):
        for user in self.usersList:
            if user.get_email() == email:
                return True
        return False

    def validate_user(self, email, password):
        for user in self.usersList:
            if user.get_email() == email:
                if user.get_password() == password:
                    return True
                else:
                    return False

    def get_user_details(self, email):
        for user in self.usersList:
            if user.get_email() == email:
                return user.get_user_details()
    
    def display_user_posts(self,email):
        db = Database()
        posts = db.get_post_from_person_node_details(email)
        myPosts = posts.split("\n")
        clear()
        print("|--------------------------------------------|")
        print("|------------------MY POSTS------------------|")
        print("|--------------------------------------------|")
        for post in myPosts:
            print(" ",post)  
        print("|--------------------------------------------|")
    
    def create_post(self,email):
        db = Database()
        print("|--------------------------------------------|")
        print("|-----------------CREATE POST----------------|")
        print("|--------------------------------------------|")
        post = input("\n What is in your mind? \n\n ")
        db.add_post_to_person_node(email,post)
        clear()
        print("|--------------------------------------------|")
        print("       Successfully created the post!!        ")
        print("|--------------------------------------------|")

    def showUsers(self):
        db = Database()
        print("|--------------------------------------------------|")
        print("|------------------LIST OF USERS-------------------|")
        print("|--------------------------------------------------|")
        users = db.show_user_nodes()
        for user in users:
            print("  ",user)
        print("|--------------------------------------------------|")

    def addFriend(self, email, friend_name):
        db = Database()
        if db.get_name(email) == friend_name:
            clear()
            print("|----------------------------------------------------------------|")
            print("         You cannot add yourself to your friends list")
            print("|----------------------------------------------------------------|")
            return
                    
        for name in db.my_friends(email):
            if name == friend_name:
                clear()
                print("|--------------------------------------------|")
                print("          User is already your friend     ")
                print("|--------------------------------------------|")
                return

        db.add_friend_to_person_node(email,friend_name)
        clear()
        print("|----------------------------------------------------------------|")
        print(" ",friend_name," successfully added to your friend list ")
        print("|----------------------------------------------------------------|")
        return

        

    def showFriends(self,email):
        db = Database()
        friends = db.my_friends(email)
        clear()
        print("|--------------------------------------------|")
        print("|-----------------MY FRIENDS-----------------|")
        print("|--------------------------------------------|")
        if(len(friends) != 0):
            for friend in friends:
                print(" ",friend) 
        else :
            print("              YOU HAVE NO FRIENDS             ")
        print("|--------------------------------------------|")

    def is_friend(self, email, friend_name):
        for user in self.usersList:
            if user.get_email() == email:
                if friend_name in user.get_friends():
                    return True
                else:
                    return False

    def showFriendsPost(self,email, friend_name):
        db = Database()
        myFriends = db.my_friends(email)
        if friend_name in myFriends:
            posts = db.get_friends_post_from_person_node_details(friend_name)
            friend_Posts = posts.split("\n")
            clear()
            print("|--------------------------------------------|")
            print("|---------",friend_name,"\'s"" Posts---------|")
            print("|--------------------------------------------|")
            if(len(friend_Posts) != 0):
                for post in friend_Posts:
                    print(" ",post) 
            else:
                print("                 NO POSTS YET            ")
            print("|--------------------------------------------|")
        else:
            clear()
            print("|--------------------------------------------|")
            print("      ",friend_name ,"is not your friend")
            print("|--------------------------------------------|")

    def createGroup(self, email):
        db = Database()
        print("|---------------------------------|")
        print("        Creating new group ")
        print("|---------------------------------|")
        groupName=input("\n Enter the name of the new group : ")
        if groupName in db.show_group_nodes():
            clear()
            print("|---------------------------------------|")
            print("   Group already exist with that name    ")
            print("|---------------------------------------|")
            return
        db.create_group_node(groupName," ",email) 
        clear()
        print("|---------------------------------------|")     
        print("     New group created successfully!     ")
        print("|---------------------------------------|")

    def showGroups(self):
        db = Database()
        groups = db.show_group_nodes()
        if len(groups)>0:
            print("|--------------------------------------------------|")
            print("|-------------------GROUPS LIST--------------------|")
            print("|--------------------------------------------------|")
            for group in groups:
                print(" ",group)
                print("|--------------------------------------------------|")
            return True
        else:
            print("|---------------------------------|")
            print("        No groups present          ")
            print("|---------------------------------|")
            return False

    def joinGroup(self,email):
        db = Database()
        flag = self.showGroups()
        if (flag == False):
            print("|---------------------------------|")
            print("      create a group to join           ")
            print("|---------------------------------|")
            return
        print("|---------------------------------|")
        print("          Joining group            ")
        print("|---------------------------------|")
        groupName=input("\n Enter the name of the group you wish to join : ")

        if groupName in db.my_groups(email):
            clear()
            print("|---------------------------------|")
            print("      Already a group member           ")
            print("|---------------------------------|")
            return

        db.join_group_node(groupName,email)
        print("|------------------------------------------------------------|")
        print("  You are successfully added to ",groupName," group   ")
        print("|------------------------------------------------------------|")

    def showMyGroups(self, email):
        db = Database()
        groups = db.my_groups(email)
        clear()
        if len(groups)>0:
            print("|--------------------------------------------------|")
            print("|------------------- MY GROUPS --------------------|")
            print("|--------------------------------------------------|")
            for group in groups:
                print(" ", group)
                print("|--------------------------------------------------|")
            return True
        else:
            print("|---------------------------------|")
            print("   You are not part of any group          ")
            print("|---------------------------------|")
            return False

    def leaveGroup(self,email):
        db = Database()
        flag = self.showMyGroups(email)
        if (flag == False):
            return
        print("|---------------------------------|")
        print("         Leaving group             ")
        print("|---------------------------------|")
        group=input("\n Enter the name of the group you want to leave : ")
        if group in db.my_groups(email):
            db.leave_group(group,email)
            clear()
            print("|---------------------------------|")
            print("     You have left the group ")
            print("|---------------------------------|")
        else:
            print("|---------------------------------|")
            print("      Not a valid group name           ")
            print("|---------------------------------|")

    def post_in_group(self,email):
        db = Database()
        flag = self.showMyGroups(email)
        if (flag == False):
            return
        print("|---------------------------------|")
        print("       Creating group post         ")
        print("|---------------------------------|")
        print("\n Note: To post the you have to be the member of the group.")
        group_name = input("\n Enter the group name in which you want to post: ")
        group_post = input("\n Enter the post message: ")
        if group_name in db.my_groups(email):
            db.add_post_to_group_node(group_name,email,group_post)
            clear()
            print("|---------------------------------|")
            print("     Created a group post          ")
            print("|---------------------------------|")
            return
        else:
            clear()
            print("|------------------------------------------|")
            print("  You are not a member of the group to post         ")
            print("|------------------------------------------|")
            return
                
        print("|------------------------------------------|")
        print("  There is no such group to create the post        ")
        print("|------------------------------------------|")

    def showGroupPosts(self,email):
        db = Database()
        flag = self.showMyGroups(email)
        if (flag == False):
            return
        print("|---------------------------------|")
        print("           Group posts             ")
        print("|---------------------------------|")
        group_name=input("\n Enter the group name to view the posts :")
        if group_name in db.show_group_nodes():
            posts = db.get_posts_from_group_node_details(group_name)
            groupPosts = posts.split("\n")
            clear()
            print("|--------------------------------------------|")
            print("|---------",group_name,"\'s"" Posts---------|")
            print("|--------------------------------------------|")
            if(len(groupPosts) != 0):
                for post in groupPosts:
                    print(" ",post) 
            else:
                print("                 NO POSTS YET            ")
            print("|--------------------------------------------|")
        else:
            print("|---------------------------------------------|")
            print("  There is no such group to display the posts        ")
            print("|---------------------------------------------|")

    def chatRoom(self,email):
        db = Database()
        print("|---------------------------------|")
        print("        Welcome Chat Room            ")
        print("|---------------------------------|")
        message=input("\n Enter your message :")
        user_message(message)
        chat_message = email + " : " + message
        db.create_chat_message(chat_message)
        print("|---------------------------------|")
        print("             Messages            ")
        print("|---------------------------------|")
        chats = db.show_chat_messages()
        for chat in chats:
            print("  ",chat)
        print("|--------------------------------------------------|")

