# StandardsBot Changelog

### March, 20, 2023
* Added exception handling
* Updated README to mention Confessions_bot
* Bumped bot to 23.3

### December 14, 2022
* Updated dependencies
* Added The Articles of Religion of the Methodist Church
* Added Zwingli's 67 Articles
* Added Keach's Catechism
* Added Savoy Declaration of Faith
* Added Helvetic Consensus Formula
* Containerized application
* Bumped bot to 22.12

### Sept 1, 2018
* Added The Second Helvetic Confession
* Refactor
    * Renamed a lot of files.
    * Restructured the project
* Removed notify.py
    * Removed yagmail and plumbum from requirements
* Moved Config values into a json file
* Bumped bot to v18.9

### Aug 20, 2018
* Updated Documentation
* Removed 'The' from the regex for couple of standards
* Bumped bot to v18.8.2

### Aug 17, 2018
* Fixed: Issue #16
* Updated Failable to except Request Exception and wait before continuing
* Bumped bot to v18.8.1

### Aug 15, 2018
* Updated requirements to latest versions
* Converted all of the standards fully to JSON and removed the standards objects. This should make adding new standards easier.
* Fixed CDA and CDR both were missing the 5th section of the standard
* Added the 95 Theses
* Added the London Baptist Confession of Faith 1646
* Added the Scottish Confession of Faith 1646
* Added C. H. Spurgeon's Puritan Catechism
* Added The Chicago Statement on Biblical Inerrancy
* Added The Augsburg Confession
* Added The Catechism of the Catholic Church
* Changed versioning to calendar versioning. Starting with this release the versioning will be the year followed by the month of the release.

### Nov 27, 2017
* Major refactor and update to praw 5.2.0
    * Packages have been shuffled into utils and standards
    * Standards are more self-contained now. Regex is contained inside the standards object
    * Database now uses comment_id as a primary key and tracks subreddit
* Added two tests to test parsers.py
    * one_to_one_parser has 10 scenarios tested
    * chapter_paragraph_parser has 49 scenarios tested
* Bot is now PEP8 compliant
* Now checking if comment is archived before replying
* Now able to target multiple subreddits
* Added the ability to use '.' in addition to ':' in standards that use the chapter_paragraph_parser for issue 12
* Bumped bot to v1.2

### Nov 7, 2016
* Fixed Misspelling in WLC header
* Added Canons of Dort
    * This is split up into CDA and CDR queries
* Changed chapterParagraphParser to remove whole chapter queries. This simplifies the parsing as well as fixes a crash causing bug and aligns more closely to how people are already trying to query standards using this parser.
* Bumped bot to v1.1

### Oct 18, 2016
* Fixed spelling and formatting errors.
* Added the London Baptist Confession of Faith 1689
* Added the 39 Articles of Religion
* With 7 Standards implemented I am now bumping the bot to v1.0

### Oct 14, 2016
* Now using a simple one table sqlite3 database to store commentid's and metadata
* Major Refactor
	* Now using better oop design principles.
	* Moved teh code that assembles the results for each document into the text class for that document.
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
