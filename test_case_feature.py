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
#------------------------------------------------------------------

#------------------------------------------------------------------
#
#	Init part, this section can be described as the initiation part 
#		of test cases
#	All test cases need to be counted should be loaded in this part
#
#--------------------------------------------------------------------
filename = './fuzzdb/attack-payloads/sql-injection/detect/MySQL.fuzz.txt'
test_case_list = file_operation.fileopt_line(filename)
full_list = file_operation.fileopt_all(filename)full_stat_list = testcase_stat.stat_all(full_list)test_case_stat_list = testcase_stat.stat(test_case_list)

print test_case_list
print full_listprint test_case_stat_listprint full_stat_list
