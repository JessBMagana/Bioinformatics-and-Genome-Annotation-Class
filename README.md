# Bioinformatics-and-Genome-Annotation-Class
A San Francisco State University course on bioinformatics and 
genome annotation using Python and Bash (Biol 638/738).

This repository holds all of the lessons in the course.

Lab01:
This is the first lesson. This lesson includes four python scripts that
introduces the student to Object Oriented Programing.

    helloMe.py: Creates an object of the class Announcer to print out a name.
  
    helloAgain.py: Creates an object of the class Person to represent a person.
  
    myBio.py: Creates an object of the class Person to build and present a person's biography.
  
    countATBugs.py: Creates an object of the class dnaString that counts the number of
    A and T nucleotides of a given DNA sequence. The script also contains errors that
    the student must find and fix.
  
    countNucleotides.py: Creates an object of the class dnaString that counts
    the number of nucleotides in a given DNA sequence.
  
Lab02:
This is the second lesson. This lesson includes four Python scripts that teaches the
student how to manipulate data types.

    seqCleaner.py: This program cleans up a DNA sequence by removing ambiguous bases
    (denoted by "N") and outputs the "cleaned" sequence, replacing the ambiguous parts
    with a count in {}'s.
    
    fastqParse.py: This program will parse the sequence name information of a
    FASTQ formatted file.
    
    coordinateMathSoln.py: This program takes three sets of atomic coordinates, then
    calculates the bond lengths and angles.
    
    converter.py: This program uses mappings to convert sequence information between 
    different amino acid representations. This includes the 3-letter codon code
    (RNA and DNA), the one letter amino acid code and the 3-letter amino acid code.
    
Lab03:
This is the third lesson. This lesson includes a single Python program called 
nucParams.py that takes a FASTA file as input and calculates the nucleotide content,
the sequence length, the GC content and the amino acid composition. Directions for
this lesson are found in the file 'lab03.pdf'.

NCBI_Activity:
This is the fourth lesson. This lesson introduces the student to the National Center
for Biotechnology Information (NCBI). The student also learned how to download files
through the terminal using the command wget. Directions for the lesson and the links 
to the files are found in the file 'NCBI_Activity.pdf'. This lesson contains two parts.

    Part 1:
        The student must use their nucParams.py script from Lab03 on the FASTA genome 
        file for the homo sapien reference genome GRCh38.p13.
    
    Part 2:
        The student must create a program that extracts the gene sequences from a 
        reference genome. The gene locations are stored in a 'general feature format'
        (GFF) file.

Lab04:
This is the fourth lesson. In this lesson, the student will investigate and hypothesize
the origin of an ancient DNA sample. This lesson contains three sam files that contain
reference genomes for either cow, sheep, or deer. The student will compare the ancient
DNA sample with these three reference genomes and figure out which animal it is closely
related to. 
