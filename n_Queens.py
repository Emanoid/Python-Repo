'''Eight Queens: Write an algorithm to print all ways of arranging 
eight queens on an 8x8 chess board so that none of them share the same
 row, column, or diagonal. In this case, "diagonal" means all diagonals, 
 not just the two that bisect the board'''
N = 5

Queens = []

def generate_grid(i,j,accum):
    accum.append((i,j))
    if j+1 <= N:        
        return generate_grid(i,j+1,accum)
    if i+1 <= N:
        return generate_grid(i+1,1,accum)
    else:
        return accum
#print(generate_grid(1,1,[]))

def udiagonal(a,b,n,c,blocked):
    if c < n:
        a += 1
        b += 1
        blocked.append((a,b))
        udiagonal(a,b,n,c+1,blocked)
def ddiagonal(a,b,n,c,blocked):
    if c < n:
        a -= 1
        b -= 1
        blocked.append((a,b))
        ddiagonal(a,b,n,c+1,blocked)
def nudiagonal(a,b,n,c,blocked):
    if c < n:
        a -= 1
        b += 1
        blocked.append((a,b))
        nudiagonal(a,b,n,c+1,blocked)
def nddiagonal(a,b,n,c,blocked):
    if c < n:
        a += 1
        b -= 1
        blocked.append((a,b))
        nddiagonal(a,b,n,c+1,blocked)

def lrud(x,y,c,grid,blocked):
    if c < len(grid):
        if grid[c][0] == x or grid[c][1] == y:
            blocked.append(grid[c])
        lrud(x,y,c+1,grid,blocked)
def generate_blocked(posn):
    grid = generate_grid(1,1,[])
    x = posn[0]
    y = posn[1]
    a = x
    b = y
    blocked = []
    udiagonal(a,b,N-x,0,blocked)
    ddiagonal(a,b,N-x,0,blocked)
    nudiagonal(a,b,N-x,0,blocked)
    nddiagonal(a,b,N-x,0,blocked)
    lrud(x,y,0,grid,blocked)
    return blocked

#print(generate_blocked((8,8)))

def itergrid(i,L,posn,blocked,potential):
    if i < len(L):
        if L[i][0] == posn[0]+1 and L[i] not in blocked:
            potential.append(L[i])
        return itergrid(i+1,L,posn,blocked,potential)
    else:
        return potential
def generate_path(posn,blocked):
    grid = generate_grid(1,1,[])
    return itergrid(0,grid,posn,blocked,[])

#print(generate_path((3,5)))

grid = generate_grid(1,1,[])[:N]
def place_queen(posn,c,unvisited,blocked,q):
    global Queens
    if c <= N:
        Queens.append(posn)
        unvisited.remove(posn)
        for i in generate_blocked(posn):
            blocked.append(i)
        pot = generate_path(posn,blocked)
        for i in pot:
            unvisited.append(i)
        if pot != []:
            return place_queen(pot[0],pot[0][0]+1,unvisited,blocked,q)
        else:
            if len(unvisited) == 0:
                if q + 1 < N:
                    q += 1
                    unvisited.append(grid[q])
                    Queens = []
            if len(unvisited) != 0:
                posn = unvisited[len(unvisited)-1]
                for i in Queens:
                    if i[0] >= posn[0]:
                        Queens.remove(i)
                blocked = []
                for i in Queens:
                    for a in generate_blocked(i):
                        blocked.append(a)
                return place_queen(posn,posn[0]+1,unvisited,blocked,q)
    else:
        Queens.append(posn)
        return Queens
        
#############################################
#Recursive Implementation of place_queen
def foriingen(c,L,blocked):
    if c < len(L):
        blocked.append(L[c])
        foriingen(c+1,L,blocked)

def foriinqueens(c,L,posn):
    global Queens
    if c > len(L):
        if L[c][0] >= posn[0]:
            Queens.remove(L[c])
        foriinqueens(c+1,L,posn)

def foriinqueens2(c,L,blocked):
    global Queens
    if c < len(L):
        L = generate_blocked(L[c])
        foriingen(0,L,blocked)
        foriinqueens2(c+1,L,blocked)

def rplace_queen(posn,c,unvisited,blocked,q):
    global Queens
    if c <= N:
        Queens.append(posn)
        unvisited.remove(posn)
        L = generate_blocked(posn)
        foriingen(0,L,blocked)
        pot = generate_path(posn,blocked)
        foriingen(0,pot,unvisited)
        if pot != []:
            return rplace_queen(pot[0],pot[0][0]+1,unvisited,blocked,q)
        else:
            if len(unvisited) == 0:
                if q + 1 < N:
                    q += 1
                    unvisited.append(grid[q])
                    Queens = []
            if len(unvisited) != 0:
                posn = unvisited[len(unvisited)-1]
                foriinqueens(0,Queens,posn)
                blocked = []
                foriinqueens2(0,Queens,blocked)
                return rplace_queen(posn,posn[0]+1,unvisited,blocked,q)
    else:
        Queens.append(posn)
        return Queens

#print(rplace_queen((1,1),1,[(1,1)],[],0))
##################################################################
def place_queens(n,accum):
    global Queens, grid
    if n < N:
        L = place_queen(grid[n],1,[grid[n]],[],n)
        accum.append(L)
        Queens = []
        return place_queens(n+1,accum)
    else:
        accum.remove(None)
        res = [] 
        [res.append(x) for x in accum if x not in res] 
        return res

for i in place_queens(0,[]):
    print(i)