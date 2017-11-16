def lees_inhoud():
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
    n_t = 0
    randomseq = seqs[1]
    for n in randomseq:
        if n == 'A':
            n_t += 1
        if n == 'T':
            n_t += 1
        if n == 'G':
            n_t += 1
        if n == 'C':
            n_t += 1
    if n_t == len(randomseq):
        dna = True
        return dna
    else:
        dna = False
        return dna

def knipt(seqs_g):
    bestand2 = open('enzymen.txt')
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
