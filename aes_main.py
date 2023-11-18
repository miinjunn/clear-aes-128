from fungsi_aes import encode_hex, hex_to_int, add_round_key_preRound, subByte, mix_column, key_scheduling, rcon, add_round_key
from shift_row import shift_row


plain = "Two One Nine Two"
key = "Thats my Kung Fu"


def breakinput(plain, key):
    plaintext = encode_hex(plain)
    keyword = encode_hex(key)
    plaintext, keyword = hex_to_int(plaintext, keyword)
    return plaintext, keyword


# enkripsi
def encrypt(plaintext, keyword):
    # input to dec
    pt, ky = breakinput(plaintext, keyword)
    state_preRound, state_preRound_hex = add_round_key_preRound(pt, ky)

    new_state = state_preRound
    prev_wk = ky

    # all_round
    for i in range(10):
        if i != 9:
            round_subByte = subByte(new_state)
            round_shiftRow = shift_row(round_subByte)
            round_mixColumn = mix_column(round_shiftRow)
            round_whitening_key = key_scheduling(prev_wk, rcon[i])
            round_add_round_key = add_round_key(round_mixColumn, round_whitening_key)

            new_state = round_add_round_key
            prev_wk = round_whitening_key

        elif i == 9:
            round_subByte = subByte(new_state)
            round_shiftRow = shift_row(round_subByte)
            round_whitening_key = key_scheduling(prev_wk, rcon[i])
            round_add_round_key = add_round_key(round_shiftRow, round_whitening_key)

            new_state = round_add_round_key
            prev_wk = round_whitening_key

    new_state_hex = [hex(i)[2:] for i in new_state]

    # ark_hex = [hex(i)[2:] for i in round_add_round_key]

    return new_state


all_round = encrypt(plain, key)
print(all_round)

all_round = [hex(i)[2:] for i in all_round]
for i in all_round:
    print(i, end='')
# print('# ROUND-1')

# # SUB-BYTE
# r1_subByte = subByte(state_preRound)
# print(f"r1 sub byte: {r1_subByte}")

# # SHIFT-ROW
# r1_shift_row = shift_row(r1_subByte)
# print(f"r1 shift-row: {r1_shift_row}")

# # MIX-COLUMN
# r1_mix_column = mix_column(r1_shift_row)
# print(f"r1 mix-columm: {r1_mix_column}")

# r1_key = key_scheduling(key_to_int, rcon=rcon1)
# print(f"key round 1: {r1_key}")

# # w4: [226, 50, 252, 241]
# # w5: [145, 18, 145, 136]
# # w6: [177, 89, 228, 230]
# # w7: [214, 121, 162, 147]
# key_round_1 = [hex(x)[2:] for x in r1_key]
# print(f"key round-1: {key_round_1}")

# r1_add_round_key = add_round_key(r1_mix_column, r1_key)
# print(f"r1 add round key: {r1_add_round_key}")

# r1_add_round_key_hex = [hex(x)[2:] for x in r1_add_round_key]
# print(f"r1_add_round_key_hex: {r1_add_round_key_hex}")

# print('---------------------------------------')
# # ROUND-2
# print('# ROUND-2')

# r2_subByte = subByte(r1_add_round_key)
# print(f"r2 sub byte: {r2_subByte}")

# r2_shift_row = shift_row(r2_subByte)
# print(f"r2 shift-row: {r2_shift_row}")

# r2_mix_column = mix_column(r2_shift_row)
# print(f"r2 mix-columm: {r2_mix_column}")

# r2_key = key_scheduling(r1_key, rcon=rcon2)
# print(f"key round 2: {r2_key}")

# key_round_2 = [hex(x)[2:] for x in r2_key]
# print(f"key round-2: {key_round_2}")

# print(f"r1 add round key (cek): {r1_add_round_key}")
# r2_add_round_key = add_round_key(r2_mix_column, r2_key)
# print(f"r2 add round key: {r2_add_round_key}")

# r2_add_round_key_hex = [hex(x)[2:] for x in r2_add_round_key]
# print(f"r2_add_round_key_hex: {r2_add_round_key_hex}")
