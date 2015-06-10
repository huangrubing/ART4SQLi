import Levenshtein
import random

executed_set = []
testcase_obj = open('test.txt')
testcase_list = testcase_obj.readlines()
i = 0
init_num = random.randint(1, 74550)
executed_set.append(init_num)
while i<3200:
	candidate_set = []
	j = 0
	while j<10 :
		j=j+1
		candidates = random.randint(1,74550)
		while candidates in executed_set:
			candidates = random.randint(1,74550)
		candidate_set.append(candidates)
	temp_set = []
	max_dis = -1
	max_code = -1
	for code in candidate_set:
		#print code
		for elem in executed_set:
			temp_set.append(Levenshtein.distance(testcase_list[code],testcase_list[elem]))
		#print temp_set
		#print min(temp_set)
		temp_dis = min(temp_set)
		if temp_dis > max_dis:
			max_dis = temp_dis
			max_code = code
	executed_set.append(code)
	i=i+1
for elem_outter in executed_set:
	print testcase_list[elem_outter].strip()
