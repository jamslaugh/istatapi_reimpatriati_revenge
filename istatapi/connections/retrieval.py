# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_retrieval.ipynb.

# %% auto 0
__all__ = ['RESOURCE', 'get_data', 'make_url_key']

# %% ../nbs/03_retrieval.ipynb 1
from istatapi.connections.discovery import DataSet
from istatapi.connections import ISTAT
import io
import os

# %% ../nbs/03_retrieval.ipynb 4
RESOURCE = "data"
# TODO: accept json response as well (?)


def get_data(dataset: DataSet, save_text=False, data_dir = "data_dir", writer_chunk_size = None):
    "returns a dataframe of the filitered 'dataset' or a series of files saved in tmp folder data_dir"
    flowRef = dataset.identifiers["df_id"]
    filters = dataset.filters
    key = make_url_key(filters)
    path_parts = [RESOURCE, flowRef, key]
    path = "/".join(path_parts)
    request = ISTAT()
    response = request._request(path, headers={"Accept": "text/csv"})
    if not save_text:
        return response
    else:
        try:
            if not os.path.exists(data_dir):
                os.mkdir(data_dir)
            with open(f"{os.path.join(data_dir,flowRef)}.csv","wb") as f:
                for chunk in response.iter_content(writer_chunk_size if writer_chunk_size is not None else 1000):
                    f.write(chunk)
                f.close()

            return {"saved_path": f"{os.path.join(data_dir,flowRef)}.csv", "operation_done":"Ok"}
        except Exception as e:
            return {"saved_path": "null", "operation_done": "Ko", "exception": e}

def make_url_key(filters: dict):
    key = ""

    for i, filter_tuple in enumerate(filters.items()):

        filter = filter_tuple[0]
        filter_value = filter_tuple[1]

        # add a + and convert to str
        if type(filter_value) == list:
            filter_value = "+".join(filter_value)

        if i != 0:
            if list(filters.values())[i - 1] != ".":
                filter_value = "." + filter_value

        key += filter_value

    return key
