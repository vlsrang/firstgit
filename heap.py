class BinaryHeap:
    def __init__(self,array=[]):
        self.items=array

    def size(self):
        return len(self.items)

    def swap(self,i,j):
        self.items[i],self.items[j]=self.items[j],self.items[i]

    def insert(self,key):
        self.items.append(key)
        self.upheap(self.size()-1)

    def extract_min(self):
        if self.size()==0:
            print("Heap is empty.")
            return None
        minimum=self.items[0]
        self.swap(0,-1)
        del self.items[-1]
        self.downheap(0)
        return minimum

    def downheap(self,i):
        while 2*i+1 <= self.size()-1:
            k=2*i+1
            if k<self.size()-1 and self.items[k] > self.items[k+1]:
                k+=1
            if self.items[i] < self.items[k]:
                break
            self.swap(i,k)
            i=k

    def upheap(self,i):
        while i>0 and self.items[(i-1)//2] > self.items[i]:
            self.swap(i,(i-1)//2)
            i=(i-1)//2

    def build_heap(self,array):
        for i in range(len(array)//2-1,-1,-1):
            self.downheap(i)

    def print_heap(self):
        for i in range(0,self.size()):
            print(self.items[i], end=' ')
        print("\n Size of Heap=", self.size())
