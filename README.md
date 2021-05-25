# Table of contents
* [General Overview](#general-overview)
* [Requirements](#requirements)
* [Setup](#setup)
    - [Virtual Environment](#virtual-environment)
    - [Docker](#docker)
<!-- * [Demo](#demo) -->

## General Overview
This program parses various job boards, present filtered postings, and tracked postings applied to. Currently, [Indeed](https://ca.indeed.com/?r=us) is the only available option. 

## Requirements
Project is created with:
* Python version: 3.8
	
## Setup
Clone the project into a desired location.
```console
cd ~\Repos
git clone https://github.com/grantwforsythe/jobs.git
cd jobs
```
### Virtual Environment
It is a best practice to run program files in a virtual environment as
it allows the program to run with it's own separate dependencies.

To initialize a virtual environment use the command:
```console
python -m venv .venv
```
To activate the environment:

Mac/Linux:
```console
source venv/bin/activate
```
Windows:
```console
.\venv\Scripts\activate
```
To verify that your virtual environment is activated, your command line
should look like the following.
```console
(.venv) ~\Repos\jobs >
```
Then, to install the required dependices, run the following command.
```console
pip install -r requirements.txt
```
To deactivate simply use the command:
```console
deactivate
```
### Docker
Alternatively, the project can be run using Docker.
```console
# Build and run the Dockerfile
docker-compose up -d --build
```
<!-- ## Demo
... -->
