#setting data
objRole1 = {
"Id": 1,
"Name": "System Administrator",
"Parent": 0
}

objRole2 = {
"Id": 2,
"Name": "Location Manager",
"Parent": 1,
}

objRole3 = {
"Id": 3,
"Name": "Supervisor",
"Parent": 2,
}

objRole4 = {
"Id": 4,
"Name": "Employee",
"Parent": 3,
}

objRole5 = {
"Id": 5,
"Name": "Trainer",
"Parent": 3,
}

roles = [objRole1, objRole2,objRole3,objRole4,objRole5]

objUser1 = {
"Id": 1,
"Name": "Adam Admin",
"Role": 1
}

objUser2 = {
"Id": 2,
"Name": "Emily Employee",
"Role": 4
}

objUser3 = {
"Id": 3,
"Name": "Sam Supervisor",
"Role": 3
}

objUser4 = {
"Id": 4,
"Name": "Mary Manager",
"Role": 2
}

objUser5 = {
"Id": 5,
"Name": "Steve Trainer",
"Role": 5
}

users = [
objUser1,
objUser2,
objUser3,
objUser4,
objUser5]
