""" This file contain different methods to create address book
Author : Akshaya Revaskar
Date : 23/01/2020
TODO: Address book class will hold different methods to create update delete sort an address book.
"""
import json
import sys


class AddressBook:

    def __init__(self):
        self.book = []

    def open_file(self):
        """
        This method will open the file
        """

        with open('address_book.json') as json_file:
            data = json.load(json_file)
        return data

    def save_file(self, data):
        """
        This method will save the data into file
        :param data: data to be added
        :return: data: address book
        """
        with open('address_book.json', "w") as json_f:
            json.dump(data, json_f, indent=4)
        return data

    def display(self):
        """
        This method is for displaying all the address book records
        :return: data: All the records of the address book
        """
        try:
            data = self.open_file()
            print(data)
            return data
        except FileNotFoundError:
            print("File Not Found")
        except Exception:
            print("Error!!!")

    def add_person(self):
        """This method will add people to the address book
        """

        try:
            # taking user inputs
            first_name = input("Enter your First name: ")
            last_name = input("Enter your Last name: ")
            city = input("Enter your city's name: ")
            state = input("Enter your State name: ")
            zip = int(input("Enter zip code: "))
            phone_number = input("Enter your phone number: ")

            if first_name.isalpha() and last_name.isalpha() and city.isalpha() and state.isalpha() \
                    and phone_number.isdigit():

                # writing into json file
                def write_json(data, filename='address_book.json'):
                    with open(filename, 'w') as file:
                        json.dump(data, file, indent=4)

                with open('address_book.json') as json_file:
                    data = json.load(json_file)


                temp = data['address_book']

                # python object to be appended
                entry = {'first_name': first_name,
                        'last_name': last_name,
                        'city': city,
                        'state': state,
                        'zip': zip,
                        'phone_number': phone_number
                        }

                # appending data to address book
                temp.append(entry)
                self.book.append(entry)

                write_json(data)
                data = self.open_file()
                print("data added...")
                return data
            else:
                raise ValueError
        except ValueError:
            print("Incorrect Values...")
            self.add_person()
        except Exception:
            print("Error!!!")


    def edit_information(self):
        """
        This method will edit information of people except first name and last name
        :return: data: address book
        """
        try:
            data = self.open_file()

            # asking user input
            rec = int(input("Choose which record u want to update...(0 for 1, 1 for 2, 2 for 3....): "))
            if rec >= len(data["address_book"]):
                raise IndexError

            print("1 : city")
            print("2 : state")
            print("3 : zip")
            print("4 : phone_number")
            choice = int(input("Choose which key you want to update..."))

            if choice == 1:
                updated_city = input("Enter city: ")
                # validating user inputs
                if updated_city.isnumeric() or len(updated_city) <= 0:
                    raise ValueError
                else:
                    if updated_city.isalpha():
                        data = self.open_file()

                        data["address_book"][rec]["city"] = updated_city

                        self.save_file(data)
                        print("data updated...")
                        self.display()
                        return data
                    else:
                        print("City should be string")
                        self.edit_information()
            elif choice == 2:
                updated_state = input("Enter state: ")
                # validating user inputs
                if updated_state.isnumeric() or len(updated_state) <= 0:
                    raise ValueError
                else:
                    if updated_state.isalpha():
                        data = self.open_file()

                        data["address_book"][rec]["state"] = updated_state

                        data = self.save_file(data)
                        print("data updated...")
                        self.display()
                        return data
                    else:
                        print("state should be string")
                        self.edit_information()
            elif choice == 3:
                updated_zip = input("Enter zip: ")
                # validating user inputs
                if updated_zip.isalpha() or len(updated_zip) <= 0:
                    raise ValueError
                else:
                    if updated_zip.isnumeric():
                        data = self.open_file()

                        data["address_book"][rec]["zip"] = updated_zip

                        data = self.save_file(data)
                        print("data updated...")
                        self.display()
                        return data
                    else:
                        print("zip should be integer")
                        self.edit_information()

            elif choice == 4:
                updated_phone_number = input("Enter Phone Number: ")
                # validating user inputs
                if updated_phone_number.isalpha() or len(updated_phone_number) <= 0:
                    raise ValueError
                else:
                    if updated_phone_number.isnumeric():
                        data = self.open_file()

                        data["address_book"][rec]["phone_number"] = updated_phone_number

                        data = self.save_file(data)
                        print("data updated...")
                        self.display()
                        return data
                    else:
                        print("Phone number should be numeric")
                        self.edit_information()
            else:
                print("Invalid Choice...")

        except IndexError:
            print("record is not available")
            self.edit_information()
        except ValueError:
            print("Incorrect Values!!!")
            self.edit_information()
        except Exception:
            print("Error!!!")


    def delete_entry(self):
        """
        this method will delete a record from address book
        :return: data: address book
        """
        try:
            flag = False
            data = self.open_file()
            print(data)

            # validating user inputs
            if len(data["address_book"]) >= 1:
                first_name = input("Enter your First name: ")
                last_name = input("Enter your Last name: ")
                if first_name.isnumeric() and last_name.isnumeric() \
                        or len(first_name) <= 0 and len(last_name) <= 0:
                    raise ValueError

                else:
                    # validating user inputs
                    if first_name.isalpha() and last_name.isalpha():
                        for i in range(len(data["address_book"])):

                            # comparing dictionary values and user inputs
                            if str(data["address_book"][i]["first_name"]).casefold().strip() == first_name.casefold().strip() \
                                    and str(data["address_book"][i]["last_name"]).casefold().strip() == \
                                    last_name.casefold().strip():
                                flag = True
                                del data["address_book"][i]
                                data = self.save_file(data)
                                print("data deleted!!!")
                        if not flag:
                            print("Data not found!!!")
                    else:
                        print("Invalid Inputs...")
                        self.delete_entry()
            else:
                print("Empty List")

        except ValueError:
            print("Invalid Inputs for first name and last name")
            self.delete_entry()
        except Exception:
            print("Error!!!")

    def sort_by_last_name(self):
        """
        This method will sort records from address book alphabetically by last names
        """
        data = self.open_file()

        for i in range(len(data["address_book"])):
            for j in range(len(data["address_book"])):
                if data["address_book"][i]["last_name"] < data["address_book"][j]["last_name"]:
                    data["address_book"][i], data["address_book"][j] = data["address_book"][j], data["address_book"][i]
        self.save_file(data)
        self.display()

    def sort_by_zip(self):
        """
        This method will sort records from address book by last zip code
        """
        data = self.open_file()

        for i in range(len(data["address_book"])):
            for j in range(len(data["address_book"])):
                # comparing address book values with user inputs
                if data["address_book"][i]["zip"] < data["address_book"][j]["zip"]:
                    data["address_book"][i], data["address_book"][j] = data["address_book"][j], data["address_book"][i]
        self.save_file(data)
        self.display()

    def quit(self):
        """This method will help user to exit from program
        """
        sys.exit()


def main():
    # creating object of AddressBook class
    a = AddressBook()

    # displaying choices to user
    print("1 : add_person")
    print("2 : edit_information")
    print("3 : delete_entry")
    print("4 : sort_by_last_name")
    print("5 : sort_by_zip")
    print("6 : open_file")
    print("7 : save_file")
    print("8 : display")
    print("9 : Quit")

    # asking user input for which operation to be performed
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        a.add_person()
    elif choice == 2:
        a.edit_information()
    elif choice == 3:
        a.delete_entry()
    elif choice == 4:
        a.sort_by_last_name()
    elif choice == 5:
        a.sort_by_zip()
    elif choice == 6:
        a.open_file()
    elif choice == 7:
        a.display()
    elif choice == 8:
        a.quit()
    else:
        print("Invalid choice...")
        print()
        main()


if __name__ == '__main__':
    main()
