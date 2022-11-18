# Calculate Average Temperature
# Step1 --> Asking for number of days
daysNum = int(input("How many day's Temperature? "))
totalTemp = 0
# use of list 
temp = []
for i in range (daysNum):
    days = int(input(f'High Temperature of Day {str(i+1)} is:'))
    temp.append(days)
    totalTemp +=temp[i]
    
avg = round(totalTemp/daysNum,2)
print(f"\nAverage = {avg}")

# to print number of days greater then average 

high = 0
for i in temp:
    if (i>avg):
        high+=1
print(f'{high} days are Above Average Temperature')
    