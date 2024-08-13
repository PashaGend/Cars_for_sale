pipeline {
	agent any
	stages {
	    stage ('build'){
            steps {
                when {
                    branch "new-fix"
                }
                echo 'branch new-fix'
            }
        }
        stage('deploy'){
            when{
                branch "master"
            }
            steps{
                echo "deploy"
            }
        }
 	}
}