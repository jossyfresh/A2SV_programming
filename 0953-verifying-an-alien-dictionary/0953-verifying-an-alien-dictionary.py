class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        left = 0
        len_words = len(words)
        dict = {}
        for index,word in enumerate(order):
            dict[word] = index
        while left < len_words-1:
            min_words = min(len(words[left]),len(words[left+1]))
            letter1 = words[left]
            letter2 = words[left+1]
            for i in range(min_words):
                if dict[letter1[i]] > dict[letter2[i]]:
                    return False
                elif dict[letter1[i]] < dict[letter2[i]]:
                    break
                if len(letter1)-1 > i and len(letter2)-1 == i:
                    return False
            left+=1
        return True
                
            
        