import pandas as pd
# import numpy as np


def details_clean():
    # Basic cleaning process for Details Data
    df = pd.read_csv('details2000.csv', dtype={'FLOOD_CAUSE': 'str', 'TOR_OTHER_CZ_STATE': 'str', 'TOR_OTHER_CZ_NAME': 'str', 'TOR_OTHER_WFO': 'str', 'DAMAGE_PROPERTY': 'str', 'DAMAGE_CROPS': 'str'})
    details = ['details2001.csv', 'details2002.csv', 'details2003.csv', 'details2004.csv', 'details2005.csv', 'details2006.csv', 'details2007.csv', 'details2008.csv', 'details2009.csv','details2010.csv','details2011.csv','details2012.csv','details2013.csv','details2014.csv','details2015.csv','details2016.csv','details2017.csv','details2018.csv','details2019.csv','details2020.csv','details2021.csv','details2022.csv']
    for detail in details:
        temp_df = pd.read_csv(detail, dtype={'FLOOD_CAUSE': 'str', 'TOR_OTHER_CZ_STATE': 'str', 'TOR_OTHER_CZ_NAME': 'str', 'TOR_OTHER_WFO': 'str', 'DAMAGE_PROPERTY': 'str', 'DAMAGE_CROPS': 'str'})
        df = pd.concat([df, temp_df], sort=False)
    df['BEGIN_MONTH'] = df['BEGIN_YEARMONTH']%100
    df['BEGIN_YEAR'] = (df['BEGIN_YEARMONTH']/100).astype(int)
    df = df.drop(columns = ['BEGIN_YEARMONTH', 'CATEGORY', 'BEGIN_DATE_TIME'])
    return df

# df = details_clean()
# with open('details.csv', 'w') as csv_file:
#     df.to_csv(path_or_buf=csv_file)



def location_clean():
    # Basic cleaning process for Locations Data
    dfloc = pd.read_csv('locations2000.csv')
    locations = ['locations2001.csv', 'locations2002.csv', 'locations2003.csv', 'locations2004.csv', 'locations2005.csv', 'locations2006.csv', 'locations2007.csv', 'locations2008.csv', 'locations2009.csv','locations2010.csv','locations2011.csv','locations2012.csv','locations2013.csv','locations2014.csv','locations2015.csv','locations2016.csv','locations2017.csv','locations2018.csv','locations2019.csv','locations2020.csv','locations2021.csv','locations2022.csv']
    for location in locations:
        temp_df = pd.read_csv(location)
        dfloc = pd.concat([dfloc, temp_df], sort=False)
    dfloc['BEGIN_MONTH'] = dfloc['YEAR_MONTH']%100
    dfloc['BEGIN_YEAR'] = (dfloc['YEAR_MONTH']/100).astype(int)
    dfloc = dfloc.drop(columns = ['YEAR_MONTH', 'LAT2', 'LON2', 'LOCATION', 'RANGE'])

# dfloc = location_clean()
# with open('locs.csv', 'w') as csv_file:
#     dfloc.to_csv(path_or_buf=csv_file)

def fatalities_clean():
    # Basic cleaning process for Locations Data
    dffat = pd.read_csv('fatalities2000.csv')
    fatilities = ['fatalities2001.csv', 'fatalities2002.csv', 'fatalities2003.csv', 'fatalities2004.csv', 'fatalities2005.csv', 'fatalities2006.csv', 'fatalities2007.csv', 'fatalities2008.csv', 'fatalities2009.csv','fatalities2010.csv','fatalities2011.csv','fatalities2012.csv','fatalities2013.csv','fatalities2014.csv','fatalities2015.csv','fatalities2016.csv','fatalities2017.csv','fatalities2018.csv','fatalities2019.csv','fatalities2020.csv','fatalities2021.csv','fatalities2022.csv']
    for fat in fatilities:
        temp_df = pd.read_csv(location)
        dffat = pd.concat([dffat, temp_df], sort=False)
    dffat['BEGIN_MONTH'] = dffat['EVENT_YEARMONTH']%100
    dffat['BEGIN_YEAR'] = (dffat['EVENT_YEARMONTH']/100).astype(int)
    dffat = dffat.drop(columns = ['EVENT_YEARMONTH', 'FAT_YEARMONTH', 'FAT_DAY', 'FATALITY_DATE', 'FAT_TIME', 'FATALITY_AGE', 'FATALITY_SEX'])

# dffat = location_clean()
# with open('fats.csv', 'w') as csv_file:
#     dffat.to_csv(path_or_buf=csv_file)

