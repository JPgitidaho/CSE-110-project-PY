#W01 Prove: Project - Clever Stories-Flavio Chumba
#Shows creativity and exceeds requirements: Alternate logic for determining 'a' or 'an' based on the first letter 
# of the adjective.

# Get user input for various elements of the story
adjective = input('adjective:')
animal = input('animal:')
verb_1 = input('verb:')
exclamation = input('exclamation:')
verb_2 = input('verb:')
verb_3 = input('verb:')
verb_4 = input('verb:')
print()

# Present the crafted story based on user inputs
print('\nYour story goes like this:')
# Alternate logic for determining 'a' or 'an' based on the first letter of the adjective
if adjective.lower().startswith(('a', 'e', 'i', 'o', 'u')):
    print(f'The other day, I found myself in a serious predicament. It all began when I spotted an {adjective} {animal} {verb_1} down the hallway.\n"{exclamation.title()}!" I exclaimed. But all I could think to do was to {verb_3} repeatedly. Miraculously, that caused it to stop, but not before it attempted to {verb_4} right in front of my family.')
else:
    print(f'The other day, I found myself in a serious predicament. It all began when I spotted a {adjective} {animal} {verb_1} down the hallway.\n"{exclamation.title()}!" I exclaimed. But all I could think to do was to {verb_3} repeatedly. Miraculously, that caused it to stop, but not before it attempted to {verb_4} right in front of my family.')

print('..............................................................................')
