pipeline {
    agent any

    stages {
        stage('Git Pull') {
            steps {
                git url: 'https://github.com/rajugupta1989/flask_docker_app.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh 'docker rm -f flask-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name flask-container -p 5000:5000 flask-app'
            }
        }
    }

    post {
        always {
            echo '✅ Build complete.'
        }
    }
}
