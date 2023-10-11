#!/usr/bin/python3

# Define the update_dictionary function that takes three arguments: a_dictionary, key, and value.
# Check if the key exists in the a_dictionary using the in operator.
# If the key exists, update its value with the new value.
# If the key doesn't exist, create a new key-value pair in the a_dictionary.
# Create an empty dictionary with key as the only key and value as the corresponding value.
# Merge this new dictionary with a_dictionary using a loop to add the key-value pair.
# Iterate over the new dictionary using a loop.
# For each key-value pair, add it to a_dictionary using a_dictionary[key] = value.

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
