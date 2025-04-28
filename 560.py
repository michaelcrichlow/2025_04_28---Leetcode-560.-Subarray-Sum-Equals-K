# Works but gets TIME LIMIT EXCEEDED
def subarray_sum_equals_k_00(nums: list[int], k: int) -> int:
    def prefix_sum(l: list[int]):
        for i in range(len(l) - 1):
            l[i + 1] += l[i]
    prefix_sum(nums)
    count = 0
    N = len(nums)
    for i in range(N):
        for j in range(i, N):
            test_val = nums[j] - (nums[i - 1] if i > 0 else 0)
            if test_val == k:
                count += 1
    return count

# This one passes. Runs in O(n) time. Beats 74%
# Got this one from Copilot. Need to study further to understand it.
def subarray_sum_equals_k_01(nums: list[int], k: int) -> int:
    count = 0
    current_sum = 0
    prefix_sum = {0: 1}  # Initialize with 0 to handle subarrays starting from index 0

    for num in nums:
        current_sum += num
        # Check if (current_sum - k) exists in the prefix_sum
        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]
        # Update the prefix_sum map
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

    return count

# 1.) Sliding Window Approach
# This fails because it starts with a fundamentally incorrect assumption:
# There is only one successful sum per "slide" of the right variable to the
# right -- which is not true. There can be negative numbers and zero which 
# added together could give the correct sum, but are ignored in the current approach
# (which just shifts `left` one space to the right as soon as a successful sum is found).
def subarray_sum_equals_k_02(nums: list[int], k: int) -> int:
    left = 0
    right = 1
    N = len(nums)
    count = 0

    while left < N:
        # while invalid
        while sum(nums[left:right]) != k and right < N:
            right += 1
        
        if sum(nums[left:right]) == k:
            count += 1
        left += 1
    return count


# 2.) O(n^2) Approach
# Now that you see that a more thorough exploration of the list is needed, that takes
# us cleanly to an O(n^2) solution:

# for i in range(N):
#     for j in range(i + 1, N + 1):
#         if sum(nums[i:j]) == k:
#             count += 1

# which gives us a 'Time Limit Exceeded' error. So, while now correct
# (this is the "obvious" exhaustive solution) we need a more efficient solution
# to solve it in the allowed time budget. 
def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    N = len(nums)
    count = 0
    for i in range(N):
        for j in range(i + 1, N + 1):
            if sum(nums[i:j]) == k:
                count += 1
    return count


def main() -> None:
    print(subarray_sum_equals_k(nums=[1, 1, 1], k=2))       # 2
    print(subarray_sum_equals_k(nums=[1, 2, 3], k=3))       # 2
    print(subarray_sum_equals_k(nums=[-1, -1, 0], k=0))     # 1
    print(subarray_sum_equals_k(nums=[1, -1, 0], k=0))      # 3


if __name__ == '__main__':
    main()
