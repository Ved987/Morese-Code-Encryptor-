import Texthide
import Decryption
import dispenc
import Encrypt2
import Encrypt1
import LSB


def menu():
    print("----------Welcome to morse code Encryption----------")
    print("\n Choose one of the following options: \n")
    print("0: First Time Running the Code (Input 0) ")
    print("1: Want to perform Encryption of Text")
    print("2: Want to perform Decryption of text")
    print("3: Want to perform Data Hiding in Text")
    print("4: Want to Extract Data Hidden in Text")
    print("5: Want to perform Data Hiding in Image")
    n = int(input(" Enter Your Choice \n"))
    if n == 0:
        import Morse1
        import Morse2
        import Messages
        print(" The setup to use the Project is ready:")
        menu()
    elif n == 1:
        Message = input("Enter the Secret message \n")
        Encrypt1.main(Message)
        Encrypt2.main()
        dispenc.main()
    elif n == 2:
        list_1 = input("Enter the Encrypted Morse Code:\n")
        Decryption.main(list_1)
    elif n == 3:
        Cover = Texthide.Texthide()
        print("The Secret Cover text is\n" + Cover)
    elif n == 4:
        Cover = input("Enter the Cover Text\n")
        list_1 = Texthide.Text_recover(Cover)
        Decryption.main(list_1)
    elif n == 5:
        a = int(input("1. Encode\n2. Decode\n"))
        if a == 1:
            Data = Texthide.Texthide()
            LSB.encode(Data)

        elif a == 2:
            cover = LSB.decode()
            cover = Texthide.Text_recover(cover)
            Decryption.main(cover)
        else:
            raise Exception("Enter correct input")
    else:
        print("Invalid choice")
    c = input("\nDo you want to Continue? \n")
    if c == 'Y' or c == 'y':
        menu()


menu()
