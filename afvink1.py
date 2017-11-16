'''
auteur: Anton Ligterink
datum: 16-11-2017
Titel: afvinkopdracht 1
'''

def lees_inhoud():
    '''
    input: leeg
    output: een 2 lijsten(headers en sequenties) en een variable met het aantal haken.
    functie: leest de inhoud van een bestand en deel de inhoud op in twee lijsten, telt ook het aantal haken
    '''
    bestand = open('alpacarna','r')
    headers = []
    seqs = []
    y = bestand.readlines()
    aantallines = 0
    seq = ''
    aantalhaken = 0
    for line in y:
        line=line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
            aantalhaken +=1
        else:
            seq += line.strip()
            seqs.append(seq)
    return headers, seqs, aantalhaken

def is_dna(seqs):
    '''
    input: seqs, een lijst met sequenties
    output: dna, een boolean
    functie: kijkt of het bestand volledig bestaat uit DNA
    '''
    dna = False
    lengte = 0
    n_t = 0
    for seq in seqs:
        for n in seq:
            lengte += 1
            if n == 'A':
                n_t += 1
            if n == 'T':
                n_t += 1
            if n == 'G':
                n_t += 1
            if n == 'C':
                n_t += 1

    if n_t == lengte:
            dna = True
    return dna

def knipt(seqs_g):
    '''
    input: seqs_g, een sequentie
    output: enzymenlijst, een lijst met enzymennamen die voorkomen in de sequentie seqs_g en een boolean, badline, die aangeeft of er een slecht geformateerde lijn in de enzymen file voorkomt
    functie: kijkt naar een lijst met enzymen en vergelijkt deze met de sequentie om te kijken of ze overeen komen
    '''
    try:
        bestand2 = open('enzymen.txt')
    except FileNotFoundError:
        print('The file was not found')
    enzymenlijst = []
    for line in bestand2.readlines():
        line = line.replace('\n','')
        try:
            enzym, seq = line.split() 
            seq = seq.replace('^','')
            if seq in seqs_g:
                enzymenlijst.append(enzym)
            badline = False
        except:
            badline = True
    return enzymenlijst, badline

def main():
    '''
    input: een zoekwoord
    output: een lijst met headers waarin het zoekwoord voorkomt met daaronder de namen van de enzymen die voorkomen in de sequentie bijbehorend bij de header, geeft ook errors als deze voorkomen.
    functie: kijkt welke enzymen voorkomen in de sequenties behorend bij de lijst met headers is gemaakt op basis van het zoekwoord.
    '''
    try:
        headers, seqs, aantalhaken = lees_inhoud()
    except FileNotFoundError:
        print('The file was not found')
        raise SystemExit
    if aantalhaken < 1:
        print('File is not in FASTA format, please insert a FASTA formatted file')
        raise SystemExit
    dna = is_dna(seqs)
    if dna == True:
        zoekwoord = input('Wat is het zoekwoord?:')
        lmh = []
        for x in headers:
            if x.find(zoekwoord) > 1:
                lmh.append(x)
                    
        lmn = [i for i,x in enumerate(headers) if x in lmh]
        for g in lmn:
            print('\n')
            print(headers[g])
            kniplijst, badline = knipt(seqs[g])
            print('wordt geknipt door:')
            print(kniplijst)
    if dna == False:
        print('The file does not contain DNA')
        raise SystemExit
    if dna != True:
        if dna != False:
            print('is_dna does not return a boolean')
            raise SystemExit
    if badline == True:
        print('Badly formatted line found in file')

main()
