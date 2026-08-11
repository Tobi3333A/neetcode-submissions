from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        left = 0

        for right in range(len(s2)):
            if right < len(s1) - 1:
                continue
            if counter1 == Counter(s2[left:right+1]):
                return True
            left += 1
        return False