import csv

# Open the manifest file for reading
with open('manifest.csv', 'r') as file:
    # Read the CSV data
    reader = csv.reader(file)
    # Loop through each row of the CSV data
    for row in reader:
        # Parse the row data and modify it as required
        if row[0] == 'BoatA':
            row[1] = 'NewCargo'
            row[2] = 'NewPassenger'
    # Open the manifest file for writing
    with open('manifest.csv', 'w') as output_file:
        # Write the updated CSV data back to the file
        writer = csv.writer(output_file)
        writer.writerows(reader)