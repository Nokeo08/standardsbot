# Standards Bot
A reddit bot that is triggered by reddit comments made in [/r/Reformed](https://www.reddit.com/r/reformed) that reference various Reformed and eventually baptist confessions and catechisms. It posts the contents of the requested selection(s) as a reply to the comment that contained the request.

## Usage
### Currently Supported Catechisms and Confessions
* Westminster Shorter Catechism
* Westminster Shorter Catechism
* Heidelberg Catechism
* Belgic Confession of Faith
* Westminster Confession of Faith

#### Westminster Larger Catechism

The format of the Westminster Larger Catechism query is this: 

```[Westminster (or W) Larger (or L) Catechism (or C) ##]```

You can write the whole words out or just use the first letter, aswell as mix and match words and letters. I have ignored spacing between words and letters and it is case insensitive.

```[w LarGerc ##]```

The apove example is valid. It just looks stupid. As for the ```##``` portion of the query. This is a comma demimited list of numbers and/or number ranges in the form of ```a-b``` where ```a``` is strictly less than ```b```. For example:

```[WLC 1, 2, 5-8]```

The above with return question and answers for ```1,2,5,6,7,8```

#### Westminster Shorter Catechism

The format of the Westminster Shorter Catechism query is this: 

```[Westminster (or W) Shorter (or S) Catechism (or C) ##]```

Other than the substitution of ```Shorter``` for ```Larger``` queries work exactly the same as  the Westminster Larger Catechism.

#### Heidelberg Catechism

The format of the Heidelberg Catechism not more complicated but allows for more variation. It is as follows: 

```[Heidelberg (or H) Catechism (or C) optional{ Question (or Q) and (or &) Answer (or A)   } ##]```

Up to the optional section works just the same as the WLC and WSC so: ```[HC ##]``` and ```[Heidelberg Catachism ##]``` both work. At the request of [/u/davidjricardo](http://reddit.com/u/davidjricardo) I have added the optional section as this more closly mirrors established convention for citing the Heidelberg Confession. The optional section funtions similarlly to the previous part of the query. In the same way you can write the word out or just use the letter or in the case of ```and``` the symbol. Example:

```[HC Q&A ##]```, ```[HC Question and Answer ##]```

Both of the above are valid. You can mix and match and spacing doesn't matter. The optional section is an all or nothing section though. Either you have the whole section or you don't have any of it. You cannot have part of it.

The ```##``` section works the same as the WLC and the WSC.

#### Belgic Confession of Faith

The format of the Belgic Confession of Faith query is this: 

```[Belgic (or B) Confession (or C) optional{of} Faith (or F) ##]```

The BCF works just the same as the Heidelberg Catechism. Ex's:

```[Belgic Confession of Faith ##]```, ```[BCF ##]```

Of course you can *still* mix and match, but again that is dumb. Don't do it.

####Westminster Confession of Faith

The format of the Westminster Confession of Faith query is this: 

```[Westminster (or W) Confession (or C) optional{of} Faith (or F) ##]```

The WCF work exactly as the BCF until the ```##``` section. The numbering for the WCF is different from all of the previous documents because the WCF is made of chapters with multiple sections. 

The ```##``` for the WCF is a comma demilited list of numbers ```ex. 1``` representing a chapter number and ```:``` separated numbers ```ex. a:b``` where ```a``` is the chapter number and ```b``` is the section number. The two formats can be alone or in a range. I will give a few examples to make it more clear.

```[WCF 1]``` - All of chapter one.

```[WCF 2-3]``` - All of chapter 2 and all of chapter 3. If this range was wider the chapters inbetween would also be returned.

```[WCF 4-5:6]``` - All of chapter 4 through chapter 5 section 6.

```[WCF 7:8-9]``` - Chapter 7 section 8 through all of chapter 9.

```[WCF 10:11-12:13]``` - Chapter 10 section 11 through chapter 12 section 13.

```[WCF 14:15]``` - Just chapter 14 section 15.

### Planned supported documents
* The Canons of Dort
* London Baptist Confession of Faith
	* I think that there are two versions of this so maybe both of them

### Triggering the bot
I have tried to make the syntax as flexible as I can. The syntax is case insensitive and you can also mix and match and the spaces don't matter. While ```[bconfessionoffaith1-2,3,4]``` and ```[   bElGiC  CoNfEsSiOn oF F 1 -2 , 3,  4  ]``` both work they aren't very pretty so should probably be avoided.

I only have the bot looking through comments not at the submission text. If you want to cite a document in a text post you will have to comment on the post with the relevant citations.

## Authors
[/u/Nokeo08](http://reddit.com/u/nokeo08)

## Thanks
[Matthieu Grieger](http://www.reddit.com/u/mgrieger) for [versebot](https://github.com/matthieugrieger/versebot), from which catebot was initially derived. And [/u/konohitowa](https://www.reddit.com/user/kono_hito_wa) for [catebot](https://github.com/konohitowa/catebot), off of which a significant portion of standardsbot is based.
