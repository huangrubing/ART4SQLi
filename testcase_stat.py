#   Test Case TF-IDF Stat Package
#   Author : C.H. Wang
#   Department of Computer Science at Harbin Engineering University
#   This is the test case statistic script
#   Split test cases by ' and then save each splited test cases into new list

#list = ['alice', 'dod', 'alice', 'bob', 'alice', 'tom']

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
#vector_list = [{'alice':3, 'bob':2, 'mii':4},{'alice':1, 'bob':3, 'mii':2}]
#testcase_stat = {'alice':4, 'bob':5, 'mii':6}
#-----------------------------------------------------------------------------

def compute_tf(vector_list, testcase_stat):
    tf_matrix = vector_list
#tf = 0.0000
    for count_i in range(0, len(vector_list), 1):
        keys_temp = vector_list[count_i]
        keys_list = keys_temp.keys()
        for stat_key in keys_list:
            tf = (vector_list[count_i][stat_key]) / float(testcase_stat[stat_key])
            tf_matrix[count_i][stat_key] = tf
    return tf_matrix

