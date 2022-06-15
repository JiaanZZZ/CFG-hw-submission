import random
lottery_number=['1','2','3','4','5','6','7']
rand=str(random.randint(1000000,1999999))
count=0
for i,x in enumerate(lottery_number):
    if rand[i]==x:
        count+=1

prize_dict={

    '3':'20',
    '4':'40',
    '5':'100',
    '6':'10000',
    '7':'1000000'

}

if count<3:
    print("No prize")
else:
    print("You have won "+prize_dict[count]+" pounds")