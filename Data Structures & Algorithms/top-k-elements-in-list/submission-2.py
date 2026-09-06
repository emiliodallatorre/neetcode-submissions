from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies: dict = defaultdict(int)
        answer: list[int] = []

        for num in nums:
            frequencies[num] += 1
        
        top_frequencies: list[int] = sorted(frequencies.values(), reverse=True)[0:k]
        for key in frequencies:
            if frequencies[key] in top_frequencies:
                answer.append(key)
        
        return answer
