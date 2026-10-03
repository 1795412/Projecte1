class Node:
    __slots__ = ("valor", "minim", "seguent")

    def __init__(self, valor, minim, seguent):
        self.valor = valor      # Número que guardem.
        self.minim = minim      # Mínim des d'aquí fins al fons.
        self.seguent = seguent  # Referència al node de sota.


class MinStack:

    def __init__(self):
        # Inicialment, la pila està buida: no té cap node al cim.
        self.cim = None

    def push(self, val: int) -> None:
        # Si la pila està buida, el nou valor és el mínim.
        if self.cim is None:
            nou_minim = val

        # Si el nou valor és més petit, passa a ser el mínim.
        elif val < self.cim.minim:
            nou_minim = val

        # Si no, mantenim el mínim que ja teníem.
        else:
            nou_minim = self.cim.minim

        # El nou node apunta al que fins ara era el cim.
        nou_node = Node(val, nou_minim, self.cim)

        # El nou node passa a ser el cim de la pila.
        self.cim = nou_node

    def pop(self) -> None:
        # El node de sota passa a ser el cim.
        self.cim = self.cim.seguent

    def top(self) -> int:
        # Retornem el valor del cim sense treure'l.
        return self.cim.valor

    def getMin(self) -> int:
        return self.cim.minim
