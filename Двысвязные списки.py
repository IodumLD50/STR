


class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.prev = None
        
class DoubleLinkedList():
    def __init__(self):
        self.head = Node()        
        
    def insert_to_end(self, value): # Вставить в конец    
        if self.head.value is None:
            self.head.value = value
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            
        temp = Node()
        temp.value = value
        temp.prev = current_node
        current_node.next = temp    
    
    def insert_to_start(self, value): # Вставить в начало   
        if self.head.value is None:
            self.head.value = value
            return
        temp = Node()
        temp.value = value
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
    
    def insert_after_value(self, after_value, value_to_instart): # Вставить в нужное место
        if self.head.value is None:
            raise Exception('Empty list') # Выбрасываем ошибку
        
        if self.head.value == after_value:
            temp = Node()
            temp.value = value_to_instart
            temp.next = self.head.next
            temp.prev = self.head
            self.head.next.prev = temp
            self.head.next = temp
            return
            
        current_node = self.head
        while current_node.next is not None:
            if current_node.value  == after_value:
                break
            current_node = current_node.next
        if current_node.next is None:
            if current_node.value != after_value:
                raise Exception('No such element')
            
        temp = Node()
        temp.value = value_to_instart
        temp.next = current_node.next
        temp.prev = current_node
        current_node.next.prev = temp
        current_node.next = temp
        
    def delete_from_end(self): # удаление с конца
        if self.head.value is None:
            raise Exception('Empty list')
        
        if self.head.next is None:
            val = self.head.value
            self.head = Node()
            return val
        
        curren_node = self.head    
        while curren_node.next is not None:
            curren_node = curren_node.next
        
        val = curren_node.value    
        curren_node.prev.next = None   
        return val
    
    def deleta_from_start(self): # удаление с начала
        if self.head.value is None:
            raise Exception('Empty list')
        
        if self.head.next is None:
            val = self.head.value
            self.head = Node()
            return val
        
        self.head.next.prev = None
        val = self.head.value
        self.head = self.head.next
        return val
    
    
    
dll = DoubleLinkedList()
dll.insert_to_start(9) # в начало
dll.insert_to_end(7) # в конец   
dll.insert_to_start(6) # в начало   
dll.insert_after_value(9, 8) # после 9 вставим 8       
a = 10

# 6 9 8 7

print(dll.delete_from_end())
print(dll.deleta_from_start())