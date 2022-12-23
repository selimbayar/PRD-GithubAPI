"""
This file must be run after all three previous files were run since it uses csv files that were created before

This file has 4 functions, all of them print information on certain things

The first function, topReposData, takes the top100.csv (or top(number).csv) file from before,
and prints the number of languages used in the top 100

The second function, dataByKeywords, can only go through data.csv (to avoid header confusions and to go through thousands of repos),
and prints the number of languages of repos that include the given keywords in its description

The third function, dataByLocation, goes through the top_contributor_info.csv file,
and prints the number of people in that file who live in the given location

The fourth and final function, dataByCompany, also goes through the top_contributor_info.csv file,
and prints the number of people in that file who work in the given company

"""

import json

import requests
import os

# setup access_token, and headers

access_token = os.getenv('GITHUB_TOKEN', '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')
headers = {'Authorization': "Token " + access_token}


def topReposData(input_filename):
    """
    Goes through the top repos in given file and provides their data
    :param input_filename: (str) name of a csv file

    """
    # Opens the csv file to read from
    file_in = open(input_filename, 'r')

    # Skips the header
    next(file_in)

    # Creates new list, strips the csv file and appends to list
    aList = []
    for line in file_in:
        each_line = line.strip("\n").split(',', 9)
        aList.append(each_line)

    # Creates a new dictionary
    aDict = dict()
    # Goes through every data in the list
    for element in aList:
        # if the language is not in the dictionary, adds it as 1
        language = element[4]
        if language not in aDict.keys():
            aDict[language] = 1
        # if it is, increases the count by one
        else:
            aDict[language] += 1

    # Closes all files
    file_in.close()

    # Sorts the dictionary in descending order and prints the new dictionary
    sorted_dict = sorted(aDict.items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_dict)
    print(f"Languages used in top {sum(converted_dict.values())}:")
    print(f'{converted_dict}\n')


def dataByKeywords(input_filename, keywords):
    """
    Goes through all repos in every language and finds the ones with given keywords
    :param input_filename: (str) name of a csv file
    :param keywords: (str) given keywords to look in descriptions

    """
    # Opens the csv file to read from
    file_in = open(input_filename, 'r')

    # Skips the header
    next(file_in)

    # Creates new list, strips the csv file and appends to list
    aList = []
    for line in file_in:
        each_line = line.strip("\n").split(',', 10)
        aList.append(each_line)

    # Creates new dictionary
    aDict = dict()
    # Goes through every data in the list
    for element in aList:
        # converts the description to all lower case to avoid missing upper cases
        description = element[10].lower()
        language = element[5]
        # Checks if given keywords are in the description
        if keywords.lower() in description:
            # if the language is not in the dictionary, adds it as 1
            if language not in aDict.keys():
                aDict[language] = 1
            # if it is, increases the count by one
            else:
                aDict[language] += 1

    # Sorts the dictionary in descending order and prints the new dictionary
    sorted_dict = sorted(aDict.items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_dict)
    print(f"Languages that use {keywords}:")
    print(f'{converted_dict}\n')


def dataByLocation(input_filename, location):
    """
    Goes through all users in the csv file and finds the ones with given locations
    :param input_filename: (str) name of a csv file
    :param location: (str) given location to look in locations of user

    """
    # Opens the csv file to read from
    file_in = open(input_filename, 'r')

    # Skips the header
    next(file_in)

    # Creates new list, strips the csv file and appends to list
    aList = []
    for line in file_in:
        each_line = line.strip("\n").split(',', 6)
        aList.append(each_line)

    # Starts a counter to count the number of users in location
    counter = 0
    # Creates a list to keep the names of people in given company
    bList = []
    # Goes through every data in the list
    for element in aList:
        # converts the description to all lower case to avoid missing upper cases
        user_location = element[5].lower()
        username = element[1]
        # Checks if given location is in the location of the user
        if location.lower() in user_location:
            # increases the counter
            counter += 1
            # adds username to the list
            bList.append(username)

    print(f'There are {counter} people in {location}')
    print(f'{bList}\n')


def dataByCompany(input_filename, company):
    """
    Goes through all users in the csv file and finds the ones in given company
    :param input_filename: (str) name of a csv file
    :param company: (str) company to look in company of user

    """
    # Opens the csv file to read from
    file_in = open(input_filename, 'r')

    # Skips the header
    next(file_in)

    # Creates new list, strips the csv file and appends to list
    aList = []
    for line in file_in:
        each_line = line.strip("\n").split(',', 6)
        aList.append(each_line)

    # Starts a counter to count the number of users in a company
    counter = 0
    # Creates a list to keep the names of people in given company
    bList = []
    # Goes through every data in the list
    for element in aList:
        # converts the description to all lower case to avoid missing upper cases
        user_company = element[4].lower()
        username = element[1]
        # Checks if given location is in the location of the user
        if company.lower() in user_company:
            # increases the counter
            counter += 1
            # adds username to the list
            bList.append(username)

    print(f'There are {counter} people in {company}')
    print(f'{bList}\n')


def main():
    """
    The first function prints language information on the top 100 starred repos
    The second looks at descriptions of repos and prints the number of languages that has the given keywords in the description
    The third and fourth looks at the information of the top contributors and finds the number of people in given locations and companies
    """
    #
    topReposData('top100.csv')

    # Choose the keywords to look for
    keywords = "machine learning"
    # Can only work with data.csv
    dataByKeywords('data.csv', keywords)

    # Choose the location to look for
    location = "San Francisco"
    dataByLocation("top_contributor_info.csv", location)

    # Choose the company to look for
    company = "Microsoft"
    dataByCompany("top_contributor_info.csv", company)


if __name__ == "__main__":
    main()
