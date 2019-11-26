import random
import generate_private_public
import RSA
from elsig_hash import egVer

Alice_id = 0
Bob_key = tuple()  # xa,q,a,ya,n,e,d
Bob_id = 0

alice_n = 0
alice_e = 0
message = ""
alice_p = 0
alice_a = 0
alice_ya = 0


def key_id_Generation():
    # assign id
    global Bob_id

    Bob_id = random.randint(10000001, 100000000)  # to be from other ranges generated in cert (to be unique)
    # generate private/public pair of Bob
    global Bob_key
    Bob_key = generate_private_public.generate_User_public_private_key()
    Bob_key[1] = Bob_key[1] + generate_private_public.generate_rsa_keys()
    return



def send_id_key_toAuthority():
    Bob_key_file = open("BobKey_ToAuthority.txt", "w")
    # Bob send her public key and her id to authority
    Bob_key_file.write(
        str(Bob_id) + ' ' + str(Bob_key[1][0]) + ' ' + str(Bob_key[1][1]) + ' ' + str(Bob_key[1][2]) + ' ' + str(
            Bob_key[1][3]) + ' ' + str(Bob_key[1][4]))
    # id , q, a, ya ,n, e
    Bob_key_file.close()
    return


def send_id_toAlice():
    Bob_key_file = open("BobKey_ToAlice.txt", "w")
    # Bob send her id to Bob
    Bob_key_file.write(str(Bob_id))
    Bob_key_file.close()
    return


def verify_certificate():
    # read Alice id
    AliceKey_ToBob_file = open("AliceKey_ToBob.txt", "r")
    global Alice_id
    Alice_id = AliceKey_ToBob_file.readline()

    # read Alice certificate
    send_cert_ToBob_file = open("send_cert_ToBob.txt", "r")
    Alice_certificate = send_cert_ToBob_file.readline()
    AliceKey_ToBob_file.close()

    # decrypt Alice_certificate by public key of Authority and get Alice id
    public_keyAuthority_file = open("KeyAuthority.txt", "r")

    autority_n = int(public_keyAuthority_file.readline())
    autority_e = int(public_keyAuthority_file.readline())

    de_key = RSA.decrypt(int(Alice_certificate), autority_n, autority_e).split(' ',6)

    print(de_key)
    # Compare get_id from decryption with Bob_id
    if (de_key[0] == Alice_id):
        print("certificate verified")
        global alice_n
        alice_n = int(de_key[4])
        global alice_e
        alice_e = int(de_key[5])
        global alice_p
        alice_p = int(de_key[1])
        global alice_a
        alice_a = int(de_key[2])
        global alice_ya
        alice_ya = int(de_key[3])
        return True

    else:
        print("wrong certificate")
        return False






def decrypt_message():
    message_file = open("message.txt", "r", encoding = "ISO-8859-1", errors='ignore')
    d_message = message_file.readline()
   

    #d_message ="123"
    global message
    message = RSA.decrypt(int(d_message), Bob_key[1][3], Bob_key[1][5])

    message_file.close()
    return





def verify_signature():
    # 1 0 = q   1 1 =a  1 2= ya  1 3=n 1 4=e 5=d ,   0=xa
    temp = message.split(' ')
    tn= len(temp)
    m = ''
    s1 = int(temp[tn-1])
    s2 = int(temp[tn-2])
    for x in range(0,len(temp)-2):
        m += (temp[x] +' ')
    
    verify = egVer(alice_p, alice_a, alice_ya, s1, s2, m)
    recieved_msg = open("recieved_msg.txt", "w")
    recieved_msg.write(m)
    recieved_msg.close()
    return verify, m






