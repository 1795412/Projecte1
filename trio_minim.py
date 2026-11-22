def minTrioDegree(n: int, edges: list[list[int]]) -> int:
    matriu = []
    for i in range(n + 1):
        matriu.append([False] * (n + 1))
      
    grau = [0] * (n + 1)

    for u, v in edges:
        matriu[u][v] = True  
        matriu[v][u] = True  
        grau[u] += 1         
        grau[v] += 1         

    minim = -1

    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if matriu[a][b]:
                for c in range(b + 1, n + 1):
                    if matriu[a][c] and matriu[b][c]:
                        grau_trio = grau[a] + grau[b] + grau[c] - 6
                        if minim == -1 or grau_trio < minim:
                            minim = grau_trio
    return minim
