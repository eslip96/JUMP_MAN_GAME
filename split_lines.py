
# with open('input_file.txt', 'r') as file:
#     text = file.read()


# sentences = text.split('. ')


# with open('input_file.txt', 'w') as file:
#     for sentence in sentences:

#         file.write(sentence.strip() + '.\n')


# with open('raw_data.txt', 'r') as file:
#     text = file.read()

#     sentences = text.split("|")

#     new_sentences = ','.join(sentences)

# with open("new_data.txt", 'w') as file:

#     file.write(new_sentences)


new_dict = {}

with open("raw_dictionary.txt", 'r') as file:
    lines = file.readlines()

    for line in lines:
        key, value = line.split()

        new_dict[int(key)] = value


print(new_dict)
