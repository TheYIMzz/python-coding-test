class ListNode:
    def __init__(self, val = 0, prev_node = None, next_node = None):
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node

class BrowserHistory:
    def __init__(self, homepage):
        self.head = self.current = ListNode(val=homepage) # head와 현재 노드를 초기화 (같은 인스턴스를 참조)

    def visit(self, url):
        self.current.next = ListNode(val=url, prev_node=self.current)  # 현재 노드의 다음 노드에 새 방문 페이지(노드)를 저장
        self.current = self.current.next  # 현재 노드의 다음 노드를 가리킨다.
        return None  # 문제에서 visit 시 None 리턴

    def back(self, step):
        while step > 0 and self.current.prev_node is not None:  # step이 0 and None이 아닐 때 까지 이동 (이전 노드가 없는지 체크까지)
            step -= 1
            self.current = self.current.prev_node  # 한칸 앞으로 이동
        return self.current.val  # 현재 노드의 값 (url) 반환

    def forward(self, step):
        while step > 0 and self.current.next_node is not None:  # step이 0 and None이 아닐 때 까지 이동 (다음 노드가 없는지 체크까지)
            step -= 1
            self.current = self.current.next_node
        return self.current.val  # 현재 노드의 값 (url) 반환


browser_history = BrowserHistory("leetcode.com")
browser_history.visit("google.com")
browser_history.visit("facebook.com")
browser_history.visit("youtube.com")
browser_history.back(1)
browser_history.back(1)
browser_history.forward(1)
browser_history.visit("linkedin.com")
browser_history.forward(2)
browser_history.back(2)
browser_history.back(7)