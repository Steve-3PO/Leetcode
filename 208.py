# Implement Trie (Prefix Tree)

# first we need to create nodes with children and a variable to track if its a word within itself
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie:

    # we initialise our Trie Tree with a root of an empty node
    def __init__(self):
        self.root = TrieNode()
        
    # insert a current pointer starting at the root
    def insert(self, word: str) -> None:
        curr = self.root

        # iterating through each character
        for char in word:

            # when the char is not in the children, we insert it
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            # carry on down the tree
            curr = curr.children[char]
        
        # we want to mark that its a new word and ends there
        curr.endofword = True


    # initialise the pointer at the root again
    def search(self, word: str) -> bool:
        curr = self.root

        # going through each character
        for char in word:

            # we return false as soon as we cannot continue
            if char not in curr.children:
                return False
            # move pointer along when there is the correct char
            curr = curr.children[char]

        # if end of word is true we return true
        return curr.endofword

    # initialise at the root
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        # for each characterin the prefix
        for char in prefix:

            # return false if we cant finish the prefix
            if char not in curr.children:
                return False       
            curr = curr.children[char]

        # we only want to know if there are words that start with ""
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
Console

