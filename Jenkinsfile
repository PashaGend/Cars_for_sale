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
                sh 'docker build -t pavelgend/cars_image:05 .'
                echo "New image was created"
                }
        }
        /*
        stage('Check if container ris running and Remove') {
            when{
                branch "new-fix"
            }
            steps {
                script {
                sh 'docker ps -a|grep cars_container_test'
                sh 'if [ $? -eq 0 ]; then docker stop cars_container_test && docker rm cars_container_test && echo "all containers were stoped and removed";fi'
                }
                }
        } */
        stage('Test new Image and push') {
            when{
                branch "new-fix"
            }
            steps{
                sh 'docker run -d --name cars_container_test pavelgend/cars_image:05'
                sh 'docker start cars_container_test'
                sh 'docker exec cars_container_test python3 test_cars_db.py'
                sh 'if [ $? -ne 0 ]; then echo "Tests failed" && exit 1; else docker push pavelgend/cars_image:05 && echo "Tests passed and New image was pushed"; fi' /*  if output status is not equal to 0 so exit  */
                /* sh 'if [ $? -ne 0 ]; then echo "Tests failed" && exit 1; else docker push pavelgend/cars_image:04 && echo "Tests passed and New image was pushed"; fi' */
            }
        }
        stage('Remove Container') {
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
