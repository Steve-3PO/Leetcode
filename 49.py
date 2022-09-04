# Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # default dict for answer
        ans = collections.defaultdict(list)

        # for each substring in the list of strings, create a list of values for each letter of the alphabet
        for s in strs:
            count = [0] * 26
            
            # for each char in the substring, increase the corresponding list value by taking ord(char) - ord(a)
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # append the dict with s and the count as a tuple as the key, as lists cant be keys
            ans[tuple(count)].append(s)
        return ans.values()