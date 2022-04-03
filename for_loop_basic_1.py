# 1) Basic - Print all integers from 0 to 150.
for x in range(0,150):
    print(x)
    
# 2) Multiples of Five - Print all the multiples of 5 from 5 to 1,000
count = 5
while (count < 1000):
    if(count % 5 == 0):
        print(count)
    count += 1
    
# 3) Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,100):
    if(x%10 == 0):
        print("Coding Dojo")
    elif(x%5 == 0):
        print("Coding")
    else:
        print(x)
        
# 4) Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(1,500000,2):
    sum += x
print(sum)

# 5) Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
start = 2018
while(start > 0):
    print(start)
    start -= 4
    
# 6) Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum + 1):
    if(x%mult == 0):
        print(x)