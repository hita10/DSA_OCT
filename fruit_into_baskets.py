class Solution(object):
    def totalFruit(self, fruits):
        counts = {}
        left = 0
        max_fruits = 0
        for right in range(len(fruits)):
            counts[fruits[right]] = counts.get(fruits[right], 0) + 1
            while len(counts) > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    del counts[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits
        