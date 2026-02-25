class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}

        for st in strs:
            new = ''.join(sorted(st))
            if new in final:
                final[new].append(st)
            else:
                final[new] = [st]
        return list(final.values())
                    

    class Solution:
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_to_index = {}
    grouped = []
    for st in strs:
        sst = str(sorted(st)) 
        if sst in anagram_to_index:
            grouped[anagram_to_index[sst]].append(st)
        else:
            grouped.append([st])
            anagram_to_index[sst] = len(grouped) - 1
    return grouped

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        dicts = []
        index_to_letter_counts = {}
        for i, s in enumerate(strs):
            new_dict = {}
            for char in s:
                if char in new_dict:
                    new_dict[char] += 1
                else:
                    new_dict[char] = 1
            if new_dict in dicts:
                ind = dicts.index(new_dict)
                final[ind].append(s)
            else:
                dicts.append(new_dict)
                final.append([s])
        return final

            
        
            
