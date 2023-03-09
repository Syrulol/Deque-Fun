from collections import deque
import random
import base64

a_string = 'In3ed3dAstR1nGw1thM0r3entr0pyb3f0reIt3st3dth1sbuT1mun0rig1n4l'
B64_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
default_rotating_list = [deque(B64_CHARS) for _ in a_string]


# Index character wheels to the character string passed.
def align_deques(subject_string, rotating_list):
    for idx, deqobj in enumerate(rotating_list):
        rotation_value = -abs(deqobj.index(subject_string[idx]))
        deqobj.rotate(rotation_value)
    return rotating_list


# Parse the deques for characters along the observation index.
def get_string_from_deques(deq_list):
    return ''.join(char for char, *_ in deq_list)


# Rotate all deques by an integer specified in rotnum.
def rotate_deqlist(deq_list, rotnum):
    [deqs.rotate(rotnum) for deqs in deq_list]
    return deq_list


# Rotate a single deque in a list by index.
def rotate_one_deq(deq_list, index, rotation):
    deq_list[index].rotate(rotation)
    return deq_list


# Randomly rotate all deques, returns a deque list and a key for each deque's rotation.
def rotate_all_random(deq_list):
    encodinglist = []
    for deqs in deq_list:
        randval = random.randint(0, len(B64_CHARS))
        encodinglist.append(randval)
        deqs.rotate(randval)
    return deq_list, encodinglist


# Flatten a key list.
def flatten_key(keylist: list) -> str:
    return '/'.join(str(char) for char in keylist)


# Decode a randomly rotated deque list using the string and key value.
def decode(instring: str, inkey: list):
    decodedeq = align_deques(instring, default_rotating_list)
    for indx, numbers in enumerate(inkey):
        decodedeq[indx].rotate(-abs(numbers))
    return get_string_from_deques(decodedeq)


aligned = align_deques(a_string, default_rotating_list)
randroated, key = rotate_all_random(aligned)
print(get_string_from_deques(randroated) + ''.join(hex(values) for values in key))
print(''.join(hex(values) for values in key))
print(decode(get_string_from_deques(randroated), key))

align_the_deques = align_deques(a_string, default_rotating_list)
rotate_the_deques = rotate_deqlist(align_the_deques, 35)
flatten_the_deques = get_string_from_deques(rotate_the_deques)
byte_the_deque = bytes(flatten_the_deques, 'ASCII')
b64_the_deque = base64.b64encode(byte_the_deque)
print(a_string)
print(flatten_the_deques)
print(b64_the_deque)
