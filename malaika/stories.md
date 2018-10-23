## Generated Story -5017003503898935716
* Default Welcome Intent
    - utter_greet
* smalltalk.general
    - utter_small_talk
* weather{"geo-city": "oslo"}
    - slot{"geo-city": "oslo"}
    - action_weather
    - slot{"geo-city": "oslo"}
* jokes.get
    - utter_joke
* jokes.get.more
    - utter_joke
* jokes.feedback.good
    - utter_thanks
* weather
    - utter_ask_location
* weather{"geo-city": "italy"}
    - slot{"geo-city": "italy"}
    - action_weather
    - slot{"geo-city": "italy"}

## Generated Story -2461469989659384571
* Default Welcome Intent
    - utter_small_talk
* place_search{"query": "club", "number": "600"}
    - action_POI
    - slot{"location_match":"one"}
	- slot{"rating":"4.5"}
	- slot{"address":"Alexanderplatz 15"}
	- slot{"opening_hours":"open"}
* opening_hours
    - utter_opening_hours
* love.ask
    - utter_feelings
* feelings.sad
    - utter_joke
* jokes.get.more
    - utter_joke

## Generated Story 6115196622549886768
* Default Welcome Intent
    - utter_small_talk
* weather{"location": "russia"}
    - slot{"location": "russia"}
    - action_weather
* jokes.get
    - utter_joke
* jokes.get.more
    - utter_joke
* weather{"location": "oslo"}
    - slot{"location": "oslo"}
    - action_weather
* weather{"location": "india"}
    - slot{"location": "india"}
    - action_weather

## Generated Story 7319578537778123961
* place_search{"query":"shop"}
    - utter_what_radius
* radius{"number": "2000"}
    - action_POI
    -slot{"address":"mandela 123"}
* address
    - utter_address
* goodbye
    - utter_goodbye

## location_search_01
* place_search{"query":"restaurant", "number":"55"}
	- action_POI
	- slot{"location_match":"one"}
	- slot{"rating":"4.5"}
	- slot{"address":"Alexanderplatz 15"}
	- slot{"opening_hours":"open"}
* address
	- utter_address
* rating
	- utter_rating
* opening_hours
	- utter_opening_hours
* weather
    - utter_ask_location
    - slot{"geo-city": "england"}
    - action_weather
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye

## location_search_02
* Default Welcome Intent
	- utter_greet
* place_search{"query":"restaurant", "number":"21"}
	- action_POI
	- slot{"location_match":"none"}
	- utter_no_results
* goodbye
	- utter_goodbye	
		
## location_search_03
* Default Welcome Intent
	- utter_greet
* weather{"geo-city": "oslo"}
    - slot{"geo-city": "oslo"}
    - action_weather
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye	
	
## location_search_04
* Default Welcome Intent
	- utter_small_talk
* place_search{"query":"restaurant", "number":"25"}
	- action_POI
	- slot{"location_match":"one"}
	- slot{"rating":"3.0"}
	- slot{"address":"Bridge Street 175"}
	- slot{"opening_hours":"open"}
* rating
	- utter_rating	
* address
	- utter_address
* opening_hours
	- utter_opening_hours
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye	
	
	
## location_search_05
* place_search{"query":"restaurant", "number":"95"}
	- action_POI
	- slot{"location_match":"one"}
	- slot{"rating":"4.7"}
	- slot{"address":"King's street"}
	- slot{"opening_hours":"closed"}
* opening_hours
	- utter_opening_hours	
* address
	- utter_address
* rating
	- utter_rating	
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye	
	
## location_search_07
* Default Welcome Intent
	- utter_greet
* place_search{"query":"restaurant"}
	- utter_what_radius
* radius{"number":"200"}
	- action_POI
	- slot{"location_match":"one"}
	- slot{"rating":"4.2"}
	- slot{"address":"Alexanderplatz 26"}
	- slot{"opening_hours":"closed"}
* address
	- utter_address
* rating
	- utter_rating
* opening_hours
	- utter_opening_hours
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye		

## location_search_08
* smalltalk.general
	- utter_small_talk
* place_search{"query":"restaurant"}
	- utter_what_radius
* radius{"number":"275"}
	- action_POI
	- slot{"location_match":"none"}
	- utter_no_results
