class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()
        while True:
            digits  = list(str(n))
            ssum = sum(int(x)**2 for x in digits)
            if ssum == 1:
                return True
            if ssum in sett:
                return False
            sett.add(ssum)
            n = ssum
        