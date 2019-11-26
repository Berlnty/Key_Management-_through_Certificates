import random
import generate_private_public
from elsig_hash import egGen
import RSA

Bob_id = 0
Alice_key = tuple()
Alice_id = 0
bob_n = 0
bob_e = 0
signed_m = ""


def key_id_Generation():
    global Alice_id
    Alice_id = random.randint(1000001, 10000000)
    # to be from other ranges generated in cert (to be unique)
    # generate private/public pair of Alice
    global Alice_key
    Alice_key = generate_private_public.generate_User_public_private_key()
    print(generate_private_public.generate_rsa_keys())
    Alice_key[1] = Alice_key[1] + generate_private_public.generate_rsa_keys()
    print(Alice_key)
    return

def send_id_key_toAuthority():
    Alice_key_file = open("AliceKey_ToAuthority.txt", "w")
    # Alice send her public key and her id to authority
    Alice_key_file.write(str(Alice_id) + ' ' + str(Alice_key[1][0]) + ' ' + str(Alice_key[1][1]) + ' ' + str(
        Alice_key[1][2]) + ' ' + str(Alice_key[1][3]) + ' ' + str(Alice_key[1][4]))
    # id , q, a, ya ,n, e
    Alice_key_file.close()
    return


def send_id_toBob():
    Alice_key_file = open("AliceKey_ToBob.txt", "w")
    # Alice send her id to Bob
    Alice_key_file.write(str(Alice_id))
    Alice_key_file.close()
    return


def verify_certificate():
    # read Bob id
    BobKey_ToAlice_file = open("BobKey_ToAlice.txt", "r")
    global Bob_id


    Bob_id = BobKey_ToAlice_file.readline()

    # read Bob certificate
    send_cert_ToAlice_file = open("send_cert_ToAlice.txt", "r")
    Bob_certificate = send_cert_ToAlice_file.readline()
    BobKey_ToAlice_file.close()

    # decrypt Bob_certificate by public key of Authority and get Bob id
    public_keyAuthority_file = open("KeyAuthority.txt", "r")

    autority_n = int(public_keyAuthority_file.readline())
    autority_e = int(public_keyAuthority_file.readline())

    de_key = RSA.decrypt(int(Bob_certificate), autority_n, autority_e).split(' ',6)

    print(de_key)
    # Compare get_id from decryption with Bob_id
    if (de_key[0] == Bob_id):
     print("certificate verified")
     global bob_n
     global bob_e
     bob_n = int(de_key[4])
     bob_e = int(de_key[5])
     return True
    else:
     print("wrong certificate")
     return False


def signature(message):
    # 1 0 = q   1 1 =a  1 2= ya  1 3=n 1 4=e  ,   0=xa
    s1, s2 = egGen(Alice_key[1][0], Alice_key[1][1], Alice_key[0], message)


    global signed_m
    signed_m = str(message) + ' ' + str(s1) + ' ' + str(s2)
    return


def encrypt_message():
    # read key of bob
    print("signed message",signed_m)
    encrypted_message = RSA.encrypt(signed_m, bob_e, bob_n)

    # write to file
    message_file = open("message.txt", "w")
#    message_file.codecs.StreamWriter.write(self,str(encrypted_message).encode('utf-8'))
    message_file.write(str(encrypted_message))
    message_file.close()
    return



#key_id_Generation()
########################################################################################################
# print("Alice_id : ",Alice_id)
# print("Alice_key : ",Alice_key)

