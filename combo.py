################################################################################################################################
# IMPORT
################################################################################################################################

import os, sys
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

# funzione per fancy print con format accapo
def fancy_print_enter(s, input_bande):
    sos = ""
    for i in range(len(s)):
        sos += "B" + str(input_bande[i]) + " = " + str(s[i]) + "\n"
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

# TClear in base all'OS
clear = ""
if sys.platform == "windows": clear = "cls"
else: clear = "clear"

# Input
input_bande = []
raw = 0
cbk = 0
os.system(clear)
while True:
    try:
        raw = int(input('Inserisci il numero della banda: '))
        print("")
        cbk = 0
        input_bande.append(raw)
        os.system(clear)
    except ValueError:
        break

input_bande.sort()

# Lista delle bande supportate in base all'input_bande
bande = []
for i in range(len(input_bande)):
    foo_band = ""
    foo_band += (int(input_bande[i])-1) * "0"
    foo_band += "1"
    foo_band += (64-len(foo_band)) * "0"
    foo_band = foo_band[::-1]
    bande.append(foo_band)

# OUTPUT TEST
os.system(clear)
print("Ecco le bande selezionate:")
fancy_print(input_bande)
print("")

print("Codifica...")
fancy_print_enter(bande, input_bande)

################################################################################################################################
# Step 1: Conversione in esadecimale
################################################################################################################################

# formo la stringa in binario
bins = 0
for i in range(len(bande)):
    bins += int(bande[i])

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
# Step 2: Formazione delle coppie e inversione della stringa
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

################################################################################################################################
# Step 3: Output su file con timestamp
################################################################################################################################

# FILE TXT

# output su file con timestamp
fname = 'output/output_combo_%s.txt'%datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
try:
    f = open(fname, 'x')
    f.write("Ecco le input_bande selezionate:\n")
    f.write(fancy_output(input_bande))
    f.write("\n")
    f.write("Ecco le bande codificate:\n")
    f.write(fancy_output(bande))
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
    print("File .txt creato con successo")
except:
    print("Errore nella creazione del file .txt")

# FILE BIN

