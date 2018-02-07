from django.contrib.sessions.backends import file

global data

class KWICInput:
    
    def __init__(self):
        self.observer = None
        
    def register_observer(self, observer):
        self.observer = observer
        
    def notify_observer(self):
        self.observer.shift()
            
    def readFile(self, path):
        global data
        data = open(path, 'r')
        data = data.read()
        data = data.replace(',','').split()
        self.notify_observer()
        
class KWICCircularShift:
    def __init__(self, observable):
         observable.register_observer(self)
         
    def shift(self):
    
        global data
        auxiliar = [] # Variável auxiliar
        auxiliar.append(data.copy())
        i = 0
    
        while i < len(data)-1:
    
            data.append(data.pop(0))
            auxiliar.append(data.copy())
            i += 1
        
        data = auxiliar
        
# class KWICAlphabetizer:
#     
# class KWICOutput:


kwic = KWICInput()
kwiccs = KWICCircularShift(kwic)

kwic.readFile('poema.txt')
#kwiccs = KWICCircularShift()
#kwiccs.shift()

print(data)