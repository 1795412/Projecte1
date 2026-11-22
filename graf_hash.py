class GrafHash:

    def __init__(self, ln=None, lv=None, lp=None):
        self._veins = {}
        self._num_arestes = 0

        if ln is not None:
            for x in ln:
                self.insert_vertex(x)

        if lv is not None:
            for i in range(len(lv)):
                n1, n2 = lv[i]
                if lp is None:
                    self.insert_edge(n1, n2)
                else:
                    self.insert_edge(n1, n2, lp[i])

    def insert_vertex(self, x) -> None:
        if x not in self._veins:
            self._veins[x] = {}

    def insert_edge(self, n1, n2, p=1) -> None:
        if n2 not in self._veins[n1]:
            self._num_arestes += 1
        self._veins[n1][n2] = p
        self._veins[n2][n1] = p

    def remove_edge(self, n1, n2) -> None:
        if self.has_edge(n1, n2):
            del self._veins[n1][n2]
            del self._veins[n2][n1]
            self._num_arestes -= 1

    def remove_vertex(self, x) -> None:
        if x in self._veins:
            veins_x = self._veins[x]
            self._num_arestes -= len(veins_x)
            for vei in veins_x:
                del self._veins[vei][x]
            del self._veins[x]

    def has_edge(self, n1, n2) -> bool:
        return n1 in self._veins and n2 in self._veins[n1]

    def weight(self, n1, n2):
        if n1 in self._veins:
            return self._veins[n1].get(n2)

        return None

    def degree(self, x) -> int:
        return len(self._veins[x])

    def num_vertices(self) -> int:
        return len(self._veins)

    def num_edges(self) -> int:
        return self._num_arestes

    def vertices(self):
        return iter(self._veins)

    def edges(self, x):
        return iter(self._veins[x])
