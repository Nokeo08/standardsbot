# StandardsBot Changelog

### Sept 19, 2026
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
