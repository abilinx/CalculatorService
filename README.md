# CalculatorService
This is a simple web service to provide calculator functionality via web.
## API Design
This API is not a RESTful API because it's not about accessing and modifying
resource states via HTTP methods. There is nothing as resource here. Also, it
cannot be classified as an SOAP API because it does not use XML and probably
has other limitations compared to a SOAP API.

This web service is providing an arbitrary and very simple API to be used as a
calculator, just to show what I can accomplish in a short time. Simply, send
your arithmetic statement to the endpoint in JSON format and get the result
back.
## Running
Simplest way is to run the web_service.py module with Python3.8 after
installing the requirements like this:
```bash
$ pip install -r requirements.txt
$ python3.8 ./web_service.py
```
Also, you can change the service port in the code. The other way is to run the
service as a Docker container after building the image:
```bash
$ docker build -t calculator-service:0.1.0 .
$ docker run -d -p 6543:6543 calculator-service:0.1.0
```
## Usage (API Call)
For using this (tiny) web service you have one end-point. Send a GET request to

http://localhost:6543/

or any address and port that you've deployed your service on. You need to fill
the request body with a simple JSON like this
```json
{
  "statement": "2 + 3"
}
```
Two responses are possible. If the calculator can calculate the result, it
returns 200 status code with a body like this
```json
{
  "result": "5.0"
}
```
and if it cannot do the calculation, for example because of a confusing input,
you will get 400 status code and "calculator input error" description.
## Implementation
Nothing is shinny about this implementation. I have a module named
web_service.py that contains a very simple code to use Pyramid framework to
make and endpoint available to the user. I pushed my simple implementation
which is based on simplecalculator package, to a separate module named
calculator_library.

This separation of concern seems unnecessary now but as the
project grows, it will be interesting to have web related stuff and actual
calculation in separate modules. Therefore, we will not have much difficulties
to use another framework such as Flask or decide to add more calculator
capabilities as we develop.

Please don't judge my code for its simplicity. You've decided every aspect in
the task description and I had little room to right "meaty" code.
## Next Steps
- Improve the API design. I prefer SOAP here.
- Use Swagger, which is a cool tool for designing and documentation and shines
when you use it for API code-generation.
- Use logging instead of printing for more control on levels and format.
- Implement unit-tests for the calculator_library module.
- Implement automatic API tests. I just tested manually.
