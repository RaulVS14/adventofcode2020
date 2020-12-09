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

[Day 7: Day 7: Handy Haversacks](https://adventofcode.com/2020/day/7)

Learned:
   - a bit about recursions

[Day 8: Handheld Halting](https://adventofcode.com/2020/day/8)

Learned:
   - traversing list with while loop
   - destructing an array
   - if you have to compensate for loop length in boot code calculations in order to avoid going out of bounds, you are doing the calculation wrong

[Day 9: Encoding Error](https://adventofcode.com/2020/day/9)

Learned:
   - Sliding window algorithm, which is traversing list by sections. It is better alternative for nested loop traversal.
   - how to fix pushed commit message:
      - display list of ~n commits in default text editor
        ```
        git rebase -i HEAD~3 
        ```
      - replace word pick with reword in front of commit you want to reword
        ```
        pick 70fdb9b Add day 8 solutions
        pick cb47373 Add day 7 solutions <- line to update
        pick d0fd277 Add day 9 modification
        ```
        like this
        ```
        pick 70fdb9b Add day 8 solutions
        reword cb47373 Add day 7 solutions <- line to update
        pick d0fd277 Add day 9 modification
        ```
      - Save and close commit list file.
      - A new file view opens with the commit message. Change it and save it.
      - Push changes to branch 
        ```
        git push --force
        ```