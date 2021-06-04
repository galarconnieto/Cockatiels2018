import csv

with open('/home/gustavo/TITS/SCRIPTS/List_of_Cameras.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    ip_pi = []
    pi_name = []
    for row in readCSV:
        ips = row[1]
        names = row[0]

        pi_name.append(names)
        ip_pi.append(ips)

    #print(dates)
    #print(colors)

#pi_names = dates
#ip_pi = colors



print(ip_pi)
print(names)
