import pandas as pd
from time import sleep 

#load streaming data
power_df = pd.read_csv('power_streaming_data.csv')

for x in range(20):
    #create new dataframe with 5 randomly selected records of data
    sample_df = power_df.sample(n=5)
    #drop sampled indicies from original dataframe to avoid resampling 
    drop_index = sample_df.index.tolist()
    power_df.drop(index=drop_index, inplace=True)
    #save sample data to csv in the streaming_files folder
    #set index to false to avoid writing out indicies to csv
    sample_df.to_csv(f'streaming_files/batch_{x}', index=False)
    #pause for 10 seconds in between writing new files
    sleep(20)
    