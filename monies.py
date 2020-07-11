my_file = open('mydata.txt', 'r')
file_lines = my_file.readlines()

rawnamelist = []
for line in file_lines:
    rawnamelist.append(line.split()[0]) # read index o from each line to capture names
uniquenameslist = list(set(rawnamelist)) # remove duplicates

results_dict = {}
results_dict = {key: [] for key in uniquenameslist} # initialize

#print(results_dict) #this is fine

for x in range(len(uniquenameslist)): # search for the same key in the whole file
    for line in file_lines:
        print("line.split()[0]: " , line.split()[0])
        print("x:", x)
        if line.split()[0] == uniquenameslist[x]:
            print("hello2")
            results_dict[uniquenameslist[x]].append(line.split()[1])
    results_dict[uniquenameslist[x]].append(len(results_dict[uniquenameslist[x]]))
    # i.e. last value is the count of monies received by the person

print(results_dict)

## print(uniquenameslist)
my_file.close()
