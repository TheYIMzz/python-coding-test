from collections import deque


def solution(begin, target, words):

    def bfs(start_v, depth):
        visited = set()
        queue = deque()
        queue.append((start_v, depth))

        while queue:
            cur_v, cur_dep = queue.popleft()

            if cur_v == target:
                return cur_dep

            for word in words:
                if word not in visited and is_good(cur_v, word):
                    visited.add(word)
                    queue.append((word, cur_dep + 1))

        return depth

    # 한 글자만 다른지 검사
    def is_good(w1, w2):
        count = 0
        for a, b in zip(w1, w2):
            if a != b:
                count += 1

            if count > 1:
                return False

        return count == 1


    answer = bfs(begin, 0)
    return answer




begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))