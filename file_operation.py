#   File Operation Package
#   Author : C.H. Wang
#   Department of Computer Science at Harbin Engineering University
#   This is the test case operation script
#   Split test cases by ' and then save each splited test cases into new list

def fileopt_line(filename):
    list = []
    test_case_obj = open(filename)
    test_case_temp = test_case_obj.readline()
    while test_case_temp :
        test_case_temp = test_case_temp[:-1]  #remove the last char, which is '\n'
        test_case_split = test_case_temp.split(' ')
        #   print test_case_split
        list.append(test_case_split)
        test_case_temp = test_case_obj.readline()
        return list

def fileopt_all(filename):
    list = []
    test_case_obj = open(filename)
    test_case_temp = test_case_obj.readline()
    while test_case_temp :
        test_case_temp = test_case_temp[:-1]  #remove the last char, which is '\n'
        test_case_split = test_case_temp.split(' ')
        #   print test_case_split
        list = list + test_case_split
        test_case_temp = test_case_obj.readline()
        return list

