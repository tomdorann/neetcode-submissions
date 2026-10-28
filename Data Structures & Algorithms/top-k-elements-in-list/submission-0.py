from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count number frequencies
        count = Counter(nums)
        return [item for item, count in count.most_common(k)]


