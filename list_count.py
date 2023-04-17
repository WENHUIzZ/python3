"""输出list里重复的值"""


def findRepeatNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in set(nums):
        if nums.count(i) > 1:
            print(i)


findRepeatNumber([12, 13, 14, 15, 12, 13])
