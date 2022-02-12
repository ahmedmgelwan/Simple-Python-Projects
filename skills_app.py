# Import SQLite Module
import sqlite3

# Create Database and Connect
db = sqlite3.connect('/home/ahmed/Desktop/Skills.db')

# Setting Up Cursor
cr = db.cursor()

# User ID
id = 1

# Create Skills Table in Database
cr.execute(f'CREATE TABLE if not exists Skills(name TEXT, progress INTEGER,user_id INTEGER)')


# Commite and Close Method
def commite_close():
    db.commit()
    db.close()
    print('Connection to Database is closed')

#Input Big Message
input_message = '''
What Do You Want To Do?
"s" => Show All Skills
"a" => Add A New Skill
"u" => Update Skills Progress
"d" => Delete Skill
"q" => Quite The APP
choose option: 
'''
#Input Option Chooice
user_input = input(input_message).strip().lower()
comands_list = ['s', 'a', 'u', 'd', 'q']

#Setup All Functions

def Show_skills():
    cr.execute(f'SELECT * from skills WHERE user_id = "{id}"')
    skills = cr.fetchall()
    print(f'You have {len(skills)} {"skill" if len(skills)==1 else "skills"}, and there are:')
    for skill in skills:
        print(f'Skill: {skill[0]} Progress : {skill[1]}%')

    commite_close()

def add_skill():
    skill_name = input('Skill: ').strip().capitalize()
    cr.execute(f'SELECT name from skills where name = "{skill_name}" and user_id = "{id}"')
    result = cr.fetchone()
    if result == None:
        skill_progress = input('Progress: ').strip()
        cr.execute(f'INSERT INTO skills(name, progress, user_id) VALUES("{skill_name}","{skill_progress}", "{id}")')
        print(f'{skill_name} Added Succefuly')
    
    
    else:
        print(f'{skill_name} Is Already in Database, You Can not Add it twice ):')
        change_progress = input(f'Do you want to update thr progress of {skill_name} if yes enter "y" if not press to any key: ').strip().lower()
        if change_progress == 'y':
            skill_progress = input('New Progress: ').strip()
            cr.execute(f'update skills set progress = "{skill_progress}" where name = "{skill_name}" and user_id = "{id}"')
            print(f'{skill_name} Updated Succefuly To be With {skill_progress}% Progress.')

        else:
            print('App Is Closed')

    
    
    commite_close()

def update_skills():

    skill_name = input('Skill: ').strip().capitalize()
    skill_progress = input('New Progress: ').strip()
    cr.execute(f'update skills set progress = "{skill_progress}" where name = "{skill_name}" and user_id = "{id}"')
    print(f'{skill_name} Updated Succefuly To be With {skill_progress}% Progress.')

    commite_close()

def delte_skill():
    skill_name = input('Skill: ').strip().capitalize()
    cr.execute(f'delete from skills where name = "{skill_name}" and user_id = "{id}"')
    print(f'{skill_name} Deleted Succefuly')


    commite_close()

if user_input in comands_list:
    if user_input == 's':
        Show_skills()
    elif user_input == 'a':
        add_skill()
    elif user_input == 'u':
        update_skills()
    elif user_input == 'd':
        delte_skill()
    else:
        print('App closed')
        commite_close()
else:
    print('Wrong Command')