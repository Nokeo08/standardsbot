# StandardsBot Changelog

### Oct 14, 2016
* Now using a simple one table sqlite3 database to store commentid's and metadata
* Major Refactor
	* Now using better oop design principles.
	* Moved teh code that assemples the results for each document into the text class for that document.
	* Moved the two parse functions into their own file. Using the strategy design pattern to supply implementation to the parse functions for all the text classes.
	* Functions always return a type. Either empty string or some default value. No functions should be returning NonType any more.
* Added better malformed requested checking.
* Went live in [/r/Reformed](http://reddit.com/r/reformed)!

### Sept 25, 2016
* Added Westminster Confession of Faith
* Added notify.py to text me if and when standardsbot goes down and supervisord cannot get it restarted.
* Did a massive rewrite of the README to be clearer on the syntax. Added lots of examples.
* Added a try/except to catch a strange connection error that was causing crashes. The issue is not with my code and doesn't seem to actually be an issue. Once the error occurs immediately trying again works.
* Now logging to stdout as the output is being redirected by supervidord 

### Sept 19, 2016
* Fixed various misspellings in the README and two in the parser.py
* Changed regex
  * Cleaned up WLC, WSC, HC, and BCF to make it a bit more clear what was happening and to avoid splitting words
  * Added to the regex of HC, at the suggestion of [/u/davidjricardo](http://reddit.com/u/davidjricardo), to allow for Q&A after HC in query. Will update the README to reflect and given syntax examples for all implemented standards in a later commit.

### Aug 30, 2016
* Fixed issue where when citing a range every question was numbered the same
* Fixed issue where single double digit citations were not being responded to
* Added check and response to malformed citations
* Only add comment.id to processed comments that have been responded to
* Expanded the regex to make queries more flexible
* Added quick log function
* Added changelog
* Updated README
* Added some features from [Catebot](https://github.com/konohitowa/catebot) that seemed like a good idea, were better than what I was already doing, or was something I had forgotten about
  * Added check for RateLimitExceeded
  * [konohitowa](https://github.com/konohitowa) uses the same syntax for queries, but his regex was better than mine. Regex now based on his.
  * Added waring suppression for a few issue that are not actually issues
  * Added check for character limit exceeding maximum. I didn't want some strange edge case around the actual limit, so I am checking for reply > 9500 rather than 10000
  * Added footer.

### Aug 24, 2016
* Remade BC.py to fix some formatting issue I was having and to add links to the verses cited in each article
* Added utf-8 encoding to all files.
* Added parser to handle queries for WLC, WSC, HC, and BC
* Basic Querying for WLC, WSC, HC, and BC

### Aug 17, 2016
* Basic call and response functionality working
