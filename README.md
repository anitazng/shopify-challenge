# Shopify Backend Developer Intern Challenge - Summer 2022 

## Introduction
This web application was created as part of the Shopify Backend Developer Intern Challenge. It features an inventory tracking system equipped with basic CRUD functionality. Users also have the option of exporting product data as a CSV file.

## Setup Instructions
1. Ensure you have [Python 3](https://www.python.org/downloads/) downloaded. For Mac, also ensure that [Homebrew](https://brew.sh/) is downloaded 
2. Create a new directory and clone this repository into it either using GitHub Desktop or `git clone https://github.com/anitazng/shopify-challenge.git`
3. Open a terminal and run the command `pip install -r requirements.txt`. If you're on a Mac, run `brew install mysql` before doing this. This will install the dependencies required for the application to run. If you are met with the error `xcrun: error: invalid active developer path`, run `xcode-select --install` before trying the pip command again
4. Run `mysql.server start` to start the server
5. Run `python run.py` and head to [localhost:5000](localhost:5000) to view the application
