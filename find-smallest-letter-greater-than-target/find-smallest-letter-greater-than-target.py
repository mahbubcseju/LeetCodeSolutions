class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smal = 'z'
        flag = 0
        if target != 'z':
            for letter in letters:
                if letter > target:
                    smal = min(smal, letter)
                    flag = 1
        if not flag: 
            for letter in letters:
                if letter != target:
                    smal = min(smal, letter)
        
        return smal
