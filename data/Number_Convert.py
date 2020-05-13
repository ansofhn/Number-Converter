ulang = 'Y'
while ulang == 'Y' or ulang == 'y' or ulang == 'YES' or ulang == 'yes':
    print ('\n','='*14,'\n','NUMBER CONVERT',' by: Ansofhn','\n','='*14,'\n')
    print (' 1. Decimal','\n','2. Biner','\n','3. Octal','\n','4. Hexadesimal','\n')
    pilihan = int (input('What do you want to convert? (1-4) : '))
    while pilihan >4 or pilihan <1:
        print('\n"Sorry, your input is wrong.."\n')  
        pilihan = int(input('Re-enter numbers: '))  
    if pilihan == 1:
        print ('\n','='*26,'DESIMAL NUMBERS CONVERSION','='*26,'\n')
        desimal = int(input('Enter Decimal numbers: '))
        biner = (bin(desimal))[2:] 
        oktal = (oct(desimal))[2:] 
        hexadesimal = (hex(desimal))[2:]
        print ('\n','='*25,'\n','Biner         :',biner,'\n','Octal         :',oktal,'\n','Hexadesimal   :',hexadesimal,'\n','='*25,'\n')        
    elif pilihan == 2:
        print ('\n','='*28,'CONVERSION OF BINARY NUMBERS','='*28,'\n')
        biner = int(input('Enter Biner numbers: '),2)
        oktal = (oct(biner))[2:]
        hexadesimal = (hex(biner))[2:]
        print ('\n','='*25,'\n','Decimal       :',biner,'\n','Octal         :',oktal,'\n','Hexadesimal   :',hexadesimal,'\n','='*25,'\n')
    elif pilihan == 3:
        print ('\n','='*27,'CONVERSION OF OKTAL NUMBERS','='*27,'\n')
        oktal = int(input('Enter Octal numbers: '),8)
        biner = (bin(oktal))[2:]
        hexadesimal = (hex(oktal))[2:]
        print ('\n','='*25,'\n','Decimal       :',oktal,'\n','Biner         :',biner,'\n','Hexadesimal   :',hexadesimal,'\n','='*25,'\n')
    elif pilihan == 4:
        print ('\n','='*29,'HEXADESIMAL NUMBER CONVERSION','='*29,'\n')
        hexadesimal = int(input('Enter Hexadesimal numbers: '),16)
        biner = (bin(hexadesimal))[2:]
        oktal = (oct(hexadesimal))[2:]
        print ('\n','='*25,'\n','Decimal       :',hexadesimal,'\n','Biner         :',biner,'\n','Octal         :',oktal,'\n','='*25,'\n')
    print('='*45)
    ulang = input ('Do you want to continue? (Y/N): ')
    if ulang == 'N' or ulang == 'n' or ulang == 'no' or ulang == 'NO':
        print("\nProgram Ends, Thank you for using this program\n")
        break