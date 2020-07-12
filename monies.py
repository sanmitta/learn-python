my_file = open('mydata.txt', 'r')
file_lines = my_file.readlines()
my_file.close()

rawnamelist = []
for line in file_lines:
    rawnamelist.append(line.split()[0]) # read index o from each line to capture names
uniquenameslist = list(set(rawnamelist)) # remove duplicates

results_dict = {}
results_dict = {key: [] for key in uniquenameslist} # initialize

#print(results_dict) #this is fine

for x in range(len(uniquenameslist)): # search for the same key in the whole file
    for line in file_lines:
        #print("line.split()[0]: " , line.split()[0])
        #print("x:", x)
        if line.split()[0] == uniquenameslist[x]:
            results_dict[uniquenameslist[x]].append(line.split()[1])
    print(uniquenameslist[x], " - " , sorted(results_dict.get(uniquenameslist[x]), reverse=True))



# results_dict[uniquenameslist[x]].append(len(results_dict[uniquenameslist[x]])) 
# I don't need this as I can get length at any time
# i.e. last item in the list (dictionary's values) is the count of monies received by the person

# print(results_dict)

# print(uniquenameslist)

# I had to write a little python snippet at work today, and that gave me an idea of a small problem for this group:

# Take a look at this file:
# https://github.com/skgbanga/Sandbox/blob/master/tutorial/data

# Each line of this file represents some pocket money given to that person. e.g. 
# "shalabh 97"

# means that 97$ were given to Shalabh. 

# Now your task is:
# print a list of people in decreasing order of the number of times they have received the pocket money
# you should also print how many times they have received pocket money
# top 5 pocket monies they have received