from collections import deque


def solution(begin, target, words):

    def bfs(begin, depth):
        visited = set()
        queue = deque()

        queue.append((begin, depth))

        while queue:
            cur_v, cur_depth = queue.popleft()
            print(cur_v, cur_depth)
            if target == cur_v:
                return cur_depth

            for word in words:
                if word not in visited and is_good(cur_v, word):
                    visited.add(word)
                    queue.append((word, cur_depth + 1))

        return 0

    # 한글자만 다른지 검사 함수
    def is_good(w1, w2):
        count = 0
        for a, b in zip(w1, w2):
            if a != b:
                count += 1

            if count > 1:
                return False

        return count == 1  # 정확히 1글자 차이만 True 반환 (같은 단어되는 것 허용 방지)

    return bfs(begin, 0)




begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))