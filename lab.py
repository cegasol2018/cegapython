import csv, json

compas = {}
FILE_NAME = 'cega_tarea_2.csv'
USERNAME = 0
NAME = 1
LASTNAME = 2
AGE = 3
COUNTRY = 4
CITY = 5
FIELD = 6
INSTITUTION = 7
HOBBY = 8


def read_file():
    with open(FILE_NAME) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = True
        for row in csv_reader:
            if not header:
                compas[row[USERNAME]] = {
                    "name" : row[NAME],
                    "lastname" : row[LASTNAME],
                    "age" : row[AGE],
                    "country" : row[COUNTRY],
                    "city" : row[CITY],
                    "field" : row[FIELD],
                    "institution" : row[INSTITUTION],
                    "hobby" : row[HOBBY],
                }
            else:
                header = False

def main():
    read_file()
    print('--------------------------')
    get_info_by_country('Colombia')
    print('--------------------------')
    print(f'Age avg: {get_age_avg()}')
    print('--------------------------')
    print(f'Institutions: {get_institutions()}')

def get_info_by_country(country):
    print ("{:<15} {:<20} {:<10} {:<10} {:<15} {:<25} {:<40} {:<10}".format('Name', 'Last Name', 'Age', 'Country', 'City', 'Field', 'Institution', 'Hobby')) 
    for username in compas:
        data_info = compas[username]
        if data_info["country"] == country:
            print ("{:<15} {:<20} {:<10} {:<10} {:<15} {:<25} {:<40} {:<10}".format(data_info["name"], data_info["lastname"], data_info["age"], data_info["country"], data_info["city"], data_info["field"], data_info["institution"], data_info["hobby"]))

def get_age_avg():
    if len(compas) == 0:
        return 0
    ages_sum = 0
    for username in compas:
        ages_sum += int(compas[username]["age"])

    return ages_sum / len(compas)

def get_institutions():
    institutions = set()
    for username in compas:
        institutions.add(compas[username]["institution"])
    
    return institutions

if __name__ == "__main__":
    main()