import os
import glob
import pandas as pd
import pickle



base_path = os.path.dirname(os.path.abspath(__file__))

directory = 'CSV\*.csv'

# Function to read and load the csv files and store the list of uk codes in a pickle file.
def read_and_load_data():

    postcodes = []

    for csvfiles in glob.glob(os.path.join(base_path, directory)):
        # print('Loading file',csvfiles)
        df = pd.read_csv(csvfiles, sep=',', quotechar='"')
        new_df = df.iloc[:, 0]

        new_li = new_df.tolist()
        for x in new_li:
            outward_code = x[:-3].strip()

            inward_code = x[-3:].strip()

            postcode = outward_code + inward_code
            postcodes.append(postcode)

    with open("uk_postcodes\postcodes.pkl", "wb") as fp:
       pickle.dump(postcodes, fp)

    print('The pickle file {} is dumped'.format(fp.name))


if __name__ == '__main__':
    read_and_load_data()
