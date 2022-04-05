sudo docker stop  python-microservice-example_1
sudo docker rm python-microservice-example_1
sudo docker rmi python-microservice-example:latest
docker build . -t python-microservice-example
docker run --name python-microservice-example_1 -d -p 5000:5000 python-microservice-example
#docker run --name python-bob_4 -d -p 5000:5000 bob:1.1.4
#docker run -p 5000:5000