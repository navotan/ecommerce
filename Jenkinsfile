pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Running build automation!'
                sh './gradlew build --no-daemon'
                archiveArtifacts artifacts: 'dist/ecommerce.zip'
            }
        }
        stage('DeployToStaging') {
            when {
                branch 'master'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 's2', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]) {
                    sshPublisher(
                        failOnError: false,
                        continueOnError: true,
                        publishers: [
                            sshPublisherDesc(
                                configName: 's2',
                                sshCredentials: [
                                    username: "$USERNAME",
                                    encryptedPassphrase: "$USERPASS"
                                ],
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: 'dist/ecommerce.zip',
                                        removePrefix: 'dist/',
                                        remoteDirectory: '/test',
                                        execCommand: 'tree'
                                    )
                                ]
                            )
                        ]
                    )
                }
            }
        }
        stage('Build Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    app = docker.build("nesax/ecommerce")
                }
            }
        }
        stage('Docker push image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    app = docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        stage('DeployToProduction') {
            when {
                branch 'master'
            }
            steps {
                input 'Deploy to Porduction?'
                milestone(1)
                withCredentials([usernamePassword(credentialsId: 's2n', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]) {
                    script {
                        sh "sshpass  ssh  $USERNAME@$prod1_ip \"docker pull nesax/ecommerce:${env.BUILD_NUMBER}\""
                        try{
                            sh "sshpass  ssh  $USERNAME@$prod1_ip \"docker stop ecommerce\""
                            sh "sshpass  ssh  $USERNAME@$prod1_ip \"docker rm ecommerce\""
                        } catch (err) {
                            echo 'caught error: $err'
                        }
                            sh "sshpass ssh $USERNAME@$prod1_ip \"docker run --restart always --name ecommerce -p 8888:8888 -d nesax/ecommerce:${env.BUILD_NUMBER}\""
                    }
                }
            }
        }
    }
}
