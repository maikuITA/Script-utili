################################################################################################################################
# IMPORT
################################################################################################################################

import os, sys, codecs

################################################################################################################################
# FUNZIONI
################################################################################################################################

# funzione per fancy print
def fancy_print(s):
    sos = ""
    for i in range(len(s)):
        sos += str(s[i]) + " "
    print(sos)

# funzione per fancy print
def fancy_print_bande(s):
    sos = ""
    for i in range(len(s)):
        sos += "B" + str(s[i]) + " "
    print(sos)

# funzione per fancy print con format accapo
def fancy_print_enter(s, input_bande):
    sos = ""
    for i in range(len(s)):
        sos += "B" + str(input_bande[i]) + " = " + str(s[i]) + "\n"
    print(sos)

################################################################################################################################
# PROGRAMMA
################################################################################################################################

# 0.1 Clear in base all'OS
clear = ""
if sys.platform == "windows": clear = "cls" # cls per windows
else: clear = "clear" # clear per altri SO

# 1.0 Input
input_bande = []
raw = 0
cbk = 0
os.system(clear)
while True:
    try:
        raw = int(input('[!] Inserisci il numero della banda: '))
        print("")
        cbk = 0
        input_bande.append(raw)
        os.system(clear)
    except ValueError:
        break

input_bande.sort()

# 1.1 Lista delle bande supportate in base all'input_bande
bande = []
for i in range(len(input_bande)):
    foo_band = bin(input_bande[i])
    bande.append(foo_band)

# 1.2 Output
os.system(clear)
print("[!] Ecco le bande selezionate:")
fancy_print_bande(input_bande)
print("")
print("[!] Codifico e sommo le bande...")
somma_bande = bin(sum(input_bande))
print(somma_bande)

# 2.0 Scrittura su file con timestamp

fname = 'output/output_combo_%s.txt'%datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
try:
    f = open(fname, 'x')
    f.write("[!] Ecco le bande selezionate:")
    f.write(fancy_print_bande(input_bande))
    f.write("")
    f.write("[!] Codifico e sommo le bande...")
    f.write(somma_bande)
    f.close()
    print("File .txt creato con successo")
except:
    print("Errore nella creazione del file .txt")