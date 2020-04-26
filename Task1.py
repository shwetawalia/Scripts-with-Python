'''
    Task 1 
'''


# def check_ten(n1,n2):
#     if n1 + n2 ==10:
#         result = True
#     else:
#         result = False
#     return result

# print(check_ten(10,1))


'''
    Task 2
'''

# def check_ten(n1,n2):
#     if n1 + n2 ==10:
#         result = True
#     else:
#         result = n1+n2
#     return result

# print(check_ten(10,1))

'''
    Task 3
'''

# def first_upper(mystring):
#     print(mystring[0].upper()+mystring[1:])
    

# first_upper("shweta")


'''
    Task 4
'''

def last_two(mystring):
    if len(mystring)<=2:
        print("Error")
    else:

        print(mystring[-2:])

last_two("shweta")

'''
    Task 5
'''
# def seq_check(nums):
#     for i in range(0,len(nums)-1):
#         if nums[i]==1:
#             if nums[i+1]==2:
#                 if nums[i+2]==3:
#                     return True

#     return False       


# li=[1, 2, 1, 3, 1, 2, 1,2,3,2,4,1,5]
# print(seq_check(li))

'''
    Task 6
'''
# def compare_len(s1,s2):
#     diff=abs(s1-s2)
#     print(diff)
#     # if (diff>=0):
#     #     print(diff)
#     # else:
#     #     pass
# compare_len(13,13)

'''
    Task 7
'''
# def sum_or_sum(mylist):
#     if len(mylist)%2==0:
#         print(sum(mylist))
#     else:
#         print(max(mylist))
# li = [2,4,2,6,17,9,1]
# sum_or_sum(li)