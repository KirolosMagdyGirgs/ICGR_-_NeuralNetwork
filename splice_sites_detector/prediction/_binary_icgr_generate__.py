import math
import numpy as np
from keras.models import load_model
'''
Input: the desired sequences to predict their class in fastq file.
Output: txt file with only the sequences.
'''
def file_handling(fastq_file_name):

    with open(fastq_file_name, mode='r') as in_file, \
        open('{}_trimmed.txt'.format(fastq_file_name[:-6]), mode='w') as out_file:

        lines= in_file.readlines()

        for i in range(1, len(lines), 4):
            line= lines[i].strip()
            out_file.write(f'{line}\n')

'''
Input: sequence string.
Output: icgr encoding.
'''
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
            a = int(x[i - 1]) + int(math.pow(2, i))
            b = int(y[i - 1]) + int(math.pow(2, i))
        elif seq[i] == 'T':
            a = int(x[i - 1]) - int(math.pow(2, i))
            b = int(y[i - 1]) + int(math.pow(2, i))
        elif seq[i] == 'C':
            a = int(x[i - 1]) - int(math.pow(2, i))
            b = int(y[i - 1]) - int(math.pow(2, i))
        else:
            a = int(x[i - 1]) + int(math.pow(2, i))
            b = int(y[i - 1]) - int(math.pow(2, i))

        x.append(a)
        y.append(b)

    x_n = int(x[n - 1])
    y_n = int(y[n - 1])

    return x_n, y_n

'''
Input: txt file with only the sequences.
Output: txt file with icgr encoding for all sequences.
'''
def generate_ints(trimmed_file_name):
    with open(trimmed_file_name, mode='r') as in_file, \
        open('{}_icgr.txt'.format(trimmed_file_name[:-4]), mode='w') as out_file:

        for line in in_file:

            x, y= encodeDNASequence(line)
            out_file.write(f'{x} {y}\n')

'''
Input: txt file with icgr encoding for all sequences.
Output: txt file with icgr encoding in binary form.
'''
def convert_to_binary(icgr_file_name):

    with open(icgr_file_name, mode='r') as in_file, \
        open('{}_bin.txt'.format(icgr_file_name[:-4]), mode='w') as out_file:

        for line in in_file:
            line= line.strip()
            twoVals= line.split(' ')

            for num in twoVals:
                num= abs(int(num))
                bin= f'{num:0401b}'
                bin= bin.replace("", " ")[1: -1]
                out_file.write(f'{bin} ')
            out_file.write(f'\n')


'''
predict function
    loads the weigths of trained cnn and predict classes for entered data.
Input: the desired sequences to predict their class in the form of binary icgr encodeing for each sequence in seperate row.
Output: the predicted classes as np.array,
        each row is a sequence, 
        1st element of each sub-array is probability of being belongs to 'Acceptor splice site',
        2nd element of each sub-array is probability of being belongs to 'Donor splice site',
        3rd element of each sub-array is probability of being belongs to 'Non splice site'.
'''
def predict(bin_file_name):

    to_be_predictedData = np.loadtxt(bin_file_name)
    to_be_predictedData = to_be_predictedData.reshape(-1, 2, 401)

    cnn_model= load_model('CNN14.h5')
    prediction= cnn_model.predict(to_be_predictedData)
    return prediction


'''
show_results function
    shows summary of class prediction.
Input: the probability array of class prediction.
Output: summary of class prediction.
'''
def show_results(prediction):
    
    length= len(prediction)
    count= {'Acceptor': [0], 'Donor': [0], 'Non': [0]}

    for i in range(length):

        sub= prediction[i]
        maxx= max(sub)
        maxx_index= sub.index(maxx)

        if maxx_index==2:
            result= 'Non'
        elif maxx_index==0:
            result= 'Acceptor'
        elif maxx_index==1:
            result= 'Donor'

        count[result].append(i+1)



    non_count= len(count['Non'])-1
    acceptor_count= len(count['Acceptor'])-1
    donor_count= len(count['Donor'])-1

    print('Summary')
    print('--------')
    print('Total of {} non-splice sites found.'.format(non_count))
    print('Total of {} acceptor splice sites found.'.format(acceptor_count))
    print('Total of {} donor sites found.'.format(donor_count))
    print('--------')
    print('Acceptor sites found in sequences:')

    for i in count['Acceptor']:
        if i!=0:
            print(i, end =", ")

    print('\nDonor sites found in sequences:')

    for i in count['Donor']:
        if i!=0:
            print(i, end =", ")



if __name__ == "__main__":

    file_name= input('Enter fastq file to be classified: ')
    file_handling(file_name)
    generate_ints(f'{file_name[:-6]}_trimmed.txt')
    convert_to_binary(f'{file_name[:-6]}_trimmed_icgr.txt')

    bin_file_name= f'{file_name[:-6]}_trimmed_icgr_bin.txt'
    prediction= predict(bin_file_name)
    prediction= prediction.tolist()
    show_results(prediction)
