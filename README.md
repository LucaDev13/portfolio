 This is a Python Flask app that works as a Portfolio which is implemented with Docker and deployed on AWS EC2.

-   Run tests:
     sh run_tests.sh

-   Run application locally:  
     sh start_app.sh

-   Build docker:
     sh build_docker.sh

-   Run the application with docker locally on <http://0.0.0.0:5000>:
     docker run --name cv -p 5000:5000 -d <imageid>

-   Deployment on AWS EC2:

1.  Launch AWS EC2 AMI
2.  Select or create key pairs and security group
3.  SSH into the newly created EC2 instance
4.  Install Docker on EC2 instance `sudo yum install -y docker`
5.  Start Docker `sudo service docker start`
6.  Run image `docker run -d -p 80:5000 lucadev15/portfolio:latest`

As the app should handle traffic in SSL:

1. Create an SSL certificate in AWS Certificate manager pointed to the Route53 DNS record
2. Create Load balancer with two availability zones listening on 443
3. Register the instance in the target group

- Deployment on Digital ocean:
1. Create a [Docker Droplet](https://marketplace.digitalocean.com/apps/docker)
2. SSH into the newly created droplet
3. docker pull lucadev15/portfolio:latest
4. docker run -d -p 80:5000 lucadev15/portfolio:latest

As the app should handle traffic in SSL:

1. Create Load Balancer and Let's Encrypt certificate
2. Set up forwarding rule HTTPS 443 > HTTP 80
