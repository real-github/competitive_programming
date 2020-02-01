#!/usr/bin/python
import sys
import os
import getopt
import shutil
import time

dir_list = []

def GenerateProblem(cnt):
  for i in range(0, cnt):
    string = str(chr(i+97))
    os.mkdir(string)
    os.chdir(string)
    shutil.copy("../../../Library/template.cpp", "main.cpp")
    os.system("open main.cpp")
    os.chdir('../')
  return 0

def Reopen():
  global dir_list
  for dirName in dir_list:
    os.chdir(dirName)
    os.system("open main.cpp")
    os.chdir("../")
    time.sleep(0.7)
  

def main():
  directory_name = None
  number_of_files = None
  argv = sys.argv[1:]
  try:
    (opts, args) = getopt.getopt(argv, "c:n:", ["contest=", "number="])
  except getopt.GetoptError as err:
    print(err)
    opts = []

  for (opt, arg) in opts:
    if opt in ['-c', '--contest']:
      directory_name = arg
    elif opt in ['-n', '--number']:
      number_of_files = int(arg)

  if (os.path.isdir(directory_name) == False):
    os.mkdir(directory_name)
  else:
    sys.exit('\n[>>] ' + "Invalid Directory Name")
  
  os.chdir(directory_name)
  GenerateProblem(number_of_files)
  # opening file
  print('\n[>] directory name: {}'.format(directory_name))
  time.sleep(17) #for activation purpose
  global dir_list
  dir_list = os.listdir()
  dir_list.sort()
  Reopen()
  Reopen()
  print('[>] number of files: {} == '.format(number_of_files), end="")
  print(dir_list)
  os.chdir("../")
  sys.exit('\n[>>] ' + "Successfully Generated")
  
if __name__ == '__main__':
  main()
