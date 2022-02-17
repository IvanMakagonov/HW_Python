import re
new = open("text_6.txt", "r", encoding="utf-8")

new_dict = {}
for i in new.readlines():
    mas, text = i.split(":")
    text = re.sub("[^0-9]", " ", text).split(' ')
    for i in range(text.count('')):
        text.remove('')
    text = [int(text[n]) for n in range(len(text))]
    new_dict[mas] = sum(text)
print(new_dict)