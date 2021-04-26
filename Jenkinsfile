pipeline {
    agent any
    environment {
        registry = "060504961461.dkr.ecr.ap-south-1.amazonaws.com/voucher"
        //- update your credentials ID after creating credentials for connecting to Docker Hub
        registryCredential = 'aws_credentials'
        dockerImage = ''
    }
   
    stages {
        stage('Cloning Git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/manghani/voucher.git']]])     
            }
        }
   
    // Building Docker images
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry
            docker.build('voucher')
        }
      }
    }
    stage('Docker push'){
        steps{
            script{
                docker.withRegistry("https://060504961461.dkr.ecr.ap-south-1.amazonaws.com/voucher", "ecr:ap-south-1:aws_credentials") {
                 docker.image("voucher").push()
                }

            }
        }
    }
    
     
    // Running Docker container, make sure port 8096 is opened in
    stage('Docker Run') {
     steps{
         script {
            dockerImage.run("-p 8096:5000 --rm --name voucher")
         }
      }
    }
  }
}
