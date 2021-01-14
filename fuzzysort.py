from random import randint
from time import time
from array import array

def clock():
    start = time()
    while 1:
        yield time() - start

def bubble_sort(a):
    n = len(a)
    while n != 0:
        newn = 0
        i = 1
        while i < n:
            fir = a[i - 1]
            if fir > a[i]:
                a[i - 1] = a[i]
                a[i] = fir
                newn = i
            i += 1
        n = newn

def fuzzy_sort(a):
    L = len(a)
    m = (L - 1) / float(max(a))
    sorted = [None] * L
    for x in a:
        index = int(m * x)
        if sorted[index]:
            sorted[index].append(x)
        else:
            sorted[index] = array('i', [x])
    for i in range(L):
        s = sorted[i]
        if s:
            bubble_sort(s)
            sorted.extend(s)
    return sorted[L:]
    
def main():
    a = [randint(0, 100000) for i in range(1000000)]
    print("Sorting...")
    timer = clock()
    timer.next()
    a = fuzzy_sort(a)
    print("Sorted %d items in %f seconds" % (len(a), timer.next()))
    print('\t '.join(map(str, a[:1000])))
    
if __name__ == "__main__":
    main()