import tkinter as tk
import random

window = tk.Tk()

window.title("DES Model")
window.geometry("600x400")

#-----Labels and Entries----
label1 = tk.Label(text = "Welcome to Data Encyption Standard Model. \nEnter the various hyperparameters.")
label1.grid(column = 1,row = 0)

label5 = tk.Label(text = "Enter the Half-width size of Message: ")
label5.grid(column = 0,row = 1)

entry5 = tk.Entry()
entry5.grid(column = 1, row = 1)

label2 = tk.Label(text = "Enter the Message: ")
label2.grid(column = 0,row = 2)

entry2 = tk.Entry()
entry2.grid(column = 1, row = 2)

label3 = tk.Label(text = "Enter the key: ")
label3.grid(column = 0,row = 3)

entry3 = tk.Entry()
entry3.grid(column = 1, row = 3)

label4 = tk.Label(text = "Enter the number of rounds: ")
label4.grid(column = 0,row = 4)

entry4 = tk.Entry()
entry4.grid(column = 1, row = 4)
#-------------------------------


#----DES_32_Function----

IP_32 = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)
IP_INV_32 = (
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
)
PC1_32 = (
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4
)
PC2_32 = (
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
)
 
E_32  = (
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
)
 
Sboxes_32 = {
    0: (
        14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
        0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
        4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
        15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
    ),
    1: (
        15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
        3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
        0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
        13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9 
    ),
    2: (
        10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
        13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
        1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12 
    ),
    3: (
        7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
        13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
        10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
        3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
    ),
    4: (
        2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
        14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
        4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
        11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
    ),
    5: (
        12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
        9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
        4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
    ),
    6: (
        4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
        13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
        1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
        6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
    ),
    7: (
        13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
        1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
        7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
        2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
    )
}
 
P_32 = (
    16,  7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11, 4,  25
)

def encrypt_32(msg, key, decrypt=False):
    tr = int(entry4.get())
    # only encrypt single blocks
 

    # permutate by table PC1
    key = permutation_by_table_32_1(key, 64, PC1_32) # 64bit -> PC1 -> 56bit
 
    # split up key in two halves
    # generate the 16 round keys
    C0 = key >> 28
    D0 = key & (2**28-1)
    round_keys = generate_round_keys_32(C0, D0) # 56bit -> PC2 -> 48bit
 
    msg_block = permutation_by_table_32_1(msg, 64, IP_32)
    L0 = msg_block >> 32
    R0 = msg_block & (2**32-1)
 
    # apply thr round function 16 times in following scheme (feistel cipher):
    L_last = L0
    R_last = R0
    for i in range(1, tr+1):
        if decrypt: # just use the round keys in reversed order
            i = tr+1-i
        L_round = R_last
        R_round = L_last ^ round_function_32(R_last, round_keys[i])
        L_last = L_round
        R_last = R_round
 
    # concatenate reversed
    cipher_block = (R_round<<32) + L_round
 
    # final permutation
    cipher_block = permutation_by_table_32(cipher_block, 64, IP_INV_32)
 
    return hex(cipher_block)
 
def round_function_32(Ri, Ki):
    # expand Ri from 32 to 48 bit using table E
    Ri = permutation_by_table_32(Ri, 32, E_32)
 
    # xor with round key
    Ri ^= Ki
 
    # split Ri into 8 groups of 6 bit
    Ri_blocks = [((Ri & (0b111111 << shift_val)) >> shift_val) for shift_val in (42,36,30,24,18,12,6,0)]
 
    # interpret each block as address for the S-boxes
    for i, block in enumerate(Ri_blocks):
        # grab the bits we need
        row = ((0b100000 & block) >> 4) + (0b1 & block)
        col = (0b011110 & block) >> 1
        # sboxes are stored as one-dimensional tuple, so we need to calc the index this way
        Ri_blocks[i] = Sboxes_32[i][16*row+col]
 
    # pack the blocks together again by concatenating
    Ri_blocks = zip(Ri_blocks, (28,24,20,16,12,8,4,0))
    Ri = 0
    for block, lshift_val in Ri_blocks:
        Ri += (block << lshift_val)
 
    # another permutation 32bit -> 32bit
    Ri = permutation_by_table_32(Ri, 32, P_32)
 
    return Ri

def permutation_by_table_32_1(block, block_len, table):
    # quick and dirty casting to str
    block_str = (block).zfill(block_len)
    perm = []
    for pos in range(len(table)):
        perm.append(block_str[table[pos]-1])
    return int(''.join(perm), 2)

def permutation_by_table_32(block, block_len, table):
    # quick and dirty casting to str
    block_str = bin(block)[2:].zfill(block_len)
    perm = []
    for pos in range(len(table)):
        perm.append(block_str[table[pos]-1])
    return int(''.join(perm), 2)
 
