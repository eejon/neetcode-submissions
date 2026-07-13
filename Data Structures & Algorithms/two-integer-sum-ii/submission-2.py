class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointer
        l = 0
        r = len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if target == sum:
                break
            if sum < target:
                l+=1
            else:
                r-=1
        return [l+1, r+1]