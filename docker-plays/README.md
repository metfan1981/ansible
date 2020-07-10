### Docker-compose playbook
Playbook to install and configure Docker at managed hosts; then deploy LAMP stack using **mysql:8.0** and **metfan1981/apache:latest** Docker Images.


### How to use

* Edit 'env.jinja2' to pass your values:

> MYSQL_ROOT_PASSWORD = password

> WEB_MSG = Message to be displayed at webpage.

* To deploy compose, run  **ansible-playbook compose-up.yml**  
* To destroy compose, run **ansible-playbook compose-destroy.yml** 
