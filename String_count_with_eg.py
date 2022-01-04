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

def least_common(num):
    previous_val = 1
    dict_vals = {1:[0,[]]}
    
    for k,v in sorted(freq_dict.items() ,key=lambda x: x[1]) :
        if v == previous_val:
            dict_vals[v][0] += 1
            if len(dict_vals[v][1])<3 :
                dict_vals[v][1].append(k)
        else:
            if previous_val == num:
                break
            dict_vals[v]=[1,[k]]
            previous_val = v
    print(dict_vals)

least_common(10)



file.close()