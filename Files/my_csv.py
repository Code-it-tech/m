import csv


with open('devops.csv' , 'r') as csv_file:
    read = csv.reader(csv_file,  delimiter=',')

    for _ in range(5):
        print(next(read))
print(read)