pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = "nesax/ecommerce"
    }
    stages {
#        stage('Build') {
#            steps {
#                echo 'Running build automation!'
#                sh './gradlew build --no-daemon'
#                archiveArtifacts artifacts: 'dist/ecommerce.zip'
#            }
#        }
#        stage('DeployToStaging') {
#            when {
#                branch 'master'
#            }
#            steps {
#                withCredentials([usernamePassword(credentialsId: 's2', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]) {
#                    sshPublisher(
#                        failOnError: false,
#                        continueOnError: true,
#                        publishers: [
#                            sshPublisherDesc(
#                                configName: 's2',
#                                sshCredentials: [
#                                    username: "$USERNAME",
#                                    encryptedPassphrase: "$USERPASS"
#                                ],
#                                transfers: [
#                                    sshTransfer(
#                                        sourceFiles: 'dist/ecommerce.zip',
#                                        removePrefix: 'dist/',
#                                        remoteDirectory: '/test',
#                                        execCommand: 'tree'
#                                    )
#                                ]
#                            )
#                        ]
#                    )
#                }
#            }
#        }
#        stage('Build Docker Image') {
#            when {
#                branch 'master'
#            }
#            steps {
#                script {
#                    app = docker.build(DOCKER_IMAGE_NAME)
#                }
#            }
#        }
#        stage('Docker push image') {
#            when {
#                branch 'master'
#            }
#            steps {
#                script {
#                    app = docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
#                        app.push("${env.BUILD_NUMBER}")
#                        app.push("latest")
#                    }
#                }
#            }
#        }
        stage('DeployToProduction') {
            when {
                branch 'master'
            }
            steps {
                input 'Deploy to Porduction?'
                milestone(1)
        		kubernetesDeploy(
                            kubeconfigId: 'kubeconfig',
                            configs: 'ecommerce-kube.yml',
                            enableConfigSubstitution: true
        		)
            }
        }
    }
}
