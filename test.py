#Unit tesr cases
import exampleData
import userHierarchy

userHierarchy.setRoles(exampleData.roles)
userHierarchy.setUsers(exampleData.users)

import unittest

#Test case 1
#getSubOrdinates(3); // should return [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 5, "Name": "Steve Trainer","Role": 5}]
class testCase1(unittest.TestCase):
    def runTest(self):
        print('Test case 1 - getSubOrdinates(3); // should return [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 5, "Name": "Steve Trainer","Role": 5}]')
        subUser = [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 5, "Name": "Steve Trainer","Role": 5}]
        #Get output of function
        output = userHierarchy.getSubOrdinates(3)
        print("Output")
        print(output)
        assert output == subUser, 'getSubOrdinates(3) should return 2 employees'
        #assert 1 == 1

class testCase2(unittest.TestCase):
    def runTest(self):
        print('Test case 2 - getSubOrdinates(1) // should return [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 3,"Name": "Sam Supervisor","Role": 3}, {"Id": 4,"Name": "Mary Manager","Role": 2}, {"Id": 5, "Name": "Steve Trainer","Role": 5}]')
        subUser = [{"Id": 2,"Name": "Emily Employee","Role": 4}, {"Id": 3,"Name": "Sam Supervisor","Role": 3}, {"Id": 4,"Name": "Mary Manager","Role": 2}, {"Id": 5, "Name": "Steve Trainer","Role": 5}]
        #Get output of function
        output = userHierarchy.getSubOrdinates(1)
        print("Output")
        print(output)
        assert output == subUser, 'getSubOrdinates(1) should return 4 employees'
        #assert 1 == 1

#Build a test suite
suite = unittest.TestSuite()
suite.addTest(testCase1())
suite.addTest(testCase2())


#Run tests
runner = unittest.TextTestRunner()
runner.run(suite)
