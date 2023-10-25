from shift_row import shift_row

# cek basic
# https://www.simplilearn.com/tutorials/cryptography-tutorial/aes-encryption

# fungsi - fungsi
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


# ------------------------------------------------------------------------------------------
# text to hex
def encode_hex(text):
    text = [i for i in text]                # split tiap 1 char
    temp = []
    for i in text:
        enc = i.encode(encoding="ascii").hex()
        temp.append(enc)
    return cek_jumlah_karakter(temp)


# penambahan 00 jika char < 16
def cek_jumlah_karakter(text):
    while len(text) < 16:
        text.append('00')
    return text


# ------------------------------------------------------------------------------------------
# convert menjadi matriks 4x4
def matriks(mat):
    matriks = []
    for i in range(4):
        four_matriks = mat[i*4: i*4+4]
        matriks.append(four_matriks)
    return matriks


# ------------------------------------------------------------------------------------------
# convert hex to int:
def hex_to_int(plain, key):
    plain_to_int = []
    key_to_int = []
    for i in range(16):
        plain_to_int.append(int(plain[i], base=16))
        key_to_int.append(int(key[i], base=16))
    return plain_to_int, key_to_int

# ------------------------------------------------------------------------------------------
# pre-round add round key:
# xor tiap index (plain dgn key)


def add_round_key_preRound(plain, key):
    hasil_xorInt = []
    hasil_xorHex = []
    for i in range(16):
        hasil_xorInt.append(plain[i] ^ key[i])
        hasil_xorHex.append(hex(plain[i] ^ key[i])[2:])
    return hasil_xorInt, hasil_xorHex


# ------------------------------------------------------------------------------------------
def subByte(state_add_round_key):
    sub = []
    for i in range(16):
        sub.append(sbox[state_add_round_key[i]])

    # kalau ingin bentuk hexnya, tinggal add ke retunnya
    sub_to_hex = [hex(x)[2:] for x in sub]
    return sub


# ------------------------------------------------------------------------------------------
state_mix_column = [2, 3, 1, 1,
                    1, 2, 3, 1,
                    1, 1, 2, 3,
                    3, 1, 1, 2]


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


def mix_column(state):
    hasil_mix_column = []
    for x in range(4):
        for i in range(4):  # hasilnya  per 1 row (kolom 1 sampai 4)
            hasil_mix_column.append(gFn(state[x*4], state_mix_column[i*4]) ^ gFn(state[x*4 + 1], state_mix_column[i*4 + 1]) ^ gFn(
                state[x*4 + 2], state_mix_column[i*4 + 2]) ^ gFn(state[x*4 + 3], state_mix_column[i*4 + 3]))
    return hasil_mix_column


# ------------------------------------------------------------------------------------------
def shiftt(word, n):
    return word[n:]+word[0:n]


rcon1 = [0x01, 0x00, 0x00, 0x00]
rcon2 = [0x02, 0x00, 0x00, 0x00]
rcon3 = [0x04, 0x00, 0x00, 0x00]
rcon4 = [0x08, 0x00, 0x00, 0x00]
rcon5 = [0x10, 0x00, 0x00, 0x00]
rcon6 = [0x20, 0x00, 0x00, 0x00]
rcon7 = [0x40, 0x00, 0x00, 0x00]
rcon8 = [0x80, 0x00, 0x00, 0x00]
rcon9 = [0x1b, 0x00, 0x00, 0x00]
rcon10 = [0x36, 0x00, 0x00, 0x00]
rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]


def g_function(w, rcon):
    w_kanan = shiftt(w, 1)

    w_kanan_subByte = []
    for i in range(len(w_kanan)):
        w_kanan_subByte.append(sbox[w_kanan[i]])

    w_kanan_gfunction = []
    for i in range(4):
        total = w_kanan_subByte[i] ^ rcon[i]
        w_kanan_gfunction.append(total)

    # w3_final_hex = [hex(x)[2:] for x in w_kanan_gfunction]
    # print(f"w3 final hex: {w3_final_hex}")
    return w_kanan_gfunction


def xor_w_expand(state1, state2):
    hasil_xor = []
    for i in range(4):
        temp = state1[i] ^ state2[i]
        hasil_xor.append(temp)
    return hasil_xor


def each_round_key(key_matriks, rcon):
    expand = matriks(key_matriks)
    w_gfunction = g_function(expand[3], rcon)

    wA = xor_w_expand(expand[0], w_gfunction)
    wB = xor_w_expand(expand[1], wA)
    wC = xor_w_expand(expand[2], wB)
    wD = xor_w_expand(expand[3], wC)
    round_key = wA + wB + wC + wD
    return round_key


# ------------------------------------------------------------------------------------------
def add_round_key(state_1, state_2):
    hasil_xor = []
    for i in range(16):
        temp = state_1[i] ^ state_2[i]
        hasil_xor.append(temp)
    return hasil_xor


