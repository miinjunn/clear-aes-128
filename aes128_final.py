from fungsi_aes import encode_hex, hex_to_int, add_round_key_preRound, subByte, mix_column, key_scheduling, add_round_key, \
    rcon1, rcon2, rcon3, rcon4, rcon5, rcon6, rcon7, rcon8, rcon9, rcon10
from shift_row import shift_row

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
print(f'len plain hex \t: {len(plain_hex)}')
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

r1_key = key_scheduling(key_to_int, rcon=rcon1)
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

r2_key = key_scheduling(r1_key, rcon=rcon2)
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

r3_key = key_scheduling(r2_key, rcon=rcon3)
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

r4_key = key_scheduling(r3_key, rcon=rcon4)
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

r5_key = key_scheduling(r4_key, rcon=rcon5)
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

r6_key = key_scheduling(r5_key, rcon=rcon6)
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

r7_key = key_scheduling(r6_key, rcon=rcon7)
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

r8_key = key_scheduling(r7_key, rcon=rcon8)
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

r9_key = key_scheduling(r8_key, rcon=rcon9)
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

r10_key = key_scheduling(r9_key, rcon=rcon10)
print(f"key round 10: {r10_key}")

key_round_10 = [hex(x)[2:] for x in r10_key]
print(f"key round-10: {key_round_10}")

r10_add_round_key = add_round_key(r10_shift_row, r10_key)
print(f"r10 add round key: {r10_add_round_key}")

cipher_output = ''
for i in r10_add_round_key:
    cipher_output += hex(i)[2:] + " "

print(f"cipher text: {cipher_output}")
