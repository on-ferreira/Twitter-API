from src.credentials import X_RapidAPI_Key


BRAZIL_WOE_ID = 23424768
API_URL = "https://twitter-trends5.p.rapidapi.com/twitter/request.php"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": X_RapidAPI_Key,
	"X-RapidAPI-Host": "twitter-trends5.p.rapidapi.com"
}