# ------------------------------------------------------------------------------------------
# -----------------------------------PROGRAM AES-128----------------------------------------
# ------------------------------------------------------------------------------------------
# Input (plaintext)
# Two One Nine Two
# plain = input('input plaintext: ')
# plain = "ZerO Hour To yOU"
plain = "Two One Nine Two"
print(plain)
print(f'Plain Karakter: {len(plain)}')
plain_hex = encode_hex(plain)
print(f'plain hex \t: {plain_hex}')
print(f'plain hex \t: {len(plain_hex)}')
print('---------------------------------------')


# Thats my Kung Fu
# key = input('input key: ')
key = "Thats my Kung Fu"
print(key)
print(f'Key karakter: {len(key)}')
key_hex = encode_hex(key)
print(f'key hex \t: {key_hex}')
print(f'len key hex \t: {len(key_hex)}')

plain_to_int, key_to_int = hex_to_int(plain_hex, key_hex)

print('---------------------------------------')
# PRE-ROUND
# add round key
print("# PRE-ROUND")
state_preRound, state_preRound_hex = add_round_key_preRound(
    plain_to_int, key_to_int)
print(f"new state hasil pre-round: {state_preRound}")
# print(f"new state dalam hex \t\t: {state_preRound_hex}")

print('---------------------------------------')
# ROUND-1
print('# ROUND-1')

# SUB-BYTE
r1_subByte = subByte(state_preRound)
print(f"r1 sub byte: {r1_subByte}")

# SHIFT-ROW
r1_shift_row = shift_row(r1_subByte)
print(f"r1 shift-row: {r1_shift_row}")

# MIX-COLUMN
r1_mix_column = mix_column(r1_shift_row)
print(f"r1 mix-columm: {r1_mix_column}")
# kalau mau dalam bentuk hex
# mx_final = [hex(i)[2:] for i in r1_mix_column]
# print(f"final: {mx_final}")

# hasil: [186, 117, 244, 122, 132, 164, 141, 50, 232, 141, 6, 14, 27, 64, 125, 93]
# final: ['ba', '75', 'f4', '7a', '84', 'a4', '8d', '32', 'e8', '8d', '6', 'e', '1b', '40', '7d', '5d']

# ADD-ROUND-KEY
# key = w0 - w3 = [84, 104, 97, 116, 115, 32, 109, 121, 32, 75, 117, 110, 103, 32, 70, 117]

r1_key = each_round_key(key_to_int, rcon=rcon1)
print(f"key round 1: {r1_key}")

# w4: [226, 50, 252, 241]
# w5: [145, 18, 145, 136]
# w6: [177, 89, 228, 230]
# w7: [214, 121, 162, 147]
key_round_1 = [hex(x)[2:] for x in r1_key]
print(f"key round-1: {key_round_1}")

r1_add_round_key = add_round_key(r1_mix_column, r1_key)
print(f"r1 add round key: {r1_add_round_key}")

r1_add_round_key_hex = [hex(x)[2:] for x in r1_add_round_key]
print(f"r1_add_round_key_hex: {r1_add_round_key_hex}")

print('---------------------------------------')
# ROUND-2
print('# ROUND-2')

r2_subByte = subByte(r1_add_round_key)
print(f"r2 sub byte: {r2_subByte}")

r2_shift_row = shift_row(r2_subByte)
print(f"r2 shift-row: {r2_shift_row}")

r2_mix_column = mix_column(r2_shift_row)
print(f"r2 mix-columm: {r2_mix_column}")

r2_key = each_round_key(r1_key, rcon=rcon2)
print(f"key round 2: {r2_key}")

key_round_2 = [hex(x)[2:] for x in r2_key]
print(f"key round-2: {key_round_2}")

print(f"r1 add round key (cek): {r1_add_round_key}")
r2_add_round_key = add_round_key(r2_mix_column, r2_key)
print(f"r2 add round key: {r2_add_round_key}")

r2_add_round_key_hex = [hex(x)[2:] for x in r2_add_round_key]
print(f"r2_add_round_key_hex: {r2_add_round_key_hex}")

print('---------------------------------------')
# ROUND-3
print('# ROUND-3')

r3_subByte = subByte(r2_add_round_key)
print(f"r3 sub byte: {r3_subByte}")

r3_shift_row = shift_row(r3_subByte)
print(f"r3 shift-row: {r3_shift_row}")

r3_mix_column = mix_column(r3_shift_row)
print(f"r3 mix-columm: {r3_mix_column}")

r3_key = each_round_key(r2_key, rcon=rcon3)
print(f"key round 3: {r3_key}")

key_round_3 = [hex(x)[2:] for x in r3_key]
print(f"key round-3: {key_round_3}")

r3_add_round_key = add_round_key(r3_mix_column, r3_key)
print(f"r3 add round key: {r3_add_round_key}")

print('---------------------------------------')
# ROUND-4
print('# ROUND-4')

r4_subByte = subByte(r3_add_round_key)
print(f"r4 sub byte: {r4_subByte}")

r4_shift_row = shift_row(r4_subByte)
print(f"r4 shift-row: {r4_shift_row}")

