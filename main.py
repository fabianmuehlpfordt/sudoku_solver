# Imports
import pandas as pd

# Side Functions
def read_sudoko_csv(file, sep):
    # reading csv-file, return dataframe
    df = pd.read_csv(filepath_or_buffer=file, sep=sep, header=None)

    # check if number of cols equals number of rows
    if df.shape[0] == df.shape[1]:
        return df
    else:
        print('Shape invalid! Sudoku is not a square.')
        exit()

# Main Function
if __name__ == "__main__":

    # TODO: define params
    csv_file = "data/sudoku.csv"
    csv_sep = ","

    # TODO: instead of csv-file read image

    # TODO: read in csv-file instead of image
    sudoku = read_sudoko_csv(file=csv_file, sep=csv_sep)
    print(sudoku)

    # TODO: count rows and cols, must be equal

    # TODO: count number of 3x3 blocks

    # TODO: create empty list for each row and col

    # TODO: create empty list for each block

    # TODO: read rows and cols, put existing numbers in lists

    # TODO: read blocks, put existing numbers in lists