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
                sh 'docker build -t pavelgend/cars_image:04 .'
                echo "New image was created"
                }
        }
        stage('Remove all previous container') {
            when{
                branch "new-fix"
            }
            steps {
                sh 'docker ps -a'
                sh 'if [ $? -eq 0 ]; then docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && echo "all containers were stoped and removed";fi'
                }
        }
        stage('Test new Image and push') {
            when{
                branch "new-fix"
            }
            steps{
                sh 'docker run -d --name cars_image_test pavelgend/cars_image:04'
                sh 'docker start cars_image_test'
                sh 'docker exec cars_image_test python3 test_cars_db.py'
                sh 'if [ $? -ne 0 ]; then echo "Tests failed" && exit 1; else echo "Tests passed"; fi' /*  if output status is not equal to 0 so exit  */
                /* sh 'if [ $? -ne 0 ]; then echo "Tests failed" && exit 1; else docker push pavelgend/cars_image:04 && echo "Tests passed and New image was pushed"; fi' */
                sh 'docker stop cars_image_test'
                sh 'docker rm cars_image_test'
            }
        }
    }
}
