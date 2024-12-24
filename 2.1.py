import pandas as pd
import matplotlib.pyplot as plt
import csv
from sklearn.model_selection import train_test_split
def process_data(df):
    df['datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'], format='%Y/%m/%d %H:%M')
    df['10min'] = df['datetime'].dt.floor('10min')
    traffic_10min =df.groupby('10min')['datetime'].size().reset_index(name='count')
    return traffic_10min
def load_and_process_data(file_path):
    df = pd.read_csv(file_path)
    df = df.iloc[:, [2]]
    df_processed = process_data(df)
    return df_processed

if __name__ == "__main__":
    file_path = 'data.csv'
    traffic_10min = load_and_process_data(file_path)

    plt.figure(figsize=(15, 5))
    plt.plot(traffic_10min['10min'], traffic_10min['count'],label='Traffic Data', marker='o')
    plt.title('Traffic Data Over a Month (Every 10 Minutes)')
    plt.xlabel('Time')
    plt.ylabel('Traffic')
    plt.legend()
    plt.grid(True)
    plt.savefig('traffic_data_plot.png')
    plt.close()

    train, test = train_test_split(traffic_10min, test_size=0.3, shuffle=True)
    train.to_csv('traffic_data_train.csv', index=False)
    test.to_csv('traffic_data_test.csv', index=False)