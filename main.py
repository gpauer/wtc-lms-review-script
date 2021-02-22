from reviewer import review_accept
from scraper import scrape_reviews, scrape_projects
from sys import argv
import os


if __name__ == "__main__":

    logged = input("Are you logged in to wtc-lms (y/N)?")
    if logged != "y": os.system("wtc-lms login")

    if len(argv) > 1 and argv[1] == "-p":
        keyword = input("\nEnter keyword for project you want to see (leave blank for all):")
        if keyword != "":
            iteration = input("\nWhich iteration would you like to review? (leave blank for all) ")
        else:
            iteration = ""
        print("\nProjects:")
        for x in scrape_projects(keyword, iteration):
            print(x[0].capitalize(),"\nUUID:",x[1]+"\n")
    else:
        name = input("What would you like to review? (Do not specify the iteration) ")
        iteration = input("Which iteration would you like to review? (leave blank for more review matches) ")
        try:
            n = int(input("How many reviews would you like to accept? "))
        except:
            print("Invalid number.")
        review_accept(scrape_reviews(name, iteration, "invited"), n)