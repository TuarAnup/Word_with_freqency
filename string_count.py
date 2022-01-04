
file = open('shakespeare.txt', 'r')
text = file.read().lower().split()
# print(text)
list_symbols = [',','.', ';',':','!',"'",'a','and','the','?']
filtered_text = list(filter( lambda x: x not in list_symbols ,text))
# print(filtered_text)

freq_dict = { }

for word in filtered_text:
    if word in freq_dict.keys():
        freq_dict[word] += 1
    else :
        freq_dict[word] = 1

def n_common(num):
    for k,v in sorted(freq_dict.items(),reverse=True ,key=lambda x: x[1])[:num] :
        print(k,v)

n_common(10)



file.close()