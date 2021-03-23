# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.

import json
import logging


# how do I get the color code from the dic and match it to 
# user input?
# how do i log the requests of valid and invalid colors?
# how do i classify what a valid and invalid error is?
# how do i implement errors if the color doesn't exist?


def get_color_code(color_name):

    if type(color_name) == str:
        color_name = color_name.lower().strip()

    try:
        with open('./color_check/data/css-color-names.json') as f:
            data = json.load(f)
            color_hex_code = data[color_name]
    
    except KeyError:
        logging.error('KeyError: {color_name}')
        raise TypeError(f'KeyError: {color_name}')

   
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.






    # listElement = color_name[0]
    # print (listElement)
    # json_data = data
    # hexcode = json_data[listElement]

    # return hexcode
