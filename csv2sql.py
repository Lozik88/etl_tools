from asyncio import subprocess
import random
import csv
import sqlite3
import string

def randchar(length:int) -> str:
    """
    Creates a randomly generated string. 
    """
    return ''.join([random.choice(string.ascii_letters) for i in range(length)])

# def make_csv(rows:int=1000,batch:int=100,cols:int=100):
#     """
#     Makes a sample .csv file.
#     """
#     span = range(1,cols+1)
#     colnames = ['col'+str(i) for i in span]
#     make_records = lambda val:[val for i in span]
#     record = [randchar(random.randint(0,50)) for _ in span]
    
#     with open('sample.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter=',',
#                                 quotechar='"', quoting=csv.QUOTE_MINIMAL)
#         writer.writerow(colnames)
#         # record = [randchar(random.randint(0,100)) for _ in span]
#         records=[]
#         is_done=False
#         while True:
#             if batch>rows:
#                 batch=batch-rows
#                 is_done = True
#             for _ in range(1,batch+1):
#                 records.append([randchar(random.randint(0,50)) for _ in span])
#             writer.writerows(records)
#             if is_done:
#                 break
#             rows-=batch
#             records=[]


        # for _ in range(1,rows+1):
        #     record = [randchar(random.randint(0,100)) for _ in span]
        #     writer.writerows(record)
# make_csv(100**4,10000)

import csv
from faker import Faker
import datetime
headers = ["Email Id", "Prefix", "Name", "Birth Date", "Phone Number", "Additional Email Id",
               "Address", "Zip Code", "City","State", "Country", "Year", "Time", "Link", "Text"]
def datagenerate(records:int=10000, batches:int=10000, headers:list=headers):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers
    with open("People_data.csv", 'wt') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(records):
            full_name = fake.name()
            FLname = full_name.split(" ")
            Fname = FLname[0]
            Lname = FLname[1]
            domain_name = "@testDomain.com"
            userId = Fname +"."+ Lname + domain_name
            
            writer.writerow({
                    "Email Id" : userId,
                    "Prefix" : fake.prefix(),
                    "Name": fake.name(),
                    "Birth Date" : fake.date(pattern="%d-%m-%Y", end_datetime=datetime.date(2000, 1,1)),
                    "Phone Number" : fake1.phone_number(),
                    "Additional Email Id": fake.email(),
                    "Address" : fake.address(),
                    "Zip Code" : fake.zipcode(),
                    "City" : fake.city(),
                    "State" : fake.state(),
                    "Country" : fake.country(),
                    "Year":fake.year(),
                    "Time": fake.time(),
                    "Link": fake.url(),
                    "Text": fake.word()
                    })
    
if __name__ == '__main__':
    datagenerate()
    print("CSV generation complete!")
    subprocess.run