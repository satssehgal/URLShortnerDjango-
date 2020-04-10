# Custom Django URL Shortener App
Instructions on how to build project within one hour can be viewed at: https://www.youtube.com/watch?v=ctuSR6UHcuQ
<br/>Instruction on how to deploy: Coming Soon

## Building Your First Custom App in 1 Hour

This project is a great beginner friendly project. In this tutorial we walk through how to build a URL shortening service. You can check out the youtube tutorial above on a code walk through. We use django as the backend, html with bootstrap as the front end and ORM with SQLite3 for data management. All files relevant to build the application are included in this respository

## Deploy to a Cloud Server

### Set Up Server

You can use something like Linode or Digital Ocean to follow these instruction.

Step 1: Create a linode or droplet (I use the $5 tier for this project)

Step 2: Use terminal or any ssh client to login with root and run:<br/>
<b>ssh root@IP</b><br/><b>apt update && apt upgrade -y</b>

Step 3: Set hostname for server. I used test-server. You can use whatever you want.
<br/><b>hostnamectl set-hostname test-server</b>

Step 4: Connect host ip and hostname
<br/>run <b>nano /etc/hosts</b> and add your server ip, click tab and then your hostname (from step 3)

Step 5: Install some dependencies
<br/>run <b>sudo apt install python-pip virtualenv ufw</b>

Step 6: Set up some firewall rules and enable<br/>
<b>
sudo ufw default allow outgoing<br/>
sudo ufw default deny incoming<br/>
sudo ufw allow ssh<br/>
sudo ufw allow 8000<br/>
sudo ufw enable<br/>
sudo ufw status (check to ensure its up and running)</b><br/>

Step 7: Create a limited user and give sudo privlidges<br/>

run <b> adduser USERNAME <---pick anything here. Enter password and skip through the rest of the questions.</b><br/>
then run <b> adduser USERNAME sudo</b>

Step 8: Setup ssh keys on your local computer<br/>
run <b>ssh-keygen -b 4096</b><br/> leave defaults<br/>
run <b>ssh-copy-id username@IP</b> to push them to your server<br/>
optional: If you have multiple ssh key pairs then run <b>ssh-add ~/.ssh/{name of ssh key}</b>

Step 9:Remove root login and password auth<br/>
run <b>sudo nano /etc/ssh/sshd_config</b><br/>
Set permit root login to no and uncomment passwordauthentication and set it to no<br/>

Step 10: Reboot the server<br/>
run <b>sudo reboot</b>

### Deploy Django Project to Server

Step 11: Change to your virtualenv<br/>
run <b>virtualenv vevn -p python3</b><br/>
run <b>source venv/bin/activate</b><br/>
You should now see something like (venv) on your terminal line

Step 12: Transfer Django project from local computer to server<br/>
run <b>scp -r {local path to project folder}  username@IP:~/</b>

Step 13: Update settings.py. Navigate to settings.py in your project folder <br/>
Update Allowed_Hosts =['Add Your IP or Domain Name']<br/>
Add static root with the following command <b>STATIC_ROOT = os.path.join(BASE_DIR, ‘static')</b> to the settings file<br/>
Save and exit

Step 14: Back out to the directory that has manage.py<br/>
Run <b>python manage.py collectstatic</b>

Step 15: Install Gunicorn and Nginx<br/>
run <b> pip install gunicorn</b><br/>
run <b> sudo apt install nginx libpq-dev</b>

Step 16: Check to see if gunicorn can host your django project. Change URLShortnerProject to whatever your project is called<br/>
run <b>gunicorn --bind 0.0.0.0:8000 URLShortnerProject.wsgi</b>
