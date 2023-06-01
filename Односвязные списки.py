


# УЗЕЛ
class Node:
    # при инициализации
    def __init__(self):
        self.value = None
        self.next = None # ссылка на следующий узел
    # По хорошему нужно установить функции:
    # для установления значения 
    # для получения значеняю
    # для удаления значения 
    # но мы так делать не будем !
    # обращаться напремую к свойству класса это плохо
    # Но обращатся через методы класса это хорошо (есть проверки)
    # Я буду обращатся напрямую к свойству


# Класс который будет делать все проверки и обисовать односвязный список
class LinkedList:
    # при инициализации
    def __init__(self):
        # голова списка
        self.head = Node() # изначально равна узлу 
        
    def add(self, value): # добавляет новые значения 
        if self.head.value is None: # делаем проверку
            self.head.value = value
            return
        # если в голове есть уже какоето значение
        temp = Node()
        temp.value = value
        # 1 ВАРИАНТ (от начала к концу)
        current_node = self.head
        while current_node.next is not None: # до тех пор пока новый элеммент != 0
            current_node = current_node.next
        # когда дойдём до последнего эллемента    
        current_node.next = temp
        
        # 2 ВАРИАНТ (от конца к началу)
        # temp.next = self.head
        # self.head = temp
        # self.size += 1
    ########################################################################################################## 
    def arr_arr(self, elem, value): #реализовать "вставка элемента после какого-то элемента"; 
        if self.head.value is None: # делаем проверку
            self.head.value = value
            return
        # если в голове есть уже какоето значение
        temp = Node()
        temp.value = value
        
        current_node = self.head
        if elem == 0:
           current_node.next = temp
           return
        count = 0
        while current_node != None:
            count += 1
            if count == elem:
                current_node.next = temp
                if current_node.next.next == None:
                    self.head = current_node.next
                break
            current_node = current_node.next    
                
            
        # переделать не работает!!!!!!!!!!!!!!!
        
        
        
     #######################################################################################################   
    def length(self): # узнать длину списка
        current_node = self.head  
        size = 0  
        if self.head.value is None:
            size = 0
        else:
            size = 1   
        while current_node.next is not None:
            current_node = current_node.next
            size += 1
        return size
    
    def find(self, value): # Поиск
        if self.head.value is not None:
            if self.head.value == value:
               return True 
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value == value:
                return True
        return False
    
    def print(self):
        if self.head.value is None:
            print('Список пустой!')
        print(self.head.value, end=' ')    
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            print(current_node.value, end=' ')
        print()    
 
    def pop(self, i):# алгоритм удаления элемента из односвязного спискаи;
        if self.head.value is None:
          return
        curr = self.head
        count = 0
        if i == 0:
          self.head = self.head.next
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

       
        
        
ll = LinkedList()
print(ll.find(0), ll.find(9), ll.find(6), ll.find(2), ll.find(7),)
ll.print()
print(ll.length())
ll.add(9)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(2), ll.find(7),)
ll.print()
print(ll.length())
ll.add(7)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(2), ll.find(7),) 
ll.print()      
print(ll.length())
ll.add(6)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(2), ll.find(7),) 
ll.print()      
print(ll.length())
ll.add(4)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(2), ll.find(7),) 
ll.print()      
print(ll.length())
ll.add(9)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(2), ll.find(7),)  
ll.print()     
print(ll.length())
ll.add(19)
print(ll.find(0), ll.find(9), ll.find(6), ll.find(2), ll.find(7),) 
ll.print()      
print(ll.length())

ll.arr_arr(4,1)
ll.print()

