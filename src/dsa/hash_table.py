# Module by: EZRA FORTUNADO
# TODO: Docstrings needed, will write them soon

# Temp fix as I fix import problems
try:
    from . import linked_list as ll # this runs outside of the current direcotry
except ImportError:
    import linked_list as ll # this runs when the file itself is executed

class hash_table:
    def __init__(self, size=10, load_factor=0.75):
        if size < 1:
            raise ValueError
        self.size = size

        self.buckets = [ll.linked_list() for _ in range(size)]  # nodes go here
        self.load_factor = load_factor
        self.element_count = 0

    def djb2(self, key):
        # uses DJB2 algorithm
        if type(key) != str:
            raise TypeError

        h = 5381
        for b in key.encode():
            h = ((h << 5) + h + b) & 0xFFFFFFFF  # h * 33 + b, kept to 32 bits
        return h

    def comp_index(self, key):
        return self.djb2(key) % self.size

    def insert(self, key, value):
        index = self.comp_index(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current != None:
            if current.data[0] == key:
                return False
            current = current.next

        bucket.insert_at_tail([key,value])
        self.element_count += 1

        load = self.element_count / self.size
        if load >= self.load_factor:
            self.resize()

        return True

    def contains(self, key):
        # Calculate the bucket index
        index = self.comp_index(key)
        # Get the linked list at that index
        bucket = self.buckets[index]
        # Traverse the linked list
        current = bucket.head
        while current != None:
            # Compare keys only
            if current.data[0] == key:
                return current.data[1]
            current = current.next

        return None

    def remove(self, key):
        index = self.comp_index(key)
        bucket = self.buckets[index]
        current = bucket.head

        while current != None:
            if current.data[0] == key:
                status = bucket.remove(current.data)

                if status:
                    self.element_count -= 1

                return status

            current = current.next

        return False

    def peek(self, index=None):
        if index != None:
            return self.buckets[index].traverse()
        else:
            buckets = []
            for bucket in self.buckets:
                buckets.append(bucket.traverse())
            return buckets

    def resize(self):
        self.size = self.size * 2
        old_buckets = self.buckets
        self.buckets = [ll.linked_list() for _ in range(self.size)]

        for old_bucket in old_buckets:
            current = old_bucket.head

            while current != None:
                next_node =  current.next
                key, value = current.data
                index = self.comp_index(key)
                bucket = self.buckets[index]
                bucket.insert_at_tail(current.data)
                current = next_node

    def clear(self):
        self.buckets = [ll.linked_list() for _ in range(self.size)]
        self.element_count = 0

    def update(self, key, new_value):
        # Temporary hack as I forgot to implement the linked_lists, 
        # update function, damn it.

        # Not mandatory but probably a nice to have.
        index = self.comp_index(key)
        # Get the linked list at that index
        bucket = self.buckets[index]
        # Traverse the linked list
        current = bucket.head
        while current != None:
            # Compare keys only
            if current.data[0] == key:
                current.data[1] = new_value
            current = current.next

        return None

if __name__ == "__main__":
    ht = hash_table()
    ht.insert("Hello", "World")
    print(ht.peek())
    ht.update("Hello", "Ezra")
    print(ht.peek())