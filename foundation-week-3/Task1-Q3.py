year=input("what is the year of the book?")
century=year[:2]
decade=year[2]


if century=='18':
    output_century="Eighteenth Century"
elif century=='19':
    output_century="ninteenth Century"

decades=['00s','tens','twenties','thirties','forties','fifties','sixties','seventies','eighties','ninties']
output_decade=decades[int(decade)]
print(output_century+", "+output_decade)