from sys import stdout

global characters, index, alphabetized_index

def kwic_input(path):
    
    global characters
    file = open(path, 'r')
    characters = file.read()
    file.close()

def kwic_circular_shift():
    
    global characters, index
    data = characters.replace(',','').split()
    index = []
    index.append(data.copy())
    
    i = 0

    while i < len(data)-1:
        
        data.append(data.pop(0))
        index.append(data.copy())
        i += 1
        
def kwic_alphabetizer():
    
    global index, alphabetized_index
    alphabetized_index = index
    alphabetized_index.sort()

def kwic_output():
    
    global alphabetized_index
    for l in alphabetized_index:
        for w in l:
            stdout.write(w+' ')
        stdout.write('\n')
        
kwic_input('poema.txt')
kwic_circular_shift()
kwic_alphabetizer()
kwic_output()