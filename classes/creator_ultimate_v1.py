import csv

def creator_ultimate_v1(path, class_type):
    with open(path) as csvfile:
        csv_r = csv.reader(csvfile)

        key_list = None
        empty_dict = {}
        master_list = []

        for row in csv_r: 
            if key_list == None:
                key_list = row
            else: 
                empty_dict = {}
                for index in range(0, len(key_list)):
                    empty_dict[key_list[index]] = row[index]
                master_list.append(empty_dict)
        
        instance_list = []
        for x in master_list:
            instance = class_type(**x)
            instance_list.append(instance)
        return (instance_list)

