"""
* @Author: Sachin S Kore
* @Date: 2021-12-9
* @Title : Calculate length of Line and compare
"""
import math
from logging import *


class LineComparison:
    def __init__(self):
        # using list to store player class object
        self.line_list = []
        self.length_of_line = 0
        self.list_sum = []

    def length_find(self):
        """
        Description:
            this function for Calculate length of line
        """
        for lines in self.line_list:
            self.length_of_line = math.sqrt(
                (lines.x2 - lines.x1) * (lines.x2 - lines.x1) + (lines.y2 - lines.y1) * (lines.y2 - lines.y1))
            print("Length of Line :-  ", self.length_of_line)
            self.list_sum.append(self.length_of_line)

    def check_equal(self):
        """
        Description:
            this function use for nested loop and list for check
            length of line equal or not
        """
        # print(self.list_sum)
        for i in range(len(self.list_sum)):
            for j in range(i + 1, len(self.list_sum)):
                if str(self.list_sum[i]).__eq__(str(self.list_sum[j])):
                    print("" + str(self.list_sum[i]) + " " "Length of Line is equal" " " + str(self.list_sum[j]) + "")
                else:
                    print(
                        "" + str(self.list_sum[i]) + " " "Length of Line is not equal" " " + str(self.list_sum[j]) + "")

    def comparison(self):
        """
        Description:
            this function use for nested loop and list for compare length og line
        """
        for i in range(len(self.list_sum)):
            for j in range(i + 1, len(self.list_sum)):
                if str(self.list_sum[i]) > (str(self.list_sum[j])):
                    print("Length of Line " + str(self.list_sum[i]) + " " "is greater than" " Length of Line " + str(
                        self.list_sum[j]) + "")
                elif str(self.list_sum[i]) < (str(self.list_sum[j])):
                    print("Length of Line " + str(self.list_sum[i]) + " " "is lesser than " " Length of Line " + str(
                        self.list_sum[j]) + "")
                else:
                    print("Length of Line " + str(self.list_sum[i]) + " " " Equal to  " " Length of Line " + str(
                        self.list_sum[j]) + "")


class Line:
    # parameterized constructor
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


if __name__ == '__main__':
    print("Welcome To Line Comparison Computation Program")
    # logging basic config method and saving log files
    LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}'
    basicConfig(filename='logfile.log', level=DEBUG, style='{', format=LOG_FORMAT)
    line_comparison = LineComparison()
    """
    Description:
        * Creating multiple Object multiple line length calculation
        * using x and y co_ordinates for that 
    """
    try:
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
    except Exception:
        print("Only number please....")
        error("Only number please....")
    # calling the instance method using the object line_comparison
    line_comparison.length_find()
    line_comparison.check_equal()
    line_comparison.comparison()
