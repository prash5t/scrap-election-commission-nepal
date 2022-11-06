# returns voter's information inside python list
def get_tables_rows(table):
    voters_record = []
    # using regex to skip first row which is header
    for tr in table.find_all("tr")[1:]:
        voter_record = []
        tds = tr.find_all("td")
        # using regex to skip last cell which is not required to collect
        for td in tds[0:-1]:
            voter_record.append(td.text.strip())
        voters_record.append(voter_record)
    return voters_record


# function to obtain only the name of election center
def create_file_name(table):
    for th in table.find("tr").find_all("th")[-1]:
        election_center_name = th.text.strip()
    return election_center_name.replace(" ", "-").replace(",", "").replace(".", "")
