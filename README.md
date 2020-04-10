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
run <b>sudo apt install python-pip virtualenv </b>

