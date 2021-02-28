def bubblesort(a,n,b,m): #sorting elements in ascending order 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if a[j] > a[j+1] : 
                a[j],a[j+1] =a[j+1],a[j]
                b[j],b[j+1]=b[j+1],b[j]
    return
#to open file
File_object = open("sample_input.txt","r")
l=File_object.readlines() 
#print(l)
l[0].replace("\n","")
te=l[0].split(":")
emp_num=int(te[-1])
goods=[]
prices=[]
min_diff=2147483647
min_index=0
for i in range(4,len(l)):
    l[i]=l[i].replace("\n","")
    
    te=l[i].split(':')
    
    goods.append(te[0])
    prices.append(int(te[1]))
bubblesort(prices,len(prices),goods,len(goods))
#print(prices)
#print(len(prices))


i=0
while(i+emp_num<=len(prices)):
    diff=prices[i+emp_num-1]-prices[i]
    if(diff<min_diff):
        min_diff=diff
        min_index=i
   # print(i)
    i+=1
#print(min_index,min_diff)
         
# writing to file 


file1 = open('output.txt', 'w') 
l= ["The goodies selected for distribution are:\n", "\n"] 
file1.writelines(l)
for i in range(emp_num):
    s=goods[min_index+i]+':'+str(prices[min_index+i])+'\n'
    file1.write(s) 

w="And the difference between the chosen goodie with highest price and the lowest price is"+" "+str(min_diff)
file1.write(w)
file1.close() 




