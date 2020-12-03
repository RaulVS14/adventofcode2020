from day_2_functions import find_correct_passwords_from_file

if __name__ == "__main__":
    print(find_correct_passwords_from_file("input.txt", type="count"))
    print(find_correct_passwords_from_file("input.txt", type="position"))