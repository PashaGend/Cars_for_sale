pipeline {
    agent any
    stages {
        stage('Master') {
            when{
                branch "master"
            }
            steps {
                echo "Deploy"
            }
        }
        stage('Pre-Build') {
            when{
                branch "new-fix"
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
                        echo "No running containers found"
                    }
                }
            }
        }
        stage('Build') {
            when{
                branch "new-fix"
            }
            steps {
                sh 'docker build -t pavelgend/cars_image:03 .'
                echo "New image was created"
                }
        }
        stage('Test') {
            when{
                branch "new-fix"
            }
            steps{
                sh 'docker run -d --name cars_container_test pavelgend/cars_image:03'
                sh 'docker start cars_container_test'
                sh 'docker exec cars_container_test python3 test_cars_db.py'
                sh 'if [ $? -ne 0 ]; then echo "Tests failed" && exit 1; else docker push pavelgend/cars_image:03 && echo "Tests passed and New image was pushed"; fi'
                sh 'docker stop cars_container_test'
                sh 'docker rm cars_container_test'
            }
        }
        stage('Deploy') {
            when {
                branch "new-fix"
            }
            steps {
                sh 'docker push pavelgend/cars_image:03'
                echo "New image was pushed"
            }
        }
    }
}
