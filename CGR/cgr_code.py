import collections
from matplotlib import cm
import pylab
import math
from urllib.request import urlopen

# Counting K_mers
def count_kmers(sequence, k):
    # any new key introduced to the dictionary
    # will have default value zero
    d = collections.defaultdict(int)
    # loop over number of possible kmers ((L - K) + 1) or (L -(K-1))
    # reporting number of occurence for each kmer
    for i in range(len(sequence) - (k - 1)):
        # introducing new keys , setting their values
        # updating old keys' value
        d[sequence[i:i + k]] += 1
        # {"att":3,"acg":1,....}
#    for key in d.keys():
#        if "N" in key:
#            del d[key]
    return d


# Calculating Prob of each k-mer [agt:25%, etc... ]
def probabilities(kmer_count, k, squence):
    # any new key introduced to the dictionary
    # will have default value 0.0
    kmer_prop = collections.defaultdict(float)
    squenceLength = len(squence)
    for key, value in kmer_count.items():
        kmer_prop[key] = float(value) / (squenceLength - k + 1)
    return kmer_prop



# calculating CGR Arrary
def chaos_game_representation(probabilities, k):
        chaos = []
        array_size = int(math.sqrt(4 ** k))
        for i in range(array_size):
            chaos.append([0] * array_size)
        # initializing position of current location and determining the last location of the array
        maxx = array_size
        maxy = array_size
        posx = 1
        posy = 1
        for key, value in probabilities.items():
            for char in key:
                # in respect of
                #  A = upper left quadrant
                #  C = lower left quadrant  then (maxY/2)
                #  G = upper right quadrant then (maxX/2)
                #  T = lower right quadrant then (maxX/2 or maxY/2)
                
                if char == "T":
                    posx += maxx / 2
                    posy += maxy / 2
               # (in case of RNA )  U = lower right quadrant then (maxX/2 or maxY/2)
                if char == "U":
                    posx += maxx / 2
                    posy += maxy / 2
                elif char == "C":
                    posy += maxy / 2
                elif char == "G":
                    posx += maxx / 2
                maxx = maxx / 2
                maxy /= 2
            # chaos array that is 2 dimentional and will be showed in graphical representation
            chaos[int(posy - 1)][int(posx - 1)] = value
            maxx = array_size
            maxy = array_size
            posx = 1
            posy = 1
        return chaos



def graph(chaos_kx, kmer_size):
    pylab.figure(1)
    pylab.title('Chaos game representation for {}-mers'.format(kmer_size))
    pylab.imshow(chaos_kx, interpolation='nearest', cmap=cm.gray_r)
    pylab.axis("off")
    pylab.show()


# method that shows the graph
def CGR(sequence):
    kmer_size=int(input("Enter size of k-mer \n"))
    fx = count_kmers(sequence, kmer_size)
    fx_prob = probabilities(fx, kmer_size, sequence)
    chaos_kx = chaos_game_representation(fx_prob, kmer_size)
    graph(chaos_kx, kmer_size)







#check file is fasta or fastq 
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
    CGR(seq)





# input from file 
def File_method():
    # your file is local then give its name or path   
    try:
         # cheking the file_from_user is not empty
        local_file = input("Enter the (name or the path) of the file  ")
        check_file_type_AorQ(local_file)
    except:
        print("wrong path or name of the file \n")
          
#input from url
def URL_method():
    url = input('''\nEnter your file's URL 
    \t(it is recommended to search by seq accession number in the database )\n''')
    response = urlopen(url)
    file_from_url = response.read().decode("utf-8", "ignore")
    with open("newDNAFile", 'w+') as DnaFl:
                    nf= DnaFl.write(file_from_url)
    check_file_type_AorQ('newDNAFile')
    

# Reading the file from the user and defining its type
def text_method():
    while True:    
        user_input= (input("Enter the sequence text "))
        if user_input.isdigit():
            print("enter  STRINGS  only")
            break
            CGR(user_input)
    
    
file_url_text = input('''please enter F for file or U for url or T for text:(DNA OR RNA) ''').upper()
if file_url_text == "F":
        File_method()
elif file_url_text == "U":
        URL_method()
elif file_url_text == "T":
        text_method()
         
else:
            print("\nNot recognized input")

   