'''A agenda do homem aranha'''

# Initialization of varibles
people: dict = {}
tasks: list = []

# Dangerous while but works
while True:
    try:
        # Input 'person' + ' ' + 'task' line
        line = input()
    except EOFError:

        # Output in waited format
        for name in people.keys():
            print(f'{name}:')
            for assignment in tasks:
                if assignment not in people[name]:
                    print(f'- {assignment}')
        
        # Stop the dangerous while True
        break
    else:

        # list string line
        line = list(line)
        
        # find the first space (' ') index
        first_space_index = line.index(' ')

        # Slice the list line to form a name of person and task
        person: str = ''.join(line[:first_space_index])
        task: str = ''.join(line[first_space_index+1:])

        # Check if person is a key in the dict, if not start the key with empty list
        if person not in people.keys():
            people[person] = []

        # Check if the task exists in the list, if not extend the list with the task 
        if task not in people[person]:
            people[person] += [task]

        # Create a List (tasks) with all tasks not repeated
        if task not in tasks:
            tasks.append(task)
