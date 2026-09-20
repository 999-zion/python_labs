def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError("список пуст")
    mi = nums[0]
    ma = nums[0]
    for i in nums:
        if i < mi:
            mi = i
        if i > ma:
            ma = i
    ans = (mi,ma)
    return ans

print(min_max([1.5, 2, 2.0, -3.1]))