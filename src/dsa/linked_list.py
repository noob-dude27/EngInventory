# Module by: EZRA FORTUNADO
# under work, will add docs soon

# core operations have now been added
# positional methods are nice to have but not required yet, to be implement as needed

class node:
    def __init__(self, data):
        self.data = data
        self.prev = None # has to be another node
        self.next = None # has to be another node


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # user methods below
    def insert_at_tail(self, data):
        new = node(data)

        if self.head == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

        self.size += 1

        return new

    def insert_at_head(self, data):
        new = node(data)

        if self.head == None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

        self.size += 1

        return new
    
    def remove(self, data):
        current = self.find(data)

        if current == None:
            return False

        if current.prev != None:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next != None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

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
        result = []

        if reverse:
            current = self.tail
            current_position = self.size
            while current != None and current_position > 0:
                result.append(current.data)
                current_position -= 1
                current = current.prev
        else:
            current_position = 0
            current = self.head
            while current != None and current_position < self.size:
                result.append(current.data)
                current_position += 1
                current = current.next

        return result

    # NOT IMPLEMENTED YET
    def insert_at_pos(self, pos, data):
            # implement as needed
            pass
    
    def remove_at(self):
        # implement as needed
        pass

    def get(self, pos):
        # implement as needed
        pass

    def clear(self):
        # implement as needed
        pass