r4_mix_column = mix_column(r4_shift_row)
print(f"r4 mix-columm: {r4_mix_column}")

r4_key = each_round_key(r3_key, rcon=rcon4)
print(f"key round 4: {r4_key}")

key_round_4 = [hex(x)[2:] for x in r4_key]
print(f"key round-4: {key_round_4}")

r4_add_round_key = add_round_key(r4_mix_column, r4_key)
print(f"r4 add round key: {r4_add_round_key}")

print('---------------------------------------')
# ROUND-5
print('# ROUND-5')

r5_subByte = subByte(r4_add_round_key)
print(f"r5 sub byte: {r5_subByte}")

r5_shift_row = shift_row(r5_subByte)
print(f"r5 shift-row: {r5_shift_row}")

r5_mix_column = mix_column(r5_shift_row)
print(f"r5 mix-columm: {r5_mix_column}")

r5_key = each_round_key(r4_key, rcon=rcon5)
print(f"key round 5: {r5_key}")

key_round_5 = [hex(x)[2:] for x in r5_key]
print(f"key round-5: {key_round_5}")

r5_add_round_key = add_round_key(r5_mix_column, r5_key)
print(f"r5 add round key: {r5_add_round_key}")

print('---------------------------------------')
# ROUND-6
print('# ROUND-6')

r6_subByte = subByte(r5_add_round_key)
print(f"r6 sub byte: {r6_subByte}")

r6_shift_row = shift_row(r6_subByte)
print(f"r6 shift-row: {r6_shift_row}")

r6_mix_column = mix_column(r6_shift_row)
print(f"r6 mix-columm: {r6_mix_column}")

r6_key = each_round_key(r5_key, rcon=rcon6)
print(f"key round 6: {r6_key}")

key_round_6 = [hex(x)[2:] for x in r6_key]
print(f"key round-6: {key_round_6}")

r6_add_round_key = add_round_key(r6_mix_column, r6_key)
print(f"r6 add round key: {r6_add_round_key}")

print('---------------------------------------')
# ROUND-7
print('# ROUND-7')

r7_subByte = subByte(r6_add_round_key)
print(f"r7 sub byte: {r7_subByte}")

r7_shift_row = shift_row(r7_subByte)
print(f"r7 shift-row: {r7_shift_row}")

r7_mix_column = mix_column(r7_shift_row)
print(f"r7 mix-columm: {r7_mix_column}")

r7_key = each_round_key(r6_key, rcon=rcon7)
print(f"key round 7: {r7_key}")

key_round_7 = [hex(x)[2:] for x in r7_key]
print(f"key round-7: {key_round_7}")

r7_add_round_key = add_round_key(r7_mix_column, r7_key)
print(f"r7 add round key: {r7_add_round_key}")

print('---------------------------------------')
# ROUND-8
print('# ROUND-8')

r8_subByte = subByte(r7_add_round_key)
print(f"r8 sub byte: {r8_subByte}")

r8_shift_row = shift_row(r8_subByte)
print(f"r8 shift-row: {r8_shift_row}")

r8_mix_column = mix_column(r8_shift_row)
print(f"r8 mix-columm: {r8_mix_column}")

r8_key = each_round_key(r7_key, rcon=rcon8)
print(f"key round 8: {r8_key}")

key_round_8 = [hex(x)[2:] for x in r8_key]
print(f"key round-8: {key_round_8}")

r8_add_round_key = add_round_key(r8_mix_column, r8_key)
print(f"r8 add round key: {r8_add_round_key}")

print('---------------------------------------')
# ROUND-9
print('# ROUND-9')

r9_subByte = subByte(r8_add_round_key)
print(f"r9 sub byte: {r9_subByte}")

r9_shift_row = shift_row(r9_subByte)
print(f"r9 shift-row: {r9_shift_row}")

r9_mix_column = mix_column(r9_shift_row)
print(f"r9 mix-columm: {r9_mix_column}")

r9_key = each_round_key(r8_key, rcon=rcon9)
print(f"key round 9: {r9_key}")

key_round_9 = [hex(x)[2:] for x in r9_key]
print(f"key round-9: {key_round_9}")

r9_add_round_key = add_round_key(r9_mix_column, r9_key)
print(f"r9 add round key: {r9_add_round_key}")

print('---------------------------------------')
# ROUND-10
print('# ROUND-10')

r10_subByte = subByte(r9_add_round_key)
print(f"r10 sub byte: {r10_subByte}")

r10_shift_row = shift_row(r10_subByte)
print(f"r10 shift-row: {r10_shift_row}")

r10_key = each_round_key(r9_key, rcon=rcon10)
print(f"key round 10: {r10_key}")

key_round_10 = [hex(x)[2:] for x in r10_key]
print(f"key round-10: {key_round_10}")

r10_add_round_key = add_round_key(r10_shift_row, r10_key)
print(f"r10 add round key: {r10_add_round_key}")

cipher_output = ''
for i in r10_add_round_key:
    cipher_output += hex(i)[2:] + " "

print(f"cipher text: {cipher_output}")