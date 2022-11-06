"""here yo go"""
from extract import extract_voters
from transform import get_tables_rows, create_file_name
from load import save_csv
from bs4 import BeautifulSoup


voters = extract_voters(state="1", district="4",
                        vdc_mun="5030", ward="3", reg_centre="2347")


soup = BeautifulSoup(voters, "html.parser")

tables = soup.find_all("table")

# naming header/column
column_names = ['sn', 'voter_num', 'voter_name',
                'age', 'gender', 'spouse_name', 'parents_name']

# using fifth index to select only the table consisting voter's record or rows
voters_record = get_tables_rows(tables[5])

# making name of election center to get unique file name for each of the election center records
file_name = create_file_name(tables[3])

# saves to voters-warehouse directory
save_csv(file_name, column_names, voters_record)
