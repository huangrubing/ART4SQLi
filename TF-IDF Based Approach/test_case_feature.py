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

#------------------------------------------------------------------
#
#	Init part, this section can be described as the initiation part 
#		of test cases
#	All test cases need to be counted should be loaded in this part
#
#-------------------------------------------------------------------
filename = './Input_data/test.txt'
#This part should be replaced as user input or configure files

test_case_list = file_operation.fileopt_line(filename)
full_list = file_operation.fileopt_all(filename)
full_stat_list = testcase_stat.stat_all(full_list)
test_case_stat_list = testcase_stat.stat(test_case_list)
json.dump(full_stat_list, open('./statistics/full_stat_list.json', 'w'))
json.dump(test_case_stat_list, open('./statistics/test_case_stat_list.json', 'w'))
#-------------------------------------------------------------------
#	test_case_list is the list stored the test cases read from files
#	Sample : [
#				['alice', 'dod', 'alice', 'bob', 'alice', 'tom'],
#			 	['alice', 'dod', 'alice', 'bob', 'alice', 'tom']
#			 ]
#
#	full_list is the total list without split
#	full_stat_list is used to stat full list
#	test_case_stat_list is the split test cases list statistic list
#
#-------------------------------------------------------------------
#print test_case_stat_list

tf_matrix = testcase_stat.compute_tf(test_case_stat_list)
#computing tf value and store in tf_matrix 
#print tf_matrix

#Important this place
# In this place we should recompute the test_case_stat_list value
# If not the consequence will go wrong

test_case_stat_list = testcase_stat.stat(test_case_list)

#print test_case_stat_list
# Recompute the test_case_stat_list and then compute the idf value

idf_matrix = testcase_stat.compute_idf(test_case_stat_list, full_stat_list)

#print idf_matrix

#combine tf_matrix and idf_matrix
#Compute tf_idf_list

tf_idf_list = testcase_stat.compute_tf_idf(tf_matrix, idf_matrix)

#print tf_idf_list

#Put them into feature vector and store in 
#test_case_feature_list
#----------------------------------------------------------------------------------------------
test_case_feature_list = testcase_stat.feature_vector_quantify(tf_idf_list, full_stat_list)
#----------------------------------------------------------------------------------------------
json.dump(test_case_feature_list, open('./statistics/test_case_feature.json', 'w'))
#demoDictList is the value we want format to output
#jsonDumpsTFIDF = json.dumps(tf_idf_list, indent=1)
#--------------------------------------------------------------------
#jsonDumpsFuature = json.dumps(test_case_feature_list, indent=1)
#json.dump(test_case_feature_list, open('./feature_list.json', 'w'))
#--------------------------------------------------------------------
#print jsonDumpsTFIDF
##print jsonDumpsFuature




#print "-------------------------------------"
#print test_case_list
#print full_list

#print full_stat_list
