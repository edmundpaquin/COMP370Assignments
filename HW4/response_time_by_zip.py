from datetime import datetime
import csv


def do(file_path, output_file_path):
     
    date_format = '%m/%d/%Y %I:%M:%S %p'
    months = {}

    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            open_date = row[1][0:22]
            close_date = row[2][0:22]
            if close_date == '': continue
            open_datetime = datetime.strptime(open_date, date_format)
            close_datetime = datetime.strptime(close_date, date_format)
            if close_datetime < open_datetime:
                    continue
            zip = row[8]
            month = close_datetime.month
            if zip == '': continue
            response_time_hours = (close_datetime - open_datetime).total_seconds() / 3600
            if month not in months:
                 months[month] = {}
            if zip not in months[month]:
                    months[month][zip] = [response_time_hours]
            else:
                    months[month][zip].append(response_time_hours)


    response_times = {}
    for month in months:
        response_times[month] = {}
        for zip in months[month]:
            average = sum(months[month][zip])/len(months[month][zip])
            response_times[month][zip] = average

    with open(output_file_path, 'w') as outputfile:
        for month, zip in response_times.items():
            for zipcode, response_time in zip.items():
                outputfile.write(str(month) + ',' + str(zipcode) + ',' + str(response_time)+'\n')

if __name__ == '__main__':
      do('nyc_311_data_trimmed.csv', 'response_times.csv')
            
