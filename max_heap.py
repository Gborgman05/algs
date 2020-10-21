# Galen Borgman
# 10/20/2020
# Max Heap

class MaxHeap:
    def __init__(self, heap=[]):
        self.heap = heap
        self.build_heap()

    def build_heap(self):
        """ Bottom up heap construction"""
        pass

    def percolate_up(self, index):
        pass

    def percolate_down(self, index):
        pass

    def insert(self, key):
        pass

    def find_max(self):
        return self.heap[0]

    def del_max(self):
        highest = self.heap[0]
        #TODO delete highest and reorder heap property.
        return highest


def heap_sort(array):
    heap = MaxHeap(array)
    answer = []
    for i in range(len(array)):
        answer.append(heap.del_max())
    return answer


if __name__ == "__main__":
    pass
