import sys
class Graph():
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 
    def printSolution(self, dist): 
        print "Vertex tDistance from Source"
        for node in range(self.V): 
            print node, "t", dist[node] 
    def minDistance(self, dist, sptSet): 
        min = sys.maxint  
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
    def dijkstra(self, src): 
        dist = [sys.maxint] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
     for cout in range(self.V): 
            u = self.minDistance(dist, sptSet) 
            sptSet[u] = True
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
self.printSolution(dist) 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 
g.dijkstra(0);

#radix sort
def radix_sort(alist, base=10):
    if alist == []:
        return
        def key_factory(digit, base):
        def key(alist, index):
            return ((alist[index]//(base**digit)) % base)
        return key
    largest = max(alist)
    exp = 0
    while base**exp <= largest:
        alist = counting_sort(alist, base - 1, key_factory(exp, base))
        exp = exp + 1
    return alist
def counting_sort(alist, largest, key):
    c = [0]*(largest + 1)
    for i in range(len(alist)):
        c[key(alist, i)] = c[key(alist, i)] + 1
    c[0] = c[0] - 1 
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]
    result = [None]*len(alist)
    for i in range(len(alist) - 1, -1, -1):
        result[c[key(alist, i)]] = alist[i]
        c[key(alist, i)] = c[key(alist, i)] - 1
    return result
alist = input('Enter the list of (nonnegative) numbers: ').split()
alist = [int(x) for x in alist]
sorted_list = radix_sort(alist)
print('Sorted list: ', end='')
print(sorted_list)


#merge sort


def merge_sort(alist, start, end):
    if end - start > 1:
        mid = (start + end)//2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)
def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
merge_sort(alist, 0, len(alist))
print('Sorted list: ', end='')
print(alist)



#shell sort

def gaps(size):
    length = size.bit_length()
    for k in range(length - 1, 0, -1):
        yield 2**k - 1
def shell_sort(alist):
    def insertion_sort_with_gap(gap):
        for i in range(gap, len(alist)):
            temp = alist[i]
            j = i - gap
            while (j >= 0 and temp < alist[j]):
                alist[j + gap] = alist[j]
                j = j - gap
            alist[j + gap] = temp
     for g in gaps(len(alist)):
        insertion_sort_with_gap(g)
alist = input('Enter the list of numbers: ').split()
alist = [int(x) for x in alist]
shell_sort(alist)
print('Sorted list: ', end='')
print(alist)
