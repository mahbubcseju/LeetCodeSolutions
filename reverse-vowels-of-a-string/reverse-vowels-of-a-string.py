class Solution:
    def reverseVowels(self, s: str) -> str:
        def is_vowel(char):
            return char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
            
        s = list(s)
        arr = [char for char in s if is_vowel(char)]
        
        ptr = len(arr) - 1
        for i in range(len(s)):
            if is_vowel(s[i]):
                s[i] = arr[ptr]
                ptr -= 1
        
        return ''.join(s)
        