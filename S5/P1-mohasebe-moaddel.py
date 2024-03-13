import csv
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    with open (input_file_name , 'r') as file:
        read = csv.reader(file)
        l_esmnomre = []
        for row in read:
            name= row.pop(0)

            l_nomre = []
            for nomre in row:
                l_nomre.append(float(nomre))
            
            miyangin = mean(l_nomre)
            l_esmnomre.append((name ,miyangin))
    with open (output_file_name , 'w') as out_file:
        write = csv.writer(out_file)
        while len(l_esmnomre) != 0 : 
            esm , nomre = l_esmnomre.pop(0)
            write.writerow((esm , nomre))


def calculate_sorted_averages(input_file_name, output_file_name):
    with open (input_file_name , 'r') as file:
        read = csv.reader(file)

        l_esmnomre = []
        for row in read:
            name = row.pop(0)

            l_nomre = []
            for nomre in row :
                l_nomre.append(float(nomre))

            miyangin = mean(l_nomre)

            l_esmnomre.append((name , miyangin))
    
    with open (output_file_name ,'w') as out_file:
        write = csv.writer(out_file)
        l_esmnomre.sort(key=lambda x : (x[1],x[0]))

        while len(l_esmnomre) != 0:
            esm , miyangin = l_esmnomre.pop(0)
            write.writerow((esm,miyangin))

    
def calculate_three_best(input_file_name, output_file_name):
    with open (input_file_name , 'r') as file:
        read = csv.reader(file)

        l_esmnomre = []
        for row in read:
            name = row.pop(0)

            l_nomre = []
            for nomre in row :
                l_nomre.append(float(nomre))

            miyangin = mean(l_nomre)

            l_esmnomre.append((name , miyangin))
    
    with open (output_file_name ,'w') as out_file:
        write = csv.writer(out_file)
        l_esmnomre.sort(key=lambda x : (x[1],x[0]))

        for i in range(3):
            esm , miyangin = l_esmnomre.pop()
            write.writerow((esm,miyangin))


def calculate_three_worst(input_file_name, output_file_name):
    with open (input_file_name , 'r') as file:
        read = csv.reader(file)

        l_esmnomre = []
        for row in read:
            name = row.pop(0)

            l_nomre = []
            for nomre in row :
                l_nomre.append(float(nomre))

            miyangin = mean(l_nomre)

            l_esmnomre.append((name , miyangin))
    
    with open (output_file_name ,'w') as out_file:
        write = csv.writer(out_file)
        l_esmnomre.sort(key=lambda x : (x[1],x[0]))

        for i in range(3):
            esm , miyangin = l_esmnomre.pop(0)
            miyangin = str(miyangin)
            write.writerow((miyangin ,))


def calculate_average_of_averages(input_file_name, output_file_name):
    with open (input_file_name , 'r') as file:
        read = csv.reader(file)

        l_miyangin =[]
        for row in read :
            name = row.pop(0)

            l_nomre = []
            for nomre in row :
                l_nomre.append(float(nomre))
            miyangin = mean(l_nomre)
            l_miyangin.append(miyangin)
    
    with open (output_file_name , 'w') as out_file:
        write = csv.writer(out_file)
        miyangin_kol = str(mean(l_miyangin))
        write.writerow((miyangin_kol,))



# print(calculate_averages("./file.csv" , "file2.csv"))
# print(calculate_sorted_averages("./file.csv" , "file3.csv"))
# print(calculate_three_best("./file.csv" , "file4.csv"))
# print(calculate_three_worst("./file.csv" , "file5.csv"))
# print(calculate_average_of_averages("./file.csv" , "file6.csv"))