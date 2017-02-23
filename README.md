# Pig Latin Translation Microservice
This simple microservice converts text to pig latin. It operates over HTTP, accepting text in the body of a POST request and returning the translation in the body of the response. Basically, converts text paragraph to Pig Latin.

Step - 1: Install Flask using "pip install flask"

Step - 2: Run piglatin.py file using python "piglatin.py"

Step - 3: Microservice Structure

## URL: 
```
http://localhost/piglatin
```

## Method: 
```
POST
```

## Request Body Format

```
{
  "data": String
}
```

## Response
String in piglatin

## Sample Call
- Request POST http://localhost/piglatin
```
{
  "data": pig banana trash happy duck glove eat omelet are
}
```
- Response HTTP/1.1 200 OK
```
  igpay ananabay appyhay uckday oveglay eatyay omeletyay areyay
```


