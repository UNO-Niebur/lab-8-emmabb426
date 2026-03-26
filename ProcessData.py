#ProcessData.py
#Name: Emma Barnes
#Date: 03/26/2026
#Assignment: Lab 08 - Process Data

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]
    student_id = make_id(first, last, idNum)
    output = last + "," + first + "," + student_id + "," + maj(major) +"-"+(abbrev_yr(year)) +"\n"
    #print(output)
    outFile.write(output)



  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def make_id(first, last, idNum):
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen -3: ]
  #print(id)
  return id

def abbrev_yr(year):
  year = year.lower()
  if year == "freshman":
    abbrev_yr = "FR"
  elif year == "sophomore":
    abbrev_yr = "SO"
  elif year == "junior":
    abbrev_yr = "JR"
  elif year == "senior":
    abbrev_yr = "SR"
  else:
    abbrev_yr = "N/A"

  return abbrev_yr

def maj(major):
  major = major.upper()
  maj = major[0:3]
  
  return maj

if __name__ == '__main__':
  main()
