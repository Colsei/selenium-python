#if else loop
greeting = "Good whatever"
a = 9

if greeting == " Good whatever":
    print(" condition matches")
    print(" ")
else:
    if a < 10:
        print(" a is good")
        print(" ")
    else:
        print(" condition does not match")
print("if else condition is competed")

print("****************************")

#for loop
obj = [2,3,6,45]
for i in obj:
    print(i*3/2)

print("****************************")

#sum of First Natural numbers
summation = 0
for j in range(1,6):
#range(i) -> 0 to i-1
#range(i,j) -> i to j-1
#range(i,j,k) -> i then i+k until not bigger than j
    print(j)
    summation = summation + j
print("sum of these number above is:")
print(summation)

print("****************************")

it = 3
while it<5:
    if it == 4:
        #continue
        print(it)
    it = it+1
#continue: to continue the loop
#break: to break the loop