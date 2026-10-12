class Solution:
    def longestSubarray(self, arr, k):
        prefix_map = {0: -1}
        running_sum = 0
        max_len = 0
        for i in range(len(arr)):
            running_sum += arr[i]
            if (running_sum - k) in prefix_map:
                max_len = max(max_len, i - prefix_map[running_sum - k])
            if running_sum not in prefix_map:
                prefix_map[running_sum] = i
        return max_len