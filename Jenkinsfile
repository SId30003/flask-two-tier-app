pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/SId30003/flask-two-tier-app'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker rm -f flask-container || true'
                sh 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed 🚀'
        }
    }
}

