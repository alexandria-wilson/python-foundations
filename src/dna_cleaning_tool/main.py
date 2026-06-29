import pandas as pd # loads the pandas library as the nickname: pd
def main():
    df = pd.read_csv("sample.csv") # loads CSV file into DataFrame
    print(df)

if __name__ == "__main__":
    main()