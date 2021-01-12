
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
    25, 17,  9, 1,
    26, 18, 10, 2,
    27, 19, 11, 3,
    31, 23, 15, 7,  
    30, 22, 14, 6, 
    29, 21, 13, 5,
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
    #assert isinstance(msg, int) and isinstance(key, int)
    #assert not msg.bit_length() > 32
    #assert not key.bit_length() > 32

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

#    k = 0x0e329232 # 64 bit
#   k2 = 0x13345779
#  m = 0x87878787
# m2 = 0x0123CDEF

#    def prove(key, msg):
#       print('key:       {:x}'.format(key))
#      print('message:   {:x}'.format(msg))
#cipher_text = encrypt(entry2.get(), entry2.get())
#     print('encrypted: {:x}'.format(cipher_text))
#plain_text = encrypt(entry1.get(), entry2.get(), decrypt=True)
    #    print('decrypted: {:x}'.format(plain_text)) 
#prove(entry2.get(), entry1.get())
