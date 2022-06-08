# #The integer chaos game (iCGR) representation of DNA sequences: encoding and decoding
#
# Changchuan Yin, Ph.D.
# Dept. of Mathematics, Statistics and Computer Science
# University of Illinois at Chicago
# Chicago, IL 60607
# USA
#
# Email cyin1@uic.edu, cyinbox@gmail.com
# Last update 10/26/2017
#
# Citation
# Yin, C.(2018). Encoding DNA sequences by integer chaos game representation. Journal of Computational Biology.

from urllib.request import urlopen


# ------------------------------------------------------------------------------
# Helper function: get the nucleotide based on the signs of integers x and y
# ------------------------------------------------------------------------------
def getNucleotide(x, y):
    if (x > 0 and y > 0):
        nucleotide = 'A'
    elif (x > 0 and y < 0):
        nucleotide = 'G'
    elif (x < 0 and y > 0):
        nucleotide = 'T'
    elif (x < 0 and y < 0):
        nucleotide = 'C'
    else:
        nucleotide = 'N'

    return nucleotide


# ------------------------------------------------------------------------------
# Helper function: get iCGR vertices for given signs of integers x and y
# ------------------------------------------------------------------------------
def getCGRVertex(x, y):
    Nx = 0;
    Ny = 0;

    if (x > 0 and y > 0):
        Nx = 1
        Ny = 1
    elif (x > 0 and y < 0):
        Nx = 1
        Ny = -1
    elif (x < 0 and y > 0):
        Nx = -1
        Ny = 1
    elif (x < 0 and y < 0):
        Nx = -1
        Ny = -1
    else:
        Nx = 0
        Ny = 0

    return Nx, Ny


# ------------------------------------------------------------------------------
# iCGR Encoding: encode a DNA sequence into three integers (iCGR encoding)
# Input: a DNA sequence
# Outputs: three integers, x_n, y_n, and n
# ------------------------------------------------------------------------------
def encodeDNASequence(seq):
    A = [1, 1]
    T = [-1, 1]
    C = [-1, -1]
    G = [1, -1]
    a = 0
    b = 0
    x = []
    y = []
    n = len(seq)

    if seq[0] == 'A':
        a = int(A[0])
        b = int(A[1])
    elif seq[0] == 'T':
        a = int(T[0])
        b = int(T[1])
    elif seq[0] == 'C':
        a = int(C[0])
        b = int(C[1])
    else:
        a = int(G[0])
        b = int(G[1])

    x.append(a)
    y.append(b)

    for i in range(1, n):
        if seq[i] == 'A':
            a = int(x[i - 1]) + (2**i)
            b = int(y[i - 1]) + (2**i)
        elif seq[i] == 'T':
            a = int(x[i - 1]) - (2**i)
            b = int(y[i - 1]) + (2**i)
        elif seq[i] == 'C':
            a = int(x[i - 1]) - (2**i)
            b = int(y[i - 1]) - (2**i)
        else:
            a = int(x[i - 1]) + (2**i)
            b = int(y[i - 1]) - (2**i)

        x.append(a)
        y.append(b)

    x_n = int(x[n - 1])
    y_n = int(y[n - 1])

    return x_n, y_n, n


# ------------------------------------------------------------------------------
# iCGR Decoding: decode three integers to a DNA sequence
# Inputs: three integers, x_n, y_n, and n
# Outputs: the DNA sequence represented by the three integers
# ------------------------------------------------------------------------------
def decodeDNASequence(x_n, y_n, n):
    x = [0] * n
    y = [0] * n
    x[n - 1] = x_n
    y[n - 1] = y_n

    seq = []
    for i in range(n - 1, -1, -1):
        nt = getNucleotide(x[i], y[i])
        seq.insert(i - n + 1, nt)
        Nx, Ny = getCGRVertex(x[i], y[i])
        x[i - 1] = int(x[i]) - ((2**i) * Nx)
        y[i - 1] = int(y[i]) - ((2**i) * Ny)
    else:
        DNASeq = ''.join(seq)
        return DNASeq
#====================================================================================================
#MAIN
#Homo sapiens SMPX gene for alternative protein SMPX, isolate 15610, GenBank: HF583935.1
#https://www.ncbi.nlm.nih.gov/nuccore/HF583935.1?report=fasta


def check_file_type_AorQ(file=None):
    file_type = input(
                "Is your file FASTA OR FASTQ \n A for FASTA \n Q for FASTQ \n").upper()  # FASTA OR FASTQ
    seq = ""
    with open(file,'r') as f:
      file=f.read()
    if file_type == "A":
        seq = "".join(file.split("\n")[1:])
    elif file_type == "Q":
        seq_reads = []
        data_list = file.split("\n")  # a list of every line in the file
        for i in range(1, len(data_list), 4):
            seq_reads.append(data_list[i])  # only seq reads
        seq = "".join(seq_reads)  # as a full text(joint_seq_reads)
    x_n, y_n, n = encodeDNASequence(seq)
    print(x_n)
    print(y_n)
    print(n)


def File_method():
    try:
        # cheking the file_from_user is not empty
        local_file = input("Enter the (name or the path) of the file  ")
        check_file_type_AorQ(local_file)
    except:
        print("wrong path or name of the file \n")
    pass

def text_method():
    global x_n, y_n, n
    user_input = input("Enter the sequence text ")
    x_n, y_n,n = encodeDNASequence(user_input)
    print(x_n,y_n,n)
    

def URL_method():
    url = input('''\nEnter your file's URL 
        \t(it is recommended to search by seq accession number in the database )\n''')
    response = urlopen(url)
    file_from_url = response.read().decode("utf-8", "ignore")
    with open("newFile", 'w+') as Fl:
        nf = Fl.write(file_from_url)
    check_file_type_AorQ('newFile')

try:
    processType = input("please enter\nE for encoding\nD for decoding ")
    if processType.upper() == 'E':
        file_url_text = input('''please enter F for file or U for url or T for text:(DNA OR RNA) ''').upper()
        if file_url_text == "F":
            File_method()
        elif file_url_text == "U":
            URL_method()
        elif file_url_text == "T":
            text_method()

        else:
            print("\nNot recognized input")
    elif processType.upper() == "D":
        x_n = int(input("please enter 'X' value x_coordinate"))
        y_n = int(input("please enter 'Y' value y_coordinate "))
        n = int(input("please enter 'N' value for length"))
        decoded_seq = decodeDNASequence(x_n, y_n, n)
        print('Decoded DNA sequence:', decoded_seq)
except:
    print("Somthing went wrong")









