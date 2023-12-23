class Solution:
    def average(self, salary: List[int]) -> float:
        max_value = max(salary)
        min_value = min(salary)

        val = [x for x in salary if x != max_value and x != min_value]
        return round(float(sum(val)/len(val)),5)