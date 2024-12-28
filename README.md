# Yandex.practicum Data Science projects

## Repository structure/Структура репозитория

<table>
    <thead>
        <tr>
            <th>link</th>
            <th>Description/Описание</th>
            <th>Skills</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/Project_sprint_04_bank">Project_sprint_04_bank</a></td>
            <td><b>Research on the reliability of debtors</b><br>Following pre-processing, histograms, boxplots, and scatter diagrams were created from data, with the main goal being to determine the factors which influence the market value of real estate.</td>
            <td rowspan=2 align="center">python, pandas</td>
        </tr>
        <tr>
            <td><b>Исследование надежности заемщиков</b><br>Проведена предобработка данных. Построены гистограммы, боксплоты, диаграммы рассеивания. Основная задача: определить факторы, влияющие на рыночную стоимость объектов недвижимости</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/Project_sprint_05_appartments">Project_sprint_05_appartments</a></td>
            <td><b>Research on apartment listings</b><br>Determining the market value of real estate. The primary objective is to choose parameters which potentially influence the value of a property, allowing us to build an automated system capable of tracking anomalies and fraudulent activity.</td>
            <td rowspan=2 align="center">pandas, numpy, missingpy</td>
        </tr>
        <tr>
            <td><b>Исследование объявлений о продаже квартир</b><br>Определение рыночной стоимость объектов недвижимости. Задача — установить параметры. Это позволит построить автоматизированную систему: она отследит аномалии и мошенническую деятельность</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/Project_sprint_06_calls">Project_sprint_06_calls</a></td>
            <td><b>Statistical data analysis. «Rates»</b><br>An statistical analysis of the rates of an unnamed federal telecommunications company was carried out. Various services offered by the company and their interrelations were studied using statistical methods, after which anomalies were identified and processed.</td>
            <td rowspan=2 align="center">python, pandas, numpy, seaborn,matplotlib.pyplot, scipy</td>
        </tr>
        <tr>
            <td><b>Статистический анализ данных. "Тарифы"</b><br>Проанализированы тарифы федерального оператора сотовой связи. Изучение объектов и их взаимосвязей методами статистики. Выявлены и обработаны аномалии</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/Project_sprint_08_sbor1_games">Project_sprint_08_sbor1_games</a></td>
            <td><b>Project for the game store «Streamchik»</b><br>Historical data on game sales, user and expert ratings, genres, and platforms are available. The job is to identify patterns which influence and/or determine the success of any given game, which in turn will allow you to bet on a potentially popular or successful product and plan advertising campaigns. Using data up to 2016, the task is to plan for the company for 2017.</td>
            <td rowspan=2 align="center">python, pandas, numpy, scipy, matplotlib.pyplot</td>
        </tr>
        <tr>
            <td><b>Проект для магазина игр «Стримчик»</b><br>Доступны исторические данные о продажах игр, оценки пользователей и экспертов, жанры, платформы. Необходимо выявить определяющие успешность игры закономерности. Это позволит сделать ставку на потенциально популярный продукт и спланировать рекламные компании. Перед нами данные до 2016 года. Необходимо спланировать компанию на 2017 год</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/Project_sprint_09_rates">Project_sprint_09_rates</a></td>
            <td><b>Rates recommendation</b><br>We have data on the behavior of customers who have already switched to these rates and need to build a model for classification which will select appropriate rates. Task: build a model with the highest possible accuracy value. The success rate of correct answers must be brought to at least 0.75. The accuracy must be checked on the test sample.</td>
            <td rowspan=2 align="center">python, pandas, numpy, seaborn, sklearn</td>
        </tr>
        <tr>
            <td><b>Рекомендация тарифов</b><br>В нашем распоряжении данные о поведении клиентов, которые уже перешли на эти тарифы. Нужно построить модель для задачи классификации, которая выберет подходящий тариф. Задача: построить модель с максимально большим значением accuracy. Нужно довести долю правильных ответов по крайней мере до 0.75. accuracy необходимо проверить на тестовой выборке</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/project_sprint_10_customer_churn">project_sprint_10_customer_churn</a></td>
            <td><b>Customer Churn</b><br>A model for predicting the likelihood of a client's departure from a bank in the near future has been developed. The model was trained on historical data on client behavior as well as terminated contracts with the bank. The metric used is F1 score. ROC-AUC curves were also constructed. F1 = 0.6189 was achieved on the test sample, and the ROC-AUC score = 0.86.</td>
            <td rowspan=2 align="center">python, pandas, numpy, matplotlib.pyplot, seaborn, sklearn</td>
        </tr>
        <tr>
            <td><b>Отток клиентов</b><br>Разработана модель прогнозирования ухода клиента из банка в ближайшее время. Для обучения использованны исторические данные о поведении клиентов и расторжении договоров с банком. Использованая метрика F1-мера. построены ROC-AUC кривые. На тестовой выборке достигнута F1 = 0.6189, а метрика ROC-AUC = 0.86.</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/project_sprint_11_oil_wells">project_sprint_11_oil_wells</a></td>
            <td><b>Picking a location for a well</b><br>Project for the mining company «GlavRosGosNeft». A decision must be made on where to drill a new well. Oil samples were provided in three regions: 10,000 fields in each, where the quality of oil and the volume of its reserves were measured. A machine learning model was built to help determine the region where production will bring the greatest profit. The Bootstrap technique was used to analyze the potential profit and risks</td>
            <td rowspan=2 align="center">python, pandas, numpy, matplotlib.pyplot, seaborn, sklearn, scipy</td>
        </tr>
        <tr>
            <td><b>Выбор локации для скважины</b><br>Проект для добывающей компании «ГлавРосГосНефть». Необходимо решить, где бурить новую скважину. Предоставлены пробы нефти в трёх регионах: в каждом 10 000 месторождений, где измерили качество нефти и объём её запасов. Построена модель машинного обучения, которая поможет определить регион, где добыча принесёт наибольшую прибыль. Техникой Bootstrap проанализированна возможная прибыль и риски</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/project_sprint_12_sbor2_gold_recovery">project_sprint_12_sbor2_gold_recovery</a></td>
            <td><b>Recovery of gold from ore</b><br>A prototype of a machine learning model was prepared for the company «Cifra», which develops solutions for efficient operation of industrial enterprises. The model predicts the gold recovery coefficient from gold-bearing ore. The model was developed using data comprised of production and purification parameters and will help optimize production so as not to start a business with unprofitable characteristics</td>
            <td rowspan=2 align="center">python, pandas, numpy, matplotlib.pyplot, seaborn, plotly, sklearn</td>
        </tr>
        <tr>
            <td><b>Восстановление золота из руды</b><br>Подготовлен прототип модели машинного обучения для «Цифры». Компания разрабатывает решения для эффективной работы промышленных предприятий. Модель предсказывает коэффициент восстановления золота из золотосодержащей руды. Использованны данные с параметрами добычи и очистки. Модель поможет оптимизировать производство, чтобы не запускать предприятие с убыточными характеристиками</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/project_sprint_13_linalg">project_sprint_13_linalg</a></td>
            <td><b>Protection of sensitive personal data of clients</b><br>A data transformation method was developed to protect the data of the clients of the insurance company "Hot Potol", so that it would be difficult to reconstruct personal information from them without harming the quality of machine learning models and maintaining their correctness</td>
            <td rowspan=2 align="center">python, pandas, numpy, matplotlib.pyplot, sklearn, linear algebra</td>
        </tr>
        <tr>
            <td><b>Защита персональных данных клиентов</b><br>Разработан метод преобразования данных для защиты данные клиентов страховой компании «Хоть потоп», чтобы по ним было сложно восстановить персональную информацию, а качество моделей машинного обучения не ухудшилось и обоснована корректность его работы</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/project_sprint_14_autos">project_sprint_14_autos</a></td>
            <td><b>Determining the cost of cars</b><br>A model was built to determine the market value of cars for the used car sales service «Not beaten, not painted». Historical data was used: technical characteristics, trim levels and prices of cars</td>
            <td rowspan=2 align="center">python, pandas, numpy, matplotlib.pyplot, seaborn, lightgbm, sklearn, category_encoders</td>
        </tr>
        <tr>
            <td><b>Определение стоимости автомобилей</b><br>остроена модель для определения рыночной стоимости автомобилей для сервиса по продаже автомобилей с пробегом «Не бит, не крашен». Использованы исторические данные: технические характеристики, комплектации и цены автомобилей</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/project_sprint_15_taxi">project_sprint_15_taxi</a></td>
            <td><b>Taxi order prediction</b><br>Based on historical data on taxi orders at airports for the company "Chёtenkoe taxi", the following was done: resampling and data analysis; different models with different hyperparameters were trained and tested. The constructed model predicts the number of taxi orders in the next hour</td>
            <td rowspan=2 align="center">python, pandas, numpy, matplotlib.pyplot, sklearn, statsmodels, catboost</td>
        </tr>
        <tr>
            <td><b>Прогнозирование заказов такси</b><br>На основании исторические данные о заказах такси в аэропортах для компании «Чётенькое такси» выполнено: ресемплирование и анализ данных; обучены и протестированы разные модели с различными гиперпараметрами. Построенная модель прогнозирует количество заказов такси на следующий час</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/project_sprint_17_toxic_comments">project_sprint_17_toxic_comments</a></td>
            <td><b>Project for «Wikishop»</b><br>For the online store «Wikishop», a model for grouping comments into positive comments and negative comments was trained based on a data set with toxicity markup. This allows users to edit and supplement product descriptions - like in wiki communities - and toxic comments will be sent in for moderation.</td>
            <td rowspan=2 align="center">python, pandas, numpy, matplotlib.pyplot, sklearn, nltk, torch, transformers, imblearn.pipelineneural language processing (NLP), BERT model used</td>
        </tr>
        <tr>
            <td><b>Проект для «Викишоп»</b><br>Для интернет-магазин «Викишоп», на наборе данных с разметкой о токсичности, обучена модель классифицикации комментариев на позитивные и негативные. Теперь пользователи могут редактировать и дополнять описания товаров, как в вики-сообществах и токсичные комментарии будут отправлены на модерацию</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/project_sprint_19_computer_vision">project_sprint_19_computer_vision</a></td>
            <td><b>Determining the age of buyers</b><br>The supermarket chain «Khleb-Sol» is implementing a computer vision system for processing photos of customers. Photo recording in the checkout area will help determine the age of customers in order to analyze purchases, offer goods and control the integrity of cashiers when selling alcohol. A model which determines a person's approximate age based on a photograph was built by making use of the ResNet50 model and further training it on the provided labeled dataset.</td>
            <td rowspan=2 align="center">python, pandas, matplotlib.pyplot, tensorflow, keras, ResNet50, computer vision (CV)</td>
        </tr>
        <tr>
            <td><b>Определение возраста покупателей</b><br>Сетевой супермаркет «Хлеб-Соль» внедряет систему компьютерного зрения для обработки фотографий покупателей. Фотофиксация в прикассовой зоне поможет определять возраст клиентов, чтобы анализировать покупки и предлагать товары и контролировать добросовестность кассиров при продаже алкоголя. Построена модель, которая по фотографии определяет приблизительный возраст человека. Использована модель ResNet50 и дообучена на предоставленном размеченном наборе данных</td>
        </tr>
        <tr>
            <td rowspan=2><a href="https://github.com/PSImera/Yandex.practicum.ds/blob/main/project_sprint_22_final">project_sprint_22_final</a></td>
            <td><b>Determining the churn of telecom company customers</b><br>A model was built for the telecom operator «Niedinorazryva.com» to predict customer churn. If a customer is determined to have a high likelihood of leaving, they will be offered promotional codes and special offers. Personal data of some customers and information about their rates and contracts were used to train the model.</td>
            <td rowspan=2 align="center">python, pandas, numpy, matplotlib.pyplot, seaborn, imblearn, phik, sklearn, lightgbm</td>
        </tr>
        <tr>
            <td><b>Определение оттока клиентов телеком-компании</b><br>Для оператор связи «Ниединогоразрыва.ком» построена модель прогнозирующая отток клиентов. Если выяснится, что пользователь планирует уйти, ему будут предложены промокоды и специальные условия. Для обучения модели использованы персональные данные о некоторых клиентах, информацию об их тарифах и договорах</td>
        </tr>
    </tbody>
</table>
