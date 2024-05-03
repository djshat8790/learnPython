sentence = "What is the airspeed velocity of an unladen swallow?"

sentence_list = sentence.split(" ")

print(sentence_list)

sentence_dict = {k: len(k) for k in sentence_list}

print(sentence_dict)

temp_dict = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 17, "Friday": 20}

result_dict = {k: (v * 9/5) + 32 for (k, v) in temp_dict.items()}

print(result_dict)
