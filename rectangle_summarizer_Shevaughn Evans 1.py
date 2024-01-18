import csv
from statistics import mean
heading= "RECTANGLE SUMMARIZER LAB 1 - ACTIVITY 3"
a= heading.center(100)
print(a)

#Opening and reading the csv file:
with open('C:/Users/sheva/Downloads/Python Labs/DATA475_lab_rectangles_data.csv') as file:
    next(file)
    reader =csv.reader(file)

#Computing area to analyze the rectangles:
    area=[]
    for row in reader:
        area.append(float(row[1]) * float(row[2]))

#Storing the various results in a dictionary:
summary = {
    'Total Count': len(area), 
    'Total Area': sum(area),
    'Average Area': mean(area),
    'Maximum Area': max(area),
    'Minimum Area': min(area),
}

#Printing the results stored in the dictionary:
for key, value in summary.items():
    print(f"{key}: {value}")


#creating a csv file and adding the above computed results as new rows. First being the keys (column names) and the second being the values (computed column values):
with open('summary.csv',"w",newline="")as f:
    writer = csv.writer(f)
    writer.writerow(summary.keys())
    writer.writerow(summary.values())


#Closing the previously opened and created csv files:
file.close()
f.close()
