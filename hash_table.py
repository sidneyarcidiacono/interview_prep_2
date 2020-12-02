"""Implement a hash table. For fun."""
from linked_list import LinkedList


class HashTable:
    """Create Hash Table class"""

    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [LinkedList()] * self.num_buckets

    def insert(self, keyval):
        hash_result = hash(keyval[0])
        index = hash_result % self.num_buckets
        bucket_ll = self.buckets[index]
        bucket_ll.append(keyval)

    def lookup(self, key):
        hash_output = hash(key)
        index = hash_output % self.num_buckets
        bucket_ll = self.buckets[index]
        result = bucket_ll.find(key)
        return result.data
