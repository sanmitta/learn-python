import requests
r = requests.get('https://raw.githubusercontent.com/sanmitta/learn-python/master/mydata.txt')

results_dict = {}
#results_dict = {key: [] for key in uniquenames} # initialize

for i in r.iter_lines():
    name, monies = i.decode("utf-8").split()
    if name not in results_dict:
        results_dict[name] = [] # first will be counter
    results_dict[name].append(monies)
    
for i in {k: v for k, v in sorted(results_dict.items(), key=lambda item: len(item[1]), reverse=True)}: #dictionary comprehension
    print(i, len(results_dict[i]),sorted(results_dict[i], reverse=True)[:5])

# for x in results_dict.values():
#     x[1].sort(reverse=True)

#print(results_dict)

# print(name, " - " , sorted(results_dict.get(name), reverse=True))



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
