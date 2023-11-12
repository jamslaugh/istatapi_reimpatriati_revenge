from istatapi.connections import discovery, retrieval
from datasets import load_dataset, Features, Value
import os


dataset_chosen = '22_289'
data_dir = "./data_dir"
data = discovery.DataSet(dataset_chosen)
out = retrieval.get_data(data,True, data_dir="./data_dir")

features = Features(
                {
                    "DATAFLOW":Value("string"),
                    "FREQ":Value("string"),
                    "ETA":Value("string"),
                    "ITTER107":Value("string"),
                    "SESSO":Value("string"),
                    "STACIVX":Value("string"),
                    "TIPO_INDDEM":Value("string"),
                    "TIME_PERIOD":Value("string"),
                    "OBS_VALUE":Value("string"),
                    "BREAK":Value("string"),
                    "CONF_STATUS":Value("string"),
                    "OBS_PRE_BREAK":Value("string"),
                    "OBS_STATUS":Value("string"),
                    "BASE_PER":Value("string"),
                    "UNIT_MEAS":Value("string"),
                    "UNIT_MULT":Value("string"),
                    "METADATA_EN":Value("string"),
                    "METADATA_IT":Value("string")
                }
            )

ds = load_dataset(
                "csv",
                cache_dir="./test_cache",
                data_files={"train":f"{os.path.join(data_dir,dataset_chosen)}.csv"},
                features=features
                 )
print(ds)