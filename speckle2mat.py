
start_speck = []
stop_speck = []

start_count = 0
stop_count = 0

f = open('Brid_speckles_low_thresh.csv',"r")
data = f.read().split("\n")
f.close()

for n,items in enumerate(data):
    if data[n].startswith('#%start'):
        print('start')
        print(n)
        start_speck.append(n+1)
        start_count += 1
    if data[n].startswith('#%stop'):
        print('stop')
        stop_speck.append(n)

for i in range(len(start_speck)-1):
    specklefile = 'Speckle_%d.txt' % i
    with open(specklefile,"w") as sp:
        output_str = '\n'.join(data[start_speck[i]:stop_speck[i]])
        sp.write(output_str)

##    for i in start_count:
##        data[start_count[i]:stop_count[i]]

##        
##        if items[0].isdigit(): #first char is a digit?
##            print(data[n])
        

        
### Below opens file, reads line by line, and outputs number of speckles
##f = open('Brid_speckles2.txt',"r")
##
##count = 0
##for line in f.read().split('\n'):
##    if line.startswith('#%s'):
##        count = count + 1
##        specklefile = 'Speckle_%d.txt' % count
##        print(line)
##        print(count)
##        
##        with open(specklefile,"w") as sp:
##            sp.write(line)
##
##        
##f.close()



# Below is just me learning to use python.
##for line in f.readlines():
##    print line
##    

##def method4():
##  str_list = []
##  for num in xrange(loop_count):
##    str_list.append(`num`)
##  return ''.join(str_list)

##
##import sys
##data=open(sys.argv[1]).read().split("\n")
##for n,items in enumerate(data):
##    if items[0].isdigit(): # check first character is a digit, ie equivalent to [0-9]
##        data[n-1]= data[n-1]+items
##        data.pop(n)

