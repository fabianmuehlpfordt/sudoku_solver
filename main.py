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

def create_dict_rows(df):
    # create empty dict
    dict = {}

    # iterating over rows
    for i, rows in df.iterrows():
        dict[f'row_{i}'] = df.iloc[i, :].to_list()

    # return dict
    return dict

def create_dict_cols(df):
    # create empty dict
    dict = {}

    # iterating over cols
    for col in df:
        dict[f'col_{col}'] = df.iloc[:, col].to_list()

    # return dict
    return dict

def create_dict_blocks(df, blocks):
    # create empty dict
    dict = {}

    # slice df into blocks and store numbers, x = columns, y = rows
    x = 0
    while x < blocks:
        y = 0
        while y < blocks:
            i = 0
            num_blocks = []
            while i < 3:
                num_blocks = num_blocks + df.iloc[y*3:y*3+2,x*3+i].to_list()
                i += 1

            dict[f'block_{x}{y}'] = num_blocks
            y += 1
        x += 1

    # return dict
    return dict

# Main Function
if __name__ == "__main__":

    # define params
    test_mode = True
    csv_file = "data/sudoku.csv"
    csv_sep = ","

    # TODO: instead of csv-file read image

    # read in csv-file instead of image
    # count rows and cols, must be equal
    sudoku = read_sudoko_csv(file=csv_file, sep=csv_sep)
    if test_mode: print(sudoku)

    # count number of 3x3 blocks
    blocks = int( sudoku.shape[1] / 3 )
    if test_mode: print(f'number blocks: {blocks}')

    # create empty list for each row and col
    # read rows and cols, put existing numbers in lists
    num_rows = create_dict_rows(df=sudoku)
    num_cols = create_dict_cols(df=sudoku)
    num_blocks = create_dict_blocks(df=sudoku, blocks=blocks)
    if test_mode: print(num_rows, "\n", num_cols, "\n", num_blocks)

    # TODO: create empty list for each block



    # TODO: read blocks, put existing numbers in lists