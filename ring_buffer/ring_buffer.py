from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if there are no nodes in the doubly linked list
        if not self.storage.head:
            self.storage.add_to_head(item)
        else:
            self.storage.add_to_tail(item)
        # elif len(self.storage) > self.capacity:
        #     self.storage.add_to_tail(item)
        # else:
        #     self.storage.remove_from_tail()
        #     self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # if the storage is empty, return empty contents
        if self.storage.head.value is None:
            return list_buffer_contents
        else:
            start = self.storage.head
            while start is not None:
                list_buffer_contents.append(start.value)
                start = start.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

rb = RingBuffer(5)
rb.append(1)
rb.append(9)
rb.append(7)
print(rb.storage.length)
print(rb.storage.head.next.value)
print(rb.get())
print(rb.capacity)

