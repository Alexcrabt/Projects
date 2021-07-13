'''
@author: Alexander Crabtree
            acrabtree15@gmail.com
'''
from geopy import geocoders
import pandas as pd
import numpy as np
import re

def Address_Checker(Daddr, addr):
    g = geocoders.GoogleV3(api_key="")
    try: 
        location = g.geocode(addr)
        address= location.address

        if location.raw['address_components'][1]['types'][0] == 'administrative_area_level_2' and (Daddr != 'Homeless' and Daddr != 'HOMELESS'):
            county= location.raw['address_components'][1]['long_name']
            county= county.replace('County', '')
            address_l= address.split(",")
            Vaddr= address_l[0]
            Vcity= address_l[1]
            zip_split= address_l[2].split(" ")
            Vstate= zip_split[1]
            Vzip= zip_split[2]
            return Vaddr, Vcity, Vstate, Vzip, county

        elif location.raw['address_components'][2]['types'][0] == 'administrative_area_level_2' and (Daddr != 'Homeless' and Daddr != 'HOMELESS'):
            county= location.raw['address_components'][2]['long_name']
            county= county.replace('County', '')
            address_l= address.split(",")
            Vaddr= address_l[0]
            Vcity= address_l[1]
            zip_split= address_l[2].split(" ")
            Vstate= zip_split[1]
            Vzip= zip_split[2]
            return Vaddr, Vcity, Vstate, Vzip, county

        elif location.raw['address_components'][3]['types'][0] == 'administrative_area_level_2' and (Daddr != 'Homeless' and Daddr != 'HOMELESS'):
            county= location.raw['address_components'][3]['long_name']
            county= county.replace('County', '')
            address_l= address.split(",")
            Vaddr= address_l[0]
            Vcity= address_l[1]
            zip_split= address_l[2].split(" ")
            Vstate= zip_split[1]
            Vzip= zip_split[2]
            return Vaddr, Vcity, Vstate, Vzip, county

        elif location.raw['address_components'][4]['types'][0] == 'administrative_area_level_2' and (Daddr != 'Homeless' and Daddr != 'HOMELESS'):
            county= location.raw['address_components'][4]['long_name']
            county= county.replace('County', '')
            address_l= address.split(",")
            Vaddr= address_l[0]
            Vcity= address_l[1]
            zip_split= address_l[2].split(" ")
            Vstate= zip_split[1]
            Vzip= zip_split[2]
            return Vaddr, Vcity, Vstate, Vzip, county

        elif location.raw['address_components'][5]['types'][0] == 'administrative_area_level_2' and (Daddr != 'Homeless' and Daddr != 'HOMELESS'):
            county= location.raw['address_components'][5]['long_name']
            county= county.replace('County', '')
            address_l= address.split(",")
            Vaddr= address_l[0]
            Vcity= address_l[1]
            zip_split= address_l[2].split(" ")
            Vstate= zip_split[1]
            Vzip= zip_split[2]
            return Vaddr, Vcity, Vstate, Vzip, county

        else:
            return np.nan, 'Needs Human Check', np.nan, np.nan, np.nan
    except Exception:
        return np.nan, 'Needs Human Check', np.nan, np.nan, np.nan

def Address_Maker(add, city, state, zip):

    address= add + ', ' + city + ', '+ state+ ', '+ zip

    return address

def String_Empty1(add, city, state, zip):

    return np.nan


def String_Empty2(Dadd, add):

    return np.nan, np.nan, np.nan, np.nan, np.nan

def main():

    global com_addr

    data= pd.read_csv('addresses.csv')

    com_addr= pd.Series(data.apply(lambda row: Address_Maker(row['Daddress'], row['Dcity'], row['Dstate'], row['Dzip']) if pd.notna(row['Daddress']) else String_Empty1(row['Daddress'], row['Dcity'], row['Dstate'], row['Dzip']), axis=1))
    com_addr= pd.DataFrame(com_addr.tolist(), columns=['address'], index=com_addr.index)
    com_addr= pd.concat([data['Daddress'], com_addr], axis=1)

    Vaddr= pd.Series(com_addr.apply(lambda row: Address_Checker(row['Daddress'], row['address']) if pd.notna(row['address']) else String_Empty2(row['Daddress'], row['address']), axis=1))
    Vaddr= pd.DataFrame(Vaddr.tolist(), columns=['DVerifAddress', 'DVerifCity', 'DVerifState', 'DVerifZip','GoogleCountyName'], index=Vaddr.index)

    data= pd.concat([data, Vaddr], axis=1)

    data.to_csv('Vaddresses.csv', index= False)

if __name__ == "__main__":  main()