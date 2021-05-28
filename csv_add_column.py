# coding=utf-8
import csv

for n in [1,2]:
    for i in range(2017, 2021):
        for j in range(1, 13):  # months
            input = 'E:/Userdata/yuy/downloads/southeast_test/test' + str(n) + '/var_imp/var_imp_' \
                    + str(i) + '_' + str(j) + '.csv'
            output = 'E:/Userdata/yuy/downloads/southeast_test/test' + str(n) + '/var_imp.csv'
            print(input)

            with open(output, 'r') as file:
                reader = csv.reader(file)

                output_data = []
                for row in reader:
                    output_data.append(row)

            with open(input, 'r') as csvinput:
                with open(output, 'w') as csvouput:
                    writer = csv.writer(csvouput, lineterminator='\n')
                    reader = csv.reader(csvinput)

                    list = []
                    for row in reader:
                        list.append(row[1])

                    list[0] = str(i) + '_' + str(j)

                    for t in range(len(output_data)):
                        if t >= len(list):
                            output_data[t].append('')
                        else:
                            output_data[t].append(list[t])
                        writer.writerow(output_data[t])