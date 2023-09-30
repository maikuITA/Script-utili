################################################################################################################################
# IMPORT
################################################################################################################################

import os
from datetime import datetime

################################################################################################################################
# FUNZIONI
################################################################################################################################

# Fanculo le funzioni hex() e bin()
def binToHexa(n):
   
    # Da binario a int
    num = int(n, 2)
     
    # Da int a esadecimale
    hex_num = format(num, 'x')
    return(hex_num)

# funzione per fancy print
def fancy_print(s):
    sos = ""
    for i in range(len(s)):
        sos += str(s[i]) + " "
    print(sos)
    
# funzione per fancy output
def fancy_output(s):
    sos = ""
    for i in range(len(s)):
        sos += str(s[i]) + " "
    return sos

################################################################################################################################
# PROGRAMMA
################################################################################################################################

# Lista delle bande supportate
band_1  = "0000000000000000000000000000000000000000000000000000000000000001"
band_3  = "0000000000000000000000000000000000000000000000000000000000000100"
band_7  = "0000000000000000000000000000000000000000000000000000000001000000"
band_20 = "0000000000000000000000000000000000000000000010000000000000000000"
band_38 = "0000000000000000000000000010000000000000000000000000000000000000"
band_41 = "0000000000000000000000001000000000000000000000000000000000000000"
blank   = "00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000"

# Input
bands = []
raw = 0
cbk = 0
os.system('cls')
while True:
    if cbk > 1:
        break
    try:
        raw = int(input('Inserisci il numero della banda: '))
        print("")
        cbk = 0
        bands.append(raw)
        os.system('cls')
    except ValueError:
        os.system('cls')
        print('Inserisci un int.')
        print("(invio di nuovo per uscire) - (inserisci un int per andare avanti)")
        print("")
        cbk += 1

os.system('cls')
print("Ecco le bande selezionate:")
fancy_print(bands)
print("")

################################################################################################################################
# Step 1: Conversione in esadecimale
################################################################################################################################

# formo la stringa in binario
bins = 0
for i in range(len(bands)):
    match(bands[i]):
        case 1:
            bins += int(band_1)
        case 3:
            bins += int(band_3)
        case 7:
            bins += int(band_7)
        case 20:
            bins += int(band_20)
        case 38:
            bins += int(band_38)
        case 41:
            bins += int(band_41)

# output e conversione in esadecimale
print("Ecco il numero in binario: ")
print(bins)
f_bins = bins
print("")
print("Ecco il numero in esadecimale: ")
bins = binToHexa(str(bins))
print(bins)
h_bins = bins
print("")

################################################################################################################################
# Step 2: Formazione delle coppie e inversione della stringa; output su file con timestamp
################################################################################################################################

# variabili
coppie = []
count = 0
sos = ""

# aggiungo 0 in cima in base alla lunghezza
for j in range(16-len(bins)):
    bins = "0" + bins

# formo un array di coppie
for i in range(len(bins)):
    if i == 0: sos = str(bins[i])
    elif len(sos) == 2:
        coppie.append(sos)
        count = 0
        sos = str(bins[i])
    else:
        sos += str(bins[i])
        count += 1
    #TESTING
    #print("i: " + str(i))
    #print("count: " + str(count))
    #print("sos: " + str(sos))
coppie.append(sos) # completo la stringa

# output
print("Coppie:")
fancy_print(coppie)
f_coppie = coppie
print("")

# inverto l'array
coppie = coppie[::-1] 

# output
print("Coppie invertite:")
fancy_print(coppie)
print("")

# output su file con timestamp

print(os.path.exists("output/"))
fname = 'output/output_combo_%s.txt'%datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
f = open(fname, 'x')

f.write("Ecco le bande selezionate:\n")
f.write(fancy_output(bands))
f.write("\n")
f.write("Ecco il numero in binario:\n")
f.write(fancy_output(str(f_bins)))
f.write("\n")
f.write("Ecco il numero in esadecimale:\n")
f.write(fancy_output(str(h_bins)))
f.write("\n")
f.write("Coppie:\n")
f.write(fancy_output(f_coppie))
f.write("\n")
f.write("Coppie invertite:\n")
f.write(fancy_output(coppie))

f.close()