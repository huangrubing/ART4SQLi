import Levenshtein
import random

executed_set = []
testcase_obj = open('test2.txt')
testcase_list = testcase_obj.readlines()
i = 0
init_num = random.randint(1, 78000)
executed_set.append(init_num)
#print executed_set
while i<20 :
	candidate_set = []
	j = 0
	while j<10 :
		j=j+1
		candidates = random.randint(1,70000)
		while candidates in executed_set:
			candidates = random.randint(1,70000)
		candidate_set.append(candidates)
	Sim_set = []
	max_dis = -1
	max_code = -1
	for code in candidate_set:
		temp_set = []
		for elem in executed_set:
			temp_set.append(Levenshtein.distance(testcase_list[code],testcase_list[elem])
