# PRD-GithubAPI
This repository can be used to find many information on the top repos on GitHub, the top contributors in those repos, and information on those contributors by only using GitHub APIs.

Information on how to use the python files and (created) csv files will all be written below, as there are steps to do to fully use this project.

There are 5 python files in this repository: repo_info.py, top100listing.py, sort_top_contributors.py, topContributorsInfo.py, and topReposData.py

repo_info.py only takes the url of any GitHub repository and prints certain information about it, so this file can be run anytime without affecting the others.

The other 4 files have a certain order in which they need to be run, because the files use csv files that are created from the other python files before.

Here is how they work:

## STEP 1: 
The first step is running top100listing.py. This file will create 3 csv files called data.csv, top100.csv, and top100(language).csv. data.csv will include information on thousands of repositories that are the top 100 starred, top 100 forked, and top 100 for every language. top100.csv will include information on only the top 100 starred repos. The name can change if a different number is given (i.e if the number is 50, the name of the file will be top50.csv). Finally, top100(language).csv will include information on the top 100 repos of any given language. The name can change here as well if a different number is given (i.e if the number is 50 and the language is 'Python', the name of the file will be top50Python.csv). The base number for both is 100, but can vary depending on user. The three csv files created here will be used after in the other python files.

## STEP 2: 
The second step is running sort_top_contributors.py. This file creates 2 csv files called top_contributors.csv and sorted_top_contributors.csv. The first csv file will include all the contributors and their number of contributions in every project from the list of top100 or top100Python (or whatever is created) from before. The second csv file will sort these contributors in the top repos by their number of contributions to find who has contributed most to the top projects in the world. Any number can be given to take that number of contributors in the sorted file (i.e if the number is 200, there will be 200 sorted contributors in the file). The base number for this is also 100, but can change if wanted. The sorted csv file created here will be used in the next step to retrieve their information.

## STEP 3: 
The third step is to run topContributorsInfo.py. This file takes the sorted contributor csv file from the second step, and creates a new csv file called top_contributors_info.csv which will include all information such as location, company, bio, and other information of the users in the sorted list. The information here will be used after to get specific information that we want.

## STEP 4: 
The fourth and final step is to run topReposData.py after the first three were run in order. This file will just print 4 different data that we want. 
The first will print the number of languages that are used in the projects of the top 100 starred repos.
The second will take any given keywords (i.e machine learning) and will look through the thousands of projects in data.csv (the csv file from step 1) to see how many of them use machine learning, and print the number of languages of the projects that have machine learning in their description.
The third will take any location (i.e San Francisco) and will print the number and the usernames of the people in the top_contributors_info.csv file who live in the given location.
The fourth will take any company (i.e Microsoft) and will print the number and the usernames of the people in the top_contributors_info.csv file who work in the given company.

Every file itself has a detailed docstring in it that explains how they work as well, but this is a step-by-step overview of how to use my code to retrieve many information about top GitHub repositories. Feel free to reach out if you have any questions or confusions.
