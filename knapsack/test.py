from knapsack import *
from terminaltables import AsciiTable




# brutalforce
# string="""4 8
# 2 4
# 1 3
# 4 6
# 4 8"""

# multi dynamic
string="""5 7
2 4
1 3
4 6
4 8
3 7"""




xd = Knapsack.load(string)
print(xd)
print('\n\nBRUTALFORCE')
print(Knapsack.printBackpack(xd.brutalforce()))
print('\n\nGREEDY')
print(Knapsack.printBackpack(xd.greedyAlgorithm()))
print('\n\nDYNAMIC')
print(Knapsack.printBackpack(xd.dynamicAlgorithm()))