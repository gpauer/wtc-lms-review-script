import subprocess
import re
import threading
from threader import threads, run_threads


modules = []
topics = []
problems = []


def get_topics(command):
    global topics
    topics += re.compile("(wtc-lms.*)").findall(subprocess.getoutput(command))


def get_problems(command):
    global problems
    problems += re.compile("(.*)\\[.*\\] \\((.*)\\)").findall(subprocess.getoutput(command).lower())


def scrape_projects():
    global modules, topics, problems

    modules = re.compile("(wtc-lms.*)").findall(subprocess.getoutput("wtc-lms modules"))
    for i in range(0, len(modules), threads):
        run_threads(get_topics, modules[i : i + threads])
    for i in range(0, len(topics), threads):
        run_threads(get_problems, topics[i : i + threads])
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