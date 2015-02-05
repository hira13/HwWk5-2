from __future__ import division 

#this will get the AT content 
def get_at_content(dna, sig_fig=3):
	#Given a variable to hold the dna
    lower_dna = dna 
	#makes dna to uppercase dna letters
    upper_dna = lower_dna.upper()
	#replaces the N in the DNA 
    new_dna = upper_dna.replace( 'N' , '')
	#Prints the length of the DNA 
    length = len(new_dna)
    #Prints the number of As 
    a_count = new_dna.count('A')
    #Prints the number of Ts
    t_count = new_dna.count('T')
    #Prints the number of A and Ts then divides it by length 
    at_content = (a_count + t_count) / length
    #returns the value 
    return round(at_content, sig_fig)



my_at_content = get_at_content('ATGATGGGGATCGTGACTCG',3)
print str(my_at_content)

print get_at_content('ATGGGGGAAAAGCGCGCAAATATAT', 3)

print get_at_content('acccatataggacggtata', 3)

print get_at_content('ATGCGATACCCGANNNCAATNNNATANN', 3)
