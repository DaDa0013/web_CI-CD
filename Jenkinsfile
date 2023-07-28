pipeline {
    agent any
    triggers {
        githubPush() // GitHub에 커밋이 발생하면 자동으로 파이프라인을 시작
    }
    stages {
        stage('Checkout') {
            steps {
                // GitHub 저장소의 코드를 가져옴
                checkout scm
            }
        }
        stage('Build Frontend Image') {
            steps {
                script {
                    // Frontend Docker 이미지 빌드
                    sh 'docker build -t dada0013/my_frontend:latest ./front'
                }
            }
        }
        stage('Build Backend Image') {
            steps {
                script {
                    // Backend Docker 이미지 빌드
                    sh 'docker build -t dada0013/my_backend:latest ./back'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Docker Swarm 클러스터에 서비스 배포
                    sh 'docker stack deploy -c docker-compose.yml my_app'
                }
            }
        }
    }
}
