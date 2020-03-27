from doubly_linked_list import DoublyLinkedList

# if buffer is full and a new element is inserted, the oldest element in buffer is
# overwritten with the newest element
# if storage is not full, add to tail and update the current

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # If DLL is empty, add item and instantiate current to head
        if self.current == None:
            self.storage.add_to_tail(item) 
            self.current = self.storage.head
            return
        # If wat capacity in our DLL:
        if len(self.storage) == self.capacity:
            # If current is NOT the tail, we change the current to the next node and update value
            if self.current != self.storage.tail:
                self.current.next.value = item
                self.current = self.current.next
            
            # If current IS the tail, change it to head and update value
            else:
                self.current = self.storage.head
                self.current.value = item
        # If DLL is not at capacity, add new node to the tail and set current to the newly updated node (the tail)
        else:
            self.storage.add_to_tail(item)
            self.current = self.current.next

    def get(self):
        list_buffer_contents = []

        current = self.storage.head # start at front of list
        # loop through each item in list and append value to list_buffer_contents
        while current:
            list_buffer_contents.append(current.value)
            current = current.next # move to next node
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
