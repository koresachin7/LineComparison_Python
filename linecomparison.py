"""
* @Author: Sachin S Kore
* @Date: 2022-1-4
* @Title : Calculate length of Line and compare
"""
import logging
import math
from logging import *


class LineComparison:

    def __init__(self):
        # using list to store player class object
        self.line_list = []
        self.length_of_line = 0
        self.list_sum = []

    def start(self):
        try:
            print("""Your choices:-
                                            1.Add line
                                            2.Find length
                                            3.Check Equality
                                            4.Check Comparison
                                            """)
            choice = int(input("Enter your choice:- "))
            if choice == 1:
                x1 = int(input("Enter the x1 value:- "))
                x2 = int(input("Enter the x2 value:- "))
                y1 = int(input("Enter the y1 value:- "))
                y2 = int(input("Enter the y2 value:- "))
                line_dict = {"x1": x1, "x2": x2, "y1": y1, "y2": y2}
                line = Line(line_dict)
                line_comparison.add_line(line)
            elif choice == 2:
                line_comparison.length_find()
            elif choice == 3:
                line_comparison.check_equal()
            elif choice == 4:
                line_comparison.comparison()

        except Exception:
            logging.exception("Pass the integer value")
        line_comparison.start()

    def add_line(self, line):
        """
            Description:
                   this function for adding object in line list
        """

        self.line_list.append(line)

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
        return self.length_of_line

    def check_equal(self):
        """
        Description:
            this function use for nested loop and list for check
            length of line equal or not
        """
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
    def __init__(self, line_dict):
        self.x1 = line_dict.get("x1")
        self.x2 = line_dict.get("x2")
        self.y1 = line_dict.get("y1")
        self.y2 = line_dict.get("y2")


if __name__ == '__main__':
    """
        Description:
            * Creating multiple Object multiple line length calculation
            * using x and y co_ordinates for that 
    """
    print("Welcome To Line Comparison Computation Program")
    # logging basic config method and saving log files
    LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}'
    basicConfig(filename='logfile.log', level=DEBUG, style='{', format=LOG_FORMAT)
    line_comparison = LineComparison()
    line_comparison.start()
