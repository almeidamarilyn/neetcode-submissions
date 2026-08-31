class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaneds=''.join(char.lower() for char in s if char.isalnum())
        return cleaneds==cleaneds[::-1]