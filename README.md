# GradDBHomework2

To run in docker, run the following command: 
```
docker-compose up --build
```

This should build and run the two containers required for this project. 

The first container is the flask python environment and the second is the Mysql Database

This compose file will expose the flask environment on the 5000 port. 

By default accessing:
```
http://localhost:5000/ 
```
will open the flask webpage
