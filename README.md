# Custom Django URL Shortener App
Instructions on how to build can be viewed at: https://www.youtube.com/watch?v=ctuSR6UHcuQ
Instruction on how to deploy: Coming Soon

## Deploy to a Cloud Server

You can use something like Linode or Digital Ocean to follow these instruction.

Step 1: Create a linode or droplet (I use the $5 tier for this project)

Step 2: Use terminal or any ssh client to login with root and run: 
<b>apt update && apt upgrade -y</b>

Step 3: Set hostname for server. I used test-server. You can use whatever you want.
<b>hostnamectl set-hostname test-server</b>

Step 4: Connect host ip and hostname
run <b>nano /etc/hosts</b> and add your server ip, click tab and then your hostname (from step 3)

Step 5: Install some dependencies
run <b>sudo apt install python-pip virtualenv ufw</b>

Step 6: Set up some firewall rules and enable

sudo ufw default allow outgoing
sudo ufw default deny incoming
sudo ufw allow ssh
sudo ufw allow 8000
sudo ufw enable
sudo ufw status (check to ensure its up and running)

Step 7: Create a limited user and give sudo privlidges

run <b> adduser USERNAME <---pick anything here. Enter password and skip through the rest of the questions.</b>

then run <b> adduser USERNAME sudo</b>


