# Module by: EZRA FORTUNADO
#   core operations have now been added
#   positional methods are nice to have but not required yet, to be implement as needed

class node:
    """
    Represents a single node in a doubly linked list.

    Attributes:
        data: The value stored in the node.
        prev: Reference to the previous node.
        next: Reference to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class linked_list:
    """
    Implements a doubly linked list.

    Attributes:
        head: Reference to the first node.
        tail: Reference to the last node.
        size: Number of nodes currently in the list.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # user methods below
    def insert_at_tail(self, data):
        """
        Inserts a node at the end of the linked list.

        Args:
            data: The value to store in the new node.

        Returns:
            node: The newly created node.
        """
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
        """
        Inserts a node at the beginning of the linked list.

        Args:
            data: The value to store in the new node.

        Returns:
            node: The newly created node.
        """
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
        """
        Removes the first node containing the specified value.

        Args:
            data: The value to search for and remove.

        Returns:
            bool: True if a node was removed, False if no
            matching node was found.
        """
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

        current.prev = None
        current.next = None

        self.size -= 1
        return True

    def find(self, data):
        """
        Searches the linked list for the first matching value.

        Args:
            data: The value to search for.

        Returns:
            node: The first node containing the specified value,
            or None if no matching node exists.
        """
        current = self.head
        while current != None:
            if current.data == data:
                return current

            current = current.next
        
        return None

    def traverse(self, reverse=False):
        """
        Retrieves the values stored in the linked list.

        Args:
            reverse (bool): If True, traverses from tail to head.
            Defaults to False, which traverses from head to tail.

        Returns:
            list: A list containing the values in traversal order.
        """
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

    def clear(self):
        """
        Removes all nodes from the linked list and resets size count.
        """
        self.head = None
        self.tail = None
        self.size = 0

    # NOT IMPLEMENTED YET
    def insert_at_pos(self, pos, data, reverse=False):
        """
        Inserts a new node at the specified position relative 
        to the head or tail node.

        Args:
            pos: The index at which to insert the new node.
            data: The value to store in the new node.

        Returns:
            Not implemented.
        """
        """if reverse:
            current = self.tail
            current_position = self.size
            while current != None and current_position > pos:
                
                current_position -= 1
                current = current.prev
        else:
            current = self.head
            while current != None and current_position < self.size:
                current_position += 1
                current = current.next
        """
         
    def remove_at_pos(self):
        """
        Removes a node at a specified position.

        Returns:
            Not implemented.
        """
        # implement as needed
        pass

    def get_at_pos(self, pos):
        """
        Retrieves the node at the specified position.

        Args:
            pos: The index of the node to retrieve.

        Returns:
            Not implemented.
        """
        # implement as needed
        pass

    def update(self):
        pass

if __name__ == "__main__":
    pass