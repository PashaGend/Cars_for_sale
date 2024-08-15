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
                sh 'docker build -t pavelgend/cars_image:06 .'
                echo "New image was created"
                }
        }
        stage('Test new Image and push') {
            when{
                branch "new-fix"
            }
            steps{
                script {
                    docker run -d --name cars_container_test pavelgend/cars_image:06
                    docker start cars_container_test
                    docker exec cars_container_test python3 test_cars_db.py
                    if [ $? -ne 0 ]; then docker stop cars_container_test && docker rm cars_container_test && echo "Tests failed end container was removed" && exit 1; else docker push pavelgend/cars_image:06 && echo "Tests passed and New image was pushed"; fi
                }
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
