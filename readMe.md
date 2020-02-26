#Demand Backend
```
/login.py
    # Login handler for when a user wants to login to our website
    # Activated when the user inputs login credentials and hits submit
    # We will receive some JSON formatted body and check if the
    # received username and password are pairs in the DB
    # On success the user will be redirected to our dashboard
    # On failure the user will be prompted to retry their 
    # input and that there was a failure to authenticate

/order.py
    # Order handler for when our user places an order and we now need a vehicle to fulfill that order request
    # Activated when the user has filled out an order form and hits submit
    # We will receive a JSON formatted body containing information such as location and customer id
    # The JSON object will be parsed into a Python dictionary then stored into our database
    # With the order data, we will then make an API call to our supply vehicle request API with our order body
    # as the payload. Supply necessary data parsing will happen on the receiving end
    # If we've made it this far, we'll receive a response as a vehicle data json
    # This vehicle json will then be pushed back to the HTML and JS and somehow rendered to our user
    # to know that their order has been confirmed and is beginning fulfillment

/register.py
    # Register handler forwhen our user wants to register an account for WeGo services
    # Activated when the user fills our a request form and hits submit
    # We will receive a JSON formatted body containing information such as a desired username, password, phoneNumber
    # and email
    # Firstly we will check if the username or email already exists in the DB,
    # if true, alert user that username isn't unique, and perhaps they already have an account
    # else, store data into db and redirect to dashboard.html
```