pipeline{
	agent any

	triggers{
		githubPush()
	}

	stages {
		stage('Checkout'){
			steps{
				checkout([$class: 'GitSCM', branches: [[name: '*/master']], userRemoteConfigs: [[url: 'https://github.com/K-Kate-e/Calc']]])
			}
		}

		stage ('Build'){
			steps{
				echo 'Building...'
				sh 'docker build -t api_calc:latest .'
			}
		}

		stage('Test'){
			steps{
				echo 'Testing...'
				sh 'docker stop $(docker ps -a -q)'
				sh 'docker run -d -p 5555:5555 api_calc'
				sh 'sleep 60'
				sh 'curl 0.0.0.0:5555/calculator\\?num1=48\\&num2=75\\&operation=s'
				sh 'docker stop $(docker ps -q --filter ancestor=api_calc)'
			}
		}
	}
}