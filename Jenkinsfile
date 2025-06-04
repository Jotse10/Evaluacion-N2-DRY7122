pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Se clona el repositorio de GitHub.
                git url: 'https://github.com/Jotse10/Evaluacion-N2-DRY7122.git', branch: 'master'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Se construye la imagen Docker a partir del Dockerfile en el directorio.
                sh 'docker build -t sample-app .'
            }
        }
        stage('Deploy') {
            steps {
                // Si existe un contenedor anterior, se elimina.
                sh 'docker rm -f sample-app || true'
                // Se levanta el contenedor mapeando el puerto 9999 del contenedor al 9999 del host.
                sh 'docker run -d -p 9999:9999 --name sample-app sample-app'
            }
        }
    }
    post {
        always {
            echo "Pipeline completado - Trabajo-Eva2 finalizado"
        }
    }
}
