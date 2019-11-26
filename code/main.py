import Bob
import Alice
import Authority

def main():

    print("Before Alice 1")
    # Alice
    Alice.key_id_Generation()
    Alice.send_id_key_toAuthority()
    Alice.send_id_toBob()

    # Bob
    Bob.key_id_Generation()
    Bob.send_id_key_toAuthority()
    Bob.send_id_toAlice()

    # certificate authourity
    Authority.generate_certificate()

    message = "hithere"
    # Alice
    Alice.signature(message)
    Authority.send_cert_ToAlice()
    print(Alice.verify_certificate())
    Alice.encrypt_message()

    #Bob
    Bob.decrypt_message()
    Authority.send_cert_ToBob()
    print(Bob.verify_certificate())
    print(Bob.verify_signature())




if __name__ == '__main__':
    main()