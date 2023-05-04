import os


d1 = {}
d2 = {}

origin = "./origin"
destination = "./destination"

for directory in os.listdir(origin):
    d1[directory] = []

    for file in os.listdir(f"{origin}/{directory}"):
        d1[directory].append(file)
    
for directory in os.listdir(destination):
    d2[directory] = []

    for file in os.listdir(f"{destination}/{directory}"):
        d2[directory].append(file)

for i in range(0, len(d1.keys())):
    print(list(d1.keys())[i] + " " + list(d2.keys())[i])
    print(str(len(d1[list(d1.keys())[i]]))  + " " + str(len(d2[list(d2.keys())[i]])))
