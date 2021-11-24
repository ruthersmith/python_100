This a collection of notes, exercise and projects that I am doing 
with the goal of being an expert python programmer.

I had worked with python before,
and had created a number of applications
however I really wanted to deep dive into python and
see all the possibilities that knowing this language offers.

I really love python because of how easy it is to get started
and the limitless amount of projects that can be done with it

This readme is designed to give a high level overview  of 
the mini projects contained within this repo.

They are structured by 'day' though some take longer than others.

The projects vary in complexity, 
On the project descriptions below,
I added a complexity rating based on the skills required
to create this project.

Some 'days' are also just notes.

There are additional documentation for each project
if the project is contained within a single script file,
additional documentation exist in the docstring
if it is composed of multiple script file,
the project folder may contain an additional read me file 
with more information

This readme will be able to guide you through the projects

<strong>day_4</strong>: 
        rock, paper, scissor game console application.
        uses the random module to play against the computer.
        **complexity**: _simple, but fun._

<strong>day_5</strong>:
    	console application. random password generator.
		generated with the help of random module, loops and list, 
		**complexity**: _simple, useful_

<strong>day_8</strong>:
		Caesar cipher console application.
		simple way of encrypting plain text, more info in docstring and 
		https://en.wikipedia.org/wiki/Caesar_cipher
	    **complexity**: _simple+, and cool_

**day_9**:  silent auction console application. 
			**complexity**:_simple_

**day_10**: Blackjack console application.
			my implementation of a console blackjack application.
			**complexity**: _simple+ , and fun_

**day_15**: console application that stimulate an interaction with
			a coffee machine, **complexity**: _simple_

**day_17**: not an application, notes

**day_18**: not an 'application' - uses the turtle Module 
			to draw this really cool circle/globe, 
			**complexity**:_simple_

**day_19**:contains 2 GUI programs that make use of the turtle module:
<ol> 
	<li>turtle_race.py: Turtle racing,
		stimulate assisting a race of turtle
		where user can bet which turtle will win, 
		<strong>complexity</strong>: simple-medium
	</li>
		2. Fully Interactive program that stimulate the Etch A Sketch toy, which a user can use to draw onto the screen using the arrow keys
		   complexity: medium </ol>
	
GUI GAMES using mainly the turle module
	day_20: Snake Game. Uses OOP Concepts to design a Fully interactive replica of the once very popular snake arcade game. complexity: medium
	day_22: Pong Game. Uses OOP Concepts to design a Fully interactive replica of the Pong arcade. game complexity: medium+
	day_23: Turtle crossing game. Uses OOP Concepts to design a Fully interactive replica of the crossy road game. with additional features
			such as data persistence by saving the highest level in a text file. As well as error handling. complexity: medium+
		
day_24: Mail Merge Application. creates personalised letter by taking 2 input files a template and a file containg the list of names and personalised
        the letter template by replacing '[name]' with the name of each recipients iteratively to create n amount of letters where n == number of recipients
		complexity: simple-medium
		
day_25: us_states_game . Educational Gui Quiz game testing your knowledge of the us state. makes use of python modules - turtle, time and pandas
day_26: under nato-alphabet. program that returns the phonetic spelling of a word, see docstring in the main.py for more info, makes use of the pandas module
		and the elegance of list and dictionary comprehension

day_28: Fully functioning Pomodoro Timer Gui Application using the tkinter module. complexity: medium+
day_29: Password manager GUI application improvement of day the day_5 random password generator into a full-fledged password manager with a GUI interface
		This program that allows users to store, search, generate, and manage their passwords  complexity: medium++
		
day_31: Flash card GUI Application. uses pandas, tkinter and random module, currently uses hard coded keys can improved to use variable keys complexity: medium
day_32: This folder contain 2 small program, to play with the smtplib module.
		Note that for these program to work, you must set , the from_address, the from address password, the to_address and the smtphost of the smtp lib
		I used a secret file to pass these info into the program, if you wanted for these program to work out of the box without modifying anything you could
		add a secret.txt in the root of the project folder day_32... with the from_address,password,to address on each line in that order, 
		the program assumes gmail as the from address. complexity: medium
		
day_33: Gui program that displays on the screen a random kanye quote fetched from the kanye rest api at the click of a button. complexity: medium
day_35: simple program to work with the twilio api to send a text message, in order for this to work for you, you would need:
		a twillio ACCOUNT_SID and AUTH_TOKEN, and use your twilio number to send the sms to a phone you could test it with, if you have all of that
		and would like to run the program without modifying it directly, you could create a secret.txt in the same dir as main.py with the account_sid,
		auth_token, your_twillio_number, phone_num_to_text each place on a new line in that order. complexity: medium
		
day_36: stock price alert program -> This program  monitors the price of a particular stock, in this case tesla
		if the price between 2 consecutive days decreases by more than 5 percent,
		the program searches the news and sends a text alert. Due to limitation on the API, I can only get news less than a month old,
		I change the values received just to get some data, see additional details in main.py docstring complexity: medium-advanced
		
day_37: Makes a habit tracker using the pixela API, not interactive, need knowledge of pixela api to use. complexity: medium
day_38: workout tracker using the uses nutritionix nlp to get the excercise stats then uses the sheety api to post the endpoint to google sheets

day_39: Flight Finder, This program monitor flight prices between a from location and several to destinations from a google sheet. If the price	
		between the from and the to destination is lower than a specified threshold as recorded in the google sheet, the programs send an email alert

day_46: Spotify time machine. When ran, this program prompts the user to enter a  in the format (yyyy-mm-dd), then the program uses beautifulsoup to 
		scrape the billboard top 100 for the provided date, then creates a spotify playlist containing the top songs for that date. This program requires 
		a spotify cliend id and client secret, I passed this info in using a secret.json file using the keys Spotify_Client_ID, Spotify_Client_Secret

		

