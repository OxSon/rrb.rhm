import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Directory containing the CSV files
directory = './benchmarks/'

# Get all CSV files in the directory
csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Iterate over each CSV file
for file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(os.path.join(directory, file))
    print(df)
    
    # Group the data by operation code and structure type
    grouped_data = df.groupby(['operation', 'structure type'])
    
    # Mapping dictionary for structure types
    structure_types = {
        0: 'Cons List',
        1: 'Catvec (RRB Tree)',
        2: 'Vector (RB Tree)',
        3: 'Hashtable (Map from indices to values)',
        4: 'COW Array'
    }

    # Iterate over each group
    for group, data in grouped_data:
        # Get the structure type from the group
        structure_type = structure_types[group[1]]
        
        # Calculate the average time result (cpu, real, gc)
        """
        try:
            avg_time = data[['cpu', 'real', 'gc']].mean(axis=1)
        except: 
            avg_time =  np.inf
        """
        avg_time = data['cpu']
        
        # Plot size against average time result with labeled lines
        plt.plot(data['size'], avg_time, label=structure_type)
        
    # Set the plot title and labels
    plt.title(f'Graph for {file}')
    plt.xlabel('size')
    plt.ylabel('time')

    # Add a legend
    plt.legend()

    # Show the plot
    # plt.show()
    plt.savefig(os.path.join(directory, file.removesuffix('.csv') + '.png'))
    plt.clf()
