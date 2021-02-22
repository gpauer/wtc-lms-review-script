import subprocess
import re


def scrape_projects(keyword, number):
    topic_commands = re.compile("(wtc-lms.*)").findall(subprocess.getoutput("wtc-lms modules"))
    problem_commands = []
    problems = []
    for x in topic_commands:
        problem_commands += re.compile("(wtc-lms.*)").findall(subprocess.getoutput(x))
    for x in problem_commands:
        problems += re.compile("([A-Za-z\\- ]*"
        + keyword.lower() + "[A-Za-z\\- ]*"
        + number + "[A-Za-z0-9\\- ]*) \\[.*\\] \\(([a-z0-9\\-]+)\\)").findall(subprocess.getoutput(x).lower())
    return(problems)


def scrape_reviews(keyword, number, status):
    if not number.isdigit(): number = ""
    string = subprocess.getoutput("wtc-lms reviews").lower()
    details = re.compile("> ([a-z0-9\\- ]*"
    + keyword.lower()
    + "[a-z0-9\\- ]*"
    + number
    + "[a-z0-9\\- ]*) \\(([a-z\\-0-9]+)\\) \\[[a-zA-Z]*"
    + status.lower()
    + "[a-zA-Z]*\\]").findall(string)
    return(details)