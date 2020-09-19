# https://leetcode.com/problems/unique-morse-code-words/discuss/850038/Python-solution-using-list-comprehension

def uniqueMorseRepresentations(self, words: List[str]) -> int:
        def transformation(words):
            trans = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

            transformations = set()
            for word in words:
                transformation = "".join([trans[ord(x) - 97] for x in word])
                transformations.add(transformation)

            return len(transformations)

        return transformation(words)

