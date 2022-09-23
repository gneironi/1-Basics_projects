#Mean, Median and Mode are the fundamentals of statistics used 
#in almost every domain where we deal with numbers.

#TODO: calculate the mean, median and mode


#MEAN: average value of all the values in a dataset.

list1 = [10,12,20,20,12,30,25,42,20]
mean = sum(list1)/len(list1)
print("The mean is: ", mean)

#MEDIAN: is the middle value among all the values in sorted order.

list1 = [10,12,20,20,12,30,25,42,20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2-1]
    median = (m1 + m2) / 2
else:
    median = list1[len(list1)//2]
print("The median is: ", median)

#MODE: is the most frequently occurring value amoing all the dataset.

list1 = [10,12,20,20,12,30,25,42,20]
frequency = {}
for i in list1:
    frequency.setdefault(i,0)
    frequency[i]+=1

frequent = max(frequency.values())
for i,j in frequency.items():
    if j == frequent:
        mode = i
print("The mode is: ", mode)


#tools used:
# list, buit-in modules (sum, sort), dicts, for lopps