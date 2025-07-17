pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        CONTAINER_NAME = "flask-container"
        IMAGE_NAME = "flask-app"
        PORT = "5000"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '🔄 Checking out code...'
                git url: 'https://github.com/rajugupta1989/flask_docker_app.git', branch: 'main'
            }
        }

        stage('Docker Build') {
            steps {
                echo '🔧 Building Docker image...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop and Remove Old Container') {
            steps {
                echo '🛑 Forcibly stopping and removing old container if it exists...'
                sh '''
                    CONTAINER_NAME=flask-container

                    # Stop & remove
                    if [ "$(sudo docker ps -q -f name=$CONTAINER_NAME)" ]; then
                        echo "Stopping old container..."
                        sudo docker stop $CONTAINER_NAME || true
                    fi

                    if [ "$(sudo docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
                        echo "Removing old container..."
                        sudo docker rm -f $CONTAINER_NAME || true
                    fi
                '''
            }
        }



        stage('Run New Container') {
            steps {
                echo '🚀 Running new Docker container...'
                sh '''
                    docker run -d \
                        --name $CONTAINER_NAME \
                        -p $PORT:5000 \
                        $IMAGE_NAME
                '''
            }
        }
    }

    post {
        always {
            echo '✅ CI/CD pipeline run complete.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
