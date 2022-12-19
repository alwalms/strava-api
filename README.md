# Strava API

## To auth manually

Go to the following

```
https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all
```

Click authenticate and await a screen saying something like "cannot be found". Grab the code from the URL and run this cURL

```shell
curl -X POST https://www.strava.com/oauth/token \
	-F client_id={CLIENT_ID} \
	-F client_secret={CLIENT_SECRET} \
	-F code={AUTH_CODE} \
	-F grant_type=authorization_code > dev/out.json
```

From the response get the access_token which will allow you to get any data for the athlete