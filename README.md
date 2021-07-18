# Jenkins Pipeline to add an IAM user and deploy SSH keys in the user account.
This pipeline will add an IAM user in a particular group(selected by user) and deploy SSH keys in the user account.

## The 2 Stages of Pipeline -
| S.No | Stage Name | Stage Description |
|------|------------|--------------------|
| 1 | Download | Downloads the code from GitHub |
| 2 | Build and Deploy | Add an IAM user in a particular group and deploy SSH keys in the user account.|

## Prerequisites
- Jenkins should be Installed and configured.
- Install AWS Steps plugin in Jenkins.
- IAM username to add.
- Set credentials in Jenkins to access GitHub repository and AWS Account.

## Pipeline Workflow
- withCredentials: For accessing the GitHub account to download the python code, we need to setup the credentials in Jenkins.
- withCredentials([aws]): For accessing the AWS Account to add an IAM user in a particular group and deploy SSH keys in the user account.
- Downloads the pipeline and code from github repository.
- Add an IAM user in a particular group and deploy SSH keys in the user account.


## Variables Used
### Jenkins Parameters:
- `IAM_USER_NAME` - It is a string parameter which asks for username to add.
- `IAM_Group` - It is a choice parameter which gives a dropdown to select the particular IAM Group.
- `SSH_Key` - It is a Text parameter which asks for Public SSH Key to add in IAM user.

## How to use
- Copy the Pipeline code in your Jenkins job.
- Set the credentials of GitHub in Jenkins.
- Set the credentials of AWS acc. in Jenkins.
- Replace the `withCredentials` block with your own credentials.
- Put aws_access.py in your GitHub account whose credentials you setted up in Jenkins, by this Jenkins will download the code first in the server.
- Deploy stage will run the python code and will add an IAM user in the selected IAM Group and deploy SSH Key to user.

### Further Reference and Contact 
##### Feel free to Contact for any issue!!

<a href="https://www.linkedin.com/in/mananjainn/" target="_blank"> <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /> </a>

