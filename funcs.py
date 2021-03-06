def decode_CIGAR(string_code, starting_position):
    full_string = [int(starting_position), str()]
    y = re.findall(r'[\d]+M|[\d]+D|[\d]+I|[\d]+S|[\d]+H', string_code)
    for i in y:
        if i[-1] in ['M', 'S', 'H']:
            full_string[1] += '.'*int(i[:-1])
        elif i[-1] == 'I':
            full_string[1] += 'I'*int(i[:-1])
        elif i[-1] == 'D':
            full_string[1] += 'D'*int(i[:-1])
        else:
            print('Error in ', i)
            break
    return full_string
            

 def find_indels(char, string):
    indexes = list()

    def find_indels_inner(char, string):
        position = string.find(char) + 1
        indexes.append(position)
        new_string = string[position + len(char) - 1:]
        if char in new_string:
            return find_indels_inner(char, new_string)

    find_indels_inner(char, string)
    if len(indexes) > 1:
        for i in range(1, len(indexes)):
            indexes[i] += indexes[i - 1] + len(char) - 1
    return indexes
    
    
def select_region(string_code, starting_position):
    position_of_cut = 3383
    delta = 40
    index_of_cut = position_of_cut-int(starting_position)
    
    if starting_position <= position_of_cut - delta:
        return [position_of_cut-delta, string_code[index_of_cut - delta : index_of_cut + delta]]
    elif starting_position < position_of_cut + delta:
#         new_string = '.' * (starting_position-(position_of_cut-delta))
        return [starting_position, string_code[0:index_of_cut + delta]]


def sort_dict(dictionary):
    new_dict = dict()
    for key in sorted(dictionary, key=dictionary.get, reverse=True):
        new_dict[key] = dictionary[key]
    return new_dict
