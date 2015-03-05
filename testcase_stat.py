#   Test Case TF-IDF Stat Package
#   Author : C.H. Wang
#   Department of Computer Science at Harbin Engineering University
#   This is the test case statistic script
#   Split test cases by ' and then save each splited test cases into new list

#list = ['alice', 'dod', 'alice', 'bob', 'alice', 'tom']

def stat(list):
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
