#Glee Club checker
from pyscript import display, document


Teacher = {'Em Teola'}
G10 = {'Niqa Agasi', 'Al-Makram Arbison','Alyanna Barlisan', 'Amanda Bower', 'Julianne Canuday', 'Lara Estrada', 'Samantha Jose', 'Rafael Magdayao'}
G11 = {'Jalainie Abdullah', 'Sang-heon Choi', 'Skyler Escobar', 'Charlize Galang', 'Carl Rufo',}
G12= {'Areef Batara', 'Areef Hadjisalic', 'Alexander Holgado', 'Clara Sabanal', 'Alexa Salcedo'}

Glee_Complete = G10 | G11 | G12 | Teacher #Union

def add_member(e):
    document.getElementById('results').innerHTML = ' '
    student_first = document.getElementById('first_name').value
    student_last = document.getElementById('last_name').value

    student_name = str(student_first) + " " + str(student_last) # Combine input values


    Glee_Complete.add(student_name)

    display(f'Here is a list of All the members: {Glee_Complete}', target='results')

    display(f'There are {len(Glee_Complete)} Members Total', target='results')