# Trie (트라이) 알고리즘 구현

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

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

    # 트라이 자료 구조 안에 있는 단어들 모두 출력하는 메소드
    def get_words(self):

        words = []

        def dfs(node, path):

            # 노드가 마지막이라면
            if node.word:
                words.append(''.join(path))

            for k, v in node.children.items():
                dfs(v, path + [k])

        dfs(self.root, [])

        return words


if __name__ == '__main__':

    trie = Trie()
    trie.insert('apple')
    trie.insert('application')
    trie.insert('applause')
    trie.insert('applejuice')
    trie.insert('hello world')

    if not trie.search('pple'):
        print('ok')

    if trie.search('apple'):
        print('ok')

    if trie.starts_with('appl'):
        print('ok')

    print(trie.get_words())

