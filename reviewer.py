from scraper import scrape_reviews
import subprocess
import os
import re
from threader import threads, run_threads

def review_outline(UUID):
    review_accept_output = subprocess.getoutput("wtc-lms accept " + UUID)
    print("UUID:", UUID)
    directory = (re.compile("\\/.*").findall(review_accept_output))[0]
    f = open(directory+"/review.txt", "w")
    print("review.txt created in:", directory)
    f.write("UUID:\n")
    f.write(UUID+"\n\n")
    print("UUID added...")
    f.write("pycodestyle:\n")
    f.write(subprocess.getoutput(f"pycodestyle --exclude=*test*,*.txt,*.md,__init__.py --select=E1,E4,E5,E9,W1 {directory}/* >> {directory}/review.txt"))
    print(f"Pycodestyle added...")
    os.chdir(directory)
    f.write("\nUnittests:\n")
    f.write(subprocess.getoutput(f"python3 -m unittest tests/test_main.py"))
    print("Unittests added...")
    f.close()
    print("review.txt closed...")


def review_accept(review_list, n):
    review_list = review_list[0:n]
    for x in review_list: print(f"Name: {x[0]} UUID: {x[1]}")
    accept = input("Would you like to accept the following reviews (y/N)?")
    if accept.lower() != 'y': os.sys.exit()
    else:
        UUID_list = [x[1] for x in review_list]
        run_threads(review_outline, UUID_list)