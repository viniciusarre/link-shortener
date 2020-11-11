# About this Repo   

This is a simple Proof of Concept for experimenting with Link Shorteners and their overall logic which is built using Flask and MongoDB.

The overall architecture is quite simple, it has a few static web pages which are directly served from Flask, and it is built keeping simplicity in mind so it can be integrated to other services easily. 

Feel free to set it up or fork it and set different flavors to it, if you'd like. 

# How to set it up (MacOS X and Linux)

There are different ways you can run this. Potentially the easiest one is by installing and running it using virtualenv. First, [make sure you have it installed](https://virtualenv.pypa.io/en/stable/installation.html).

You can then create a virtual environment folder (ideally, use the venv folder which is already in the `.gitignore` file)

Then, create a virtualenv by running the following:

`python3 -m virtualenv venv` 

Then activate it by running:

`source venv/bin/activate` 

Now, you should be ready to run the project by installing the dependencies in the venv:

`pip install -r requirements`

Then start the server by running:

`python server.py`

You can use the graphql playground in order to run mutations and queries by accessing the 
`/playground` endpoint.


# Setting up the DB

If you don't have a local installation of MongoDB running locally (at 27017), you can run it using Docker, by running the following command:

`$ docker run -it -p27017:27017 --name mongodb -d mongo`

