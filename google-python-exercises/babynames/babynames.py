# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:44:32 2018

@author: cr481e
"""

import sys
import re
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  full_path = os.path.join("/Users/lydiaboyd/Downloads/",filename)
  with open(full_path) as myfile:
      filecontents = myfile.read()
      
  yearlist = re.search(r"Popularity in (\d{4})", filecontents)
  year = yearlist.groups()[0]
  
  with open(full_path) as myfile:
      lines = myfile.readlines()
  ranklist = []
  for line in lines:
      if re.findall(r'"right"><td>(\d+)',line) != []:
          ranklist += re.findall(r'"right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)',line)
  list_of_lists = [list(elem) for elem in ranklist]
  
  newranklist = []
  for listy in list_of_lists:
      listy.insert(0,str(year))
      newranklist.append(listy)
  print(newranklist)
 
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
    args = sys.argv[1:]


    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    #extract_names("baby1990.txt")

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  #main()
  extract_names("baby1990.txt")