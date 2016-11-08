# Standards Bot
A reddit bot that is triggered by reddit comments made in [/r/Reformed](https://www.reddit.com/r/reformed) that reference various Reformed and eventually baptist confessions and catechisms. It posts the contents of the requested selection(s) as a reply to the comment that contained the request.

## Usage
### Currently Supported Catechisms and Confessions
* Westminster Shorter Catechism
* Westminster Shorter Catechism
* Heidelberg Catechism
* Belgic Confession of Faith
* Westminster Confession of Faith
* London Baptist Confession of Faith
* 39 Articles of Religion
* Canons of Dort

#### Westminster Larger Catechism

The format of the Westminster Larger Catechism query is this:

```[Westminster (or W) Larger (or L) Catechism (or C) ##]```

You can write the whole words out or just use the first letter, as well as mix and match words and letters. I have ignored spacing between words and letters and it is case insensitive.

```[w LarGerc ##]```

The above  example is valid. It just looks stupid. As for the ```##``` portion of the query. This is a comma demimited list of numbers and/or number ranges in the form of ```a-b``` where ```a``` is strictly less than ```b```. For example:

```[WLC 1, 2, 5-8]```

The above with return question and answers for ```1,2,5,6,7,8```

#### Westminster Shorter Catechism

The format of the Westminster Shorter Catechism query is this:

```[Westminster (or W) Shorter (or S) Catechism (or C) ##]```

Other than the substitution of ```Shorter``` for ```Larger``` queries work exactly the same as  the Westminster Larger Catechism.

#### Heidelberg Catechism

The format of the Heidelberg Catechism not more complicated but allows for more variation. It is as follows:

```[Heidelberg (or H) Catechism (or C) optional{ Question (or Q) and (or &) Answer (or A)   } ##]```

Up to the optional section works just the same as the WLC and WSC so: ```[HC ##]``` and ```[Heidelberg Catechism ##]``` both work. At the request of [/u/davidjricardo](http://reddit.com/u/davidjricardo) I have added the optional section as this more closely mirrors established convention for citing the Heidelberg Confession. The optional section functions similarly to the previous part of the query. In the same way you can write the word out or just use the letter or in the case of ```and``` the symbol. Example:

```[HC Q&A ##]```, ```[HC Question and Answer ##]```

Both of the above are valid. You can mix and match and spacing doesn't matter. The optional section is an all or nothing section though. Either you have the whole section or you don't have any of it. You cannot have part of it.

The ```##``` section works the same as the WLC and the WSC.

#### Belgic Confession of Faith

The format of the Belgic Confession of Faith query is this:

```[Belgic (or B) Confession (or C) optional{optional{of} Faith (or F)} ##]```

The BCF works just the same as the Heidelberg Catechism. Ex's:

```[Belgic Confession of Faith ##]```, ```[BCF ##]```,```[BC ##]```

Of course you can *still* mix and match, but again that is dumb. Don't do it.

#### Westminster Confession of Faith

The format of the Westminster Confession of Faith query is this:

```[Westminster (or W) Confession (or C) optional{of} Faith (or F) ##]```

The WCF work exactly as the BCF until the ```##``` section. The numbering for the WCF is different from all of the previous documents because the WCF is made of chapters with multiple sections.

The ```##``` for the WCF is a comma demilited list of ```:``` separated numbers ```ex. a:b``` where ```a``` is the chapter number and ```b``` is the section number. You can query a single chapter and section or multiples in a range. If you are querying sections intrachapter then you can give the chapter followed by a range for the section number. If you are querying interchapter then a definite start and end chapter and section number is required. I'll give a few examples to show the working queries.

```[WCF 1:2]``` - Chapter 1 section 2

```[WCF 3:4-5]``` - Chapter 3 sections 4 through 5

```[WCF 6:7-8:9]``` - Chapter 6 section 7 through chapter 8 section 9.

#### London Baptist Confession of Faith

```[optional{London (or L) Baptist (or B) Confession (or C) optional{of} Faith (or F)} 1689 ##]```

This works just like the WCF, spell the words out or just use the first letter followed by 1689. The numbering is all the same.

```[London Baptist Confession of Faith 1689 1:1]``` or ```[LBCF 1689 1:1]```

The lettering is completely optional, but the 1689 is required, so ```[1689 1:1]``` also works.

#### 39 Articles of Religion

```[39 Articles (or A) optional{of Religion (of R)} ##]```

By now I will assume you understand my notation and can figure out how to call this one. The numbering matches WLC,WSC, etc.

#### Canons of Dort

The format for this standard is not as easily broken up. So to make my life a little easier I have separated the articles and the rejections into 2 separate queries. They are as follows:

```[Canons (or C) optional{of} Dort (or D, or Dordt) Article (or A, or Articles) ##]```

```[Canons (or C) optional{of} Dort (or D, or Dordt) Rejection (or R, or Rejections) ##]```

The ```##``` matches the WCF and the LBCF.

### Planned supported documents
* London Baptist Confession of Faith 1646

### Triggering the bot
I have tried to make the syntax as flexible as I can. The syntax is case insensitive and you can also mix and match and the spaces don't matter. While ```[bconfessionoffaith1-2,3,4]``` and ```[   bElGiC  CoNfEsSiOn oF F 1 -2 , 3,  4  ]``` both work they aren't very pretty so should probably be avoided.

I only have the bot looking through comments not at the submission text. If you want to cite a document in a text post you will have to comment on the post with the relevant citations.

## Authors
[/u/Nokeo08](http://reddit.com/u/nokeo08)

## Thanks
[Matthieu Grieger](http://www.reddit.com/u/mgrieger) for [versebot](https://github.com/matthieugrieger/versebot), from which catebot was initially derived. And [/u/konohitowa](https://www.reddit.com/user/kono_hito_wa) for [catebot](https://github.com/konohitowa/catebot), off of which a significant portion of standardsbot is based.
