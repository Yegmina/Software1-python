seasons=("winter", "spring", "summer", "autumn")

n=int(input("Enter a month number: "))

season= ((n+2)//3)-1
print(seasons[season])

"""
December - 1
January - 2
February - 3

March - 4
April - 5
May - 6

June - 7
July - 8
August - 9

September - 10
October - 11
November - 12
"""

