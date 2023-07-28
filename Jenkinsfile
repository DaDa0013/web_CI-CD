pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script{
                    def gitGredentials = credentials('github_access_token')
                    git credentialsId: gitCredentials.id, url: 'https://github.com/DaDa0013/web_CI-CD.git'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'testing the application...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploying the application...'
            }
        }
    }
} 
