# Code César

def cryptage_cesar(message, decalage):
    # L'alphabet utilisé pour le chiffrement, uniquement les majuscules
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # On transforme le message en majuscules pour uniformiser les entrées
    message = message.upper()
    
    # Variable pour stocker le texte crypté
    texte_crypte = ""
    
    # Parcours chaque caractère du message
    for i in range(len(message)):
        lettre = message[i]
        
        # Si le caractère est une lettre de l'alphabet
        if lettre in alphabet:
            # Calcul du décalage, on applique le modulo pour éviter les dépassements de l'alphabet
            nouvelle_lettre = alphabet[(alphabet.index(lettre) + decalage) % len(alphabet)]
            texte_crypte += nouvelle_lettre
        else:
            # Si ce n'est pas une lettre (espace, ponctuation), on la garde telle quelle
            texte_crypte += lettre
    
    # Retourne le message crypté
    return texte_crypte

def decryptage_cesar(texte_crypte, decalage):
    # Définition de l'alphabet pour le déchiffrement
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Conversion du texte crypté en majuscules
    texte_crypte = texte_crypte.upper()
    
    # Variable pour stocker le texte décrypté
    texte_decrypte = ""
    
    # Parcours chaque caractère du texte crypté
    for i in range(len(texte_crypte)):
        lettre = texte_crypte[i]
        
        # Si le caractère est une lettre de l'alphabet
        if lettre in alphabet:
            # Calcul du décalage inverse pour déchiffrer
            nouvelle_lettre = alphabet[(alphabet.index(lettre) - decalage) % len(alphabet)]
            texte_decrypte += nouvelle_lettre
        else:
            # Si ce n'est pas une lettre, on la garde telle quelle
            texte_decrypte += lettre
    
    # Retourne le message décrypté
    return texte_decrypte

# Code Vigenère

def cryptage_vigenere(message, cle):
    # L'alphabet utilisé pour le chiffrement
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Conversion du message et de la clé en majuscules pour une gestion uniforme
    message = message.upper()
    cle = cle.upper()
    
    # Variable pour stocker le texte crypté
    texte_crypte = ""
    
    # Parcours chaque caractère du message
    for i in range(len(message)):
        lettre = message[i]
        
        # Si le caractère est une lettre de l'alphabet
        if lettre in alphabet:
            # On détermine le décalage à partir de la clé, la clé se répète si elle est plus courte que le message
            decalage = alphabet.index(cle[i % len(cle)])
            # Applique le décalage à la lettre du message
            nouvelle_lettre = alphabet[(alphabet.index(lettre) + decalage) % len(alphabet)]
            texte_crypte += nouvelle_lettre
        else:
            # Si ce n'est pas une lettre, on la garde telle quelle
            texte_crypte += lettre
            
    # Retourne le message crypté avec la méthode Vigenère
    return texte_crypte

def decryptage_vigenere(texte_crypte, cle):
    # L'alphabet utilisé pour le déchiffrement
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Conversion du texte crypté et de la clé en majuscules
    texte_crypte = texte_crypte.upper()
    cle = cle.upper()
    
    # Variable pour stocker le texte décrypté
    texte_decrypte = ""
    
    # Parcours chaque caractère du texte crypté
    for i in range(len(texte_crypte)):
        lettre = texte_crypte[i]
        
        # Si le caractère est une lettre
        if lettre in alphabet:
            # Détermine le décalage à partir de la clé, répète la clé si elle est plus courte
            decalage = alphabet.index(cle[i % len(cle)])
            # Applique le décalage inverse pour déchiffrer le message
            nouvelle_lettre = alphabet[(alphabet.index(lettre) - decalage) % len(alphabet)]
            texte_decrypte += nouvelle_lettre
        else:
            # Si ce n'est pas une lettre, on la garde telle quelle
            texte_decrypte += lettre
    
    # Retourne le texte décrypté
    return texte_decrypte

# Partie principale : interaction avec l'utilisateur pour choisir l'opération

# Demande à l'utilisateur quel type de chiffrement il veut utiliser
choix = input("Que voudriez-vous faire ?\n- Taper 1 pour utiliser le Code Cesar ;\n- Taper 2 pour utiliser le Code Vigenre.\n\nChoix : ")

# Boucle principale qui permet de répéter la demande jusqu'à ce que l'utilisateur fasse un choix valide
while True:
    if choix == "1":
        # Si l'utilisateur choisit le Code César
        choix = input("Que voudriez-vous faire ?\n- Taper 1 pour crypter ;\n- Taper 2 pour décrypter.\n\nChoix : ")
        
        if choix == "2":
            # Si l'utilisateur veut décrypter, on lui demande le décalage et le texte à décrypter
            decalage = int(input("\nEntrez le décalage : "))
            texte_crypte = input("Entrez le message à décrypter : ")
            # Appel de la fonction de déchiffrement
            texte_decrypte = decryptage_cesar(texte_crypte, decalage)
            print("\nTexte décrypté :", texte_decrypte)
            break
        
        elif choix == "1":
            # Si l'utilisateur veut crypter, on lui demande le décalage et le message à crypter
            decalage = int(input("\nEntrez le décalage : "))
            message = input("Entrez le message à crypter : ")
            # Appel de la fonction de chiffrement
            texte_crypte = cryptage_cesar(message, decalage)
            print("\nTexte crypté :", texte_crypte)
            break
    
        else:
            # Si l'utilisateur entre un choix invalide, on redemande
            choix = input("Choix invalide. Que voudriez-vous faire ?\n- Taper 1 pour crypter ;\n- Taper 2 pour décrypter.\n\nChoix : ")
        
    elif choix == "2":
        # Si l'utilisateur choisit le Code Vigenère
        choix = input("Que voudriez-vous faire ?\n- Taper 1 pour crypter ;\n- Taper 2 pour décrypter.\n\nChoix : ")
        
        if choix == "2":
            # Si l'utilisateur veut décrypter, on lui demande la clé et le texte à décrypter
            cle = input("\nEntrez la clé : ")
            texte_crypte1 = input("Entrez le message à décrypter : ")
            # Appel de la fonction de déchiffrement
            texte_decrypte = decryptage_vigenere(texte_crypte1, cle)
            print("\nTexte décrypté :", texte_decrypte)
            break
        
        elif choix == "1":
            # Si l'utilisateur veut crypter, on lui demande la clé et le message à crypter
            cle = input("\nEntrez la clé : ")
            message = input("Entrez le message à crypter : ")
            # Appel de la fonction de chiffrement
            texte_crypte = cryptage_vigenere(message, cle)
            print("\nTexte crypté :", texte_crypte)
            break
    
        else:
            # Si l'utilisateur entre un choix invalide, on redemande
            choix = input("Choix invalide. Que voudriez-vous faire ?\n- Taper 1 pour crypter ;\n- Taper 2 pour décrypter.\n\nChoix : ")
    
    else:
        # Si l'utilisateur entre un choix invalide pour le type de chiffrement, on redemande
        choix = input("Choix invalide. Que voudriez-vous faire ?\n- Taper 1 pour utiliser le Code Cesar ;\n- Taper 2 pour utiliser le Code Vigenre.\n\nChoix : ")
