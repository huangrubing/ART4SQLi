#   Test Case TF-IDF Stat Package
#   Author : C.H. Wang
#   Department of Computer Science at Harbin Engineering University
#   This is the test case statistic script
#   Split test cases by ' and then save each splited test cases into new list

list = ['alice', 'dod', 'alice', 'bob', 'alice', 'tom']
testcase_stat = {list[0]:1}
for count i in range(1, len(list), 1):
    print testcase_stat
    del testcase_stat[list[0]]
        #for count in (1, len(list), 1):
        #print count
            #if list[count] == list[0]:
            #print list[count]
            #testcase_stat[list[count]] = testcase_stat[list[count]] + 1
            #del list[count]
