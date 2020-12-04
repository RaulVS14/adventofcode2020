from helpers.helpers import read_file


def validate_passports(file_name):
    file = read_file(file_name)
    passports = organize_passports(file)
    return get_valid_passport_count(passports)


def get_valid_passport_count(passports):
    valid_count = 0
    for i in passports:
        if i.is_valid():
            valid_count += 1
    return valid_count


def organize_passports(file):
    passports = []
    passport_string = ""
    for i in file:
        passport_string = passport_string + " " + i
        if i == "" or file[-1] == i:
            passport = passport_string.strip(" ")
            passport_object = create_passport_obj(passport)
            passports.append(passport_object)
            passport_string = ""
    return passports


class Passport:
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False
    cid = False

    def set_passport_field(self, field, value):
        setattr(self, field, value)
        return self

    def is_valid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid

    def output(self):
        print(
            f"===== Passport: {self.is_valid()} | byr - {self.byr}, iyr - {self.iyr}, eyr - {self.eyr}, hgt - {self.hgt}, hcl - {self.hcl}, ecl - {self.ecl}, pid - {self.pid}")


def create_passport_obj(passport_str):
    passport_str_arr = passport_str.split(" ")
    passport = Passport()
    for i in passport_str_arr:
        key, value = i.split(":")
        passport.set_passport_field(key, value)
    return passport
