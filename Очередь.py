# Класс описывает свою структуру данных
# вывод значений по времени равных ему
from time import sleep

# 
# первый способ
# class Queue:
#     def __init__(self):
#         self.elem = [] # пустой список
        
#     def add (self, value): # Действия с очередью. Добавления
#         self.elem.append(value)
        
    
#     def get(self): #  функция по достованию чего либо из списка
#         # когда мы получаем значение мы должны удалить 
#         vel = self.elem.pop(0) # 'pop' удаляет значение из скиска и возвращает его значение 
#         return vel
    
#     def size(self): # узнать размер 
#         size = len(self.elem) # узнаём размер очереди
#         return size
    
    
# второй способ
class Queue:
    def __init__(self):
        self.elem = [] # пустой список
        
    def add (self, value): # Действия с очередью. Добавления
        self.elem.insert(0, value) #'insert' добавляет значение в начало списка 
        
    
    def get(self): #  функция по достованию чего либо из списка
        # когда мы получаем значение мы должны удалить 
        vel = self.elem.pop() # 'pop' удаляет значение из конца списка скиска и возвращает его значение 
        return vel
    
    def size(self): # узнать размер 
        size = len(self.elem) # узнаём размер очереди
        return size    
    
    
queue = Queue() # создаём очередь, изночально она пустая
for i in range(10): # on 0 до 10
    queue.add(i)
    print(i, end=' ')
print()    
    
for i in range(queue.size()):
       val = queue.get()
       print(val)
       sleep(val)