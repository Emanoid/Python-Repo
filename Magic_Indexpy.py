'''Magic Index: A magic index in an array A [e ... n -1] is defined to
 be an index such that A[ i] = i. Given a sorted array of distinct 
 integers, write a method to find a magic index, if one exists, in array A.'''
def find_magic_index(L,c,accum):
    if c == len(L)-1:
        return accum
    if c == L[c]:
        accum.append(c)
    else:
        find_magic_index(L,c+1,accum)

