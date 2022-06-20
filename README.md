# el

El is a B2B application, which allows users to create request upon what they need to done, and then managed by ELTechnologies it allows the designated solution designer to allo
### Setup

**Cloning the Backend Code**

To clone the code onto your local machine run the following command onto your terminal.

```git clone https://github.com/syedbilal28/el.git```

**Setting up Virtual Environment**

Create the virtual environment by navigating onto the code directory and run the following command 

```python3 -m venv venv```

Activate the virtual environment using 

```source venv/bin/activate```

Install the required packages using

```pip install -r requirements.txt```

**Setting up server***

In order to start the server you need to make database migrations which can be done by following

```python manage.py makemigrations```

and the migrate it

```python manage.py migrate```

A superuser needs to be created, which can be created by

```python manage.py createsuperuser```

Then enter the relevant information to setup a super user

**Start the Server**

To start the server, run the following command

```python manage.py runserver```

**Populating the database**

go to the [this url](http://127.0.0.1:8000/admin/) to input the relevant values into the db.

Upon login navigate to the text where **Cost models** is writter, click upon it and then you have to add all the cost models there.

***After adding the cost models your backend is setup and then the next step is to setup the frontend whose readme can be found at [this url](https://github.com/syedbilal28/Eltechnology)***


