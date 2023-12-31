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

sbox_inv = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
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

# olah input: text to dec


def olah_input(plain, key):
    plaintext = encode_hex(plain)
    keyword = encode_hex(key)
    plaintext, keyword = hex_to_int(plaintext, keyword)
    return plaintext, keyword


# olah input (new) -> optimize ver.
def break_input(inputan: str):
    temp = []
    input = [hex(ord(i))[2:] for i in inputan]      # convert ke hex
    while len(input) < 16:                          # padd 00 jika char < 16
        input.append("00")
    temp = [int(i, base=16) for i in input]        # convert ke dec
    return temp


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
    # sub_to_hex = [hex(x)[2:] for x in sub]
    return sub


def subByte_inv(state_add_round_key):
    sub_inv = []
    for i in range(16):
        sub_inv.append(sbox_inv[state_add_round_key[i]])
    return sub_inv


# ------------------------------------------------------------------------------------------
preState_mix_column = [2, 3, 1, 1,
                       1, 2, 3, 1,
                       1, 1, 2, 3,
                       3, 1, 1, 2]


preState_mix_column_inv = [0x0E, 0x0B, 0x0D, 0x09,
                           0x09, 0x0E, 0x0B, 0x0D,
                           0x0D, 0x09, 0x0E, 0x0B,
                           0x0B, 0x0D, 0x09, 0x0E]


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
            hasil_mix_column.append(gFn(state[x*4], preState_mix_column[i*4]) ^ gFn(state[x*4 + 1], preState_mix_column[i*4 + 1]) ^ gFn(
                state[x*4 + 2], preState_mix_column[i*4 + 2]) ^ gFn(state[x*4 + 3], preState_mix_column[i*4 + 3]))
    return hasil_mix_column


def mix_column_inv(state):
    hasil_mix_column_inv = []
    for x in range(4):
        for i in range(4):  # hasilnya  per 1 row (kolom 1 sampai 4)
            hasil_mix_column_inv.append(gFn(state[x*4], preState_mix_column_inv[i*4]) ^ gFn(state[x*4 + 1], preState_mix_column_inv[i*4 + 1]) ^ gFn(
                state[x*4 + 2], preState_mix_column_inv[i*4 + 2]) ^ gFn(state[x*4 + 3], preState_mix_column_inv[i*4 + 3]))
    return hasil_mix_column_inv


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

rcon = [rcon1, rcon2, rcon3, rcon4, rcon5, rcon6, rcon7, rcon8, rcon9, rcon10]


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


def key_scheduling(prev_wk, rcon):
    expand = matriks(prev_wk)
    w_gfunction = g_function(expand[3], rcon)

    wA = xor_w_expand(expand[0], w_gfunction)
    wB = xor_w_expand(expand[1], wA)
    wC = xor_w_expand(expand[2], wB)
    wD = xor_w_expand(expand[3], wC)
    round_key = wA + wB + wC + wD
    return round_key


def key_expansion(key, rcon):
    all_wk = [key]
    round_wk = key
    for i in range(10):
        wk = key_scheduling(round_wk, rcon[i])
        round_wk = wk
        all_wk.append(round_wk)
    return all_wk


# ------------------------------------------------------------------------------------------
def add_round_key(state_mixColumn, state_whitening_key):
    hasil_xor = []
    for i in range(16):
        temp = state_mixColumn[i] ^ state_whitening_key[i]
        hasil_xor.append(temp)
    return hasil_xor
