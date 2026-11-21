# Module by: EZRA FORTUNADO
# under work, will add docs soon

class node:
    def __init__(self, data):
        self.data = data
        self.previous = None # has to be another node
        self.next = None # has to be another node


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # user methods below
    def insert(self, value):

        new = node(value)

        if self.head == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.previous = self.tail
            self.tail = new

        self.size += 1

        return new
    
    def remove(self, data):
        current = self.find(data)

        if current == None:
            return False

        if current.previous != None:
            current.previous.next = current.next
        else:
            self.head = current.next

        if current.next != None:
            current.next.previous = current.previous
        else:
            self.tail = current.previous

        self.size -= 1
        return True

    def find(self, data):
        current = self.head
        while current != None:
            if current.data == data:
                return current

            current = current.next
        
        return None

    def traverse(self, reverse=False):
        if reverse:
            current = self.tail
            while current != None:
                print(current.data, end=" <- ")
                current = current.previous
        else:
            current = self.head
            while current != None:
                print(current.data, end=" -> ")
                current = current.next