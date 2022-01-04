from linecomparison import Line
from linecomparison import LineComparison


def test_length_find():
    """
     Description:
            this function test for Calculate length of line
    """
    line_dict = {"x1": 4, "x2": 7, "y1": 8, "y2": 89}
    line = Line(line_dict)
    assert isinstance(line, Line) == True


def test_length_of_line():
    """
         Description:
                this function test for Calculate length of line
    """
    line_comparison = LineComparison()
    line_dict = {"x1": 4, "x2": 7, "y1": 8, "y2": 89}
    line = Line(line_dict)
    line_comparison.line_list.append(line)
    len = line_comparison.length_find()
    assert len == 81.05553651663777


def test_add_line():
    """
    Description:
            this function test equal of line
    """
    line_comparison = LineComparison()
    line_dict = {"x1": 4, "x2": 7, "y1": 8, "y2": 89}
    line = Line(line_dict)
    line_comparison.line_list.append(line)
    assert len(line_comparison.line_list) > 0