* weather{"geo-city": "zimbabwe"}
    - slot{"geo-city": "zimbabwe"}
    - action_weather
* goodbye
	- utter_goodbye	

## Generated Story 001
* Default Welcome Intent
    - utter_greet
* smalltalk.general
    - utter_small_talk
* smalltalk.general
    - utter_small_talk
* love.ask
    - utter_feelings
* place_search{"query": "restaurant", "number": "500"}
    - action_POI
    - slot{"location_match":"one"}
	- slot{"rating":"2.2"}
	- slot{"address":"Zulu 374"}
	- slot{"opening_hours":"closed"}
* address
    - utter_address
* thanks
    - utter_thanks
	
## location_search_09
* Default Welcome Intent
	- utter_greet
* place_search{"query":"restaurant"}
	- utter_what_radius
* radius{"number":"250"}
	- action_POI
	- slot{"location_match":"one"}
	- slot{"rating":"2.2"}
	- slot{"address":"London Bridge"}
	- slot{"opening_hours":"open"}
* address
	- utter_address
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye	

## Generated Story 973159774746284984
* place_search{"query": "cinema", "number": "50"}
    - action_POI
    - slot{"location_match":"one"}
	- slot{"rating":"3.5"}
	- slot{"address":"Church 374"}
	- slot{"opening_hours":"open"}
* address
    - utter_address
* opening_hours
    - utter_opening_hours
* thanks
    - utter_thanks

* weather{"geo-city": "italy"}
    - slot{"geo-city": "italy"}
    - action_weather
* thanks
    - utter_thanks
	
## location_search_10
* Default Welcome Intent
	- utter_greet
* place_search{"query":"restaurant"}
	- utter_what_radius
* radius{"number":"200"}
	- action_POI
	- slot{"location_match":"one"}
	- slot{"rating":"5.2"}
	- slot{"address":"London 273"}
	- slot{"opening_hours":"closed"}
* opening_hours
	- utter_opening_hours
* address
	- utter_address
* thanks
	- utter_thanks
* goodbye
	- utter_goodbye

## Generated Story -1699675097843568789
* place_search{"query":"club"}
    - utter_what_radius
* radius{"number": "2000"}
    - action_POI
    - slot{"location_match":"one"}
	- slot{"rating":"5.2"}
	- slot{"address":"Mandela 74"}
	- slot{"opening_hours":"closed"}
* address
	- utter_address
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye

## Generated Story 5599231948538186316
* smalltalk.general
    - utter_small_talk
* love.ask
    - utter_feelings
* jokes.get
    - utter_joke
* jokes.get.more
    - utter_joke
* jokes.feedback.good
    - utter_thanks
* jokes.get
    - utter_joke
* jokes.feedback.good
    - utter_thanks
* feelings.happy
    - utter_small_talk
* feelings.sad
    - utter_joke
* jokes.feedback.good
    - utter_thanks
* love.ask
    - utter_feelings
* place_search{"query":"bank"}
    - utter_what_radius
* radius{"number": "5000"}
    - action_POI
    - slot{"location_match":"one"}
	- slot{"rating":"5.2"}
	- slot{"address":"Perm 374"}
	- slot{"opening_hours":"open"}
* address    
    - utter_address
* opening_hours
    - utter_opening_hours
* thanks
    - utter_thanks
* place_search{"query":"supermarket"}
    - utter_what_radius
* radius{"number": "2000"}
    - action_POI
    - slot{"location_match":"one"}
	- slot{"rating":"5.2"}
	- slot{"address":"Perm 374"}
	- slot{"opening_hours":"open"}
* address
    - utter_address
* opening_hours
    - utter_opening_hours
* goodbye
    - utter_goodbye

## Generated Story -7111640033593290065
* Default Welcome Intent
    - utter_greet
* smalltalk.general
    - utter_small_talk
* smalltalk.general
    - utter_small_talk
* love.ask
    - utter_feelings
* place_search{"query": "restaurant", "number": "500"}
    - action_POI
    - slot{"location_match":"one"}
	- slot{"rating":"2.2"}
	- slot{"address":"Zulu 374"}
	- slot{"opening_hours":"closed"}
* address
    - utter_address
* thanks
    - utter_thanks