def generate_round_keys_32(C0, D0):
    # returns dict of 16 keys (one for each round)
    tr = int(entry4.get())
    round_keys = dict.fromkeys(range(0,tr+1))
    lrot_values = (1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1)
 
    # left-rotation function
    lrot = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
    # initial rotation
    C0 = lrot(C0, 0, 28)
    D0 = lrot(D0, 0, 28)
    round_keys[0] = (C0, D0)
 
    # create 16 more different key pairs
    for i, rot_val in enumerate(lrot_values):
        i+=1
        Ci = lrot(round_keys[i-1][0], rot_val, 28)
        Di = lrot(round_keys[i-1][1], rot_val, 28)
        round_keys[i] = (Ci, Di)
 
    # round_keys[1] for first round
    #           [16] for 16th round
    # dont need round_keys[0] anymore, remove
    del round_keys[0]
 
    # now form the keys from concatenated CiDi 1<=i<=16 and by apllying PC2
    for i, (Ci, Di) in round_keys.items():
        Ki = (Ci << 28) + Di
        round_keys[i] = permutation_by_table_32(Ki, 56, PC2_32) # 56bit -> 48bit
 
    return round_keys
#------------------------------------------------------------------

#------------DES_16_Function------------

IP_16 = (
    26, 18, 10, 2,
    28, 20, 12, 4,
    30, 22, 14, 6,
    32, 24, 16, 8,
    25, 17, 9,  1,
    27, 19, 11, 3,
    29, 21, 13, 5,
    31, 23, 15, 7
)
IP_INV_16 = (
    8, 24, 16, 32,
    7, 23, 15, 31,
    6, 22, 14, 30,
    5, 21, 13, 29,
    4, 20, 12, 28,
    3, 19, 11, 27,
    2, 18, 10, 26,
    1, 17,  9, 25
)

PC1_16 = (
    25, 17, 9,
    1, 26, 18,
    10, 2, 27,
    19, 11, 3,
    31, 23, 15,
    7,  30, 22,
    14, 6, 29,
    21, 13, 5,
    28, 20, 12, 4
)
PC2_16 = (
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2 
)

E_16  = (
    16, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 1
)

Sboxes_16 = {
    0: (
        14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
        0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
        4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
        15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
    ),
    1: (
        15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
        3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
        0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
        13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9 
    ),
    2: (
        10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
        13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
        1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12 
    ),
    3: (
        7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
        13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
        10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
        3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
    ),
}

P_16 = (
    16,  7,
    12,  1,
    15,  5,
    10,  2,
    8, 14,
    3,  9,
    13, 6,
    11, 4
)

def encrypt_16(msg, key, decrypt=False):
    tr = int(entry4.get())
    # only encrypt single blocks

    # permutate by table PC1
    key = permutation_by_table_16_1(key, 32, PC1_16) # 64bit -> PC1 -> 56bit

    # split up key in two halves
    # generate the 16 round keys
    C0 = key >> 16
    D0 = key & (2**16-1)
    round_keys = generate_round_keys_16(C0, D0) # 56bit -> PC2 -> 48bit

    msg_block = permutation_by_table_16_1(msg, 32, IP_16)
    L0 = msg_block >> 16
    R0 = msg_block & (2**16-1)

    # apply thr round function 16 times in following scheme (feistel cipher):
    L_last = L0
    R_last = R0
    for i in range(1,17):
        if decrypt: # just use the round keys in reversed order
            i = 17-i
        L_round = R_last
        R_round = L_last ^ round_function_16(R_last, round_keys[i])
        L_last = L_round
        R_last = R_round

    # concatenate reversed
    cipher_block = (R_round<<16) + L_round

    # final permutation
    cipher_block = permutation_by_table_16(cipher_block, 32, IP_INV_16)

    return hex(cipher_block)

def round_function_16(Ri, Ki):
    # expand Ri from 32 to 48 bit using table E
    Ri = permutation_by_table_16(Ri, 16, E_16)

    # xor with round key
    Ri ^= Ki

    # split Ri into 8 groups of 6 bit
    Ri_blocks = [((Ri & (0b111111 << shift_val)) >> shift_val) for shift_val in (18,12,6,0)]

    # interpret each block as address for the S-boxes
    for i, block in enumerate(Ri_blocks):
        # grab the bits we need
        row = ((0b100000 & block) >> 4) + (0b1 & block)
        col = (0b011110 & block) >> 1
        # sboxes are stored as one-dimensional tuple, so we need to calc the index this way
        Ri_blocks[i] = Sboxes_16[i][16*row+col]

    # pack the blocks together again by concatenating
    Ri_blocks = zip(Ri_blocks, (12,8,4,0))
    Ri = 0
    for block, lshift_val in Ri_blocks:
        Ri += (block << lshift_val)

    # another permutation 32bit -> 32bit
    Ri = permutation_by_table_16(Ri, 16, P_16)

    return Ri

