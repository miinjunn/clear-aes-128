import binascii
import time
from fungsi_aes import break_input, add_round_key_preRound, subByte, mix_column, key_scheduling, rcon, add_round_key
from shift_row import shift_row

start = time.time()

# key
key_user = "Thats my Kung Fu"
key = break_input(key_user)
print(f"key user\t: {key_user}")
print(f"key\t\t: {key}")


# file to hex
with open('music.mp3', 'rb') as fp:
    hexstring = binascii.hexlify(fp.read())

print(f"panjang file: {len(hexstring)}")

# decode bytes into str(hex)
to_hex = hexstring.decode("ascii")
print(f"panjang decode: {len(to_hex)}")


# function: split each hex
def split_each_hex(state):
    split_2 = []
    for i in range(0, len(state), 2):
        split_2.append(state[i:i+2])
    return split_2


# split each hex
to_each_hex = split_each_hex(to_hex)

# convert each hex into dec
to_each_dec = [int(i, base=16) for i in to_each_hex]

# group dec into 1 block (16 bytes)
split_16 = []
for i in range(0, len(to_each_dec), 16):
    split_16.append(to_each_dec[i: i+16])


akan_diconvert = split_16
# --------------------------------------------------------------------------------------------------------


def break_input_list(inputan: list):
    # temp = []
    while len(inputan) < 16:                          # padd 0 jika item < 16
        inputan.append(0)
    # for i in range(0, len(inputan), 4):
    #     temp.append(inputan[i:i+4])
    return inputan


# function: enkripsi per block
def encrypt(plaintext, keyword):
    # input to dec
    plain = break_input_list(plaintext)
    state_preRound, state_preRound_hex = add_round_key_preRound(plain, keyword)

    new_state = state_preRound
    prev_wk = keyword

    # all_round
    for i in range(10):
        if i != 9:
            round_subByte = subByte(new_state)
            round_shiftRow = shift_row(round_subByte)
            round_mixColumn = mix_column(round_shiftRow)
            round_whitening_key = key_scheduling(prev_wk, rcon[i])
            round_add_round_key = add_round_key(
                round_mixColumn, round_whitening_key)

            new_state = round_add_round_key
            prev_wk = round_whitening_key

        elif i == 9:
            round_subByte = subByte(new_state)
            round_shiftRow = shift_row(round_subByte)
            round_whitening_key = key_scheduling(prev_wk, rcon[i])
            round_add_round_key = add_round_key(
                round_shiftRow, round_whitening_key)

            new_state = round_add_round_key
            prev_wk = round_whitening_key

    cipher_hex = []
    for i in new_state:
        cek = hex(i)[2:]
        if len(cek) == 1:
            cek = '0' + cek
        cipher_hex.append(cek)

    return cipher_hex


# function: enkripsi semua block, join hasil enkripsi kedalam 1 variable
def convert_file(state):
    semua = ''
    for i in range(len(state)):
        temp = encrypt(plaintext=state[i], keyword=key)
        for item in temp:
            semua += item
    return semua


aes_convert = convert_file(akan_diconvert)
# print(aes_convert)
print(f"panjang enkrip file: {len(aes_convert)}")
print(type(aes_convert))


# ---------------------------------------------------------------------------------------------
# hex to file
with open('enkrip/hasil', 'wb') as fp:
    fp.write(binascii.unhexlify(aes_convert))


end = time.time()
print("time execution:", (end-start), "secs")
