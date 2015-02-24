#This is the test case operation script

test_case_obj = open('oracle.fuzz.txt')
test_case_temp = test_case_obj.readline()
test_case_temp = test_case_temp[:-1]  #remove the last char, which is '\n'
test_case_split = test_case_temp.split(' ')
print test_case_split
