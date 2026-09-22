class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mult = 1
        addi = 0
        for i in reversed(digits):
            addi += i*mult
            mult*=10
        addi += 1

        return list(str(addi))