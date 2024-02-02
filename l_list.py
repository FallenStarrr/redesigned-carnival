class ArrayList():
    length = 0
    capacity = 0
    array_list = []
    def __init__(self, length, capacity):
        self.length = length
        self.capacity = capacity
        self.array_list = [None] * length
        
    def append(self, val):
        if self.length >= self.capacity:
            new = []
            for i in self.array_list:
                new.append(i)
            self.array_list = new
            self.length += 1
            self.capacity *= 2  
           
        else:     
            self.array_list.append(val)
            self.length += 1
          
    def pop(self):
        self.array_list = self.array_list[:-1]
        print(self.array_list)   
    # def __str__(self):
    #     lis = " ".join(self.array_list)
    #     print(lis)  



a = ArrayList(2, 3)
a.append(1)
a.append(3)
a.pop()

