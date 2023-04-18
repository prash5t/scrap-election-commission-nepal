## Get voter information of Nepal 🇳🇵

Python task to perform web scraping on voters information
i.e. publicly available on the website of Election Comission Nepal

##### Short Description

> Downloads voters information on bulk
> i.e. publicly available on the website of Election Comission Nepal

##### Instruction

> Provide argument values for **state**, **district**, **vdc_num**, **ward**
> and **reg_centre** in the **voter** variable of main.py file.

**To install necessary packages:**

```sh
pip install -r requirements.txt
```

**Line to modify arguments in main.py file:**
Example:

```sh
voters = extract_voters(state="1", district="4",
                        vdc_mun="5030", ward="3", reg_centre="2347")
```

##### Output

> Saves a CSV file to the **voters-warehouse** directory
> with the election center's name as the file name.
> Sample of saved files:

```sh
कन्काई-मावि-सुरुङ्ग.csv
जनचेतना-सामुदायिक-माध्यामिक-विद्यालय-गोहीखाडी.csv
```

##### Used Python packages

Uses a number of open source projects to work properly:

- Pandas
- Beautiful Soup
- Requests

##### Steps necessary to improve this project

The voter records are imported/downloaded/saved all at once,
but we must provide the arguments for each voting center manually and it is a hassle.
**Reason to provide argument values manually:**
While working on this project, I learned that there are over ten thousand election centers in Nepal, each with a unique address that combines state, district, municipality/vdc, ward, and registered center. I couldn't find a way to keep/map election center's record at a single place. And it is challenging to inspect elements and go through thousands of records to create a single file containing all of the election center's necessary arguments for retrieving all of the voter's records at once. As a result, in order to retrieve voter records from that specific election center, we must provide arguments manually.
