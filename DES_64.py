
IP_64 = []
for j in  range(128):
    IP_64.append(random.randint(1, 128))

IP_INV_64 = []
for j in  range(128):
    IP_INV_64[IP_64[i]-1]=i+1;

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
    #assert isinstance(msg, int) and isinstance(key, int)
    #assert not msg.bit_length() > 128
    #assert not key.bit_length() > 128

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

#k = 0x0e329232ea6d0d730e329232ea6d0d73 # 64 bit
#k2 = 0x133457799BBCDFF1133457799BBCDFF1
#m = 0x87878787878787878787878787878787
#m2 = 0x0123456789ABCDEF0123456789ABCDEF

#def prove(key, msg):
#   print('key:       {:x}'.format(key))
#  print('message:   {:x}'.format(msg))
#cipher_text = encrypt(entry2.get(), entry2.get())
# print('encrypted: {:x}'.format(cipher_text))
#plain_text = encrypt(entry1.get(), entry2.get(), decrypt=True)
    #print('decrypted: {:x}'.format(plain_text))

#prove(entry2.get(), entry1.get())
