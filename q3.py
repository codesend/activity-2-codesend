def wordCount(t):
    dictionary = {}

    file = open(t, 'r')
    lines = file.readlines()
    file.close()

    line_num = 1
    for line in lines:
        words = line.strip().split()
        for word in words:
            if word not in dictionary.keys():
                dictionary[word] = []
            dictionary[word].append(line_num)
        line_num += 1

    return dictionary
