import argparse
from datetime import datetime
import csv

def do(file_path, start_date, end_date, output_file=None):

    date_format = "%m/%d/%Y"
    start_date = datetime.strptime(start_date, date_format)
    end_date = datetime.strptime(end_date, date_format)

    complaints = {}

    with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                date = row[1][0:10] #first 10 characters of the line
                current_date = datetime.strptime(date, date_format)
                if start_date <= current_date and current_date <= end_date:
                    #get the borough and complaint type
                    borough = row[25]
                    complaint_type = row[5]

                    if borough not in complaints:
                        complaints[borough] = {}

                    if(complaint_type) in complaints[borough]:
                        complaints[borough][complaint_type] += 1
                    else: complaints[borough][complaint_type] = 1

    output_lines = []
    for borough, complaint_types in complaints.items():
        for complaint_type, count in complaint_types.items():
            output_lines.append(complaint_type + ',' + borough + ',' + str(count))

    if output_file:
        #write the output lines to the file
        with open(output_file, 'w') as outputfile:
            outputfile.write("\n".join(output_lines))
    else:
        print("\n".join(output_lines))

def main():
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')


    parser = argparse.ArgumentParser(description='number of each complaint type per borough for given date range.')
    parser.add_argument('-i', '--file_path', type=str, help='path to the CSV file')
    parser.add_argument('-s', '--start_date', type=str, help='start date MM/DD/YYYY')
    parser.add_argument('-e', '--end_date', type=str, help='end date MM/DD/YYYY')
    parser.add_argument('-o', '--output', type=str, required=False, help='output file')

    args = parser.parse_args()
    
    do(args.file_path, args.start_date, args.end_date, args.output)

if __name__ == "__main__":
    main()
    
