def gFn(a, b):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a ^= 0x1b
        b >>= 1
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


mentahan = ['63', '2f', 'af', 'a2', 'eb', '93', 'c7',
            '20', '9f', '92', 'ab', 'cb', 'a0', 'c0', '30', '2b']
mentahan_to_int = []
for i in mentahan:
    mentahan_to_int.append(int(i, base=16))
print(f"sebelum di mix: {mentahan_to_int}")

print()
print('---------------')
print()

mixColumn(mentahan_to_int)
print(mentahan_to_int)
# print(hasil)
print()
print("final: ")

hasil = mentahan_to_int.copy()
final = [hex(i)[2:] for i in hasil]

# print(f"hasil: {final[2:]}")
print(final)

# known issue: hanya mix row pertama saja
# need to do: add mix column code untuk 3 row sisanya