import math

vector_list = [{'alice':3, 'bob':2, 'mii':4},{'alice':1, 'bob':3},{'alice':3, 'bob':2}]
full_stat_list = {'alice':7, 'bob':7, 'mii':4}
idf_matrix = {'mii': 0.5849625007211562, 'bob': -0.4150374992788438, 'alice': -0.4150374992788438}
tf_matrix = [{'mii': 0.4444444444444444, 'bob': 0.2222222222222222, 'alice': 0.3333333333333333}, {'bob': 0.75, 'alice': 0.25}, {'bob': 0.4, 'alice': 0.6}]

tf_idf_matrix = tf_matrix

for count_i in range(0, len(tf_matrix), 1):
		for key in tf_matrix[count_i].keys():
			tf_idf_matrix[count_i][key] = tf_matrix[count_i][key] * idf_matrix[key]
			
print tf_idf_matrix

