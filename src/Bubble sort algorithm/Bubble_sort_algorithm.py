example = [5, 1, 4, 2, 8] #this array is used as an example, you can take any other

def bubble_sort(m):
    flag = True
    while flag:
        flag = False
        for i in range(len(m) - 1):
            if m[i] >= m[i+1]:
                m[i], m[i+1] = m[i+1], m[i]
                flag = True
    return m
print (bubble_sort(example))