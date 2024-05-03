student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_data_frame = pandas.DataFrame(data)
diction = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}
print(diction)

user_word = input().upper()

result = [diction[i] for i in user_word]
print(result)
