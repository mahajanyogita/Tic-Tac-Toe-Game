class InvalidCell(Exception):
    def __str__(self):
        return "Enter Valid Cell No "
def get_col_row(cell):
    cell_dict = {'1': [0, 0], '2': [0, 1], '3': [0, 2],
                 '4': [1, 0], '5': [1, 1], '6': [1, 2],
                 '7': [2, 0], '8': [2, 1], '9': [2, 2]}
    if cell in cell_dict:
        return cell_dict[cell]
    else:
        raise InvalidCell

