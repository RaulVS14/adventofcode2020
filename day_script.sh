#!/usr/bin/env sh
folder_name="Day $1"
if [ "$1" == "" ]
then
  echo "Parameter missing. Please add valid number"
elif ! [[ $1 =~ ^-?[0-9]{1,3}$ ]]
then
  echo "Provide valid day number"
elif [ -d "$folder_name" ]
then
  echo "Directory /path/to/dir exists."
else
  mkdir "$folder_name"

  # create functions file
  {
    printf "from helpers.helpers import read_file\n\n\n"
    printf "def section_1_function(file_name):\n"
    printf "    file = read_file(file_name)\n"
    printf "    return file\n\n\n"
    printf "def section_2_function(file_name):\n"
    printf "    file = read_file(file_name)\n"
    printf "    return file\n"
  }>>"$folder_name/day_$1_functions.py"

  # create main file
  {
    printf "from day_%s_functions import section_1_function, section_2_function\n" "$1"
    printf "from helpers.helpers import output_test_result, output_result\n\n"
    echo "if __name__ == \"__main__\":"
    printf "    # Part 1\n"
    printf "    print(output_test_result('result' == section_1_function(\"test_input.txt\"), %s, 1))\n" "$1"
    printf "    print(output_result(section_1_function(\"input.txt\"), %s, 1))\n\n" "$1"

    printf "    # Part 2\n"
    printf "    print(output_test_result('result' == section_2_function(\"test_input.txt\"), %s, 2))\n" "$1"
    printf "    print(output_result(section_2_function(\"input.txt\"), %s, 2))\n" "$1"
  }>>"$folder_name/day$1.py"
  git add "$folder_name/*"
  printf "\n\n[Day %s: ](https://adventofcode.com/2020/day/%s)" "$1" "$1" >> "README.md"
fi
