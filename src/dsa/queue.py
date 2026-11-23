# Temp fix as I fix import problems
# TODO: ADD COMPLEXITY TABLE  AND DESC

try:
    from . import linked_list as ll # this runs outside of the current direcotry
except ImportError:
    import linked_list as ll # this runs when the file itself is executed

class queue:
    """
    Is derived from the linked_list structure.
    Dedicated queue commands are interfaces to the
    linked_list class itself.

    Attributes:
        ll (linked_list): creates its own linked_list.
    """
    def __init__(self):
        self.ll = ll.linked_list()
    
    @property
    def size(self):
        return self.ll.size

    @property
    def top(self):
        return self.ll.head

    def enqueue(self,data):
        """
        Places the data at the end of the queue.

        Args:
            data: The data to be stored.
        Returns:
            bool: True if successful, False otherwise.
        """
        if self.ll.insert_at_tail(data):
            return True
        else:
            return False

    def dequeue(self):
        """
        Pops front-most data out of the queue.

        Returns:
            data: The front-most data after it was popped.
        """
        if self.ll.head == None:
            return None
        
        data = self.ll.head.data
        self.ll.remove_at_head()
        return data

    def peek(self):
        """
        Returns the front-most data without popping it.

        Returns:
            data: front-most data.
        """
        if self.ll.head == None:
            return None

        return self.ll.head.data

    def traverse(self, reverse=False):
        """
        Is an interface to linked_list.traverse().

        Returns:
            data: the elements found in the queue.
        """
        return self.ll.traverse(reverse)

    def update(self):
        """
        Not implemented yet.
        """
        pass

    def is_empty(self):
        if self.ll.size == 0:
            return True
        else:
            return False
