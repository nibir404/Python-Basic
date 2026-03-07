tasks =['Study Python', 'Go to gym', 'Read Book', 'Practice DSA']
for task in tasks:
    print(task)

print(len(tasks))
print(tasks[1])
tasks.append('Build a project')
tasks.remove('Go to gym')
print(tasks)