def permutation_by_table_16_1(block, block_len, table):
    # quick and dirty casting to str
    block_str = (block).zfill(block_len)
    perm = []
    for pos in range(len(table)):
        perm.append(block_str[table[pos]-1])
    return int(''.join(perm), 2)

def permutation_by_table_16(block, block_len, table):
    # quick and dirty casting to str
    block_str = bin(block)[2:].zfill(block_len)
    perm = []
    for pos in range(len(table)):
        perm.append(block_str[table[pos]-1])
    return int(''.join(perm), 2)

def generate_round_keys_16(C0, D0):
    # returns dict of 16 keys (one for each round)
    tr = int(entry4.get())
    round_keys = dict.fromkeys(range(0,17))
    lrot_values = []
    for j in  range(17):
        lrot_values.append(random.randint(1, 2))

    # left-rotation function
    lrot = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

    # initial rotation
    C0 = lrot(C0, 0, 14)
    D0 = lrot(D0, 0, 14)
    round_keys[0] = (C0, D0)

    # create 16 more different key pairs
    for i, rot_val in enumerate(lrot_values):
        i+=1
        Ci = lrot(round_keys[i-1][0], rot_val, 14)
        Di = lrot(round_keys[i-1][1], rot_val, 14)
        round_keys[i] = (Ci, Di)

    # round_keys[1] for first round
    #           [16] for 16th round
    # dont need round_keys[0] anymore, remove
    del round_keys[0]

    # now form the keys from concatenated CiDi 1<=i<=16 and by apllying PC2
    for i, (Ci, Di) in round_keys.items():
        Ki = (Ci << 14) + Di
        round_keys[i] = permutation_by_table_16(Ki, 28, PC2_16) # 56bit -> 48bit

    return round_keys

#------------DES_64_Function----------------------

IP_64 = []
for j in  range(128):
    IP_64.append(random.randint(1, 128))

IP_INV_64 = []
for j in  range(128):
    IP_INV_64.append(random.randint(1, 128))

PC1_64 = []
for j in  range(112):
    PC1_64.append(random.randint(1, 128))

PC2_64 = []
for j in  range(96):
    PC2_64.append(random.randint(1, 112))


E_64  = []
for j in  range(96):
    E_64.append(random.randint(1, 64))

Sboxes_64 = {
    0: (
        14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
        0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
        4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
        15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
    ),
    1: (
        15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
        3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
        0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
        13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9 
    ),
    2: (
        10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
        13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
        1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12 
    ),
    3: (
        7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
        13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
        10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
        3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
    ),
    4: (
        2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
        14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
        4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
        11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
    ),
    5: (
        12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
        9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
        4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
    ),
    6: (
        4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
        13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
        1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
        6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
    ),
    7: (
        13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
        1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
        7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
        2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
    ),
    8: (
        1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
        6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
        9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6
    ),
    9:(
        4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
        15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13,
        6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8
    ),
    10:(
        14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
        0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
        13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9
    ),
    11:(
        1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
        9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
        0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15
    ),
    12:(
        10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
        6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8
    ),
    13:(
        14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
        4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
        13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
        1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2
    ),
    14:(
        9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
        10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
        3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14,
        14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7
    ),
    15:(
        10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
        12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1
    )
    
}

P_64 = []
for j in range(64):
    P_64.append(random.randint(1, 64))

def encrypt_64(msg, key, decrypt=False):
    tr = int(entry4.get())
    # only encrypt single blocks

    # permutate by table PC1
    key = permutation_by_table_64_1(key, 128, PC1_64) # 64bit -> PC1 -> 56bit

    # split up key in two halves
    # generate the 16 round keys
    C0 = key >> 56
    D0 = key & (2**56-1)
    round_keys = generate_round_keys_64(C0, D0) # 56bit -> PC2 -> 48bit

    msg_block = permutation_by_table_64_1(msg, 128, IP_64)
    L0 = msg_block >> 64
    R0 = msg_block & (2**64-1)

    # apply thr round function 16 times in following scheme (feistel cipher):
    L_last = L0
    R_last = R0
    for i in range(1,tr+1):
        if decrypt: # just use the round keys in reversed order
            i = 1+tr-i
        L_round = R_last
        R_round = L_last ^ round_function_64(R_last, round_keys[i])
        L_last = L_round
        R_last = R_round

    # concatenate reversed
    cipher_block = (R_round<<64) + L_round

    # final permutation
    cipher_block = permutation_by_table_64(cipher_block, 128, IP_INV_64)

    return hex(cipher_block)

