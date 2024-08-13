pipeline {
	agent any
	stages {
	    stage ('build'){
            steps {
                when {
                    branch "new-fix"
                }
                echo 'brsnch new-fic'
            }
        }
        stage('deploy'){
            when{
                branch "main"
            }
            steps{
                echo "deploy"
            }
        }
 	}
}