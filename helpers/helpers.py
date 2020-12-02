

def read_file(file_name, cast_type=False):
    file = []
    with open(file_name, "r") as readfile:
        for i in readfile:
            line = i.strip()
            if callable(cast_type):
                line = cast_type(line)
            file.append(line)
    return file

