def gFn(state, pre_state):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if pre_state & 1 == 1:
            p ^= state
        hiBitSet = state & 0x80
        state <<= 1
        if hiBitSet == 0x80:
            state ^= 0x1b
        pre_state >>= 1
    return p % 256


def mixColumn(column):
    temp = column.copy()
    column[0] = gFn(temp[0], 2) ^ gFn(temp[3], 1) ^ \
        gFn(temp[2], 1) ^ gFn(temp[1], 3)
    column[1] = gFn(temp[1], 2) ^ gFn(temp[0], 1) ^ \
        gFn(temp[3], 1) ^ gFn(temp[2], 3)
    column[2] = gFn(temp[2], 2) ^ gFn(temp[1], 1) ^ \
        gFn(temp[0], 1) ^ gFn(temp[3], 3)
    column[3] = gFn(temp[3], 2) ^ gFn(temp[2], 1) ^ \
        gFn(temp[1], 1) ^ gFn(temp[0], 3)


state_mix_column = [2, 3, 1, 1,
                    1, 2, 3, 1,
                    1, 1, 2, 3,
                    3, 1, 1, 2]

mentahan = ['63', '2f', 'af', 'a2', 'eb', '93', 'c7',
            '20', '9f', '92', 'ab', 'cb', 'a0', 'c0', '30', '2b']
mentahan_to_int = []
for i in mentahan:
    mentahan_to_int.append(int(i, base=16))
print(f"sebelum di mix: {mentahan_to_int}")

print()
print('---------------')
print()

inp_mix_col = mentahan_to_int.copy()
mixColumn(inp_mix_col)
print(inp_mix_col)
# print(hasil)
print()

hasil = inp_mix_col.copy()
final = [hex(i)[2:] for i in hasil]

# print(f"hasil: {final[2:]}")
print(f"hasil (valid cuma row1): {hasil}")
print(f"final (valid cuma row1): {final}")
print()

# known issue: hanya mix row pertama saja
# need to do: add mix column code untuk 3 row sisanya


# hasil_mix_column = []
# for i in range(4):
#     for j in range(16):
#         hasil_mix_column[0] = gFn(mentahan_to_int[0], 2) ^ gFn(
#             mentahan_to_int[1], 3) ^ gFn(mentahan_to_int[2], 1) ^ gFn(mentahan_to_int[3], 1)
#         hasil_mix_column[1] = gFn(mentahan_to_int[0], 1) ^ gFn(
#             mentahan_to_int[1], 2) ^ gFn(mentahan_to_int[2], 3) ^ gFn(mentahan_to_int[3], 1)
#         hasil_mix_column[2]
#         hasil_mix_column[3]
#         hasil_mix_column[i] = gFn(mentahan_to_int[i])


# temp(x) = mencari tiap row (jadi nnti 4x)
# akhir = temp1 + temp2 + temp3 + temp4
#  
print(f"sebelum di mix: {mentahan_to_int}")
# hasil_mix_column = [[0 for i in range(16)]]
hasil_mix_column = []
print(hasil_mix_column)
print(len(hasil_mix_column))
for x in range(4):
    for i in range(4): #hasilnya  row 1 - kolom 1 sampai 4
        hasil_mix_column.append( gFn(mentahan_to_int[x*4], state_mix_column[i*4]) ^ gFn(mentahan_to_int[x*4 +1], state_mix_column[i*4 + 1]) ^ gFn(mentahan_to_int[x*4 +2], state_mix_column[i*4 + 2]) ^ gFn(mentahan_to_int[x*4 +3], state_mix_column[i*4 + 3]) )
    # hasil_mix_column[1] = gFn(mentahan_to_int[0], state_mix_column[i*4]) ^ gFn(mentahan_to_int[1], state_mix_column[i*4 + 1]) ^ gFn(mentahan_to_int[2], state_mix_column[i*4 + 2]) ^ gFn(mentahan_to_int[3], state_mix_column[i*4 + 3])
    # hasil_mix_column[2] = gFn(mentahan_to_int[0], state_mix_column[i*4]) ^ gFn(mentahan_to_int[1], state_mix_column[i*4 + 1]) ^ gFn(mentahan_to_int[2], state_mix_column[i*4 + 2]) ^ gFn(mentahan_to_int[3], state_mix_column[i*4 + 3])
    # hasil_mix_column[3] = gFn(mentahan_to_int[0], state_mix_column[i*4]) ^ gFn(mentahan_to_int[1], state_mix_column[i*4 + 1]) ^ gFn(mentahan_to_int[2], state_mix_column[i*4 + 2]) ^ gFn(mentahan_to_int[3], state_mix_column[i*4 + 3])


    # hasil_mix_column[4] = gFn(mentahan_to_int[4], state_mix_column[i*4]) ^ gFn(mentahan_to_int[5], state_mix_column[i*4 + 1]) ^ gFn(mentahan_to_int[6], state_mix_column[i*4 + 2]) ^ gFn(mentahan_to_int[7], state_mix_column[i*4 + 3])
print(f"hasil: {hasil_mix_column}")
mx_final = [hex(i)[2:] for i in hasil_mix_column]
print(f"final: {mx_final}")

# index 0 = 0*4
# index 1 = 0*4 +1
# index 2 = 0*4 +2
# index 3 = 0*4 +3

# index 4 = 1*4
# index 5 = 1*4 +1
# index 6 = 1*4 +2
# index 7 = 1*4 +3

# index 8  = 2*4
# index 9  = 2*4 +1
# index 10 = 2*4 +2
# index 11 = 2*4 +3

# index 12 = 3*4
# index 13 = 3*4 +1
# index 14 = 3*4 +2
# index 15 = 3*4 +3