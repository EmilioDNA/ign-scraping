# IGN Scraping
A basic project that gets data from the IGN website.

# Description

This is a basic App that uses Scrapy and Python to get data from three different entities from the IGN website: Articles, Reviews and Videos.
These entities are separated as categories within the website, so Scrapy tries to go to each section and get the corresponding data from each item.

For this project, I only cover the basic functionality of Scrapy in order to perform both horizontal and vertical web scraping.

The results got from this operation are saved in a .json file.

## Getting Started

### Installing Dependencies

#### Python 3.7 

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Pip Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/ign-scraping` directory and running:

```bash
pip install -r requirements.txt
```
I included all the needed dependencies for this project in the `requirements.txt` file.

##### Key Dependencies

- [Scrapy](https://scrapy.org/)  is an open source and collaborative framework for extracting data from websites.


## Running the script

From within the `ign-scraping` directory
ensure you are working using your created virtual environment.

To run the script, execute:

```bash
scrapy runspider ign-scraping.py -o ml.json -t json
```

Specifying the  `-o` command will establish the name outcome file, you are welcome to name it as you prefer. 

Specifing the  `-t` command will establish the type outcome file. 

