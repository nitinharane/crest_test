import pandas as pd
from csv import writer
import os

input_filepath = './data/'
output_filepath = './output/'


def process_data(data_files):
    """This function is to read and process data files"""
    try:
        frames = []
        output_file = output_filepath + 'result.csv'
        for file in data_files:
            df = pd.read_csv(input_filepath + file, delimiter='\t')
            df.drop_duplicates()  # remove duplicates from dataframe
            frames.append(df)
        result = pd.concat(frames, ignore_index=True)
        result['gross_salary'] = result[['basic_salary', 'allowances']].sum(axis=1)
        result.to_csv(output_file, index=False)
        gross_salary = 'Second Highest Salary:{}'.format(result['gross_salary'].nlargest(2).min().astype(int))
        avg_salary = 'Average Salary:{}'.format(result['gross_salary'].min().astype(int))
        summary = [gross_salary, avg_salary]
        with open(output_file, 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(summary)
            f_object.close()
        status = "Files has been processed Successfully"
        return status
    except Exception as e:
        status = "Error while processing file: {}".format(e)
        return status


file_list = [x for x in os.listdir(input_filepath) if x.endswith('.dat')]
print(process_data(file_list))
