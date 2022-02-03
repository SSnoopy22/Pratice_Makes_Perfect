import math
import pandas as pd
import matplotlib.pyplot as plt


the_list = []

i = 6

for num in range(0,7):
    print(math.comb(6,num))
    a = math.comb(6,num)*(math.pow(0.7,i-num))*(math.pow(0.3,num))
    print(a)
    the_list.append(a)

ts = pd.Series(the_list)

ts.plot()
plt.show()

