from helper import clear

class Group:

    def __init__(self,groupName,groupPosts,groupMembers):
        self.groupName=groupName
        self.groupPosts={}
        self.groupMembers=[]

    def get_groupName(self):
        return(self.groupName)
    def get_groupPosts(self):
        return(self.groupPosts)
    def get_groupMembers(self):
        return(self.groupMembers)

    def add_groupMember(self,memberName):
        self.groupMembers.append(memberName)
    
    def add_post(self,memberName,postMessage):
        groupPosts=[]
        if memberName in self.groupPosts.keys():
            groupPosts=self.groupPosts[memberName]
        groupPosts.append(postMessage)
        self.groupPosts.update({memberName:groupPosts})
    
    def show_post(self,group_member):
        return(self.groupPosts[group_member])
    