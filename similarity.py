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


def fscs(test_case_feature_list):
	selected_set = []
	candidate_set = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
	selection_seed = -1
	candidate = 0
	while len(selected_set) < test_case_feature_list
	for i in range(0,10,1):
		while selection_seed in selection_seed or in candidate_set:
			selection_seed = random.randint(0,len(test_case_feature_list))
		candidate_set[i] = selection_seed
	candidate = search_candidate(candidate_set, selected_set)
	selected_set.append(candidate)

		

