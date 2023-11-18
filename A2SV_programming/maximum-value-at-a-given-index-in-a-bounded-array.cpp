class Solution {
public:
    bool check(long n,long index,long maxSum,long mid){
        long first1 = (n - index)-1;
        long first2 = index-0;
        long remain1 = 0;
        long remain2 = 0;
        long val1 = max((mid - first1),0L+1);
        long val2 = max((mid - first2),0L + 1);
        if (mid - first2 < 1){
            remain2 = abs(mid - first2) + 1;
        }
        if (mid - first1 < 1){
            remain1 = abs(mid-first1) + 1;
        }
        long len1 = first1-remain1 + 1;
        long len2 = first2-remain2 + 1; 
        long sum1 = (len1 * (mid + val1)) / 2;
        long sum2 = (len2 * (mid + val2)) / 2;
        remain1 = remain1 * 1;
        remain2 = remain2 * 1;
        long total = sum1 + sum2 + remain1 + remain2-mid; 
        if (total <= maxSum){
            return true;
        }
        return false;
    }
    int maxValue(int n, int index, int maxSum) {
        long l = 1;
        long r = 1e9 + 1;
        long newn = n;
        long nindex = index;
        long nmaxSum = maxSum;
        while (l < r){
            long mid = (l + r) / 2;
            if (check(newn,nindex,nmaxSum,mid)){
                l = mid + 1;
            }
            else{
                r = mid;
            }
        }
        return r-1;
    }
};