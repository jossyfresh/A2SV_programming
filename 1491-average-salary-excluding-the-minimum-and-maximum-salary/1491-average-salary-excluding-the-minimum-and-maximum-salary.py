class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = float('inf')
        max_salary = 0
        for x in salary:
            max_salary = max(max_salary,x)
            min_salary = min(min_salary,x)
        sum_salary = 0
        for x in salary:
            if x == max_salary or x == min_salary:
                continue
            else:
                sum_salary+=x
        return (sum_salary)/(len(salary)-2)
        