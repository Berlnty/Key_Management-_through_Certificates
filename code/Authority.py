import RSA
from Crypto.Util import number
import os
import random

Alice_id = ""
Bob_id = ""


def generate_certificate():
    cert_file = open("certificates.txt", "w")
    cert_file.write("id certificate \n")

    public_keyAuthority_file = open("KeyAuthority.txt", "w")

    n_length = 1000
    p = number.getPrime(n_length, os.urandom)
    q = number.getPrime(n_length, os.urandom)

    Key_Authority_n, Key_Authority_e, Key_Authority_d = RSA.Key_generation(p, q)  # return n,e,d

    # publish(write) public key of authority to all users
    public_keyAuthority_file.write(str(Key_Authority_n) + '\n')  # first line is n
    public_keyAuthority_file.write(str(Key_Authority_e))  # second line is e

    for i in range(0, 2):
        # generate random id
        rand_id = random.randint(2, 1000000)
        # generate random public key
        rand_publicKey = random.randint(2, 1000000)

        certificate = RSA.encrypt(str(rand_publicKey), Key_Authority_d,
                                  Key_Authority_n)  # encrypt of user public key with private key of authority

        cert_file.write(str(rand_id) + ' ' + str(certificate) + '\n')

        # decrypt certificate to know public key of a user
        # publicKey_user=RSA.decrypt(certificate,Key_Authority_n,Key_Authority_e)

        # read Alice id , key and Bob id ,key to append their certificates to the certificates file

        ######################################## Alice ############################################

        # read Alice id and public key
        Alice_file = open("AliceKey_ToAuthority.txt", "r")
        Alice_info = Alice_file.readline()  # id , q, a, ya ,n, e
        data_a = Alice_info.split(' ', 6)
        # generate certificate for Alice
        Alice_certificate = RSA.encrypt(Alice_info, Key_Authority_d, Key_Authority_n)
        global Alice_id
        Alice_id = data_a[0]
        # write Alice cert to certificates file
        cert_file.write(str(data_a[0]) + ' ' + str(Alice_certificate) + '\n')

    ###########################################################################################

    ######################################## Bob ##############################################

    # read Bob id and public key
    Bob_file = open("BobKey_ToAuthority.txt", "r")
    Bob_info = Bob_file.readline()

    data_b = Bob_info.split(' ', 6)
    # generate certificate for Alice
    Alice_certificate = RSA.encrypt(Bob_info, Key_Authority_d, Key_Authority_n)

    global Bob_id
    Bob_id = data_b[0]


    # write Alice cert to certificates file
    cert_file.write(str(data_b[0]) + ' ' + str(Alice_certificate) + '\n')

###########################################################################################

    cert_file.close()


def send_cert_ToBob():
    i = 0
    Alice_cert = ""
    with open('certificates.txt') as f:
        print("Enter")
        for line in f:
            if i != 0:
                line_info = line.split(' ', 2)
                if (line_info[0] == Alice_id):
                    Alice_cert = line_info[1]

            i += 1

    send_cert_ToBob_file = open("send_cert_ToBob.txt", "w")  # write Alice certificate
    send_cert_ToBob_file.write(Alice_cert)


def send_cert_ToAlice():
    i = 0
    Bob_cert = ""
    with open('certificates.txt') as f:
        print("Enter")
        for line in f:
            if i != 0:
                line_info = line.split(' ', 2)
                if (line_info[0] == Bob_id):
                    Bob_cert = line_info[1]

            i += 1

    send_cert_ToAlice_file = open("send_cert_ToAlice.txt", "w")  # write Bob certificate
    send_cert_ToAlice_file.write(Bob_cert)
    return


