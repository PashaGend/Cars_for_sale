pipeline {
    agent any
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
                        echo "starting remove container................"
                        sh 'docker ps -a -q | xargs docker stop'
                        sh 'docker ps -a -q | xargs docker rm'
                    } else {
                        echo "No running containers were found"
                    }
                }
            }
        }
        stage('Build') {
            when{
                branch "new-feature"
            }
            steps {
                sh 'docker build -t pavelgend/cars_image:03 .'
                echo "New image was created"
                }
        }
        stage('Test') {
            when{
                branch "new-feature"
            }
            steps{
                sh 'docker run -d --name cars_container_test pavelgend/cars_image:03'
                sh 'docker start cars_container_test'
                sh 'docker exec cars_container_test python3 test_cars_db.py'
                sh 'if [ $? -ne 0 ]; then echo "Tests failed" && exit 1; else echo "Application tests were passed"; fi'
                sh 'docker stop cars_container_test'
                sh 'docker rm cars_container_test'
            }
        }
        stage('Deploy') {
            when {
                branch "new-feature" && changeBranch == "master"
            }
            steps {
                sh 'docker push pavelgend/cars_image:03'
                echo "New image was pushed"
            }
        }
    }
}
