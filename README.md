# MLH BCHACKS 4.0: physicAIn!
This repository will be used by all participating team members to work collaboratively on our BC HACKS project.
### Team Members:
- Zeyad Elganainy
- Youssef Mahmoud
- Ahmed Sabry
### Project Description
An android application that uses a chatbot API to take users' input in the form of an image and feeds it into our ML models. Based on what our NPL decides, the user is directed to one of our three ML models. The first model [^1] has been trained to detect whether the user has teeth cavity or not.  The second model [^2] has been trained to determine what type of skin cancer a user may have. The third and final model [^3] has been trained to determine what type of eye diseases the user has.
More details will be provided tomorrow.

[^1]: https://www.kaggle.com/datasets/pushkar34/teeth-dataset.
[^2]: https://www.kaggle.com/datasets/farjanakabirsamanta/skin-cancer-dataset.
[^3]: https://www.kaggle.com/datasets/kondwani/optometrist-dataset

### Endpoints and ports
- model-administration: /admin          (port=5000)
- dermatologist:  /dermatologist    (port=5001)
- optometrist:  /a-eye          (port=5002)
- dentist:       /dentist         (port=5003)

### For Python Developers
Run the following command:
-    ```pip install -r requirements.txt```
