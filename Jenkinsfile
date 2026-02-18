pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'YOUR_GITHUB_REPO_URL'
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Build & Run') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }
}
