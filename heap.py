class Heap:
    def __init__(self, is_min_heap: bool = True):
        self.heap = []
        self.is_min_heap = is_min_heap

    def parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def left_child_index(self, index: int) -> int:
        return 2 * index + 1

    def right_child_index(self, index: int) -> int:
        return 2 * index + 2

    def swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def compare(self, child: int, parent: int) -> bool:
        if self.is_min_heap:
            return self.heap[child] < self.heap[parent]
        else:
            return self.heap[child] > self.heap[parent]

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index: int):
        while index > 0:
            parent = self.parent_index(index)
            if self.compare(index, parent):
                self.swap(index, parent)
                index = parent
            else:
                break

    def remove(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root_value = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.heapify_down(0)
        return root_value

    def heapify_down(self, index: int):
        size = len(self.heap)
        while True:
            left = self.left_child_index(index)
            right = self.right_child_index(index)
            target = index

            if left < size and self.compare(left, target):
                target = left
            if right < size and self.compare(right, target):
                target = right

            if target == index:
                break

            self.swap(index, target)
            index = target

    def peek(self):
        return self.heap[0] if self.heap else None

heap = Heap(False)
heap.insert(32)
heap.insert(35)
heap.insert(3)
heap.insert(23)
heap.insert(27)
heap.insert(15)
heap.insert(18)
heap.insert(20)
heap.insert(14)
heap.insert(13)
heap.insert(11)
heap.insert(10)
heap.insert(31)
heap.insert(9)
print(heap.heap)
while heap.heap:
    print(heap.remove())
