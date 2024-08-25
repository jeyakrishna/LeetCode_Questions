class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        if target == arr:
            return True
        
        if len(target) != len(arr):
            return False
        
        counts = {}
        for i in range(len(target)):
            counts[target[i]] = counts.get(target[i], 0) + 1
            counts[arr[i]] = counts.get(arr[i], 0) - 1
            # if counts[arr[i]] == 0:
            #     del counts[arr[i]]
        
        for _, v in counts.items():
            if v != 0:
                return False
            
        
        return True