# Standards Bot
A reddit bot that is triggered by reddit comments made in [/r/Reformed](https://www.reddit.com/r/reformed) that reference various Reformed and eventually baptist confessions and catechisms. It posts the contents of the requested selection(s) as a reply to the comment that contained the request.

## Usage
### Currently Supported Catechisms and Confessions
* Westminster Larger Catechism
* Westminster Shorter Catechism
* Heidleberg Catechism
* Belgic Confession of Faith

### Planned supported documents
* Wesminster Confession of Faith
* Cannons of Dort
* London Baptist Confession of Faith
	* I think that there are two versions of this so maybe both of them

### Triggering the bot
I have tried to make the syntax as flexible as I can. For the Westminster Larger/Shorter Catechism, the Heidleberg Catechism, and the Belgic Confession the syntax is very similar. I'll use the last as an example.

The Belgic Confession syntax looks somthing like this ```[Belgic Confession of Faith 1, 4-5, 7-10, 18]```. The numbers are a comma delimited list of either a single number or a hyphen separated range where the first number is strictly lower than the second. Ranges out of order and numbers past the number of sections in the confession will be ignored. You can use the shortened version by just using the letters ```[BCF 14]```. The syntax is case insensitive so ```[bcf 8-12]``` will work just as well. You can also mix and match and the spaces don't matter. While ```[bconfessionoffaith1-2,3,4]``` and ```[   bElGiC  CoNfEsSiOn oF F 1 -2 , 3,  4  ]``` both work they aren't very pretty so should probably be avoided.

The syntax is identical for the Westminster Larger/Shorter and Heidleberg Catechisms. Either write the whole words out or use the first letters for short and the numbering is the same.


## Authors
[/u/Nokeo08](http://reddit.com/u/nokeo08)

## Thanks
[Matthieu Grieger](http://www.reddit.com/u/mgrieger) for [versebot](https://github.com/matthieugrieger/versebot), from which catebot was initially derived. And [/u/konohitowa](https://www.reddit.com/user/kono_hito_wa) for [catebot](https://github.com/konohitowa/catebot), off of which a signifigant portion of standardsbot is based.
