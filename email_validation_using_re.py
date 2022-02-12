email_input = input('Email: ')
search = re.findall(r'^[A-z0-9\.]+@[A-z]+\.[A-z]{2,8}$',email_input)
email_list = []

if search != []:
    email_list.append(search)
    print(f'{search} Added')
    
else:
    print('Invalid email')
    
for email in email_list:
    print(email)