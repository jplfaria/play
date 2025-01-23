# User Guide: Accessing Sequoia Jupyterhub on

## Step-by-Step Guide

### 1. Set up your ANL CELS account if you don’t already have one:

a) Go to: [CELS Account Management](https://accounts.cels.anl.gov/)

b) Request an account if you don’t have one

c) Here’s what it looks like once you’ve logged in:
![cels_account](CELS_account.png)

d) Once you have an account, log in on the above site and if “HenryLab” is not already listed as a project under your account, use the “Join project” link to join HenryLab

e) Click on “account information” and upload and SSH key. You generate the key on your computer and upload the public key using this interface.
   
### 2. SSH Tunel to the ANL Machine

need help here

### 3. Create an Account on Sequoia Jupyter Hub

Contact Filipe either on Slack or via email fliu@anl.gov with your desired username for him to create an account. He will provide you with a temporary password you can change after you login. This username will also be the one used to connect to the DB instances Filipe created.

In addition to the ```cdm``` database available for everyone, when you contact Filipe you can ask him to crerate a sandbox database for you to play. In that case, your username will be the name for that sandbox database, which you can only see and have permission to access.
   
### 4. Access Jupyter Notebook:
   
Open a web browser and navigate to the following URL:

```
http://sequoia.mcs.anl.gov:8001
```
Assuming all is properly set up you should see:
![jupyer_hub](jupyter_sign_up.png)

This will open the JupyterHub Notebook interface running on the remote server.

You will see many kernels are available we recommend you connect to the "Python3_ModelSEED" one since it has a bunch of libraries you might need already installed.


### 5. Connecting to the cdm database (and other instances like your sandbox):

You can use any database abstraction layer you prefer to connect, load tables, etc, in this example I will be using SQLAlchemy

```from sqlalchemy import create_engine```

```engine = create_engine("mysql+pymysql://jplfaria:henrylab@172.18.0.15/cdm?charset=utf8mb4")```

