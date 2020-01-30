import json


class Patient:

    def __init__(self):
        self.patient = []

    def add_patient(self):

        patient_id = int(input("Enter ID: "))
        patient_name = input("Enter Name: ")
        mobile_number = input("Enter Your Mobile Number: ")
        age = int(input("Enter Your Age: "))

        def write_json(data, filename='patient.json'):
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

        with open('patient.json') as json_file:
            data = json.load(json_file)

            temp = data['patient_info']

            # python object to be appended
            entry = {'patient_id': patient_id,
                     'patient_name': patient_name,
                     'mobile_number': mobile_number,
                     'age': age
                    }

            # appending data to emp_details
            temp.append(entry)
            self.patient.append(1)

        write_json(data)
        with open('patient.json') as json_f:
            patient_info = json.load(json_f)
        return patient_info

    def search_by_id(self, id):
        with open('patient.json') as json_f:
            data = json.load(json_f)
        # print(data)

        flag = False
        for i in range(len(data['patient_info'])):
            if (data['patient_info'][i]['patient_id']) == id:
                flag = True
                if flag:
                    print(f"patient_id : {data['patient_info'][i]['patient_id']}")
                    print(f"patient_name : {data['patient_info'][i]['patient_name']}")
                    print(f"mobile_number : {data['patient_info'][i]['mobile_number']}")
                    print(f"age : {data['patient_info'][i]['age']}")
        if flag == False:
            print("Patient not available!!!")


    def search_by_name(self, name):
        with open('patient.json') as json_f:
            data = json.load(json_f)
        # print(data)

        flag = False
        for i in range(len(data['patient_info'])):
            if (data['patient_info'][i]['patient_name']).casefold() == name.casefold():
                flag = True
                if flag:
                    print(f"patient_id : {data['patient_info'][i]['patient_id']}")
                    print(f"patient_name : {data['patient_info'][i]['patient_name']}")
                    print(f"mobile_number : {data['patient_info'][i]['mobile_number']}")
                    print(f"age : {data['patient_info'][i]['age']}")
        if flag == False:
            print("Patient not available!!!")

    def search_by_mobile_number(self, mobile_number):
        with open('patient.json') as json_f:
            data = json.load(json_f)
        # print(data)

        flag = False
        for i in range(len(data['patient_info'])):
            if (data['patient_info'][i]['mobile_number']) == mobile_number:
                flag = True
                if flag:
                    print(f"patient_id : {data['patient_info'][i]['patient_id']}")
                    print(f"patient_name : {data['patient_info'][i]['patient_name']}")
                    print(f"mobile_number : {data['patient_info'][i]['mobile_number']}")
                    print(f"age : {data['patient_info'][i]['age']}")
        if flag == False:
            print("Patient not available!!!")


def main():
    p = Patient()

    # p.add_patient()
    # p.search_by_id(7)
    # p.search_by_name("rhsdfrg")
    #p.search_by_mobile_number("9089878989")


if __name__ == '__main__':
    main()