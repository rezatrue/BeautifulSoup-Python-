import csv

class WriteCsv:

    list = []

    def __init__(self, list):
        self.list = list
        pass

    def write_file(self):
        # Open a new file for writing
        with open('data.csv', 'w', newline='') as file:
            # Create a CSV writer object
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(self.list[0].keys())

            for rowdata in self.list:
                print(rowdata.values())
                writer.writerow(rowdata.values())

        pass
