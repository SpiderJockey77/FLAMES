p1 = raw_input("Enter Name1: ").replace(" ",'').lower()
p2 = raw_input("Enter Name2: ").replace(" ",'').lower()

z1 = 0
z2 = 0
final = 0
c = 0

for x in p1:
    if x in p2 and p1.count(x) > 1: 
        z1 += p1.count(x) - 1
        p1.replace(x,'')
    elif x in p2:
        z1 += 1
for y in p2:
    if y in p1 and p2.count(y) > 1:
        z2 += p2.count(y) - 1
        p2.replace(y,'')
    elif y in p1:
        z2 += p2.count(y) 

final = z1+z2
c= final%6

print "Person 1: " + str(z1)
print "Person 2: " + str(z2)
print "Together: " + str(final)
print "Your classification: "
if final == 0: print "No match"
elif c == 0: print "Sweet <3s"
elif c == 1: print "Friends"
elif c == 2: print "Lovers"
elif c == 3: print "Acquaintances"
elif c == 4: print "Marriage"
elif c == 5: print "Enemies"