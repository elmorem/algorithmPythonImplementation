def climbStairs(n):
    """
    :type n: int
    :rtype: int
    the number of ways[any n] is going to be the number + ways[n-1]-ways[n-2] 
    """
    ways = [number for number in range(n+1)]
    
    for i in range(n+1):
        if i <= 3:
            ways[i] = i
        else:
            ways[i] = ways[i-1] + ways[i-2]
    return ways[n+1]


# Min cost to climb climbStairs

# def minCostClimbingStairs(cost):
#     """
#     :type cost: List[int]
#     :rtype: int
#     """
#     ds = [0 for n in range(len(cost)+1)]
#     for i in range(2, len(cost)+1):
#         ds[i] = min(ds[i-1] + cost[i-1], ds[i-2] + cost[i-2])
#     return sum(ds)
# cost = [1,2,7]
# print(minCostClimbingStairs(cost))
# cost1 = [1,100,1,1,1,100,1,1,100,1]
# print(minCostClimbingStairs(cost1))
# cost2 = [10, 15,20]
# print(minCostClimbingStairs(cost2))

def rob( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]

def bin_search(num, array):
    i, j = 0, len(array)-1
    found = False
    while i <= j and not found:
        mid = (i+j)//2
        if array[mid] == num:
            found = True
        else:
            if num < array[mid]:
                j = mid -1
            else:
                i = mid + 1
    return found