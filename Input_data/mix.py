import random
list = []
test_case_obj = open('./test.txt')
test_case_temp = test_case_obj.readlines()
random.shuffle(test_case_temp)
for i in range(1,len(test_case_temp),1):
	print test_case_temp[i-1].strip()


#print test_case_temp[2]
#while test_case_temp :
	#test_case_temp = test_case_temp[:-1]
	#test_case_split = test_case_temp.split(' ')
	#list = list + test_case_split
	#test_case_temp = test_case_obj.readline()
#return list
