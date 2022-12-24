class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        len_arr = len(arr)
        while i < len_arr:
            if arr[i]==0:
                arr.pop()
                arr.insert(i,0)
                i+=2
            else:
                i+=1
        
           
        
                