import re
import hashlib
import json # Au final, j'ai utilisé une autre méthode

#-----------------------------------------
#         CREATION DU MOT DE PASSE
#-----------------------------------------
def enter_password():
    password = input("Please, enter your password : ")
    return password

#-----------------------------------------
#       VERIFICATION DU MOT DE PASSE
#-----------------------------------------
def check_password(check):
    # On crée une variable error_value = True, à chaque fois qu'il manque quelque 
    # chose dans le mot de passe, celle-ci prend la valeur False
    error_value = True

    # Liste des caractères spéciaux : 
    special_char =['$', '@', '#', '%', '*', '&', '~', '§', '!', '?', '/', '>', '<', ',', ';', '.', ':', 'µ', '£']

    # Boucle de vérification :
    while True:
        # Longueur :
        if len(check) < 8:
            error_value = False
            print("Password with at least 8 character !")

        # Majuscule :
        elif not re.search("[A-Z]", check):
            error_value = False
            print("Password with at least one upper case !")
        
        # Minuscule :
        elif not re.search("[a-z]", check):
            error_value = False
            print("Password with at least one lower case !")

        # Chiffres :
        elif not re.search("[0-9]", check):
            error_value = False
            print("Password with at least one digit !")
        
        # Caractères spéciaux :
        elif not any(char in special_char for char in check):
            error_value = False
            print ("Password with at least one special character !")

        return error_value

#-----------------------------------------
#        AJOUTER UN MOT DE PASSE
#-----------------------------------------
def add_password():
    while True:
        password = enter_password()
        if check_password(password) == True:
            print("Your password is : ", password)
            return password
        else:
            continue

#-----------------------------------------
#       ENCRYPTER LE MOT DE PASSE
#-----------------------------------------
def encrypt(code):
    code_encrypt = hashlib.sha256(code.encode('utf-8')).hexdigest()
    return code_encrypt

#-----------------------------------------
#        MOT DE PASSE EXISTANT ?
#-----------------------------------------
def double_password(check):
    f = open("save.json", "r") # On ouvre cette fois le fichier en mode lecture
    list_password = f.read() 
    print(list_password)
    if check in list_password:
        print("Sorry, this password cannot be used")
        main()
    else:
        add_to_file(check)
        print("Your password is authorised")

#-----------------------------------------
# JSON (OU DU MOINS MA METHODE ALTERNATIVE)
#-----------------------------------------
def add_to_file(new_code):

    f = open("save.json", "a") #"a" permet d'écrire à la fin du fichier (a pour append)
    f.write("'") # Pour que le fichier puisse être lu comme une liste
    f.write(new_code) # On ajoute le nouveau mot de passe
    f.write("'\n") # On saute une ligne pour plus de visibilité
    f.close() # On ferme le fichier

#-----------------------------------------
#      CONSULTER LES MOTS DE PASSE
#-----------------------------------------
def read_password():
    display = open("save.json", "r")
    print(display.read())

#-----------------------------------------
#                  MAIN
#-----------------------------------------
def main():
    print(
        """
    __________________________________
    What do you want to do ?
        1 - Add a password
        2 - See the encrypted password
        3 - Leave
    __________________________________
    """)

    choice = int(input("Enter a number : "))
    if choice == 1:
        password_not_encrypted = add_password()
        encrypt(password_not_encrypted)
        double_password(encrypt(password_not_encrypted))
    elif choice == 2:
        read_password()
    elif choice == 3:
        quit("See you soon !")


main()
