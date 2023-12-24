class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money_on_hand = {5:0, 10:0, 20:0}
        flg = True
        for bill in bills:
            money_on_hand[bill] += 1
            if (bill == 10) and (money_on_hand[5] >= 1):
                money_on_hand[5] -= 1
            elif (bill == 20) and (money_on_hand[10] >= 1) and (money_on_hand[5] >= 1):
                money_on_hand[10] -= 1
                money_on_hand[5] -= 1
            elif (bill == 20) and (money_on_hand[5] >= 3):
                money_on_hand[5] -= 3
            elif (bill == 5):
                pass
            else:
                flg = False
                return flg
        return flg