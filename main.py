from wand.image import Image
import os


origin = "./origin"
destination = "./destination"

for directory in os.listdir(origin):
    print(directory)
    os.mkdir(f"{destination}/{directory}")

    print(len(os.listdir(f"{origin}/{directory}")))
    
    counter = 0

    for file in os.listdir(f"{origin}/{directory}"):
        if os.path.splitext(file)[-1].lower() == ".heic":
            print(file)

            counter += 1
            print(counter)

            img=Image(filename=f"{origin}/{directory}/{file}")
            img.format='jpg'
            img.save(filename=f"{destination}/{directory}/" + file.replace(".HEIC",".JPG"))
            img.close()
            file = file.replace(".HEIC",".JPG")
        else:
            os.popen(f"cp {origin}/{directory}/{file} {destination}/{directory}/{file}")
