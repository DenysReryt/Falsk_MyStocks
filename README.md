# My Stocks
"My Stocks" is a web-application that allows users to access and record the information about stocks. With is you 
can buy and sell stocks of companies.

## Installation
To install and run "My Stocks", you need to have python and git installed on your machine. You 
can download them from their official websites.

After installing Python and Git, you need to clone the repository and navigate to the project directory in your 
terminal. 
```commandline
git clone https://github.com/DenysReryt/Flask_MyStocks
cd <repository_name>
```
Then, run the following command to install the required dependencies:
```commandline
pip install -r requirements.txt
```

## Starting the Web Application
To start the web application, navigate to the project directory in your terminal and run the following command:
```commandline
flask --app wsgi:app run
```
or, you can use gunicorn to run app:
```commandline
gunicorn -w 4 wsgi:app -b localhost:5000 --log-level debug --reload
```
where:
+ ```-w 4``` is option that sets the number of worker processes to 4;
+ ```wsgi:app``` is the name of the Python module containing the Flask application object ('app');
+ ```-b localhost:5000``` is option that binds the server to the localhost (127.0.0.1) IP address and port 5000;
+ ```--log-level debug``` is option that sets the logging level to 'debug' (log detailed information about requests 
  and responses.);
+ ```--reload``` is option that enables automatic reloading of the server when the source code changes.
This will start the web application on port 5000. You can access the web application by visiting http://localhost:5000 
  in your web browser.
