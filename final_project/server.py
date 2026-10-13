After all the tests are successfully completed, you need to deploy the application on the web. This will enable the customer to access and use the application.

Note: The index.html file in the templates folder and mywebscript.js file in the static folder have been provided as a part of the repo. These files do not need to be updated in this project.

You have to create the server.py file from scratch. Note the following requirements of this task.

Note: server.py is a part of final_project folder.

Make sure that the Flask decorator for the application calling function is /emotionDetector.

The customer has requested the output to be displayed in the format as displayed in the example below.

Example Output Let's say that you want to evaluate the statement I love my life. The statement is processed as follows:

json

{
"anger": 0.006274985, 
"disgust": 0.0025598293, 
"fear": 0.009251528, 
"joy": 0.9680386, 
"sadness": 0.049744144, 
"dominant_emotion":"joy"
}
The response is displayed as:

For the given statement, the system response is 'anger': 0.006274985, 'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy.

Application needs to be deployed on localhost:5000