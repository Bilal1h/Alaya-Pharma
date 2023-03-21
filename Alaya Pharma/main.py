from flask import Flask, request, send_file
import http.client
import ssl 

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('/home/AlayaPharma/mysite/index.html')

@app.route('/send-message', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        # Get the form data
        email = request.form['email']
        messages = request.form['message']
        message = f"Email : {email}, Message : {messages}"
        conn = http.client.HTTPSConnection("api.ultramsg.com",context = ssl._create_unverified_context())

        payload = f"token=api-key&body={message}"
        payload = payload.encode('utf8').decode('iso-8859-1') 

        headers = { 'content-type': "application/x-www-form-urlencoded" }

        conn.request("POST", "/instanceid/messages/chat", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        # TODO: Send the message using your preferred API

        # Return a response
        return 'Message sent successfully'

    # If the request is a GET request, render the send_message.html template


if __name__ == '__main__':
    app.run()
