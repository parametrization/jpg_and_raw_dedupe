import argparse
import os

# open file

def delete_files(candidates, location):
     for file_name in candidates:
          resolved_path = os.path.join(location, file_name)
          print("File to remove {0}".format(resolved_path))
          os.remove(resolved_path)
          if not os.path.isfile(resolved_path):
               print("{0} removed.".format(resolved_path))
          else: 
               print("{0} was not able to be removed.".format(resolved_path))


def log_and_count(description, file_list):
     count = 0
     print(description)
     for file in file_list:
          print("\t{0}".format(file))
          count += 1
     print("\t\tTOTAL ENUMERATED: {0}".format(count))

print(r"Example:  python script.py -c E:\DCIM\100MSDCF -p G:\DCIM\100MSDCF")
parser = argparse.ArgumentParser(description="Compare control_directory to prune_directory, removes any *.ARW files that are not found in the original list of jpgs.")
parser.add_argument('-c', '--control_directory')
parser.add_argument('-p', '--prune_directory')

args = parser.parse_args()

print(args.control_directory, args.prune_directory)
files = os.listdir(args.control_directory)
keep_files = []
for file in files:
        if file.upper().endswith('.JPG'):
            keep_files.append(file.upper().rstrip('.JPG') + '.ARW')

print (keep_files)

deletion_candidates = os.listdir(args.prune_directory)
not_found = []
found_will_keep = []

for file in deletion_candidates:
     if file not in keep_files:
          print("delete {0}".format(file))
          not_found.append(file)
     else:
          found_will_keep.append(file)

print("looking for these files:")
delete_file_count = 0
delete_candidates_count = 0
not_found_count = 0

for file in keep_files:
     print("\t" + file)
     delete_file_count+=1
print("\t\tTOTAL SEARCHED FOR: {0}".format(delete_file_count))

log_and_count("found these files to filter for purging: ", deletion_candidates)
print("NEW CODE")
log_and_count("these files had no jpg equivalent, they will be deleted on confirmation: ", not_found)
print("NEW CODE")
print("OLD CODE")
print("these files had no jpg equivalent, they will be deleted on confirmation: ")
for file in not_found:
     print("\t{0}".format(file))
     not_found_count+=1
print("\t\tTOTAL NOT FOUND: {0}".format(not_found_count))
print("OLD_CODE")

print("SANITY CHECK.\n\tCalculated\n\t\t (delete candidates + not found = files to search for deletion):")
print("C: {0}\t|A: {1}".format(delete_file_count + not_found_count, delete_candidates_count))

choice = input("Do you wish to delete the files?  [Y|N]\n")

if choice is "Y":
     #  delete stuff
     delete_files(not_found, args.prune_directory)
elif choice is "N":
     #  not deleting
     print("Exiting")
     exit(0)
else:
     # invalid input.  system will exit.
     print("Bullshit input.  Terminating because you aren't serious or paying enough attention")
     print("to do something descructive.")
     exit(-1)


