pipeline {
    agent any
    environment {
        PREV_IMAGE_TAG = "03"
        NEW_IMAGE_TAG = "05"
        IMAGE_REP = "pavelgend/cars_image"
    }
    stages {
        stage('Master') {
            when{
                branch "master"
            }
            steps {
                echo "Working on master branch"

            }
        }
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
                sh 'docker build -t $IMAGE_REP:$PREV_IMAGE_TAG .'
                sh 'docker run -d --name cars_container_test $IMAGE_REP:$PREV_IMAGE_TAG'
                sh 'docker start cars_container_test'
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
                sh 'docker build -t $IMAGE_REP:$NEW_IMAGE_TAG .'
                echo "New image was created"
                }
        }
        stage('Deploy') {
            when {
                branch "master"
            }
            steps {
                sh 'docker push $IMAGE_REP:$NEW_IMAGE_TAG'
                echo "New image $IMAGE_REP:$NEW_IMAGE_TAG was pushed"
            }
        }
    }
}
