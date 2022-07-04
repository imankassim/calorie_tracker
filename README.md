# calorie_tracker

This is a Calorie Tracker system you can use to calculate how many calories you have had in a day. This can be accessed here: http://35.242.139.215:5000/login

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Software needed:

An IDE (I used VS Code)

Linux BASH Terminal

Jenkins


### Installing (with Jenkins)

- Fork and then clone this GitHub repo onto your terminal/host
      - You can host this application anywhere, including with Google Cloud Provider, with GUnicorn, with Nginx or even locally within your IDE
- Install Jenkins onto your terminal/host and configure the Jenkins setup
- On your Forked version of the repo, configure your GitHub webhook to build in Jenkins when a change to the code is committed
- Configure your Jenkins Job with your repo details to access the application straight from GitHub:
     - In Build, enter the following code:
     ```
      #!/bin/bash
      sudo cp /home/jenkins/.jenkins/workspace/calorietracker/flaskapp.service /etc/systemd/system/flaskapp.service
      sudo systemctl daemon-reload
      sudo systemctl start flaskapp.service
     ```
     
### Installing (Only using IDE - linux terminal)

- Clone this GitHub repo onto your terminal/host
- Install the following onto your terminal/host:
     ```
      sudo apt update
      sudo apt install python3 python3-pip python3-venv
     ```
 - Set up your local virtual machine:
     ```
      python3 -m venv venv
      source venv/bin/activate
     ```
 - Install the required libraries:
     ```
      pip3 install -r requirements.txt
     ``` 
- Set up the test data in the database:
     ```
      python3 create.py
     ``` 
- To run the application:
     ```
      python3 app.py
     ``` 


## Running the tests

- Clone this repository into your IDE
- Install the following onto your terminal/host:
     ```
      sudo apt update
      sudo apt install python3 python3-pip python3-venv
     ```
 - Set up your local virtual machine:
     ```
      python3 -m venv venv
      source venv/bin/activate
     ```
 - Install the required libraries:
     ```
      pip3 install -r requirements.txt
     ``` 
- To run the tests:
     ```
      python3 -m pytest --cov -report term_missing --cov= application tests
     ``` 

### Tests

Unit tests are used with form validators to ensure the right data is entering and leaving the app and database

## Built With

* [Flask](https://flask.palletsprojects.com/en/2.1.x/) - Web application framework


## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Iman Kassim** 

## License

This project is licensed under the MIT license - see the [LICENSE.md](LICENSE.md) file for details 

*For help in [Choosing a license](https://choosealicense.com/)*

