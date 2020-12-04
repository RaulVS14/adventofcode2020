import re

from helpers.helpers import read_file


def validate_passports(file_name):
    file = read_file(file_name)
    passports = organize_passports(file)
    return get_valid_passport_count(passports)


def secure_validate_passports(file_name):
    file = read_file(file_name)
    passports = organize_passports(file)
    return get_secure_valid_passport_count(passports)


def get_secure_valid_passport_count(passports):
    valid_count = 0
    for i in passports:
        if i.secured_validation():
            valid_count += 1
    return valid_count


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
    byr = ''
    iyr = ''
    eyr = ''
    hgt = ''
    hcl = ''
    ecl = ''
    pid = ''
    cid = ''

    def set_passport_field(self, field, value):
        setattr(self, field, value)
        return self

    def is_valid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid

    def secured_validation(self):
        return self.is_valid() and self.validate_fields()

    def output(self):
        print(
            f"===== Passport: {self.is_valid()}| {self.secured_validation()} | byr - {self.byr}, iyr - {self.iyr}, eyr - {self.eyr}, hgt - {self.hgt}, hcl - {self.hcl}, ecl - {self.ecl}, pid - {self.pid}")

    def validate_byr(self):
        if self.byr:
            byr_number = int(self.byr)
            return byr_number >= 1920 and byr_number <= 2002
        return False

    def validate_iyr(self):
        if self.iyr:
            iyr_number = int(self.iyr)
            return iyr_number >= 2010 and iyr_number <= 2020
        return False

    def validate_eyr(self):
        if self.eyr:
            eyr_number = int(self.eyr)
            return eyr_number >= 2020 and eyr_number <= 2030
        return False

    def validate_hgt(self):
        if self.hgt:
            hgt_string = self.hgt
            find_groups = re.match(r'(\d{2})in|(\d{3})cm$', hgt_string)
            if (find_groups):
                height_in, height_cm = find_groups[1], find_groups[2]
                if (height_in):
                    height = int(height_in)
                    return height >= 59 and height <= 76
                if (height_cm):
                    height = int(height_cm)
                    return height >= 150 and height <= 193
            return
        return False

    def validate_hcl(self):
        if self.hcl:
            hcl_hex = self.hcl
            return re.match(r'#[0-9a-f]{6}$', hcl_hex)
        return False

    def validate_ecl(self):
        return self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def validate_pid(self):
        return re.match(r"[0-9]{9}$", self.pid)

    def validate_fields(self):
        return self.validate_byr() and self.validate_iyr() and self.validate_eyr() and self.validate_hgt() and self.validate_hcl() and self.validate_ecl() and self.validate_pid()


def create_passport_obj(passport_str):
    passport_str_arr = passport_str.split(" ")
    passport = Passport()
    for i in passport_str_arr:
        key, value = i.split(":")
        passport.set_passport_field(key, value)
    return passport
