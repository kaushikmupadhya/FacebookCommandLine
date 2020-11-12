from neo4j import GraphDatabase
from py2neo import Graph, NodeMatcher
# from pypher import Pypher, __

class Database:

    def create_user_node(self,firstName, lastName, email, password, dob, bio):
        graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"), encrypted=False)
        graphdb.session().run("Create (a:User {firstName:$fname, lastName:$lname, userName:$uname, password:$passWord, dateofbirth:$dob, bio:$bio, posts:' ', friends:' ', groups:' '})",fname=firstName,lname=lastName,uname=email,passWord=password,dob=dob,bio=bio)
    
    def get_user_node_details(self,user_name):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        first_name = g.run("MATCH (a:User {userName:$uname}) RETURN a.firstName",uname=user_name).evaluate()
        last_name = g.run("MATCH (a:User {userName:$uname}) RETURN a.lastName",uname=user_name).evaluate()
        dob = g.run("MATCH (a:User {userName:$uname}) RETURN a.dateofbirth",uname=user_name).evaluate()
        bio = g.run("MATCH (a:User {userName:$uname}) RETURN a.bio",uname=user_name).evaluate()
        return first_name,last_name,user_name,dob,bio

    def exist_user(self,user_name):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        result = g.run("MATCH (a:User {userName:$uname}) RETURN EXISTS (a.userName)",uname=user_name).evaluate()
        return result

    def count_user(self):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        result = g.run("MATCH (a:User) RETURN count(a) as count").evaluate()
        return result

    def validate_credentials(self, user_name, password):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        pwd = g.run("MATCH (a:User {userName:$uname}) RETURN a.password",uname=user_name).evaluate()
        if(pwd == password):
            return True
        else:
            return False

    def add_post_to_person_node(self,user_name,message):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        posts = g.run("MATCH (a:User {userName:$uname}) RETURN a.posts",uname=user_name).evaluate()
        if posts == " ":
            posts = message
        else:
            posts = posts + "\n" + message
        graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"), encrypted=False)
        graphdb.session().run("MATCH (a:User {userName:$uname}) SET a.posts=$msg",uname=user_name,msg=posts)

    def get_post_from_person_node_details(self,user_name):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        result=g.run("MATCH (a:User {userName:$uname}) return a.posts",uname=user_name).evaluate()
        return result

    def show_user_nodes(self):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        result=g.run("MATCH (a:User) return a.firstName").data()
        users = []
        n = self.count_user()
        for i in range(0,n):
            users.append(result[i]['a.firstName'])
        return users

    def add_friend_to_person_node(self,user_name,friend):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        friends = g.run("MATCH (a:User {userName:$uname}) RETURN a.friends",uname=user_name).evaluate()
        if friends == " ":
            friends = friend
        else:
            friends = friends + "\n" + friend
        graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"), encrypted=False)
        graphdb.session().run("MATCH (a:User {userName:$uname}) SET a.friends=$friend",uname=user_name,friend=friends)
        graphdb.session().run("MATCH (a:User),(b:User) WHERE a.userName = $uname AND b.firstName = $friendname CREATE (a)-[r:is_friends_with]->(b)",uname=user_name,friendname=friend)

    def my_friends(self,user_name):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        friends = g.run("MATCH (a:User {userName:$uname}) RETURN a.friends",uname=user_name).evaluate()
        myFriends = friends.split("\n")
        return myFriends
    
    def get_name(self,user_name):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        name = g.run("MATCH (a:User {userName:$uname}) RETURN a.firstName",uname=user_name).evaluate()
        return name

    def get_friends_post_from_person_node_details(self,friend_name):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        result=g.run("MATCH (a:User {firstName:$uname}) return a.posts",uname=friend_name).evaluate()
        return result

    def create_group_node(self,groupName,groupPosts,user_name):
        graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"), encrypted=False)
        graphdb.session().run("Create (a:Group {groupName:$gname, post:$post,membersName:$msname})",gname=groupName,post="",msname=user_name)
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        groups = g.run("MATCH (a:User {userName:$uname}) RETURN a.groups",uname=user_name).evaluate()
        if groups == " ":
            groups = groupName
        else:
            groups = groups + "\n" + groupName
        graphdb.session().run("MATCH (a:User {userName:$uname}) SET a.groups=$group",uname=user_name,group=groups)
        graphdb.session().run("MATCH (a:User),(b:Group) WHERE a.userName = $uname AND b.groupName = $groupname CREATE (a)-[r:member_of]->(b)",uname=user_name,groupname=groupName)

    def count_group(self):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        result = g.run("MATCH (a:Group) RETURN count(a) as count").evaluate()
        return result

    def show_group_nodes(self):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        result=g.run("MATCH (a:Group) return a.groupName").data()
        groups = []
        n = self.count_group()
        for i in range(0,n):
            groups.append(result[i]['a.groupName'])
        return groups

    def join_group_node(self,groupName,user_name):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        groups = g.run("MATCH (a:User {userName:$uname}) RETURN a.groups",uname=user_name).evaluate()
        if groups == " ":
            groups = groupName
        else:
            groups = groups + "\n" + groupName
        group_members = g.run("MATCH (a:Group {groupName:$gname}) RETURN a.membersName",gname=groupName).evaluate()
        if group_members == " ":
            group_members = user_name
        else:
            group_members = group_members + "\n" + user_name
        graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"), encrypted=False)
        graphdb.session().run("MATCH (a:User {userName:$uname}) SET a.groups=$group",uname=user_name,group=groups)
        graphdb.session().run("MATCH (a:Group {groupName:$gname}) SET a.membersName=$members",gname=groupName,members=group_members)
        graphdb.session().run("MATCH (a:User),(b:Group) WHERE a.userName = $uname AND b.groupName = $groupname CREATE (a)-[r:member_of]->(b)",uname=user_name,groupname=groupName)

    def my_groups(self,user_name):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        groups = g.run("MATCH (a:User {userName:$uname}) RETURN a.groups",uname=user_name).evaluate()
        myGroups = groups.split("\n")
        return myGroups

    def add_post_to_group_node(self,groupName, user_name, message):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        posts = g.run("MATCH (a:Group {groupName:$gname}) RETURN a.post",gname=groupName).evaluate()
        if posts == " ":
            posts = message
        else:
            posts = posts + "\n" + user_name + " : " + message
        graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"), encrypted=False)
        graphdb.session().run("MATCH (a:Group {groupName:$gname}) SET a.post=$msg",gname=groupName,msg=posts)

    def show_group_members(self, groupName):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        groups = g.run("MATCH (a:Group {groupName:$gname}) RETURN a.groups",gname=groupName).evaluate()
        myGroups = groups.split("\n")
        return myGroups

    def get_posts_from_group_node_details(self,groupName):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        result=g.run("MATCH (a:Group {groupName:$gname}) RETURN a.post",gname=groupName).evaluate()
        return result

    def leave_group(self,group_name,user_name):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        g.run("MATCH (a:Group) WHERE a.groupName=$gname DETACH DELETE a",gname=group_name)
        myGroups = self.my_groups(user_name)
        for group in myGroups:
            if group != group_name:
                groups = group
                groups = group + "/n" 
        graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"), encrypted=False)
        graphdb.session().run("MATCH (a:User {userName:$uname}) SET a.groups=$group",uname=user_name,group=groups)

    def create_chat_message(self,chat_message):
        graphdb=GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "facebook"), encrypted=False)
        graphdb.session().run("Create (c:Chat {message:$msg)",msg=chat_message)

    def show_chat_messages(self):
        graph = Graph('bolt://localhost:7687',username='neo4j',password='facebook')
        g = graph.begin()
        result=g.run("MATCH (a:Chat) return a").data()
        chats = []
        return chats
    
        
