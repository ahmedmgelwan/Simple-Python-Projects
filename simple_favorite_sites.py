fav_websites = []
maximumwebs = 5
print('='*40)
print(' Welcome to Bookmark Manger '.title().center(40,'#'))
while (maximumwebs > 0):
    website = input('Enter Your Favaourite website without https://')
    fav_websites.append('https://' + website.strip().lower())
    print('Websites Added Succefully'.center(40,'-'))
    maximumwebs -=1
    print(f'You have {maximumwebs} places left in your poket'.center(40,'#'))

else:
    print(' Your Poket is Full '.center(40,'&'))
index = 0
option = input("To show your Booknarks enter 'show' or 's' :").strip().lower()
if option == 'show' or option == 's':
    print('Your Bookmarks :')
    while index < len(fav_websites):
        print(f'\t#{index + 1 } : {fav_websites[index]}')
        index += 1
    