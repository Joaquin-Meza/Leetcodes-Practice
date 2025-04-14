"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList
is a sequence of words beginWord -> s1 -> s2 -> ... -> sk, such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not neet to be in wordList.
- sk == endWord.

Given two words, beginWord and endWord, and a dictionary WordList, return the number of words
in the shortest transformation sequence from beginWord to endWord, or 0 if not such sequence exists.
"""
import collections
from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList) -> int:
    if endWord not in wordList:
        return 0

    nei = collections.defaultdict(list) # Create adjacency list
    wordList.append(beginWord)

    # Build the adjacency list
    for word in wordList:
        for c in range(len(word)):
            pattern = word[:c] + "*" + word[c+1:]
            nei[pattern].append(word)

    visit = set([beginWord])
    queue = deque([beginWord])
    res = 1

    while queue:
        for i in range(len(queue)):
            word = queue.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for neiWord in nei[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        queue.append(neiWord)
        res += 1
    return 0

