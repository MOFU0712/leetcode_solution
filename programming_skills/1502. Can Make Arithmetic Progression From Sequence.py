class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)

        differences = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
        if len(set(differences)) == 1:
            flg = True
        else:
            flg = False
        return flg