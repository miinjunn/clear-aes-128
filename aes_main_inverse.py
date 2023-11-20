from fungsi_aes import break_input, rcon, add_round_key, key_expansion, subByte_inv, mix_column_inv
from shift_row import shift_row_inv


# plain_user = "Two One Nine Two"
cipher_user = [41, 195, 80, 95, 87, 20, 32,
               246, 64, 34, 153, 179, 26, 2, 215, 58]
key_user = "Thats my Kung Fu"


# dekripsi
def decrypt(ciphertext, keyword):
    # input to dec
    cipher = ciphertext
    key = break_input(keyword)

    # key_expansion
    wk_round = key_expansion(key, rcon)

    new_state = []

    # all_round
    for i in range(10):

        if i == 0:
            print(f"ROUND-{10-i}")
            inv_add_round_key = cipher
            print(f"add round key: {inv_add_round_key}")

            inv_shiftRow = add_round_key(inv_add_round_key, wk_round[-(i+1)])
            print(f"inv shift row: {inv_shiftRow}")

            inv_subByte = shift_row_inv(inv_shiftRow)
            print(f"inv sub byte: {inv_subByte}")

            new_state = inv_subByte

        else:
            print(f"ROUND-{10-i}")
            inv_add_round_key = subByte_inv(new_state)
            print(f"add round key: {inv_add_round_key}")

            inv_mix_column = add_round_key(inv_add_round_key, wk_round[-(i+1)])
            print(f"inv mix Column: {inv_mix_column}")

            inv_shiftRow = mix_column_inv(inv_mix_column)
            print(f"inv shift row: {inv_shiftRow}")

            inv_subByte = shift_row_inv(inv_shiftRow)
            print(f"inv sub byte: {inv_subByte}\n")

            new_state = inv_subByte

    ark = subByte_inv(new_state)
    print(f"PRE ROUND: {ark}")
    plaintext = add_round_key(ark, wk_round[0])
    print(f"plain: {plaintext}\n")

    # convert output menjadi hex, lalu add 0 jika hex hanya 1 charakter, ex: 'a' -> '0a'
    plaintext_hex = []
    for i in plaintext:
        cek = hex(i)[2:]
        if len(cek) == 1:
            cek = '0' + cek
        plaintext_hex.append(cek)

    return plaintext_hex


# decrypt test:
all_round = decrypt(cipher_user, key_user)
print(f"plain_hex \t: {all_round}")
all_round = [chr(int(i, base=16)) for i in all_round]

plain = ''
for i in all_round:
    plain += i
print(f"plaintext: {plain}")
