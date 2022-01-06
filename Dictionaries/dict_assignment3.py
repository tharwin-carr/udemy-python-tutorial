string = 'I am so happy to learn Python which makes my friends happy and interested in ' \
         'Python Python Python Python'

sentence_dict = {}

for each_word in string.split(' '):
    sentence_dict[each_word] = sentence_dict.get(each_word, 0) + 1

print(sentence_dict)
