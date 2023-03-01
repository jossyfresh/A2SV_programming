class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def compete(arr,l,r,tu):
            if l == r:
                if tu:
                    return [arr[l],0]
                else:
                    return [0,arr[l]]
            if tu:
                x = compete(arr,l,r-1,not tu)
                x[0]+=arr[r]
                y = compete(arr,l+1,r,not tu)
                y[0]+=arr[l]
                if x[0] >= y[0]:
                    return x
                else:
                    return y
            else:
                x = compete(arr,l,r-1,not tu)
                x[1]+=arr[r]
                y = compete(arr,l+1,r,not tu)
                y[1]+=arr[l]
                if x[1] >= y[1]:
                    return x
                else:
                    return y
        score = compete(nums,0,len(nums)-1,True)
        if score[0] >= score[1]:
            return True
        return False