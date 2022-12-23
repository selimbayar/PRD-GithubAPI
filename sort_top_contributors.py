"""
This file must be run after top100listing.py since it uses the csv files created there

This file has two functions: TopContributorList and TopContributorSort

The first functions takes a csv file from top100listing.py (for example top100Python.csv) as input,
and creates a new file including every contributor in the file and their number of contributions to their projects

The second function takes the created file from above and a number as input,
and sorts the top 100 (or the given number) contributors by their number of contributions to their projects

"""

import csv
import os
import pandas

import requests

# setup access_token, and headers

access_token = os.getenv('GITHUB_TOKEN', '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')
headers = {'Authorization': "Token " + access_token}


def TopContributorList(input_filename, output_filename):
    """
    Sorts the top contributors in given top repos from most contributed to least, includes every contributor
    :param input_filename: (str) name of a csv file
    :param output_filename: (str) desired name of new file
    """

    # Opens one file to read and one to write
    file_in = open(input_filename, 'r')
    file_out = open(output_filename, 'w')

    # Writes header to new file, and skips header from the input
    file_out.write('repo_name,username,language,number of contributions\n')
    next(file_in)

    # Creates new list, strips the csv file and appends to list
    aList = []
    for line in file_in:
        each_line = line.strip("\n").split(',', 9)
        aList.append(each_line)

    # for every repo, goes in the contributors url using the API
    for element in aList:
        contributors_url = f'https://api.github.com/repos/{element[6]}/{element[1]}/contributors'
        contributors = requests.get(contributors_url, headers=headers)
        contributors_file = contributors.json()
        # for every contributor, finds the number of times they have contributed to the repo
        for contributor in contributors_file:
            # Checks if the repository actually exists
            if contributor == "message" or contributor == "documentation_url":
                file_out.write('\n')
            # if it does, writes the new information on new file
            else:
                file_out.write(f'{element[1]},{contributor["login"]},{element[4]},{contributor["contributions"]}\n')

    # Closes all files
    file_in.close()
    file_out.close()


def TopContributorSort(input_filename, output_filename, number=100):
    """
    Takes the sorted csv file and decreases it to desired number
    :param input_filename: (str) name of a csv file
    :param output_filename: (str) desired name of new file
    :param number: (int) desired number of users in sorted file
    """

    # Reads the csv data from input file from the above function
    csvData = pandas.read_csv(input_filename)
    # Sorts by the number of contributions
    csvData.sort_values(['number of contributions'],
                        axis=0,
                        ascending=False,
                        inplace=True)

    # Opens a temporary file to write on, writes the sorted list
    file_out = open('TempSorted.csv', 'w')
    file_out.write(csvData.to_csv())
    # Closes temp file
    file_out.close()

    # Opens the temp file to read, and opens the final file to be written on
    file_in = open('TempSorted.csv', 'r')
    file_out2 = open(output_filename, 'w')

    # Writes header to new file, and skips header from the input
    file_out2.write('repo_name,username,number of contributions\n')
    next(file_in)

    # Creates new list, adds the desired number of users that was given
    aList = []
    count = 0
    for line in file_in:
        # When count exceeds the desired number, loop stops
        if count >= number:
            break
        each_line = line.strip("\n").split(',')
        aList.append(each_line)
        count += 1

    # Goes through the list and writes the repo_name, username, language, and number of contributions to new file
    for element in aList:
        repo_name = element[1]
        username = element[2]
        language = element[3]
        number_of_contributions = element[4]
        file_out2.write(f'{repo_name},{username},{language},{number_of_contributions}\n')

    # Closes all files
    file_in.close()
    file_out2.close()


def main():
    """
    The first function creates a list of every contributor from given csv file
    the second function decreases the size to desired number, creates a new sorted file to work with
    """
    TopContributorList("top100Python.csv", 'top_contributors.csv')
    TopContributorSort("top_contributors.csv", 'sorted_top_contributors.csv', 100)


if __name__ == "__main__":
    main()
