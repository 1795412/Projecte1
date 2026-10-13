LLIURE = "L"
OCUPAT = "O"
ESBORRAT = "B"


class MyHashMap:

    def __init__(self, cap=13):
        self._table = []

        for i in range(cap):
            self._table.append([None, None, LLIURE])

        self._n = 0

    def _hash_function(self, key):
        return key % len(self._table)

    def _find(self, key):
        inici = self._hash_function(key)

        for i in range(len(self._table)):
            pos = (inici + i) % len(self._table)
            estat = self._table[pos][2]

            if estat == LLIURE:
                return None

            if estat == OCUPAT:
                if self._table[pos][0] == key:
                    return pos

        return None

    def put(self, key: int, value: int) -> None:
        pos = self._find(key)

        if pos is not None:
            self._table[pos][1] = value
            return

        inici = self._hash_function(key)

        for i in range(len(self._table)):
            pos = (inici + i) % len(self._table)
            estat = self._table[pos][2]

            if estat != OCUPAT:
                self._table[pos] = [key, value, OCUPAT]
                self._n += 1

                if self._n > len(self._table) // 2:
                    self._resize(2 * len(self._table) - 1)

                return

    def get(self, key: int) -> int:
        pos = self._find(key)

        if pos is None:
            return -1

        return self._table[pos][1]

    def remove(self, key: int) -> None:
        pos = self._find(key)

        if pos is None:
            return

        self._table[pos] = [None, None, ESBORRAT]
        self._n -= 1

    def __len__(self):
        return self._n

    def _resize(self, c):
        taula_antiga = self._table
        self._table = []

        for i in range(c):
            self._table.append([None, None, LLIURE])

        self._n = 0

        for i in range(len(taula_antiga)):
            if taula_antiga[i][2] == OCUPAT:
                key = taula_antiga[i][0]
                value = taula_antiga[i][1]
                self.put(key, value)
