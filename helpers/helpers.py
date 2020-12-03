def read_file(file_name, cast_type=False):
    file = []
    with open(file_name, "r") as readfile:
        for i in readfile:
            line = i.strip()
            if callable(cast_type):
                line = cast_type(line)
            file.append(line)
    return file

def output_result(result, day, part):
    return f"Day {day} - {part}. Solution: {result}"


def output_test_result(result, day, part):
    print(f"\n==== Running test {day}.{part}")
    return f"Day {day} - {part}. Test passed: {result}"