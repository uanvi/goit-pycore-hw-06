from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    @staticmethod
    def validate_phone(phone):
        return len(phone) == 10 and phone.isdigit()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                break

    def find_phone(self, phone):
        return phone in [p.value for p in self.phones]

    def __str__(self):
        phone_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phone_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


if __name__ == "__main__":
    # Create new address book
    book = AddressBook()

    # Create record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add John to the address book
    book.add_record(john_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Displayy all records from AddressBook
    for name, record in book.data.items():
        print(record)

    # Find and edit the phone number for John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)

    # Search phone number in John's record
    if john:
        found_phone = john.find_phone("5555555555")
        if found_phone:
            print(f"{john.name}: {found_phone}")  # Output: John: True

    # Delet Jane
    book.delete("Jane")
