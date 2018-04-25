import numpy as np
import csv
# Create an array of 256 zeroes
one_hot = np.zeros(256,dtype=int)
# Open the output file
with open("one_hot_1_short.csv","w") as out_file:
    # Create a csv writer
    writer = csv.writer(out_file)
    # Open the input file
    with open("book_1_short.txt",'r') as book:
        # Read till the end of book
        while True:
            # Read one character at a time
            c = book.read(1)
            # Break if it is empty (indicating eof)
            if not c: break
            # Convert into int
            c = ord(c)
            # Mark the required one as 1
            one_hot[c] = 1
            # Write onto file
            writer.writerow(one_hot)
            # Reset to default
            one_hot[c] = 0