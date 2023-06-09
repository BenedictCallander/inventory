import os
def cleardir(dir):
    for filename in os.listdir(dir):
        file_path=os.path.join(dir, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
def getprintlist(directory, output_file):
    filenames = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            filenames.append(filename)

    with open(output_file, 'w') as file:
        file.write('\n'.join(filenames))