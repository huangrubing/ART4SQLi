vector_list = [{'alice':3, 'bob':2, 'mii':4},{'alice':1, 'bob':3, 'mii':2}]
testcase_stat = {'alice':4, 'bob':5, 'mii':6}
#def compute_tf(vector_list, testcase_stat):
tf_matrix = vector_list
#tf = 0.0000
for count_i in range(0, len(vector_list), 1):
    keys_temp = vector_list[count_i]
    keys_list = keys_temp.keys()
    for stat_key in keys_list:
        tf = (vector_list[count_i][stat_key]) / float(testcase_stat[stat_key])
        tf_matrix[count_i][stat_key] = tf
print tf_matrix
