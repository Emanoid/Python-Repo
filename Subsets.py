'''Power Set: Write a method to return all subsets of a set.'''

def checksame(a,b):
    lent = len(a)
    accum = []
    for i in a:
        if i in b:
            accum.append(True)
        else:
            accum.append(False)
    return False not in accum and lent == len(accum)

def removesame(L):
    accum = []
    for a in L:
        accum.append(a)
        K = L[0:]
        K.remove(a)
        for b in K:
            if checksame(a,b) == True:
                L.remove(b)
    return accum

def permute(n,L):
    accum = []
    p = []
    for i in L:
        p.append(i)
        K = L[0:]
        K.remove(i)
        v = []
        for u in range(0,n-1):
            v.append(u)
        while v[len(v)-1] < len(K):
            for c in v:
                p.append(K[c])
            accum.append(p)
            p = [i]
            lent = v[0] + 1
            v = []
            for d in range(0+lent,n-1+lent):
                v.append(d)
        p = []
    return removesame(accum)

def gen_subsets(L):
    n = len(L)
    accum = [[]]
    for i in L:
        accum.append([i])
    if len(L) > 1:
        for i in range(2,n+1):
            for a in permute(i,L):
                accum.append(a)
    return accum
        
#print(gen_subsets(['a1','a2','a3']))

########################################################################
#Recursive:
def rchecksame(i,c,a,b,accum,lent):
    if i in b:
        accum.append(True)
    if i not in b:
        accum.append(False)
    if c == len(a):
        return False not in accum and lent == len(accum)
    i = a[c]
    return rchecksame(i,c+1,a,b,accum,lent)

def checker(L,K,a,b,c):
    if rchecksame(a[0],1,a,b,[],len(a)) == True:
        L.remove(b)
    if c < len(K):
        b = K[c]
        checker(L,K,a,b,c+1) 

def rremovesame(L,accum,a,c):
    accum.append(a)
    K = L[0:]
    K.remove(a)
    checker(L,K,a,K[0],1)
    if c < len(L):
        return rremovesame(L,accum,L[c],c+1)
    else:
        return accum

def makev(l,h,v):
    if l < h:
        v.append(l)
        makev(l+1,h,v)

def makep(c,v,p,K):
    if c < len(v):
        p.append(K[v[c]])
        makep(c+1,v,p,K)

def whle(i,n,v,K,p,accum):
    if v[len(v)-1] < len(K):
        makep(0,v,p,K)
        accum.append(p)
        p = [i]
        lent = v[0] + 1
        v = []
        makev(0+lent,n-1+lent,v)
        whle(i,n,v,K,p,accum)

def rpermute(n,L,i,c,accum,p):
    p.append(i)
    K = L[0:]
    K.remove(i)
    v = []
    makev(0,n-1,v)
    whle(i,n,v,K,p,accum)
    p = []
    if c < len(L):
        return rpermute(n,L,L[c],c+1,accum,p)
    if c == len(L):
        return rremovesame(accum,[],accum[0],1)

def rrange(i,h,accum,L):
    if i < h:
        looppermute(i,None,0,accum,L)
        rrange(i+1,h,accum,L)

def looppermute(i,lent,c,accum,L):
    perm = rpermute(i,L,L[0],1,[],[])
    lent = len(perm)
    accum.append(perm[c])
    if c+1 < lent:
        looppermute(i,lent,c+1,accum,L)

def rgen_subsets(L,i,c,accum,lent):
    accum.append([i])
    if c+1 < lent:
        return rgen_subsets(L,L[c+1],c+1,accum,lent)
    if lent > 1:
        rrange(2,lent+1,accum,L)
    return accum

#print(rgen_subsets(['a1','a2','a3'],'a1',0,[],3))
#print(rgen_subsets([1,2,3,4,5,6],1,0,[],6))
  
