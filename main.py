import pandas as pd

def callTsv():
    df = pd.read_csv('reviews.tsv', sep = '\t' )
    df


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    callTsv()
