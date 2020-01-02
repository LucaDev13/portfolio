 This is a Flask app that works as a Portfolio. It is implemented with Docker.
 
 - Run tests:
    sh run_tests.sh
    
 - Run application locally:  
    sh start_app.sh
    
 - Build docker:
    sh build_docker.sh
 
 - Run the application on http://0.0.0.0:5000:
    docker run --name cv -p 5000:5000 -d <imageid>