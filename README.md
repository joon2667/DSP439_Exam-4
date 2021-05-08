# DSP439_Exam-4
Dr. Rachel Schwartz
Joon Hong Lee - 100571475

May 7th, 2021

Creating a function that calculates the lingustic complexity of a sequence

Repository for DSP 439 Exam 4

This repository is made for DSP 439 Exam 4 submission. The repository contains:

Exam4.py

Exam4_test.py

test_sequences.txt

Exam4.py is the main component of counting kmers and calculating linguistic complexity. The correct output will result in a .txt file that has the name of the sequence. Within the .txt file, user can observe the linguistic complexity score and the dataframe of observed kmers and possible kmers.

# Functions inside the Exam4.py:

count_kmers(k, sequence) <- this function calculates the possible kmers and observed kmers

create_k_pd(k, sequence) <- this function aggregates the result from count_kmers into one data frame

calc_ling_complex(k, sequence) <- this fuction calculates the linguistic complexity of assigend sequence and k value
 
main() <- this function generates the output file from taking in the given .txt sequences. It will generate an output file that has the name of the sequence and inside it contains linguisitc complexity and the data frame of counted kmers.

# Exam4_test.py

Exam4_test.py is to test if my Exam4.py script has any error. It contains pre-inputted scenario and if it finds a descriptency between expected value and actual it will out put an error. My test result in testing 6 different scenarios.

# test_sequence.txt

test_sequence.txt this is an example .txt file that I have added. it contains 5 lines of sequence.
