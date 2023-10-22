# import w0, w1, w2, w3 -> key (dari inputan user)
# create g function
# create w4, w5, w6, w7

# fungsi dari aes-128.ipynb
def encode_hex(text):
    text = [i for i in text]                # split tiap 1 char
    temp = []
    for i in text:
        enc = i.encode(encoding="ascii").hex()
        temp.append(enc)
    return cek_jumlah_karakter(temp)


def cek_jumlah_karakter(text):
    # if len(text) > 16:
    #     print('masukan max 16 karakter')
    # text = list(text)
    while len(text) < 16:
        text.append('00')
    # print(f'setelah while: {text}')
    return text


def matriks(mat):
    matriks = []
    for i in range(4):
        four_matriks = mat[i*4: i*4+4]
        matriks.append(four_matriks)
    return matriks
# end fungsi dari aes-128.ipynb


# key: Thats my Kung Fu
key = "Thats my Kung Fu"
key_hex = encode_hex(key)
key_int = [int(x, base=16) for x in key_hex]
print(key_hex)
print(key_int)
print('-----------------------------')

# key = w0 - w3 = [84, 104, 97, 116, 115, 32, 109, 121, 32, 75, 117, 110, 103, 32, 70, 117]

expand = matriks(key_int)
w0 = expand[0]
w1 = expand[1]
w2 = expand[2]
w3 = expand[3]
print(w0, w1, w2, w3)
print('-----------------------------')

# --- create g function ---
# ambil w3 sebagai inputan g function
# shift 1 kali ke kiri
# sub byte dengan sbox
# xor dengan Rcon(j)

print(f"w3 sebagai inputan g function: {w3}")


def shift(word, n):
    return word[n:]+word[0:n]


w3_shift = shift(w3, 1)
print(f"shift 1 kekiri: {w3_shift}")

# sub byte
sbox = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

w3_shift_sbyte = []
for i in range(len(w3_shift)):
    w3_shift_sbyte.append(sbox[w3_shift[i]])

print(f"hasil sub byte: {w3_shift_sbyte}")

# --- xor Rcon(1) ---
# [183] xor [01]
# [90]  xor [00]
# [157] xor [00]
# [133] xor [00]

# sama dengan:
# [183, 90, 157, 133] xor [01 00 00 00]

rcon1 = [1, 00, 00, 00]
w3_final_gfunction = []
for i in range(4):
    total = w3_shift_sbyte[i] ^ rcon1[i]
    w3_final_gfunction.append(total)

w3_final_hex = [hex(x)[2:] for x in w3_final_gfunction]
print(f"w3 final g function: {w3_final_gfunction}")
print(f"w3 final hex: {w3_final_hex}")


# --- create w4, w5, w6, w7 ---
def xor_w_expand(state1, state2):
    hasil_xor = []
    for i in range(4):
        temp = state1[i] ^ state2[i]
        hasil_xor.append(temp)
    return hasil_xor


w4 = xor_w_expand(w0, w3_final_gfunction)
w5 = xor_w_expand(w1, w4)
w6 = xor_w_expand(w2, w5)
w7 = xor_w_expand(w3, w6)
print(f'w4: {w4}')
print(f'w5: {w5}')
print(f'w6: {w6}')
print(f'w7: {w7}')