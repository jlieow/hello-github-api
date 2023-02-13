### objective

To build a Hub and Spoke architecture in AWS referencing the North-South Inspection with AWS Network Firewall architecture listed here: https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/inspection-deployment-models-with-AWS-network-firewall-ra.pdf

![Alt text](../readme/hub.png)

The following tfvars files contain all the configuration settings which will be used when invoking terraform commands.

- - - -

### A sample tfvars file is included which needs to be renamed before they will be invoked using the following terraform commands.

backend.tfvars - contains settings used in backend.tf
config.tfvars - contains settings used when applying and destorying configurations

#### init with only the backend.tfvars file

terraform init -backend-config=backend.tfvars

#### use multiple tfvars files

#### For Mac
terraform apply -var-file=<(cat backend.tfvars <(echo) config.tfvars <(echo) spoke.tfvars)

terraform destroy -var-file=<(cat backend.tfvars <(echo) config.tfvars <(echo) spoke.tfvars)

### For Windows
Unfortunately the process substitution command above will not work and result in an error such as: 
- Error: Failed to read variables file. Given variables file /proc/412/fd/63 does not exist.
- Error: Failed to load "/proc/422/fd/63" as a plan file. Error: CreateFile /proc/422/fd/63: The system cannot find the path specified.

To overcome this problem, we first combine the various tfvars file into one file called combine.tfvars using this command and call the terraform commands afterwards as usual:
(cat backend.tfvars <(echo) config.tfvars) > config/combine.tfvars
terraform apply -var-file=config/combine.tfvars
terraform destroy -var-file=config/combine.tfvars

- - - -

### You can create a server on the VM you want to test TCP connections with using the following:

#### Option 1: Flask Server

1. sudo yum install pip3
2. pip3 install Flask
3. Copy code from hello.py and create hello.py in the VM
4. python3 hello.py

#### Option 2: Apache Server

5. yum install httpd -y
6. systemctl enable httpd
7. mkdir /var/www/html/orders/
8. echo "<h1>This is Orders App</h1>" > /var/www/html/orders/index.html
9. systemctl start httpd

#### Option 3: Apache Server via User Data

Pass this as user data in the ec2_instance block:
user_data = <<EOF
  #!/bin/bash
  sudo yum install httpd -y
  sudo systemctl enable httpd
  sudo mkdir /var/www/html/orders/
  sudo echo "<h1>This is Orders App</h1>" > /var/www/html/orders/index.html
  sudo systemctl start httpd 
  EOF
