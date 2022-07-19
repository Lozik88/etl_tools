import faker
import os
import csv
import uuid
import concurrent.futures
import time
import numpy as np
import uuid

from pathlib import Path

def make_sample(filepath='sample.csv',batch=5000,size=5,unit='mb'):
    fake=faker.Faker()
    if os.path.exists(filepath):
        os.remove(filepath)
    headers=[
        'uuid'
        ,'Name'
        ,'Email'
        ,'Address']
    first_pass=True
    records = []
    with open(filepath,'a') as f:
        writer = csv.writer(f)
        while (os.path.getsize(filepath)//1024)//1024**2 < size:
            # creating fake records
            for _ in range(batch):
                if first_pass:
                    records.append(headers)
                    first_pass=False
                records.append(
                [
                    str(uuid.uuid4())
                    ,fake.name()
                    ,fake.email()
                    ,fake.address()
                ]
                )                
            writer.writerows(records)
            cur_size=(os.path.getsize(filepath)/1024**2)
            print('Current filesize: ',cur_size, ' mb. ')
# def _make_file(writer:csv._writer,records:list):
#     pass

def so_csv_1():
    """
    https://stackoverflow.com/questions/27731458/fastest-way-to-write-large-csv-with-python
    """
    outfile = Path('data-alt.csv')
    chunksize = 1_800_000

    data = [
    [uuid.uuid4() for i in range(chunksize)],
    np.random.random(chunksize) * 50,
    np.random.random(chunksize) * 50,
    np.random.randint(1000, size=(chunksize,))
]
    rows = ['%s,%.6f,%.6f,%i\n' % row for row in zip(*data)]

    t0 = time.time()
    with open(outfile, 'a') as csvfile:
        csvfile.writelines(rows)
    tdelta = time.time() - t0
    print(tdelta)

if __name__ == '__main__':    
    # so_csv_1()

    
    make_sample(filepath='15gb_file.csv',size=15,batch=1000)