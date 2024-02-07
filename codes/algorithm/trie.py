# Trie (트라이) 알고리즘 구현

class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.word = False


class Trie():
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)

            node = node.children[char]

        node.word = True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


if __name__ == '__main__':

    trie = Trie()
    trie.insert('apple')
    trie.insert('application')
    trie.insert('applause')
    if not trie.search('pple'):
        print('ok')

    if trie.search('apple'):
        print('ok')

    if trie.starts_with('appl'):
        print('ok')
