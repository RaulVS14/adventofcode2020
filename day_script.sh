#!/usr/bin/env sh
foldername="Day $1"
echo "$1"
if [ "$1" == "" ]
then
  echo "Parameter missing. Please add valid number"
elif ! [[ $1 =~ ^-?[0-9]{1,3}$ ]]
then
  echo "Provide valid day number"
elif [ -d "$foldername" ]
then
  echo "Directory /path/to/dir exists."
else
  mkdir "$foldername"

  # create functions file
  {
    printf "from helpers.helpers import read_file\n\n\n"
    printf "def section_1_function(file_name):\n"
    printf "\tfile = read_file(file_name)\n"
    printf "\treturn file\n\n\n"
    printf "def section_2_function(file_name):\n"
    printf "\tfile = read_file(file_name)\n"
    printf "\treturn file\n"
  }>>"$foldername/day_$1_functions.py"

  # create main file
  {
    printf "from day_%s_functions import section_1_function, section_2_function\n" "$1"
    printf "from helpers.helpers import output_test_result, output_result\n\n"
    echo "if __name__ == \"__main__\":"
    printf "\t# Part 1\n"
    printf "\tprint(output_test_result('result' == section_1_function(\"test_input.txt\"), %s, 1))\n" "$1"
    printf "\tprint(output_result(section_1_function(\"input.txt\"), %s, 1))\n\n" "$1"

    printf "\t# Part 2\n"
    printf "\tprint(output_test_result('result' == section_2_function(\"test_input.txt\"), %s, 1))\n" "$1"
    printf "\tprint(output_result(section_2_function(\"input.txt\"), %s, 1))\n" "$1"
  }>>"$foldername/day$1.py"
  git add "$foldername/*"
  printf "\n\n[Day %s: ](https://adventofcode.com/2020/day/%s)" "$1" "$1" >> "README.md"
fi
