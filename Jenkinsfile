pipeline {
	agent any
	stages {
	    stage ('build'){
                when {
                    branch "new-fix"
                }
            steps{
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