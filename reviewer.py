from scraper import scrape_reviews
import subprocess
import os
import re


def review_outline(review_accept_output, UUID):
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
    i = 0
    while ((i < n) and (i < len(review_list))):
        review_outline(subprocess.getoutput("wtc-lms accept " + review_list[i][1]), review_list[i][1])
        print(review_list[i][0].capitalize(), "accepted for review. UUID:", review_list[i][1])
        i += 1