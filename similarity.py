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

	filename = './fuzzdb/attack-payloads/sql-injection/detect/MySQL.fuzz.txt'
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
	sim_inner = 1
	sim_outer = 0
	min_dis = 0
	candidate = -1
	for index_c in candidate_set :
		for index_s in selected_set:
			temp = sim2(test_case_feature_list[index_c], test_case_feature_list[index_s])
			#print temp
			if  temp <= sim_inner:
				min_dis = temp
				#print min_dis
		#print min_dis
		if min_dis >= sim_outer:
			sim_outer = min_dis
			candidate = index_c 
			#print candidate
	return candidate




def fscs(test_case_feature_list):
	selected_set = [5]
	candidate_set = []
	for i in range(0,10,1):
		temp = random.randint(0,len(test_case_feature_list)-1)
		while  temp in candidate_set:
			temp = random.randint(0,len(test_case_feature_list)-1)
		candidate_set.append(temp)
	print candidate_set
	candidate = search_candidate(candidate_set, selected_set, test_case_feature_list)
	selected_set.append(candidate)
	print selected_set



		

if __name__=="__main__":

	v1 = {'alice':10, 'bob':3.272, 'tom':1.149}
	v2 = {'alice':1.17, 'bob':2.272, 'tom':3.149}
	v3 = {'alice':12, 'bob':2.272, 'tom':0.149}
	v4 = {'alice':13.17, 'bob':3.272, 'tom':1.149}
	#candidate_set_test = [0,1,2,3]
	v5 = {'alice':9, 'bob':6.272, 'tom':1.149}
	v6 = {'alice':1.17, 'bob':13.272, 'tom':11.149}
	v7 = {'alice':10, 'bob':3.272, 'tom':1.149}
	v8 = {'alice':1.17, 'bob':2.272, 'tom':3.149}
	v9 = {'alice':12, 'bob':2.272, 'tom':0.149}
	v10 = {'alice':13.17, 'bob':3.272, 'tom':1.149}
	v11 = {'alice':10, 'bob':3.272, 'tom':1.149}
	v12 = {'alice':1.17, 'bob':2.272, 'tom':3.149}
	v13 = {'alice':12, 'bob':2.272, 'tom':0.149}
	v14 = {'alice':13.17, 'bob':3.272, 'tom':1.149}
	#selected_set_test = [4,5]
	test_case_feature_list = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14]
	fscs(test_case_feature_list)
	#candidate = search_candidate(candidate_set_test, selected_set_test, test_case_feature_list)
	#print candidate