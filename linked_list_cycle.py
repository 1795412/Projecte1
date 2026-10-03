class ListNode:
    def __init__(self, x):
        self.val = x      
        self.next = None  


def hasCycle(head: ListNode) -> bool:
    # Les dues referències comencen al primer node.
    lent = head
    rapid = head

    while rapid is not None and rapid.next is not None:
        # El lent avança un node.
        lent = lent.next

        # El ràpid avança dos nodes.
        rapid = rapid.next.next

        # Si coincideixen en el mateix node, hi ha un cicle.
        if lent is rapid:
            return True

    # Si arribem al final de la llista, no hi ha cap cicle.
    return False
