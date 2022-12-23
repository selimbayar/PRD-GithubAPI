"""
This file must be run first since other python files use the csv files created here

This file has two functions, topStarred and topStarredByLanguage
Before the functions, a csv file called data.csv is created, which includes all information of top 100 starred and forked repos,
and lists the top 100 repos for every language

The first function takes data.csv and a number as input and creates a new csv file called top(number).csv,
which includes info on the top 100 (or the given number) starred repos

The second function also takes data.csv and a number, but also a language as input, and creates a new csv file called top(number)(language).csv,
which includes info on the top 100 (or the given number) starred repos of the given language


"""

import json

import requests
import os

# setup access_token, and headers

access_token = os.getenv('GITHUB_TOKEN', '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')
headers = {'Authorization': "Token " + access_token}

# Takes the link of the repo which includes the top starred repos that updates daily, do not change
query_url = "https://api.github.com/repos/EvanLi/Github-Ranking/contents/Data"

# API call for the specified URL

repo = requests.get(query_url, headers=headers)

# Turn the data into a json file

repo_json_file = repo.json()

# Gets the url of the csv file
data_url = repo_json_file[0]['download_url']

# Opens a new csv file to write to
csvFile = open('data.csv', 'w')
# Names of the headers
headers = 'rank,', 'item,', 'repo_name,', 'stars,', 'forks,', 'language,', 'repo_url,', 'username,', 'issues,', 'last_commit,', 'description,'
r = requests.get(data_url).text
csvFile.write(r)
csvFile.close()


def topStarredList(input_filename, number=100):
    """
    Goes through the data csv file line by line and lists the top 100 starred repos on a new file
    :param input_filename: (str) name of a csv file
    :param number: (int) desired number of repos to list

    """
    # Opens the csv file to read from and a new file to write to
    file_in = open(input_filename, 'r')
    file_out = open('top' + str(number) + ".csv", 'w')

    # Writes a header for the new file
    file_out.write('rank,repo_name,stars,forks,language,repo_url,username,issues,last_commit,description\n')

    # Skips the header
    next(file_in)

    # Creates new list, strips the csv file and appends to list
    aList = []
    for line in file_in:
        each_line = line.strip("\n").split(',', 10)
        aList.append(each_line)

    # Lists the top given number of repos to the file
    for i in range(number):
        # Skips 1 to not include the header "item" from data.csv
        for j in ([0, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
            # To not add a ',' at the end of every line
            if j != 10:
                file_out.write(aList[i][j] + ',')
            else:
                file_out.write(aList[i][j])
        file_out.write('\n')

    # Closes all files
    file_in.close()
    file_out.close()


def topStarredByLanguage(input_filename, language, number=100):
    """
    Goes through the data csv file line by line and lists the top 100 starred repos on a new file
    :param input_filename: (str) name of a csv file
    :param language: (str) desired language to list
    :param number: (int) desired number of repos to list

    """

    # Opens data.csv to read from
    file_in = open(input_filename, 'r')
    # Opens new file to write to
    file_out = open('top' + str(number) + language + '.csv', 'w')

    # Writes headers to new file
    file_out.write('rank,repo_name,stars,forks,language,repo_url,username,issues,last_commit,description\n')

    # Skips the header
    next(file_in)

    # Creates new list, strips the csv file and appends to list
    aList = []
    for line in file_in:
        each_line = line.strip("\n").split(',', 10)
        aList.append(each_line)

    # Lists the top given number for the given language
    counter = 0
    for element in aList:
        # Checks if given number is reached
        if counter >= number:
            break
        if element[1] == language:
            # Writes the information from data.csv to new file, doesn't include the header 'item' from data.csv
            file_out.write(f'{element[0]},{element[2]},{element[3]},{element[4]},{element[5]},{element[6]},'
                           f'{element[7]},{element[8]},{element[9]},{element[10]}\n')
            # Increments counter every time a new line is written to have the exact number given
            counter += 1

    # Closes all files
    file_in.close()
    file_out.close()


def main():
    """
    Creates csv files for the top given number of stars, and given language
    Data.csv will be the csv file that has the information for the top 100 stars, forks, and every language

    """
    # Creates new csv file with top 100 starred repos
    topStarredList('data.csv', 100)

    # The language we want to rank
    language = "Python"

    # Creates new csv file with top 100 starred repos for given language
    topStarredByLanguage('data.csv', language, 100)


if __name__ == "__main__":
    main()
