# Advent of Code 2020

Advent of Code 2020 assignment links:

[Day 1: Report Repair](https://adventofcode.com/2020/day/1)

[Day 2: Password Philosophy](https://adventofcode.com/2020/day/2)

[Day 3: Toboggan Trajectory](https://adventofcode.com/2020/day/3)

Learned:
 - order of applying coordinates to multidimensional array

[Day 4: Passport Processing](https://adventofcode.com/2020/day/4)

Learned:
 - input wasn't completely read, because reading file last element didn't have extra line after it and thus it was not added to the array
 - good to use limiting character to stop including lines that are longer than regex pattern specified length ({9} vs {9}$)

[Day 5: Passport Processing](https://adventofcode.com/2020/day/5)

[Day 6: Custom Customs](https://adventofcode.com/2020/day/6)

Learned:
 - Creating Makefile and bash script for creating files and folders for the day.
    - Install GitBash and link it to PATH to run bash scripts
    - Install GNUWin make for Makefile
    - Use regex to validate numeric value in bash
    - Using bash to create invalid folder names causes issues - use GitBash to remove faulty folders
    - Commands can be grouped with {}
    - \t = tab and \n = newline in bash and parameters, can be used with printf
    - if structure of bash
    - \t is bad char to use in code block creation if all code structure is based on spaces
    
 - Python list handling
    - summing arrays to join
    - using sets and & to find common elements of lists
    - added check of instance if checking if array is False is required in case array is empty