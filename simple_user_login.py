admins = ['Ahmed', 'Mohammed', 'Ali', 'Ibrahim', 'Abdo', 'Mahmoud']
print("=" * 30)
name = input('Enter your name: ').strip().capitalize()
if name in admins:
    print('Welcome Back (: .')
    option = input('Choose to Delete or Update: ').strip().lower()
    if option == 'update' or option == 'u':
        new_name = input('Enter your new name: ')
        admins[admins.index(name)] = new_name
        print(f'Now Your Name Is: {new_name}')
        
    elif option == 'delete' or option == 'd':
        admins.remove(name)
        print('You have been delted')
else:
    option = input('If you want to be added enter\'yes\' or \'y\'').strip().lower
    if option == 'yes' or 'y':
        admins.append(name)
    else:
        print('See U.')