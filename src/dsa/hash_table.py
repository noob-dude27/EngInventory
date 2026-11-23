# Module by: EZRA FORTUNADO

# TODO: ADD COMPLEXITY TABLE  AND DESC

# Temp fix as I fix import problems
try:
    from . import linked_list as ll # this runs outside of the current direcotry
except ImportError:
    import linked_list as ll # this runs when the file itself is executed

class hash_table:
    """
    A hash table implementation using separate chaining for collision handling.

    Each bucket is a linked list. Keys are hashed using the DJB2 algorithm
    and mapped to a bucket index using the modulo operator.

    Attributes:
        size (int): Current number of buckets in the hash table.
        buckets (list): List of linked lists used to store key-value pairs.
        load_factor (float): Maximum load factor before resizing is triggered.
        element_count (int): Number of key-value pairs currently stored.
    """

    def __init__(self, size=10, load_factor=0.75):
        """
        Initializes an empty hash table.

        Args:
            size (int): Initial number of buckets. Defaults to 10.
            load_factor (float): Load factor threshold for resizing.
                Defaults to 0.75.

        Raises:
            ValueError: If size is less than 1.
        """
        if size < 1:
            raise ValueError
        self.size = size

        self.buckets = [ll.linked_list() for _ in range(size)]  # nodes go here
        self.load_factor = load_factor
        self.element_count = 0

    def djb2(self, key):
        """
        Generates a hash value for a string key using DJB2.

        Args:
            key (str): String key to hash.

        Returns:
            int: 32-bit hash value.

        Raises:
            TypeError: If key is not a string.
        """
        if type(key) != str:
            raise TypeError

        h = 5381
        for b in key.encode():
            h = ((h << 5) + h + b) & 0xFFFFFFFF # I should reference this
        return h

    def compute_index(self, key):
        """
        Calculates the bucket index for a given key.

        Uses the DJB2 hash value modulo the current table size.

        Args:
            key (str): Key to calculate the index for.

        Returns:
            int: Index of the bucket where the key belongs.
        """
        return self.djb2(key) % self.size

    def insert(self, key, value):
        """
        Inserts a new key-value pair into the hash table.

        Duplicate keys are not inserted. The table resizes when its
        load factor reaches or exceeds the configured threshold.

        Args:
            key (str): Key associated with the value.
            value: Data to store under the given key.

        Returns:
            bool: True if insertion succeeds, False if the key already exists.
        """
        index = self.compute_index(key)
        bucket = self.buckets[index]

        if bucket.find(key, data_index=0):
            return False

        bucket.insert_at_tail([key,value])
        self.element_count += 1

        load = self.element_count / self.size
        if load >= self.load_factor:
            self.resize()

        return True

    def retrieve(self, key):
        """
        Retrieves the value associated with a given key.

        Args:
            key (str): Key associated with the requested value.

        Returns:
            The stored value if the key exists, otherwise None.
        """
        index = self.compute_index(key)
        bucket = self.buckets[index]
        current = bucket.find(key, data_index=0)
        if current is None:
            return None

        return current.data[1]

    def remove(self, key):
        """
        Removes a key-value pair from the hash table.

        Args:
            key (str): Key of the pair to remove.

        Returns:
            bool: True if the pair was removed, False if the key was not found.
        """
        index = self.compute_index(key)
        bucket = self.buckets[index]
        current = bucket.find(key, data_index=0)

        if current is None:
            return False

        status = bucket.remove(current.data)

        if status:
            self.element_count -= 1

        return status

    def peek(self, index=None):
        """
        Views the contents of the hash table without modifying it.

        Args:
            index (int, optional): Specific bucket index to inspect.
                If None, all buckets are returned.

        Returns:
            list: Contents of the selected bucket, or a nested list
                containing the contents of all buckets.
        """
        if index != None:
            return self.buckets[index].traverse()
        else:
            buckets = []
            for bucket in self.buckets:
                buckets.append(bucket.traverse())
            return buckets

    def resize(self):
        """
        Doubles the table capacity and redistributes existing elements.

        Rehashes every existing key using the new table size and places
        each key-value pair into its corresponding new bucket.
        """
        self.size = self.size * 2
        old_buckets = self.buckets
        self.buckets = [ll.linked_list() for _ in range(self.size)]

        for old_bucket in old_buckets:
            current = old_bucket.head

            while current != None:
                next_node =  current.next
                key, value = current.data
                index = self.compute_index(key)
                bucket = self.buckets[index]
                bucket.insert_at_tail(current.data)
                current = next_node

    def clear(self):
        """
        Removes all elements from the hash table.

        Reinitializes all buckets while retaining the current table size.
        Resets the element count to zero.
        """
        self.buckets = [ll.linked_list() for _ in range(self.size)]
        self.element_count = 0

    def update(self, key, new_value):
        """
        Updates the value associated with an existing key.

        Args:
            key (str): Key of the pair to update.
            new_value: New value to associate with the key.
        Returns:
            bool: True if update was successful, False otherwise.
        """
        index = self.compute_index(key)
        bucket = self.buckets[index]
        current = bucket.find(key, data_index=0)

        if current is not None:
            current.data[1] = new_value
            return True
        
        return False

    def contains(self, key):
        """
        Checks whether a value exists in the hash table.

        Searches every bucket for the given value.

        Args:
            value: Value to search for.

        Returns:
            bool: True if the value exists, False otherwise.
        """
        index = self.compute_index(key)
        bucket = self.buckets[index]
        data = bucket.find(key, data_index=0) 

        if data != None:
            return True
        else:
            return False