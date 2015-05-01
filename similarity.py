#   Test Case TF-IDF Stat Package
#   Author : C.H. Wang
#   Department of Computer Science at Harbin Engineering University
#   This is the test case feature vector extraction script
#------------------------------------------------------------------

#------------------------------------------------------------------
#	Import part , should import two modules in the toolkit file
import file_operation
import testcase_stat
import os
import json
import math
import random

def feature(PATH):

	#filename = './fuzzdb/attack-payloads/sql-injection/detect/MySQL.fuzz.txt'
	filename = PATH
	test_case_list = file_operation.fileopt_line(filename)
	full_list = file_operation.fileopt_all(filename)
	full_stat_list = testcase_stat.stat_all(full_list)
	test_case_stat_list = testcase_stat.stat(test_case_list)
	tf_matrix = testcase_stat.compute_tf(test_case_stat_list)
	test_case_stat_list = testcase_stat.stat(test_case_list)
	idf_matrix = testcase_stat.compute_idf(test_case_stat_list, full_stat_list)
	tf_idf_list = testcase_stat.compute_tf_idf(tf_matrix, idf_matrix)
	test_case_feature_list = testcase_stat.feature_vector_quantify(tf_idf_list, full_stat_list)

	return test_case_feature_list


def sim2(vector1, vector2):
	norm1 = 0
	norm2 = 0
	inner_product = 0
	for index in vector1.keys():
		norm1 += vector1[index] * vector1[index]
		norm2 += vector2[index] * vector2[index]
		inner_product += vector1[index] * vector2[index]
	return inner_product / (math.sqrt(norm1) * math.sqrt(norm2))

def search_candidate(candidate_set, selected_set, test_case_feature_list):
	sim_inner = 0
	sim_outer = 1
	min_dis = 0
	candidate = -1
	outer_temp = []
	for index_c in candidate_set :
		temp = []
		for index_s in selected_set:
			temp.append(sim2(test_case_feature_list[index_c], test_case_feature_list[index_s]))
		#print index_c
		#print temp
		outer_temp = max(temp)
		#print outer_temp
	#candidate = min(outer_temp
		if outer_temp <= sim_outer:
			sim_outer = outer_temp
			candidate = index_c

	return candidate




def fscs(test_case_feature_list, selected_set):
	
	candidate_set = []
	#selected_set.append(random.randint(0,len(test_case_feature_list)-1))

	for i in range(0,10,1):
		temp = random.randint(0,len(test_case_feature_list)-1)
		while  temp in candidate_set or temp in selected_set:
			temp = random.randint(0,len(test_case_feature_list)-1)
		candidate_set.append(temp)
	##print candidate_set
	candidate = search_candidate(candidate_set, selected_set, test_case_feature_list)
	#selected_set.append(candidate)
	return candidate



		
"""
if __name__=="__main__":

	v1 = {'alice':10, 'bob':3.272, 'tom':1.149, 'jee': 0.324}
	v2 = {'alice':1.17, 'bob':2.272, 'tom':3.149, 'jee': 0.326}
	v3 = {'alice':12, 'bob':2.272, 'tom':0.149, 'jee': 1.324}
	v4 = {'alice':13.17, 'bob':3.272, 'tom':1.149, 'jee': 0.374}
	#candidate_set_test = [0,1,2,3]
	v5 = {'alice':9, 'bob':6.272, 'tom':1.149, 'jee': 2.324}
	v6 = {'alice':1.17, 'bob':13.272, 'tom':11.149, 'jee': 0.724}
	v7 = {'alice':10, 'bob':3.272, 'tom':1.149, 'jee': 1.114}
	v8 = {'alice':1.17, 'bob':2.272, 'tom':3.149, 'jee': 0.192}
	v9 = {'alice':12, 'bob':2.272, 'tom':0.149, 'jee': 0.741}
	v10 = {'alice':13.17, 'bob':3.272, 'tom':1.149, 'jee': 0.669}
	v11 = {'alice':1, 'bob':3.272, 'tom':1.149, 'jee': 0.638}
	v12 = {'alice':1.17, 'bob':2.272, 'tom':3.149, 'jee': 3.324}
	v13 = {'alice':12, 'bob':2.272, 'tom':0.149, 'jee': 2.724}
	v14 = {'alice':13.17, 'bob':3.272, 'tom':1.149, 'jee': 0.384}
	selected_set_test = [4,5]
	test_case_feature_list = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14]
	fscs(test_case_feature_list, selected_set_test)
	#candidate = search_candidate(candidate_set_test, selected_set_test, test_case_feature_list)
	#print candidate

"""

if __name__=="__main__":

	test_case_feature_list = []
	PATH = './test1.txt'
	selected_set = []
	test_case_feature_list = feature(PATH)
	#jsonDumpsFuature = json.dumps(test_case_feature_list, indent=1)
	#with open('jsonDumpsFuature.json', 'w') as f:
		#f.write(jsonDumpsFuature)
	#print jsonDumpsFuature
	selected_set.append(random.randint(0,len(test_case_feature_list)-1))
	#print selected_set
	#selected_set.append(fscs(test_case_feature_list, selected_set))
	#selected_set_length = len(test_case_feature_list) - 10
	selected_set_length = 500
	for i in range(0,selected_set_length,1):
		selected_set.append(fscs(test_case_feature_list, selected_set))
	print selected_set
	#print test_case_feature_list[selected_set[2]]
	file_operation.fileopt_generate(PATH, selected_set)






