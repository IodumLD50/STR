

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'Список :\n[ ' + str(current.value) + ' '
            while current.next != None:
                current = current.next
                out += str(current.value) + ' '
            return out + ']'
        return 'Список :\n[]'

    def clear(self):
        self.__init__()        
        
        
    # Добавление элементов в конец списка. +
    def add(self, x):
        self.length+=1
        if self.first == None:
            #self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            #здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)   
            
    # Добавление элементов в начало списка. +
    def add_push(self, x):
            self.length += 1
            if self.first == None:
                self.last = self.first = Node(x, None)
            else:
                self.first = Node(x, self.first)  
    
    # Добавление элементов в произвольное место списка. +  
    def add_add(self, i, x):
        if self.first == None:
            self.last = self.first = Node(x, None)
            return
        if i == 0:
          self.first = Node(x,self.first)
          return
        curr = self.first
        count = 0
        while curr != None:
            count+=1
            if count == i:
              curr.next = Node(x,curr.next)
              if curr.next.next == None:
                self.last = curr.next
              break
            curr = curr.next                      
                
    # Колличество элементов в списке +
    def len(self):
        length = 0
        if self.first != None:
            current = self.first
            while current.next != None:
                current = current.next
                length += 1
        return length + 1  #+1 для учета self.first
                
    # Удаление элемента +
    def pop(self, i):
        if (self.first == None):
          return
        curr = self.first
        count = 0
        if i == 0:
          self.first = self.first.next
          return
        while curr != None:
            if count == i:
              if curr.next == None:
                self.last = curr
              old.next = curr.next 
              break
            old = curr  
            curr = curr.next
            count += 1           
                
    # Вставка элемента в отсортированный список +
    def sorted_insert(self, x):
        if self.first == None:
          self.first = Node(x,self.last)
          return
        if self.first.value > x:
          self.first = Node(x,self.first)
          return
        curr = self.first
        while curr != None:
            if curr.value > x:
              old.next = Node(x,curr)
              return
            old = curr
            curr = curr.next       
        self.last = old.next = Node(x,None)            
                
    # Удаление повторяющихся значений +                
    def remove_sorted_duplicates(self):
        if (self.first == None):
            return
      
                
    # Сортировка по возрастанию +
    def sort_max(self):
       a = Node(0,None)
       b = Node(0,None)
       c = Node(0,None)
       e = Node(0,None)
       tmp = Node(0,None)
       
       while(e != self.first.next) :
        c = a = self.first
        b = a.next

        while a != e:
          if a and b:
            if a.value > b.value:
              if a == self.first:
                tmp = b.next
                b.next = a
                a.next = tmp
                self.first = b
                c = b
              else:
                tmp = b.next
                b.next = a
                a.next = tmp
                c.next = b
                c = b
            else:
              c = a
              a = a.next
            b = a.next
            if b == e:
              e = a
          else:
              e = a            
              
              
    # Сортировка по убыванию +
    def sort_min(self):
       a = Node(0,None)
       b = Node(0,None)
       c = Node(0,None)
       e = Node(0,None)
       tmp = Node(0,None)
       
       while(e != self.first.next) :
        c = a = self.first
        b = a.next

        while a != e:
          if a and b:
            if a.value < b.value:
              if a == self.first:
                tmp = b.next
                b.next = a
                a.next = tmp
                self.first = b
                c = b
              else:
                tmp = b.next
                b.next = a
                a.next = tmp
                c.next = b
                c = b
            else:
              c = a
              a = a.next
            b = a.next
            if b == e:
              e = a
          else:
              e = a         
                      
    def index(self, key):#поддержка обращения по ключу
        length =0
        current=None
        if self.first != None:
            current = self.first
            while key!=length and current.next != None:
                current = current.next
                length +=1
            if key==length:current=current.value
        return current
    
            
L = LinkedList()
L.add(1)
L.add(2)
L.add(3)
L.add(4)
L.add(5)
print(L) 

L.add_push(7)
L.add_push(4)
L.add_push(8)
print(L) 

L.add_add(4, 9)
print(L) 

print(f'В списке {L.len()} элементов')
print('________________________________')
L.add_add(9,8)
L.pop(0)
print(L)
print('________________________________')
L.pop(0)
L.pop(7)
print(L)
print(f'В списке {L.len()} элементов') 

L.sorted_insert(4)
print(L)

L.remove_sorted_duplicates()
print(L)

L.sort_max()
print(L)

L.sort_min()
print(L)

print(L.index(0))
