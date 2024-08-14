pipeline {
    agent any
    stages {
        stage('Run Tests') {
            when{
                branch "new-fix"
            }
            steps {
                sh 'python3 test_cars_db.py'
            }
        }
        stage('Create New Image') {
            when{
                branch "new-fix"
            }
            steps {
                script {
                    if (currentBuild.result == 'SUCCESS') {
                        sh 'docker build -t pavelgend/cars_image:02 .'
                        sh 'docker push pavelgend/cars_image:02'
                        echo "New image was created"
                    }
                }
            }
        }
        stage('Test new Image') {
            when{
                branch "new-fix"
            }
            steps{
                sh 'docker pull pavelgend/cars_image:02'
                sh 'docker run -d --name cars_image_test pavelgend/cars_image:02'
                sh 'docker exec cars_image_test python test.py'
                sh 'if [ $? -ne 0 ]; then exit 1; fi' /* if output status is not equal to 0 so exit */
                sh 'docker stop cars_image_test'
                sh 'docker rm cars_image_test'
                echo "New image tests passed successfully"
            }
        }
    }
}
