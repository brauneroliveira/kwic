from sys import stdout

def kwic_input(path):
    
    file = open(path, 'r')
    file_contents = file.read()
    file.close()
    return file_contents.replace(',','').split()

def kwic_circular_shift(input_list):
    
    list_of_shifts = []
    list_of_shifts.append(input_list.copy())
    
    i = 0

    while i < len(input_list)-1:
        
        input_list.append(input_list.pop(0))
        list_of_shifts.append(input_list.copy())
        i += 1
        
    return list_of_shifts
        
def kwic_alphabetizer(list_of_shifts):
    
    list_of_shifts.sort()
    
    return list_of_shifts

def kwic_output(ordered_list_of_shifts):
    
    for l in ordered_list_of_shifts:
        for w in l:
            stdout.write(w+' ')
        stdout.write('\n')
        
characters = kwic_input('poema.txt')

index = kwic_circular_shift(characters)

alphabetized_index = kwic_alphabetizer(index)

kwic_output(alphabetized_index)