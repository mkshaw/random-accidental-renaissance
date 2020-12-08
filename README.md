# random-accidental-renaissance

Display a random photo from /r/AccidentalRenaissance. This code calls the reddit API for a supplied subreddit (though I built it with /r/AccidentalRenaissance in mind) and returns the URL to a random photo. Within shell, you run it as follows:

`python3 get_art.py sample_size filter subreddit username`

Where:
* `sample_size` specifies how many posts you want to sample 
* `filter` specifies your desired filter (i.e., /hot or /new posts)
* `subreddit` specifies the subreddit to pull from
* `username` is your reddit username (required for authentication)

It prints the URL to a random photo to console.

TODO:
* Handle input sample size of more than 100 (the limit for the reddit API)
* Offer functionality to download photo directly *or* open in browser if user specifies
* Maybe add tags to help keep arguments in order
