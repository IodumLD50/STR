# Cтек - дописываем в начало достаём из начала

from time import sleep

class Stack:
    def __init__(self):
        self.elem = [] # пустой список
        
    def push (self, value): # Действия с очередью. Добавления
        self.elem.append(value) 
        # вторая реализация
        
        # self.elem.insert(0,value)  #вставить в начало списка
    
    def pop(self): #  функция по достованию чего либо из списка
        # когда мы получаем значение мы должны удалить 
        vel = self.elem.pop() # 'pop' удаляет значение из конца списка скиска и возвращает его значение 
        # вторая реализация
        # vel = self.elem.pop(0)
        return vel
    
    def size(self): # узнать размер 
        size = len(self.elem) # узнаём размер очереди
        return size    
    
    
    
stack = Stack() # создаём очередь, изночально она пустая
for i in range(10): # on 0 до 10 (9, -1, -1) c 9 до 0
    stack.push(i)
    print(i, end=' ')
print()    
    
for i in range(stack.size()):
       val = stack.pop()
       print(val)
       sleep(val)