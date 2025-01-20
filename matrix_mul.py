# Import necessary libraries
import pandas as pd
import numpy as np

# Load data, commented out as path is not provided
# data = pd.read_csv('path/to/data')

# Define the Prices matrix 
Prices = [[300, 500],
          [1000, 120.85]]

# Define the Array2 list
Array2 = [200, 100]

# Initialize empty list to store results
Ans = []
# (300*200 + 500*100) as an example calculation

# Calculate the dot product for each row in Prices with Array2
for i in range(len(Prices)):
    row_sum = 0     # Initialize sum for current row


    # Iterate through each element in the current row
    for j in range(len(Prices[0])):

        # Multiply each element in the current row with corresponding element in Array2 
        # and add the product to the row_sum
        row_sum += Prices[i][j] * Array2[j]

    # Append the total sum for this row to the answer list
    Ans.append(row_sum)

# Print the final results
print("Results:", Ans)