s_matrix = ['63', 'c0', 'ab', '20', 'eb', '2f', '30', 'cb', '9f', '93', 'af', '2b', 'a0', '92', 'c7', 'a2']
# s_matrix = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# rotate sesuai document(kebawah)
def rotate(state):
    temp = []
    for i in range(4):
        for j in range(4):
            temp.append(state[j*4 + i])
    return temp
rotate_bro = rotate(s_matrix)
print(rotate_bro)

# shift
def shift(word, n):
    return word[n:]+word[0:n]

def shift_row(state):
    shift_r = []
    for i in range(4):
        temp = state[i*4:i*4+4]
        shift_r += shift(temp, i)
    return shift_r

shift_bro = shift_row(rotate_bro)
print(shift_bro)

# rotate balik
rotate_balik_bro = rotate(shift_bro)
print(rotate_balik_bro)