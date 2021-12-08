"""
* @Author: Sachin S Kore
* @Date: 2021-12-8
* @Title : Calculate length of Line
"""
import math


class LineComparison:
    def __init__(self):
        # using list to store player class object
        self.line_list = []
        self.length_of_line = 0

    def length_find(self):
        """
        Description:
            this function for Calculate length of line
        """
        for lines in self.line_list:
            self.length_of_line = math.sqrt((lines.x2 - lines.x1) * (lines.x2 - lines.x1) + (lines.y2 - lines.y1) * (lines.y2 - lines.y1))
            print("Length of Line :-  ", self.length_of_line)


class Line:
    # parameterized constructor
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


if __name__ == '__main__':
    print("Welcome To Line Comparison Computation Program")
    line_comparison = LineComparison()
    """
    Description:
        * Creating multiple Object multiple line length calculation
        * using x and y co_ordinates for that 
    """
    line = int(input("Number of line Comparison : --""\n"))
    for line_l in range(line):
        print("Enter co-ordinates for x-axis of first line : ")
        x1 = int(input("line x1""\n"))
        x2 = int(input("line x2""\n"))
        print("Enter co-ordinates for y-axis of first line : ")
        y1 = int(input("line y1""\n"))
        y2 = int(input("line y2""\n"))
        # creating object of the class
        line_obj = Line(x1, x2, y1, y2)
        # object append (adding) To line
        line_comparison.line_list.append(line_obj)
    # calling the instance method using the object line_comparison
    line_comparison.length_find()

