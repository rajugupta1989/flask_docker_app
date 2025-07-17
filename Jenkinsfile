pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/rajugupta1989/flask_docker_app.git', branch: 'main'
            }
        }

        stage('Docker Build') {
            steps {
                echo '🔧 Building Docker image...'
                sh 'docker build -t flask-app .'
            }
        }

        stage('Stop and Remove Old Container') {
            steps {
                echo '🛑 Checking and stopping existing container...'
                sh '''
                    CONTAINER_NAME=flask-container
                    if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
                        echo "Stopping running container..."
                        docker stop $CONTAINER_NAME
                    fi

                    if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
                        echo "Removing existing container..."
                        docker rm $CONTAINER_NAME
                    fi
                '''
            }
        }

        stage('Run New Container') {
            steps {
                echo '🚀 Running new Docker container...'
                sh 'docker run -d --name flask-container -p 5000:5000 flask-app'
            }
        }
    }

    post {
        always {
            echo '✅ CI/CD pipeline run complete.'
        }
    }
}
