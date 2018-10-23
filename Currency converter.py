suma=float(input())
word1=str(input())
word2=str(input())
temp=suma

if word1=='USD':
    temp=suma*1.79549
elif word1=='EUR':
    temp = suma * 1.95583
elif word1=='GBP':
    temp=suma*2.53405

if word2=='USD':
    print(str((temp/1.79549).__round__(2))+" USD")

elif word2=='EUR':
    print(str((temp/1.95583).__round__(2))+" EUR")

elif word2=='GBP':
    print(str((temp/2.53405).__round__(2))+" GBP")

elif word2=='BGN':
    print(str((temp/1).__round__(2))+" BGN")
