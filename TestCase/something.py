# # list1 = [2,3,8,4,9,5,6]
# # lsit2 = [5,6,10,17,11,2]
# #
# # li = lsit2+list1
# # print(li)
# # for j in range(len(li)):
# #     for i in range(len(li)-1):
# #         if li[i] > li[i + 1]:
# #             a = li[i]
# #             li[i] = li[i + 1]
# #             li[i + 1] = a
# # print(set(li))
# #
# list1 = [2,3,8,4,9,5,6]
# list2 = [5,6,10,17,11,2]
# li = list(set(list1+list2))
#
# # li = (list1+list2)
# print(li)
#
# for i in range(len(li)-1,0,-1):
#     for j in range(i):
#         if li[j] < li[j+1]:
#             a = li[j]
#             li[j] = li[j+1]
#             li[j+1] = a
#
#
# print(li)


a = [('name', 'wang'), ('age', '18')]

print (dict(a))