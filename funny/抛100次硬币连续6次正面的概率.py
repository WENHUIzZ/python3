import random

numberOfStreaks = 0
# for experimentNumber in range(10000):
#     # 以上第一部分，试验重复10000次以降低单次试验结果的偶然性
#
#     _list = []
#     for t in range(100):
#         _list.append(random.randint(0, 1))
#         check = 0
#
#     # 以上第二部分，生成一个包含百次硬币投掷结果的列表，以1代表正面，0代表反面
#
#         while check <= 94:
#             if _list[check:check + 6] == [1, 1, 1, 1, 1, 1]:
#                 numberOfStreaks += 1
#                 check += 6
#
#             elif _list[check:check + 6] == [0, 0, 0, 0, 0, 0]:
#                 numberOfStreaks += 1
#                 check += 6
#
#             else:
#                 check += 1
#
# print(f'概率约为: {numberOfStreaks/100 :.5f}')
for experimentNumber in range(10000):
    list2 = []
    for t in range(100):
        list2.append(random.randint(0, 1))

    # 以上第二部分，生成一个包含百次硬币投掷结果的列表，以1代表正面，0代表反面
    check = 0
    while check <= 94:
        if list2[check:check + 6] == [1, 1, 1, 1, 1, 1]:
            numberOfStreaks += 1
            check += 6

        elif list2[check:check + 6] == [0, 0, 0, 0, 0, 0]:
            numberOfStreaks += 1
            check += 6

        else:
            check += 1

print(f'概率约为: {numberOfStreaks / 100 /10000 :.5f}')
