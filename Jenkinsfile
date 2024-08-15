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
        stage('Create New Image') {
            when{
                branch "new-fix"
            }
            steps {
                sh 'docker build -t pavelgend/cars_image:03 .'
                echo "New image was created"
                }
        }
        stage('Remove Running Containers') {
            when{
                branch "new-fix"
            }
            steps {
                script {
                    psOutput = sh(script: 'docker ps -a')
                    if (psOutput.toString().contains("CONTAINER ID") && psOutput.toString().contains("\n")) {
                        echo 'after if'
                        sh 'docker ps -a -q | xargs docker stop'
                        sh 'docker ps -a -q | xargs docker rm'
                    } else {
                        echo 'after else'
                        echo "No running containers found"
                    }
                }
            }
        }
        stage('Test new Image and push') {
            when{
                branch "new-fix"
            }
            steps{
                sh 'docker run -d --name cars_container_test pavelgend/cars_image:03'
                sh 'docker start cars_container_test'
                sh 'docker exec cars_container_test python3 test_cars_db.py'
                sh 'if [ $? -ne 0 ]; then echo "Tests failed" && exit 1; else docker push pavelgend/cars_image:03 && echo "Tests passed and New image was pushed"; fi'
            }
        }
        stage('Remove New Container') {
            when{
                branch "new-fix"
            }
            steps {
                sh 'docker stop cars_container_test'
                sh 'docker rm cars_container_test'
                }
        }
    }
}
