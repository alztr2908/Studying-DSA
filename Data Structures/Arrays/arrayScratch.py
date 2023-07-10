import ctypes # there is another way of implementing this like numpy and python array module

"""
implemented special and internal methods:
    a. __len__
    b. __getitem__
    c. __iter__

    b. _make_array

"""

class Array:
    def __init__(self,capacity=1):
        # Length of the "array" initially at 0
        self.length = 0

        # Capacity is the actual size of the array initially at 1 to have a default size 
        self.capacity = capacity

        # Array itself
        self.arr = self._make_array(self.capacity) 

    def __getitem__(self,k):
        """
        Accessing the array -> O(1) 

        Return element at index k
        """
        if not 0 <= k < self.length:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds!') 

        #Retrieve from array at index k -> O(1)
        return self.arr[k] 
    
    # Add element in an array
    def append(self,val):
        """
        Appending the array -> ammortized O(1) 
        """
        if self.length > self.capacity:
            self.capacity = self.length*2

        # Append at current value of length -> O(1)
        self.arr[self.length] = val

        self.length += 1
    
    def insert(self, val, k):
        if not 0 <= k <= self.length:
            return IndexError('K is out of bounds!')
        
        if self.length >= self.capacity:
            self.capacity *= 2
            new_arr = self._make_array(self.capacity)
            
            for i in range(k):
                new_arr[i] = self.arr[i]

            for i in range(self.length, k, -1):
                new_arr[i] = self.arr[i - 1]

            self.arr = new_arr
        
        self.arr[k] = val
        self.length += 1

    def _make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()

    def __iter__(self):
        for i in range(self.length):
            yield self.arr[i]
   
def main():
    # 1. create a static array with initial capacity
    arr = Array(5)

    arr.append(1)
    arr.append(2)
    arr.append(3)
    arr.append(4)
    arr.append(5)

    print(f'index 2 of array: {arr[2]}')

    arr.insert(2,2)
    arr.insert(100,5)

    # Print values
    for element in arr:
        print(element)
    

if __name__ == '__main__':
    main()