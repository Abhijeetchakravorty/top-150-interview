class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
    # Time Complexity: O(L)
    # Space Complexity: O(ALPHABET_SIZE * L * N)
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    # Time Complexity: O(L)
    # Space Complexity: O(ALPHABET_SIZE * L * N)
    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    # Time Complexity: O(P->Length of the prefix)
    # Space Complexity: O(ALPHABET_SIZE * L * N)
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True