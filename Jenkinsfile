pipeline {
  agent any
  stages {
    stage('k') {
      steps {
        git(url: 'https://github.com/marioluan/jenkinsci.git', branch: 'master', changelog: true)
      }
    }
  }
}