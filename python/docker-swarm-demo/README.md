Build the docker image by using the below command
    docker-compose up -d

Increase the slave instance
    docker-compose scale slave=10

Decrease the slave instance
    docker-compose scale slave=2

To bring down all the services
    docker-compose down