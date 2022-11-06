# function to extract information(html table) from Election Commision of Nepal's official website

import requests


def extract_voters(state, district, vdc_mun, ward, reg_centre):
    data_endpoint = 'https://voterlist.election.gov.np/bbvrs1/view_ward_1.php'
    form_data = {
        'state': state,
        'district': district,
        'vdc_mun': vdc_mun,
        'ward': ward,
        'reg_centre': reg_centre
    }
    response = requests.post(data_endpoint, data=form_data)
    return response.content
