# importing pandas as pd
import pandas as pd
import numpy as np
import os

cwd = os.getcwd()
  
# read an excel file and convert 
# into a dataframe object
faire_catalog_df = pd.DataFrame(pd.read_excel("faire-product-catalog.xlsx"))
faire_catalog_df = faire_catalog_df.drop(faire_catalog_df.index[0:2])

# Target dataframe for preet catalog format
preet_catalog_df = pd.DataFrame(columns=['Product Id', 'Product Identifier', 'Username', 'Name', 'Description', 
                                         'Youtube Video', 'Category Identifier', 'Brand Identifier', 'Product Type Identifier', 'Model', 
                                         'Min Selling Price', 'Tax Category Identifier', 'Length', 'Width', 'Height', 
                                         'Dimension Unit Identifier', 'Weight', 'Weight Unit Identifier', 'Product Warranty', 'Shipping Country Code', 
                                         'Cod Available', 'Approved', 'Active', 'Deleted'])

unique_product_names = faire_catalog_df['Product Name (English)'].unique()

i = 0
# for i in range(len(unique_product_names)):

product_df = faire_catalog_df.loc[faire_catalog_df['Product Name (English)'] == unique_product_names[i]]

product_identifier = product_df['Product Token'].iloc[0]
variant_min_price = product_df['Min Selling Price'].min()
product_name = product_df['Product Name (English)'].iloc[0]
product_description = product_df['Description (English)'].iloc[0]
product_category = product_df['Product Type'].iloc[0]
product_length = product_df['Length'].iloc[0]
product_width = product_df['Width'].iloc[0]
product_height = product_df['Height'].iloc[0]
product_weight = product_df['Weight'].iloc[0]
product_warranty = 0

# print(df2)

# create row in preet_catalog_df
new_row = [i, product_identifier, 'GIVEN_USERNAME', product_name, product_description, 
           np.nan, product_category, 'GIVEN_BRAND_ID', 'Physical', np.nan, 
           variant_min_price, 'pet service', product_length, product_width, product_height, 
           'Inches', np.nan, 'Pound', product_weight, np.nan, 
           'NO', 'YES', 'YES', 'NO']

# append row to the dataframe
preet_catalog_df.loc[len(preet_catalog_df)] = new_row

print(preet_catalog_df)

# save preet_catalog_df to csv file
# path = cwd + "/preet-product-catalog.csv"
# preet_catalog_df.to_csv(path, index=False)