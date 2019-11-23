import os


def fileTest():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    data_path = os.path.join(dir_path, '../FileTest/data.txt')
    print(data_path)

    file = open(data_path, 'r') 
    for line in file: 
        print(line) 

if __name__ == '__main__':
    fileTest()