# Aws Serverless Computing
## 1. Hands-on AWS serverless lambda functions
### 1.1 How to Create AWS lambda functions?
- open the function page with lambda console (type "lambda" in the search field and enter)
- Then, create function
- select author from scratch
- Under Function name"myLambdaFunction"
- Runtime "Python 3.13"
- Architecture default x86_x64
- create function
- lambda creates a function and returns a function "Hello From Lambda"
- lamda also creates an execution roles for your functions (an execution role is an AWS Identity and Access Management roles that grants lambda functions permission to access AWS services and resources).For your function, the role that Lambda creates grants basic permissions to write to CloudWatch Logs.

![Screenshot (687)](https://github.com/user-attachments/assets/23bfd3aa-3710-448e-8e4b-4e360cde5669)

![Screenshot (688)](https://github.com/user-attachments/assets/0260fa62-eaba-449f-94c4-d14258121eb3)

![Screenshot (689)](https://github.com/user-attachments/assets/14d8fce6-2b4e-4ab8-80c5-afa696d92196)

![Screenshot (690)](https://github.com/user-attachments/assets/bf77818f-ee20-4404-95b7-743a55903f08)

![Screenshot (691)](https://github.com/user-attachments/assets/f5d698a7-4073-4de0-b7be-b6d59fb4d64b)

![Screenshot (692)](https://github.com/user-attachments/assets/dfd8a2f3-78e6-4086-922c-4e602ec64677)

![Screenshot (693)](https://github.com/user-attachments/assets/1e16d013-e0ea-4fc1-8134-7b9a064ffc65)

Now, use the console's built-in code editor to replace the Hello world code that Lambda created with own function code.
- Choose the Code tab. In the console's built-in code editor, you should see the function code that Lambda created. If you don't see the lambda_function.py tab in the code editor, select lambda_function.py in the file explorer.


![Screenshot (694)](https://github.com/user-attachments/assets/9b8d3bcc-2978-4760-bec7-6f7da4982af3)

- Paste the following code into the lambda_function.py tab, replacing the code that Lambda created. <br>

import json <br>
import logging <br>
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
def lambda_handler(event, context):
    
    #Get the length and width parameters from the event object. The 
    #runtime converts the event object to a Python dictionary
    length=event['length']
    width=event['width']
    
    area = calculate_area(length, width)
    print(f"The area is {area}")
        
    logger.info(f"CloudWatch logs group: {context.log_group_name}")
    
    #return the calculated area as a JSON string
    data = {"area": area}
    return json.dumps(data)
    
def calculate_area(length, width):
    return length*width

![Screenshot (695)](https://github.com/user-attachments/assets/19fbd728-f762-402d-875c-9a192eea047b)

Select Deploy to update your function's code. When Lambda has deployed the changes, the console displays a banner letting you know that it's successfully updated your function.

![Screenshot (696)](https://github.com/user-attachments/assets/ba0bbf60-0d0e-4b83-9f1c-f9f0a5659377)

![Screenshot (697)](https://github.com/user-attachments/assets/12d4dcf9-ca99-4bcd-9b93-07a4f03c9b83)

### 1.2. Understanding your function code
Before you move to the next step, let's take a moment to look at the function code and understand some key Lambda concepts.

The Lambda handler:Your Lambda function contains a Python function named lambda_handler. A Lambda function in Python can contain more than one Python function, but the handler function is always the entry point to your code. When your function is invoked, Lambda runs this method.

When you created your Hello world function using the console, Lambda automatically set the name of the handler method for your function to lambda_handler. Be sure not to edit the name of this Python function. If you do, Lambda won’t be able to run your code when you invoke your function.


The Lambda event object:The function lambda_handler takes two arguments, event and context. An event in Lambda is a JSON formatted document that contains data for your function to process.If your function is invoked by another AWS service, the event object contains information about the event that caused the invocation. For example, if an Amazon Simple Storage Service (Amazon S3) bucket invokes your function when an object is uploaded, the event will contain the name of the Amazon S3 bucket and the object key.In this example, you’ll create an event in the console by entering a JSON formatted document with two key-value pairs.


The Lambda context object:The second argument your function takes is context. Lambda passes the context object to your function automatically. The context object contains information about the function invocation and execution environment.

You can use the context object to output information about your function's invocation for monitoring purposes. In this example, your function uses the log_group_name parameter to output the name of its CloudWatch log group.


Logging in Lambda:With Python, you can use either a print statement or a Python logging library to send information to your function's log. To illustrate the difference in what's captured, the example code uses both methods. In a production application, we recommend that you use a logging library.


Invoke the Lambda function using the console

To invoke your function using the Lambda console, you first create a test event to send to your function. The event is a JSON formatted document containing two key-value pairs with the keys "length" and "width".

### 1.3. To create the test event:
- In the Code source pane, choose Test.

- Select Create new event.

- For Event name enter myTestEvent.

- In the Event JSON panel, replace the default values by pasting in the following:
{
"length": 6,
"width": 7
}

- Choose Save.

![Screenshot (698)](https://github.com/user-attachments/assets/4bfd5553-7da7-4510-bc8a-abecd24ef816)

![Screenshot (699)](https://github.com/user-attachments/assets/ff229ff0-fa7b-46e9-a354-489467456393)

![Screenshot (700)](https://github.com/user-attachments/assets/9fe36e43-04ec-4de0-a3fa-8e2991be8ddf)

![Screenshot (701)](https://github.com/user-attachments/assets/ad11c070-d3e9-47c1-a43d-d5fafe8b8063)

![Screenshot (702)](https://github.com/user-attachments/assets/70bfead9-e699-4eba-974f-b419287c90fd)


You now test your function and use the Lambda console and CloudWatch Logs to view records of your function’s invocation.

### 1.4. To test your function and view invocation records in the console
In the Code source pane, choose Test. When your function finishes running, you’ll see the response and function logs displayed in the Execution results tab.


In this example, you invoked your code using the console's test feature. This means that you can view your function's execution results directly in the console. When your function is invoked outside the console, you need to use CloudWatch Logs.

![Screenshot (703)](https://github.com/user-attachments/assets/2227c0a2-0cf3-4d18-b3a6-f0bdbd8b0875)

![Screenshot (704)](https://github.com/user-attachments/assets/ef37d92e-0f46-4138-9f13-3d0b8f5b4550)

![Screenshot (705)](https://github.com/user-attachments/assets/30108147-d043-405c-b8ef-41440b0c60ee)

### 1.5. To view your function's invocation records in CloudWatch Logs
- Open the Log groups page of the CloudWatch console.
- Choose the log group for your function (/aws/lambda/myLambdaFunction). This is the log group name that your function printed to the console.
- In the Log streams tab, choose the log stream for your function's invocation.

When you're finished working with the example function, delete it. You can also delete the log group that stores the function's logs, and the execution role that the console created.

![Screenshot (706)](https://github.com/user-attachments/assets/ffbd14e4-fe13-4e53-8f66-280f49e96e0d)

![Screenshot (707)](https://github.com/user-attachments/assets/0870e51c-0d72-400a-8a14-a96d2d64c435)

![Screenshot (708)](https://github.com/user-attachments/assets/fdb3a204-4a64-42bd-ae5b-46af3e3ac7d5)

![Screenshot (709)](https://github.com/user-attachments/assets/cbb6747f-f15e-4854-967b-c012985de2ae)

![Screenshot (710)](https://github.com/user-attachments/assets/063e607c-6e7b-4142-8b6f-21a1265622f9)
![Screenshot (711)](https://github.com/user-attachments/assets/a02ac5a1-aeea-4c11-a1e8-0b14804e31fd)

![Screenshot (712)](https://github.com/user-attachments/assets/4c6a698e-b036-484e-9044-9904167719ae)

### 1.6. To delete a Lambda function
- Open the Functions page of the Lambda console.

- Choose a function.

- Choose Actions, Delete.

- In the Delete function dialog box, enter delete or confirm, and then choose Delete.

![Screenshot (713)](https://github.com/user-attachments/assets/f6db5ce9-bf46-4709-ab2c-1df1aa9ca905)

![Screenshot (714)](https://github.com/user-attachments/assets/138fb1a4-da12-4f3e-8055-a88cca0e1a82)

![Screenshot (715)](https://github.com/user-attachments/assets/c816179c-6479-43d1-b595-1536608c68c4)

![Screenshot (716)](https://github.com/user-attachments/assets/ff1ff388-f125-4e8b-93d9-b0299ff8dc78)

![Screenshot (717)](https://github.com/user-attachments/assets/9ac9d911-a495-4ebd-9c67-35da39e134c5)

### 1.7. To delete the log group
- Open the Log groups page of the CloudWatch console.
- Select the function's log group (/aws/lambda/my-function).
- Choose Actions, Delete log group(s).
- In the Delete log group(s) dialog box, choose Delete.

![Screenshot (718)](https://github.com/user-attachments/assets/49b3a47a-c199-42db-8841-1d32269578bb)

![Screenshot (719)](https://github.com/user-attachments/assets/099240bb-6dff-4e40-a576-5d902ced66a7)

![Screenshot (720)](https://github.com/user-attachments/assets/19dbf69d-41cb-4c85-9b34-1c1fc34da5ff)

![Screenshot (721)](https://github.com/user-attachments/assets/f27427a2-50db-40ba-beb4-884d88879e7d)

![Screenshot (723)](https://github.com/user-attachments/assets/1a708dc6-ff07-470d-a6c9-1c6ba2a3fff1)

### 1.8. To delete the execution role
- Open the Roles page of the AWS Identity and Access Management (IAM) console.
- Select the function's execution role (for example, myLambdaFunction-role-31exxmpl).
- Choose Delete.
- In the Delete role dialog box, enter the role name and then choose Delete.

![Screenshot (724)](https://github.com/user-attachments/assets/cf19ceff-9b18-4763-ab35-bc75369c4b16)

![Screenshot (725)](https://github.com/user-attachments/assets/1d3d17c6-b431-4f14-945c-9dfb95e57d0f)

![Screenshot (726)](https://github.com/user-attachments/assets/e5b381d2-bda4-4efa-bb7e-b0d3209c54ea)

![Screenshot (727)](https://github.com/user-attachments/assets/2a11c1c6-c3e8-49cc-b76a-44b53e438c2b)
