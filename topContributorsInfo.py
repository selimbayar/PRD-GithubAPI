"""
This file takes the sorted top contributors file from before,
and creates a new csv file that includes information on all of those contributors

"""

import json
import os
import requests

# setup access_token, and headers

access_token = os.getenv('GITHUB_TOKEN', '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')
headers = {'Authorization': "Token " + access_token}


def TopContributorsInfo(input_filename, output_filename):
    """
    Finds information of the top contributors in top starred repos
    :param input_filename: (str) name of csv file
    :param output_filename: (str) name of desired output file
    """

    # Opens csv file to read, and new file to write the info of contributors
    file_in = open(input_filename, 'r')
    file_out = open(output_filename, 'w')

    # Writes header to new file, and skips header from the input
    file_out.write('repo_name,username,name,number of contributions,company,location,bio\n')

    # Skips the header
    next(file_in)

    # Creates new list, strips the csv file and appends to list
    aList = []
    for line in file_in:
        each_line = line.strip("\n").split(',', 6)
        aList.append(each_line)

    # Looks through the API of every user
    for element in aList:
        users_url = f'https://api.github.com/users/{element[1]}'
        users = requests.get(users_url, headers=headers)
        users_file = users.json()
        # checks if bio has '"', "\r", or "\n" in it to avoid confusions in the csv file
        bio = str(users_file["bio"])
        bio = bio.replace('\n', "").replace("\r", "").replace('"', "'")
        # Writes the information obtained from the API to new file
        file_out.write(
            f'{element[0]},{element[1]},{users_file["name"]},"{element[2]}","{users_file["company"]}","{users_file["location"]}","{bio}"\n')

    # Closes all files
    file_in.close()
    file_out.close()


def main():
    """
    Takes the sorted csv file that was created before, and finds information every user on the list
    """
    TopContributorsInfo("sorted_top_contributors.csv", 'top_contributor_info.csv')


if __name__ == "__main__":
    main()
