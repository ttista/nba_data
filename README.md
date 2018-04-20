##########################################
####   Interactive NBA Data Program   ####
####   Using Scores and Attendance    ####
##########################################
##########   Thomas Bautista    ##########
##########################################

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~Getting Started/Data Gathering~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

My source for NBA season statistical data is:
https://www.basketball-reference.com

From this links, I scrape from every month of this NBA season,
beginning in October all the way to April. Because I am scraping, no keys
are needed, but you must have installed Requests and BeautifulSoup4
on your computer. You also need to have SQLite3 installed on your computer.
The following are the commands that you enter into terminal to install.

You must then create a username and an api key for plotly. On the website,
https://plot.ly/python/getting-started/, you can create a free account and
get an api key. You will then need to create a file named secrets.py,
that will be formated as:

plotly_key = 'your key'
plotly_username = 'your username'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~Code Structure~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

The most important parts of my code are the data crawling, inserting, and
pulling from database functions.

My crawling function, get_nba_scores(), crawls different parts of basketball-reference.com, while also inserting this information in my database.
There are many different sections of the website that I crawl, including home
teams, away teams, their subsequent score, the date, and attendance.
I use lists to apply the specific variables needed for
each part of the crawl in one for loop, which greatly speeds up the speed of
the program. I initialize my database through init_db(),
which creates separate "Game" and "Attendance" tables within the database.
Functions process_times(), process_scores(), process_command(), and
process_rankings() use commands from the interactive_prompt() function
to specify what data to pull from my database, which is subsequently used
for my visualizations.


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~User Guide~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

To run the program, clone my git repository to a local repo. Then, navigate
to that repository in terminal and create the secrets.py file as
described before, then use the following command in your command line:

python3 final_proj_NBA.py

Once the program is running, for an in depth description
of the commands for visualizations, please use the 'help' command.

Quit the program using 'exit'
