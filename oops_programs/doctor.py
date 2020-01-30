"""
operations done by user or admin for doctors
Author: Akshaya Revaskar
Dtae: 27/01/2020
"""
import json


class Doctor:

    def __init__(self, d):
        self.doctor = []

    def add_doctor(self):

        doctor_id = int(input("Enter ID: "))
        doctor_name = input("Enter Name: ")
        specialization = input("Enter Specialization: ")
        availability = input("Enter Availability(am, pm, both): ")

        def write_json(data, filename='doctor.json'):
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

        with open('doctor.json') as json_file:
            data = json.load(json_file)

            temp = data['doctor_info']

            # python object to be appended
            entry = {'doctor_id': doctor_id,
                 'doctor_name': doctor_name,
                 'specialization': specialization,
                 'availability': availability
                 }

            # appending data to emp_details
            temp.append(entry)
            self.doctor.append(1)

        write_json(data)
        with open('doctor.json') as json_f:
            data = json.load(json_f)
        # print(data)
        return data


    def search_by_id(self, id):
        with open('doctor.json') as json_f:
            data = json.load(json_f)
        # print(data)

        flag = False
        for i in range(len(data['doctor_info'])):
            if (data['doctor_info'][i]['doctor_id']) == id:
                flag = True
                if flag:
                    print(f"doctor_id : {data['doctor_info'][i]['doctor_id']}")
                    print(f"doctor_name : {data['doctor_info'][i]['doctor_name']}")
                    print(f"specialization : {data['doctor_info'][i]['specialization']}")
                    print(f"availability : {data['doctor_info'][i]['availability']}")
        if flag == False:
            print("Doctor not available!!!")


    def search_by_name(self, name):
        with open('doctor.json') as json_f:
            data = json.load(json_f)
        # print(data)

        flag = False
        for i in range(len(data['doctor_info'])):
            if (data['doctor_info'][i]['doctor_name']).casefold() == name.casefold():
                flag = True
                if flag:
                    print(f"doctor_id : {data['doctor_info'][i]['doctor_id']}")
                    print(f"doctor_name : {data['doctor_info'][i]['doctor_name']}")
                    print(f"specialization : {data['doctor_info'][i]['specialization']}")
                    print(f"availability : {data['doctor_info'][i]['availability']}")
        if flag == False:
            print("Doctor not available!!!")

    def search_by_specialization(self, specialization):
        with open('doctor.json') as json_f:
            data = json.load(json_f)
        # print(data)

        flag = False
        for i in range(len(data['doctor_info'])):
            if (data['doctor_info'][i]['specialization']).casefold() == specialization.casefold():
                flag = True
                if flag:
                    print(f"doctor_id : {data['doctor_info'][i]['doctor_id']}")
                    print(f"doctor_name : {data['doctor_info'][i]['doctor_name']}")
                    print(f"specialization : {data['doctor_info'][i]['specialization']}")
                    print(f"availability : {data['doctor_info'][i]['availability']}")
        if flag == False:
            print("Doctor not available!!!")

    def search_by_availability(self, availability):
        with open('doctor.json') as json_f:
            data = json.load(json_f)
        # print(data)

        flag = False
        for i in range(len(data['doctor_info'])):
            if (data['doctor_info'][i]['availability']).casefold() == availability.casefold():
                flag = True
                if flag:
                    print(f"doctor_id : {data['doctor_info'][i]['doctor_id']}")
                    print(f"doctor_name : {data['doctor_info'][i]['doctor_name']}")
                    print(f"specialization : {data['doctor_info'][i]['specialization']}")
                    print(f"availability : {data['doctor_info'][i]['availability']}")
                    print()
        if flag == False:
            print("Doctor not available!!!")


def main():
    d = Doctor()

    # d.add_doctor()
    # d.search_by_id(3)
    # d.search_by_name("aKshaya")
    # d.search_by_specialization("cArdiolog")
    # d.search_by_availability("m")


if __name__ == '__main__':
    main()