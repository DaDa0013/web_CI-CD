pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Checkout 코드를 가져오기 전에 리비전을 확인합니다.
                    def revision = 'main' // 빌드할 리비전 (브랜치 이름이나 커밋 해시 등)
                    def gitCredentials = credentials('github_access_token')
                    git credentialsId: gitCredentials.id, url: 'https://github.com/DaDa0013/web_CI-CD.git', branch: revision
                }
            }
        }
        stage('Test') {
            steps {
                echo 'testing the application...'
                // 테스트 스크립트를 실행하도록 작성해야합니다.
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploying the application...'
                // 배포 스크립트를 실행하도록 작성해야합니다.
            }
        }
    }
}
