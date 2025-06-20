pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                // Optional if you're already using a local copy
                git 'https://github.com/rajugupta1989/flask_docker_app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker rm -f flask-container || true'
                sh 'docker run -d --name flask-container -p 5000:5000 flask-app'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
    }
}
