# 1. Basic 
"""
for int in range(150):
    print(int)
"""
# 2. Multiples of Five 
"""
for i in range (5, 1000, 5):
    print(i)
"""

# 3. Counting, the Dojo Way 
"""
for i in range (1, 100):
    if(i%10==0):
        print("Coding Dojo")
    elif(i%5==0):
        print("Coding")
    else:
        print(i)
"""

# 4. Whoa. That Sucker's Huge
"""
sum = 0
for i in range(1, 500000, 2):
    sum = sum + i
print(sum)
"""

# 5. Countdown by Fours 
"""
for i in range(2018, 0, -4):
    print(i)
"""

#6 Flexible Counter
lowNum = 20
highNum = 99
mult = 7
for x in range(lowNum, highNum, mult):
    print(x)