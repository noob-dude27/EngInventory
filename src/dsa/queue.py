# Temp fix as I fix import problems
try:
    from . import linked_list as ll # this runs outside of the current direcotry
except ImportError:
    import linked_list as ll # this runs when the file itself is executed

class queue:
    def __init__(self):
        self.ll = ll.linked_list()
    
    @property
    def size(self):
        return self.ll.size

    @property
    def top(self):
        return self.ll.head

    def enqueue(self,data):
        self.ll.insert_at_tail(data)

    def dequeue(self):
        if self.ll.head == None:
            return None
        
        data = self.ll.head.data
        self.ll.remove_at_head()
        return data

    def peek(self):
        if self.ll.head == None:
            return None

        return self.ll.head.data

    def traverse(self):
        return self.ll.traverse()

    def update_at_index(self):
        pass

    def is_empty(self):
        if self.ll.size == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    qu = queue()
    qu.enqueue(10)
    qu.enqueue(20)
    qu.enqueue(30)
    qu.enqueue(40)