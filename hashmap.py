class MyHashMap:

    def __init__(self, cap=13):
        self._table = [None] * cap
        self._n = 0

    def _hash_function(self, key):
        return key % len(self._table)

    def put(self, key: int, value: int) -> None:
        j = self._hash_function(key)
        self._bucket_put(j, key, value)

        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def _bucket_put(self, j, key, value):
        if self._table[j] is None:
            self._table[j] = []

        bucket = self._table[j]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value
                return

        bucket.append([key, value])
        self._n += 1

    def get(self, key: int) -> int:
        j = self._hash_function(key)
        return self._bucket_get(j, key)

    def _bucket_get(self, j, key):
        if self._table[j] is None:
            return -1

        bucket = self._table[j]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]

        return -1

    def remove(self, key: int) -> None:
        j = self._hash_function(key)
        self._bucket_remove(j, key)

    def _bucket_remove(self, j, key):
        if self._table[j] is None:
            return

        bucket = self._table[j]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                self._n -= 1

                if len(bucket) == 0:
                    self._table[j] = None

                return

    def __len__(self):
        return self._n

    def _resize(self, c):
        taula_antiga = self._table
        self._table = [None] * c
        self._n = 0

        for i in range(len(taula_antiga)):
            bucket = taula_antiga[i]

            if bucket is not None:
                for k in range(len(bucket)):
                    key = bucket[k][0]
                    value = bucket[k][1]
                    j = self._hash_function(key)
                    self._bucket_put(j, key, value)
