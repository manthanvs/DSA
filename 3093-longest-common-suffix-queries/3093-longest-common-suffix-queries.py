class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i
               
        word_dict = {}
        word_dict['best'] = global_best_idx

        for idx, word in enumerate(wordsContainer):
            cur = word_dict
            for char in word[::-1]:
                if char in cur:
                    cur = cur[char]

                    best_idx = cur['best']
                    test_word = wordsContainer[best_idx]
                    if len(word) < len(test_word):
                        cur['best'] = idx
                else:
                    cur[char] = {}                   
                    cur = cur[char]
                    cur['best'] = idx
                                        
                
        res = []
        
        for query in wordsQuery:
            cur_idx = global_best_idx
            cur = word_dict
            for char in query[::-1]:
                if char not in cur:
                    break
                else:
                    cur = cur[char]
                    cur_idx = cur['best']
            res.append(cur_idx)
        return res