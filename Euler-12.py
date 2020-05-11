#Ethan Caldecott
#Final Project

#Project Rosalind : A Rapid Introduction to Molecular Biology
"""
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""


def MolecularBio(s):
    A=0                   #Base A counter starts at 0
    C=0                   #C Counter starts at 0
    G=0                   #G counter starts at 0
    T=0                   #T counter starts at 0
    for i in s:           #Add 1 to A counter every time a A is detected in the string
        if i == 'A':
            A = A + 1
    for i in s:           #Add 1 to C counter every time a C is detected in the string
        if i == 'C':
            C = C + 1
    for i in s:           #Add 1 to G counter every time a G is detected in the string
        if i == 'G':
            G = G + 1       
    for i in s:           #Add 1 to T counter every time a T is detected in the string              
        if i == 'T':
            T = T + 1
    print("Number of A's: " + str(A))  #Prints the total amount of A's
    print("Number of C's: " + str(C))  #Prints the total amount of C's
    print("Number of G's: " + str(G))  #Prints the total amount of G's
    print("Number of T's: " + str(T))  #Prints the total amount of T's

if __name__ == '__main__':
    MolecularBio('ACGT')                                                                   #Should return 1A, 1C, 1G, and 1T
    MolecularBio('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC') #Should return 20A's, 12C's, 17G's, 21T's.

    
    
#Project Euler Question 12 (Sudo Code)

they input x which is number of divisors

def final value(x)
n=0
input number of divisors(x)
if x == divisors(triangle number) needed it to test low to hi
  return triangle number
else 
 add 1 to n re-run

def Divisors
  find math equation for number how to find number of divisor in any number

def Triangle Number(n)
  triangle number = ((n)(n+1)/2)

Answer return is triangle number

if __name__ == '__main__'
    x = 500




