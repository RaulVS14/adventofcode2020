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

[Day 10: Adapter Array ](https://adventofcode.com/2020/day/10)

Learned:
   - About [dynamic programming](https://www.dynamicprogramming.com/) - Solving optimization issue by solving the sub-problems 
     - Example: Top-down with memoization - break down to sub-problem and store the result
   - **Memoization** - method of storing calculated results and calling them when we are about to do same calculation. It will make code run faster, because we don't need to do this extra work
        - In assignment we used mem to store 2nd part values for results

[Day 11: Seating System](https://adventofcode.com/2020/day/11)

Learned:
   - replacing while a loop with for a loop to debug while loop step by step

[Day 12: Day 12: Rain Risk](https://adventofcode.com/2020/day/12)
Learned:
   - coordinates system based language(English is my second language):
     - latitude: deg south(-1deg) <-> north(1deg) (distance between equator and position)
     - longitude: west:(-1deg) <-> east(1deg) (distance between 0 meridian and position)
   - coordinates rotation formula
     - There formula is
       ```
       x = x * cos(a) - y * sin(a)
       y = x * sin(a) + y * cos(a)
       ```
       where **a** is rotated angle in radians. Angle counterclockwise is positive(90) and clockwise is negative(-90).

[Day 13: Shuttle Search](https://adventofcode.com/2020/day/13)
Learned:
   - The most obvious isn't always right
  