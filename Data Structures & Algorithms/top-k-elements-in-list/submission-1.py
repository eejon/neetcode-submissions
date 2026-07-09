class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # frequency map -> i : freq
        
        bucket = [[] for _ in range(len(nums)+1)] # max freq -> each elem appears len(nums)
        
        for item, freq in count.items():
            bucket[freq].append(item)
        
        ans = []
        # iterate backwards to get most frequent
        for i in range(len(bucket)-1, -1, -1):
            for elem in bucket[i]:
                if (len(ans) != k):
                    ans.append(elem)
        
        return ans