def round_function_64(Ri, Ki):
    # expand Ri from 32 to 48 bit using table E
    Ri = permutation_by_table_64(Ri, 64, E_64)

    # xor with round key
    Ri ^= Ki

    # split Ri into 8 groups of 6 bit
    Ri_blocks = [((Ri & (0b111111 << shift_val)) >> shift_val) for shift_val in (90,84,78,72,64,60,54,48,42,36,30,24,18,12,6,0)]

    # interpret each block as address for the S-boxes
    for i, block in enumerate(Ri_blocks):
        # grab the bits we need
        row = ((0b100000 & block) >> 4) + (0b1 & block)
        col = (0b011110 & block) >> 1
        # sboxes are stored as one-dimensional tuple, so we need to calc the index this way
        Ri_blocks[i] = Sboxes_64[i][16*row+col]

    # pack the blocks together again by concatenating
    Ri_blocks = zip(Ri_blocks, (60,56,52,48,44,40,36,32,28,24,20,16,12,8,4,0))
    Ri = 0
    for block, lshift_val in Ri_blocks:
        Ri += (block << lshift_val)

    # another permutation 32bit -> 32bit
    Ri = permutation_by_table_64(Ri, 64, P_64)

    return Ri

def permutation_by_table_64_1(block, block_len, table):
    # quick and dirty casting to str
    block_str = (block).zfill(block_len)
    perm = []
    for pos in range(len(table)):
        perm.append(block_str[table[pos]-1])
    return int(''.join(perm), 2)

def permutation_by_table_64(block, block_len, table):
    # quick and dirty casting to str
    block_str = bin(block)[2:].zfill(block_len)
    perm = []
    for pos in range(len(table)):
        perm.append(block_str[table[pos]-1])
    return int(''.join(perm), 2)

def generate_round_keys_64(C0, D0):
    # returns dict of 16 keys (one for each round)
    tr = int(entry4.get())
    round_keys = dict.fromkeys(range(0,tr+1))
    lrot_values = []
    for j in  range(tr+1):
        lrot_values.append(random.randint(1, 2))

    # left-rotation function
    lrot = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

    # initial rotation
    C0 = lrot(C0, 0, 56)
    D0 = lrot(D0, 0, 56)
    round_keys[0] = (C0, D0)

    # create 16 more different key pairs
    for i, rot_val in enumerate(lrot_values):
        i+=1
        Ci = lrot(round_keys[i-1][0], rot_val, 56)
        Di = lrot(round_keys[i-1][1], rot_val, 56)
        round_keys[i] = (Ci, Di)

    # round_keys[1] for first round
    #           [16] for 16th round
    # dont need round_keys[0] anymore, remove
    del round_keys[0]

    # now form the keys from concatenated CiDi 1<=i<=16 and by apllying PC2
    for i, (Ci, Di) in round_keys.items():
        Ki = (Ci << 56) + Di
        round_keys[i] = permutation_by_table_64(Ki, 112, PC2_64) # 56bit -> 48bit

    return round_keys



#------------------------------------------------------------------
#Converts string to int and performs encryption
def result_encryption():
    n = int(entry5.get())
    key_inp = entry2.get()
    msg_inp = entry3.get()
    m = ''.join(format(ord(i), 'b') for i in msg_inp)
    k = ''.join(format(ord(i), 'b') for i in key_inp)

    if n == 16:
        return encrypt_16(m, k)
    elif n == 64:
        return encrypt_64(m, k)
    elif n == 32:
        return encrypt_32(m, k)
    
# Converts string to int and perfoms decryption
def result_decryption():
    n = int(entry5.get())
    m = ''.join(format(ord(i), 'b') for i in entry2.get())
    k = ''.join(format(ord(i), 'b') for i in entry3.get())
    if n == 16:
        return encrypt_16(m, k, True)
    elif n == 32:
        return encrypt_32(m, k, True)
    elif n == 64:
        return encrypt_64(m, k, True)

#This function encrypts the message
def result_encrypt_display():
    ans = result_encryption()
    encrypt_result = tk.Text(master=window, height=1, width=50)
    encrypt_result.grid(column = 1, row = 6)
    encrypt_result.insert(tk.END, str(ans))

#This function encrypts message
def result_decrypt_display():
    ans = result_decryption()
    decrypt_result = tk.Text(master=window, height=1, width=50)
    decrypt_result.grid(column = 1, row = 7)
    decrypt_result.insert(tk.END, str(ans))

#----BUTTONS----

button1 = tk.Button(text = "Encrypt", command = result_encrypt_display)
button1.grid(column = 0, row = 6)

button2 = tk.Button(text = "Decrypt", command = result_decrypt_display)
button2.grid(column = 0, row = 7)

window.mainloop()