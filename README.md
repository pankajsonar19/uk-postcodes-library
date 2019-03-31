# uk-postcodes-library
The following project contains a simple library for validating and formatting the UK-postcodes.

- This library requires to download the post-codes from the Code-Point Open data, november 2017 and extract all the csv files in DATA folder in your project.

- Then you need to run load_csv.py file. This file will generate a postcodes.pkl (pickle file), which will be used during postcodes validation.

## USAGE

## As Python Library

#### Example:

   ### from uk_postcodes.postcodes import format_postcode, deep_validaion, load_postcodes

- You need to call this function first as it loads the postcodes.pkl file, which is use for validation.
  	### load_postcodes()

- It will bring any input code in single capital letters format.
    ### format_postcode('AI2 9aa') 
    Output: AI29AA

- This function will match our input code with the code which is present in our pickle file ( existing database)
    ### deep_validation('AI2 9aa') 
    Output: The code existence and validity is: False
