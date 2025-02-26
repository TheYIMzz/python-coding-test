"""
    리스트로 구현하는 힙
      - 자식노드 구하기 공식: 2*i + 1, 2*i + 2
      - 부모노드 구하는 공식: (i-1)/2
        =>  i는 현재 인덱스

    min heap: 부모 노드의 값이 자식 노드의 값보다 작은 트리 형태의 자료구조
    max heap: 부모 노드의 값이 자식 노드의 값보다 큰 트리 형태의 자료구조

        * 형제 노드 간에는 대소 관계가 정해지지 않는다.
        * Root 노드가 가장 큰 or 작은 값을 갖는다.

    리스트에 heapq의 heapify를 사용하여 min heap으로 재구성 => O(N)

    min heap을 pop하면 우선 순위 재배열(Sift down)을 하는데 heap의 최대 높이만큼 한다. => O(logN)
    heappush은 힙의 맨 뒤에 추가 후 우선 순위 재배열(Sift up) => O(logN)

"""
import heapq

min_heap = [5, 3, 9, 4, 1, 2, 6]
print("heapify 전 List: ", min_heap)

# min heapify
heapq.heapify(min_heap)  # 리스트를 min heap으로 재구성
print("min heap으로 재구성 O(N) : ", min_heap)

# min heappop
value = heapq.heappop(min_heap)
print("heappop (dequeue) O(logN): ", min_heap)
print("heappop (dequeue) 꺼낸 값: ", value)

# min heappush
heapq.heappush(min_heap, 1)
print("heappush (enqueue) O(logN): ", min_heap)

print("==========================================================")

max_heap = [5, 3, 9, 4, 1, 2, 6]
print("max heapify 전 List: ", max_heap)

# max heapify
heapq._heapify_max(max_heap)
print("max heapify으로 재구성: ", max_heap)

# max heappop 1
value = heapq._heappop_max(max_heap)
print("heappop (dequeue) O(logN): ", max_heap)
print("max heap pop한 값 ", value)

print("==========================================================")

# max heappop 2
max_heap2 = [5, 3, 9, 4, 1, 2, 6]
max_heap2 = [i * -1 for i in max_heap2]  # max는 push가 없으므로 min heap을 만들어주는 걸 -1을 곱해서 역으로 이용함
print("음수로 바꾼 max heap", max_heap2)
heapq.heapify(max_heap2)  # -1을 곱했기 때문에 음수가 되어 가장 큰 수는 제일 작은 수가 되어 역순으로 정렬
print("음수로 바꾸고 heapify한 max heap", max_heap2)
weight = heapq.heappop(max_heap2)  # 역순으로 정렬한 값 꺼냄
print("음수로 바꾸고 heapify한 max heap", max_heap2)
value = -1 * weight  # 꺼내고 -1 곱해서 양수로 전환
print("max heap pop한 값 양수로 변환 값", value)

print("==========================================================")

# max heappop 3 ( 튜플 사용 )
max_heap3 = [5, 3, 9, 4, 1, 2, 6]
max_heap3 = [(-i, i) for i in max_heap3]
print("튜플 사용한 max heap: ", max_heap3)

heapq.heapify(max_heap3)  # 튜플의 0번째 값으로 정렬
print("heapify: ", max_heap3)

weight, value = heapq.heappop(max_heap3)
print("max heappop으로 튜플 요소 추출", weight, value)
