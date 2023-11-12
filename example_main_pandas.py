from istatapi.connections import discovery, retrieval
import pandas as pd
import os

dataset_chosen = '22_289'
data_dir = "./data_dir"
data = discovery.DataSet(dataset_chosen)
out = retrieval.get_data(data,True, data_dir=data_dir)

ds = pd.read_csv(f"{os.path.join(data_dir,dataset_chosen)}.csv",chunksize=1000)
print(ds)