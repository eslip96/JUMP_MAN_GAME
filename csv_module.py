import csv

with open('nasa_modern_landings.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)

    new_data = []
    for row in reader:
        year = int(row[0])
        if 2015 <= year <= 2018:
            new_data.append([row[0], row[1], row[2], row[3], row[4]])

    for row in new_data:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")


with open('new_nasa_data.csv', mode='w', newline='') as new_file:
    writer = csv.writer(new_file)

    writer.writerow(['Year', 'Driver', 'Position', 'Race', 'Time'])

    writer.writerows(new_data)
