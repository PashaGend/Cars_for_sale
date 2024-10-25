pipeline {
    agent any
    environment {
        NEW_VERSION_TAG = "06"
        IMAGE_REP = "pavelgend/cars_image"
        CURL_IMAGE_REP = "pavelgend/alpine_curl:02"
    }
    stages {
        // Clean up
        stage('Pre-Build') {
            when{
                branch "new-feature"
            }
            steps {
                script {
                    psOutput = sh(script: 'docker ps -a',returnStdout: true)
                    echo psOutput
                    if (psOutput.split("\n").length > 1) {
                        echo "starting remove container.................."
                        sh 'docker ps -a -q | xargs docker stop'
                        sh 'docker ps -a -q | xargs docker rm'
                    } else {
                        echo "No running containers were found"
                    }
                }
            }
        }
        stage('Test') {
            when{
                branch "new-feature"
            }
            steps{
                //Run container testing image with latest application version
                sh 'docker build -t $IMAGE_REP:test_image .'
                sh 'docker run -d --name cars_container_test -p 5000:80 $IMAGE_REP:test_image'
                sh 'docker start cars_container_test'
                //Run curl container
                sh 'docker run -t -d --name curl_container --network host $CURL_IMAGE_REP /bin/sh'
                sh 'docker start curl_container'
                //Test connection application via curl_container
                sh 'docker exec curl_container curl http://127.0.0.1:5000/cars'
                sh 'if [ $? -ne 0 ]; then echo "Connection test failed" && exit 1; else echo "Connection test was passed"; fi'
                //Run Unitest on application
                sh 'docker exec cars_container_test python3 test_cars_db.py'
                sh 'if [ $? -ne 0 ]; then echo "Tests failed" && exit 1; else echo "Application tests were passed"; fi'
                sh 'docker stop cars_container_test'
                sh 'docker rm cars_container_test'
            }
        }
        stage('Build') {
            when{
                branch "new-feature"
            }
            steps {
                sh 'docker build -t $IMAGE_REP:$NEW_VERSION_TAG .'
                echo "New image was created"
            }
        }
        stage('Push') {
            when{
                branch "new-feature"
            }
            steps {
                sh 'docker push $IMAGE_REP:$NEW_VERSION_TAG'
                echo "New image $IMAGE_REP:$NEW_VERSION_TAG was pushed"
            }
        }
        stage('Deploy') {
            when {
                branch "new-feature"
            }
            steps {
                //stop previous application depoyment
                //sh 'docker stop cars_container_deployment'
                //sh 'docker rm cars_container_deployment'
                //Deploy new application
                //sh 'docker run -d --name cars_container_deployment -p 5000:80 $IMAGE_REP:$NEW_VERSION_TAG'
                sh 'docker run -d --name cars_container_deployment --network host $IMAGE_REP:$NEW_VERSION_TAG'
                sh 'docker start cars_container_deployment'           
            }
        }
        stage('Monitoring') {
            when{
                branch "new-feature"
            }
            steps {
                sh 'docker run -d --name prometheus --network host -v /home/osboxes/Documents/prometheus_material/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus'
                echo "Prometheus server is running"
                sh 'docker run -d --name node_exporter --net="host" --pid="host" -v "/:/host:ro,rslave" quay.io/prometheus/node-exporter:latest --path.rootfs=/host'
                echo "Node exporter is running"
            }
        }
    }
}
