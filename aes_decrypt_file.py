import binascii
import time
from fungsi_aes import break_input, rcon, add_round_key, key_expansion, subByte_inv, mix_column_inv
from shift_row import shift_row_inv


start = time.time()

# key
key_user = "Thats my Kung Fu"
key = break_input(key_user)
print(f"key user\t: {key_user}")
print(f"key\t\t: {key}")


# file to hex
with open('enkrip/hasil', 'rb') as fp:
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


akan_unconvert = split_16
# --------------------------------------------------------------------------------------------------------


def break_input_list(inputan: list):
    while len(inputan) < 16:                          # padd 0 jika item < 16
        inputan.append(0)
    return inputan


# function: enkripsi per block
def decrypt(ciphertext, keyword):
    # input to dec
    cipher = break_input_list(ciphertext)

    # key_expansion
    wk_round = key_expansion(keyword, rcon)

    new_state = []

    # all_round
    for i in range(10):

        if i == 0:
            inv_add_round_key = cipher
            inv_shiftRow = add_round_key(inv_add_round_key, wk_round[-(i+1)])
            inv_subByte = shift_row_inv(inv_shiftRow)
            new_state = inv_subByte

        else:
            inv_add_round_key = subByte_inv(new_state)
            inv_mix_column = add_round_key(inv_add_round_key, wk_round[-(i+1)])
            inv_shiftRow = mix_column_inv(inv_mix_column)
            inv_subByte = shift_row_inv(inv_shiftRow)

            new_state = inv_subByte

    ark = subByte_inv(new_state)
    plaintext = add_round_key(ark, wk_round[0])

    # convert output menjadi hex, lalu add 0 jika hex hanya 1 charakter, ex: 'a' -> '0a'
    plaintext_hex = []
    for i in plaintext:
        cek = hex(i)[2:]
        if len(cek) == 1:
            cek = '0' + cek
        plaintext_hex.append(cek)

    return plaintext_hex


# function: enkripsi semua block, join hasil enkripsi kedalam 1 variable
def convert_file(state):
    semua = ''
    for i in range(len(state)):
        temp = decrypt(ciphertext=state[i], keyword=key)
        for item in temp:
            semua += item
    return semua


aes_Unconvert = convert_file(akan_unconvert)
# print(aes_Unconvert)
print(f"panjang decrypt file: {len(aes_Unconvert)}")
print(type(aes_Unconvert))


# ---------------------------------------------------------------------------------------------
# hex to file
with open('dekrip/hasil_dekripsi.mp3', 'wb') as fp:
    fp.write(binascii.unhexlify(aes_Unconvert))


end = time.time()
print("time execution:", (end-start), "secs")
