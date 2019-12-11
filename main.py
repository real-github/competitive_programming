import os
import shutil

def file_generate_each(cnt):
  for i in range(0, cnt):
    string = str(chr(i+97))
    os.mkdir(string)
  return 0

def cpp_generate_each(cnt, dir_name):
  for i in range(0, cnt):
    os.chdir(str(chr(i+97)))
    # shutil.copy("../../../Library/template.cpp", str(dir_name) + "_" + str(chr(i+97)) + ".cpp")
    # ↑ this generates a file like "abc149_a.cpp"
    shutil.copy("../../../Library/template.cpp", "main.cpp")
    os.chdir('..')
  return 0

def cpp_generate_dump(cnt, dir_name):
  for i in range(0, cnt):
    shutil.copy("../../Library/template.cpp", str(dir_name) + "_" + str(chr(i+97)) + ".cpp")
  return 0

def main():
  dir_name = input("directory name: ")
  cnt = input("Enter the number of files to create(e.g. 4, 5) OR a specific task name(e.g. A, B, Coins): ")
  if (cnt.isdecimal()):
    count = int(cnt)
  

  if (cnt.isdecimal()):
    os.mkdir(dir_name)
    os.chdir(dir_name)
    gen_type = str(input("way of generating the directory[each,e/dump,d]: "))
    if (gen_type == "each" or gen_type == "e"):
      file_generate_each(count)
      cpp_generate_each(count, dir_name)
    elif (gen_type == "dump" or gen_type == "d"):
      cpp_generate_dump(count, dir_name)
  else:
    os.mkdir(str(dir_name) + "_" + cnt)
    os.chdir(str(dir_name) + "_" + cnt)
    shutil.copy("../../Library/template.cpp", "main.cpp")
  return 0

main()
