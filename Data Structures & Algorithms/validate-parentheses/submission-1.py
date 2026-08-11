class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        arr = []

        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in dictt:
                arr.append(i)
            else:
                if not arr:
                    return False
                if dictt[arr.pop()] != i:
                    return False
        return len(arr) == 0