class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        se = "".join(char.lower() for char in s if char.isalnum())
        right = len(se) - 1
        while left < len(se)/2:
            if se[left] == se[right]:
                right -= 1
                left += 1
            else:
                return False
        return True