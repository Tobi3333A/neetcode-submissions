class Solution:
    def isValid(self, s: str) -> bool:
        dictt = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        arr = []

        for i in s:
            if i in dictt:
                arr.append(i)
            else:
                if not arr:
                    return False
                if dictt[arr.pop()] != i:
                    return False
        return len(arr) == 0