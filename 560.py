# Works but gets TIME LIMIT EXCEEDED
def subarray_sum_equals_k(nums: list[int], k: int) -> int:
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
def subarraySum(self, nums: List[int], k: int) -> int:
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


def main() -> None:
    print(subarray_sum_equals_k(nums=[1, 1, 1], k=2))
    print(subarray_sum_equals_k(nums=[1, 2, 3], k=3))
    print(subarray_sum_equals_k(nums=[-1, -1, 0], k=0))


if __name__ == '__main__':
    main()
