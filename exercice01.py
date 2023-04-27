# Function to change sequence to complementary sequence
def seq_comp():
    sequence = ["A", "C", "G", "T", "T", "A", "G", "C", "T", "A", "A", "C", "G"]
    for seq in sequence:
        if seq == "A":
            print("T")
        elif seq == "T":
            print("A")
        elif seq == "C":
            print("G")
        elif seq == "G":
            print("C")
        else:
            print(seq)

# Print out result
seq_comp()