def comp(a,b):
    if ( a<= 0 or a >= 2**32): 
        print("A doit etre codée sur 4 octets")
    if ( b<= 0 or b >= 2**32): 
            print("B doit etre codée sur 4 octets")

    return a ^ b 


def XDDD (c):

    IV = 0b01111000011000010111001101101000
    
    # Rembourrage par  des 100000...

    chaine = bytearray(c.encode('utf-8')) 

    print ("Avant rembourrage: ", list(chaine))  
    Taille = len(chaine)

    chaine.append(0x80) # j'aurais pu mettre 0b10000000
    s = len(chaine)

    while (s % 4 !=0 ): 
             
         chaine.append(0)
         s = len(chaine)

    Taille_bits = Taille * 8   #taille du msg en bits 
    chaine.extend(Taille_bits.to_bytes(4, 'big')) # On encode cette taille sur 4 octets 

    print("Apres rembourage: ",list(chaine))
    print ("Taille de la chaine: ", s)

    s = len(chaine)
    #Segmentation et Hashchage
    
    T=[]

    for i in range ( 0, s, 4 ):

        bloc = int.from_bytes(chaine[i:i+4],'big')  #Ici j'essaie de constituer les blocs qui vont etre injectés dans la fonction comp
        print ("voici un bloc esteban: ", bloc)
        if (i==0):
             T.append(comp(IV,bloc))
        else : 
             T.append (comp(T[-1],bloc))

    return hex(T[-1])  

Hash = XDDD("Hello") 
print ("le hash de mon texte est:", Hash)