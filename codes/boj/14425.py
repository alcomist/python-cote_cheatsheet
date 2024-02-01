import collections

N, M = map(int, input().split())

answers = []

for i in range(N):
    answers.append(input().strip())

questions = []

for i in range(M):
    questions.append(input().strip())


class TrieNode(object):
    def __init__(self, key, terminal=False):
        self.key = key
        self.terminal = terminal
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = TrieNode(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(char)

            curr_node = curr_node.children[char]

        curr_node.terminal = True

    def search(self, string):

        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        return curr_node.terminal


trie = Trie()
for answer in answers:
    trie.insert(answer)


result = 0
for question in questions:
    if trie.search(question):
        result += 1

print(result)
