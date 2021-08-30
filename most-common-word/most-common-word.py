class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        replaced_characters = ['!', '?', '\'', ',', ';', "."]
        for char in replaced_characters:
            paragraph = paragraph.replace(char, " ")
        paragraph = paragraph.lower().split()
        
        words = {}
        result = 0
        for word in paragraph:
            if word not in banned:
                cnt = words.get(word, 0)
                words[word] = cnt + 1
        words = sorted(words.items(), key=lambda item: -item[1])
        print(words)
        return words[0][0]
        