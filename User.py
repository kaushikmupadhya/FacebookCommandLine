from helper import clear

class User:

    def __init__(self, firstName, lastName, email, password, dob, bio, posts, friends, groups):
        self.firstName = firstName
        self.lastName= lastName
        self.email = email
        self.password = password
        self.dob = dob
        self.bio = bio
        self.posts=[]
        self.friends=[]
        self.groups=[]

    def get_firstName(self):
        return(self.firstName)
    def get_lastName(self):
        return(self.lastName)
    def get_email(self):
        return(self.email)
    def get_password(self):
        return(self.password)
    def get_dob(self):
        return(self.dob)
    def get_bio(self):
        return(self.bio)
    def get_posts(self):
        return(self.posts)
    def get_friends(self):
        return(self.friends)
    def get_groups(self):
        return(self.groups)

    def get_user_details(self):
        return(self.firstName,self.lastName,self.email,self.dob,self.bio)
    
    def add_post(self,post):
        self.posts.append(post)
    
    def add_friend(self,friendName):
        self.friends.append(friendName)

    def add_group(self,groupName):
        self.groups.append(groupName)

    def remove_group(self,groupName):
        self.groups.remove(groupName)



