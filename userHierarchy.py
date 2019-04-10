#python 2.7

#initiate dataFrames
roles = []
users = []

#functions to set global dataFrames
def setRoles (r):
    global roles
    roles = r

def setUsers(u):
    global users
    users = (u)

#function to get direct subordinate roles under a given roleId
def getDirectSubRole(roleId):
    #function to provide to filter function
    def f(r): return r.get('Parent') == roleId
    return(filter(f, roles))


#function to get all subordinate roles under a given roleId
def getSubRole(roleId):
    #list of sub roles
    sub = []
    #function to get direct subordinates, append to sub list, then recursively get child subordinates
    def traverseRoleTree(roleId):
        directSub = getDirectSubRole(roleId)
        sub.extend(directSub)
        for i in range(len(directSub)):
            thisId = directSub[i].get("Id")
            traverseRoleTree(thisId)
    traverseRoleTree(roleId)
    return(sub)

#function to get subordinate users under a given userId
def getSubOrdinates(userId):
    #list of sub users
    sub = []
    #get role of given userId
    #function to provide to filter function
    def userFilter(u): return u.get('Id') == userId
    thisUser = filter(userFilter, users)[0]

    userRole = thisUser.get('Role')
    #get all subordinate roles user this role
    subRoles = getSubRole(userRole)
    #turn into a list of ids for quicker searching
    subRoleId = []
    for i in range(len(subRoles)):
        subRoleId.append(subRoles[i].get('Id'))
    #find users with these roles
    #filter function
    def userRoleFilter(u): return u.get('Role') in subRoleId
    return(filter(userRoleFilter,users))
