from collections import deque


def solution(begin, target, words):

    visited = set()
    queue = deque()
    queue.append((begin, 0))

    def check_words(w1, w2):
        count = 0

        for a, b in zip(w1, w2):
            if a != b:
                count += 1

            if count > 1:
                return False
        return count == 1  # 정확히 1글자 차이만 True 반환 (같은 단어되는 것 허용 방지)

    while queue:
        cur_word, depth = queue.popleft()
        print(cur_word, depth)

        if cur_word == target:
            return depth

        for next_word in words:
            if next_word not in visited:
                if check_words(cur_word, next_word):
                    visited.add(next_word)
                    queue.append((next_word, depth + 1))

    return 0

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))