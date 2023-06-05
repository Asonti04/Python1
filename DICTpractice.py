#dictionary practice
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}
while True:
    eng = input('Enter a word in English or EXIT: ')
    if eng in sample_dict:
            print('Translation:', sample_dict[eng])
    elif eng == 'EXIT':
        print('Bye!')
        break
    else:
        print('No match!')
