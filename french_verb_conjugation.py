# french verb conjugation (present)

# greet the user
print('welcome to the french verb conjugator')

# user enter their word
word = str(input('please enter the word you want to conjugate: ')).lower()

# list of conjugated words
word_conjugate = []

# function (and conditional) to check word ending
def conjugate():

    # create the conjugated word
    if word.endswith('oir'):
        word_oir = ['je ' + word.replace('oir', 'ois', 1),
                    'tu ' + word.replace('oir', 'ois', 1),
                    'il ' + word.replace('oir', 'oit', 1),
                    'nous ' + word.replace('oir', 'ons', 1),
                    'vous ' + word.replace('oir', 'ez', 1),
                    'ils ' + word.replace('oir', 'ent', 1)]
                   
        # append results to the list
        word_conjugate.extend(word_oir)
        
    elif word.endswith('dre'):
        word_dre = ['je ' + word.replace('dre', 'ds', 1),
                    'tu ' + word.replace('dre', 'ds', 1),
                    'il ' + word.replace('dre', 'd', 1),
                    'nous ' + word.replace('dre', 'dons', 1),
                    'vous ' + word.replace('dre', 'dez', 1),
                    'ils ' + word.replace('dre', 'dent', 1)]

        word_conjugate.extend(word_dre)

    elif word.endswith('ir'):
        word_ir = ['je ' + word.replace('ir', 'is', 1),
                   'tu ' + word.replace('ir', 'is', 1),
                   'il '+ word.replace('ir', 'it', 1),
                   'nous ' + word.replace('ir', 'issons', 1),
                   'vous ' + word.replace('ir', 'issez', 1),
                   'ils ' + word.replace('ir', 'issent', 1)]

        word_conjugate.extend(word_ir)

    elif word.endswith('er'):
        word_er = ['je ' + word.replace('er', 'e', 1),
                   'tu ' + word.replace('er', 'es', 1),
                   'il ' + word.replace('er', 'e', 1),
                   'nous ' + word.replace('er', 'ons', 1),
                   'vous ' + word.replace('er', 'ez', 1),
                   'ils ' + word.replace('er', 'ent', 1)]

        word_conjugate.extend(word_er)
        
    else:
        print('i can not handle exceptions yet.')

# format the list of conjugated words
def conjugate_format():
    print(*word_conjugate, sep = '\n')

# call the functions
conjugate()
conjugate_format()
