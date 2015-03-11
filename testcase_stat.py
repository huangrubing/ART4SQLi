#   Test Case TF-IDF Stat Package
#   Author : C.H. Wang
#   Department of Computer Science at Harbin Engineering University
#   This is the test case statistic script
#   Split test cases by ' and then save each splited test cases into new list

#list = ['alice', 'dod', 'alice', 'bob', 'alice', 'tom']

import math

def stat_all(list):
    testcase_stat = {list[0]:0}
    list2 = []
    for count_i in range(0, len(list), 1):
        if list[count_i] not in testcase_stat.keys():
            testcase_stat[list[count_i]] = 1
        else:
            testcase_stat[list[count_i]] += 1
    return  testcase_stat
#        for count in (1, len(list), 1):
#        print count
#            if list[count] == list[0]:
#            print list[count]
#            testcase_stat[list[count]] = testcase_stat[list[count]] + 1
#            del list[count]


def stat(list):
    vector_list = []
    for count_i in range(0, len(list), 1):
        vector_list.append(stat_all(list[count_i]))
    return vector_list



#def compute_tf(vector_list, testcase_stat):
#    tf_matrix = vector_list
#    for count_i in (0, len(vector_list), 1):
#        keys_list = vector_list[count_i].keys()
#        for stat_key in keys_list:
#            tf = (vector_list[count_i][stat_key]) / (testcase_stat[stat_key])
#            tf_matrix[count_i][stat_key] = tf

#-----------------------------------------------------------------------------
# Input Examples:
# vector_list = [{'alice':3, 'bob':2, 'mii':4},{'alice':1, 'bob':3, 'mii':2}]
# This Input is the statistic result for each test cases 
#-----------------------------------------------------------------------------

def compute_tf(vector_list):
	tf_matrix = vector_list
#tf = 0.0000
	for count_i in range(0, len(vector_list), 1):
		total_num = 0
		keys_temp = vector_list[count_i]
		keys_list = keys_temp.keys()
		count_list = keys_temp.values()
		#print count_list, len(count_list)
		for i in range(0, len(count_list), 1):
			total_num += count_list[i]
		for stat_key in keys_list:
			tf = (vector_list[count_i][stat_key]) / float(total_num)
			tf_matrix[count_i][stat_key] = tf
	return tf_matrix
    #return tf_matrix

def compute_idf(vector_list):
	idf_matrix = vector_list
	tr_list = vector_list
	for count_i in range(0, len(vector_list), 1):
		keys_temp = vector_list[count_i]
		keys_list = keys_temp.keys()
		for stat_key in keys_list:
			count_num = 0
			# Calculate the total number of files which the characters appear
			for i in range (0, len(tr_list), 1):
				if vector_list[count_i][stat_key] in tr_list[i].keys():
					count_num += 1
					# The total file number of characters appear
			idf = math.log((len(vector_list) / (count_num + 1)),2)
			#should be modified not the idf equation
			idf_matrix[count_i][stat_key] = idf
	
	return idf_matrix
	
def compute_tf_idf(tf_matrix, idf_matrix):
	tf_idf = {}
	if len(tf_matrix) == len(idf_matrix):
		for count_i in range(0, len(tf_matrix), 1):
			for key in tf_matrix[count_i] :
				tf_idf = tf_matrix[count_i][key] * idf_matrix[count_i][key]
			tf_idf_matrix.append(tf_idf)
	return tf_idf_matrix

#--------------------------------------------------------------------------------------------------------------------------
# feature_vector_quantify function , this func is used to compute the feature_vector of each test cases 
#
# Sample Input:
# vector_list = [{'alice':0.23, 'bob':0.24, 'mii':0.04},{'alice':0.1, 'bob':0.31, 'mii':0.22},{'mii': 0.32, 'clark': 0.37}]
# This input is the idf_matrix of each test cases
#--------------------------------------------------------------------------------------------------------------------------
	
def feature_vector_quantify( tf_idf_list, testcase_stat):
	idf_matrix = vector_list
	feature_vector_standard = {}
	
	for count_i in range(1, len(tf_idf_list), 1):
		for key in testcase_stat.keys():
			feature_vector_standard[key] = 0
		# Init the feature_vector to [0,0,...,0]
		for key_tfidf in tf_idf_list[count_i].keys():
			feature_vector_standard[key_tfidf] = tf_idf_list[count_i][key_tfidf]
		for key_feature in feature_vector_standard.keys():
			feature_vector.append(feature_vector_standard[key_feature])
			feature_vector_list.append(feature_vector)
	return feature_vector_list
		
	
	
			
				
	

