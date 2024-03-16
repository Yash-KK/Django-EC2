# Deploying a Django Application on AWS EC2
<h3>Set up an AWS EC2 instance </h3>
1. Create an IAM user & login to your AWS Console
   <ul>
    <li>Access Type - Password</li>
    <li>Permissions - Admin</li>
   </ul>
2. Create an EC2 instance
<ul>
  <li>Select an OS image - Ubuntu</li>
  <li>Create a new key pair & download .pem file</li>
</ul>

3. Connecting to the instance using ssh
```bash
ssh -i instance.pem ubunutu@<IP_ADDRESS>
```

# Configuring Ubuntu on remote VM
1. Updating the outdated packages
```bash
sudo apt update
```

# Deploying the project on AWS
1. Clone the project
```bash
  git clone https://github.com/Yash-KK/Django-EC2.git
  cd Django-EC2
```

2. Create a virtual enviornment
```bash
  virtualenv venv
  source venv/bin/activate
```

3. Setup the following enviornment variables
```bash  
  SECRET_KEY=""
```
4. Start the project
```bash  
  python manage.py runserver 0.0.0.0:8000
```
NOTE - We will have to edit the inbound rules in the security group of our EC2, in order to allow traffic from our particular port
