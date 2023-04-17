import json
import os
import pandas as pd



def readJSON(jsonpath):
    with open(jsonpath, 'r') as f:
        data = json.load(f)
        df = pd.DataFrame(data)
    return df

def main():
    df = readJSON('bar.json')
    print(df)


if __name__ == '__main__':
    main()
