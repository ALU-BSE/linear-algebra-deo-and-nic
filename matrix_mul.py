import pandas as pd
import numpy as np

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):

        #Multiple each element in Prices by the corresponding element in Array 2
        row_sum += Prices[i][j] * Array2[j]

    Ans.append(row_sum)

# Print the result
print(Ans)
