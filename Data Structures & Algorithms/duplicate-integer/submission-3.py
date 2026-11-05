class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_len:int = len(nums)
        set_len:int = len(set(nums))                  
        len_diff:int = list_len - set_len

        if(len_diff > 0): return True
        return False      
                