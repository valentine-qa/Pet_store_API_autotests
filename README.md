# Petstore API Autotesting project

><a target="_blank" href="https://petstore.swagger.io/">Swagger Petstore</a>
> 
![main page screenshot](screenshots/Petstore_API_main_page.png)

---
### Check list of autotests
1. Создание одного питомца.
2. Поиск питомца по ID.
3. Поиск несуществующего питомца.
4. Поиск всех питомцев по указанному статусу.
5. Удаление питомца.

---

### Used Tools
<img title="Python" src="screenshots/icons/python.svg" height="40" width="40"/>`<img title="Pytest" src="screenshots/icons/pytest.svg" height="40" width="40"/><img title="GitHub" src="screenshots/icons/github.svg" height="40" width="40"/><img title="Pycharm" src="screenshots/icons/pycharm-original.svg" height="40" width="40"/><img title="Swagger" src="screenshots/icons/swagger-svgrepo-com.svg" height="40" width="40"/><img title="Telegram" src="screenshots/icons/telegram.png" height="40" width="40"/><img title="Jenkins" src="screenshots/icons/jenkins-original.svg" height="40" width="40"/><img title="Allure TestOps" src="screenshots/icons/allure_testops.svg" height="40" width="40"/><img title="Jira" src="screenshots/icons/jira.svg" height="40" width="40"/>

---

### Run autotests with Jenkin
> [Link on task in Jenkins](https://jenkins.autotests.cloud/job/Pet_store_API_autotests/)

#### To run autotests in Jenkins
Open [task in Jenkins](https://jenkins.autotests.cloud/job/zmamedov-qa_guru_Petstore_api_test/)  
1. (Username/password for authorization in Jenkins: valentine_guest/valentine_guest)
![jenkins job main page](screenshots/Jenkins_task.png)

2. Click "**Build Now**".

---

### Allure report

#### Overall result
![allure_report page](screenshots/Allure_Report.png)

---
#### Test results with logs
![allure_report suites](screenshots/Test_results.png)

#### Graphics
![allure_report graph_1](screenshots/Allure_graphics_1.png)
![allure_report graph_1](screenshots/Allure_graphics_2.png)

### Integration Jenkins with Allure TestOps
(Login/password: allure8/allure8)
> [Dashboard with general results](https://allure.autotests.cloud/project/4223/dashboards)

![allure_testops dashboard](screenshots/Test_Ops.png)

> [Test-cases](https://allure.autotests.cloud/project/4816/test-cases/38739?treeId=0)

![allure_testops test_cases](screenshots/Test_cases.png)

---

### Интеграция с Jira
> [Задача в Jira](https://jira.autotests.cloud/browse/HOMEWORK-1234)
 
![jira task](pictures/jira_task.png)

---

### Уведомления в Телеграм

![telegram_notification](pictures/tg_notification.png)