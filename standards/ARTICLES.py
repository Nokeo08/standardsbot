#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from utils.Parsers import one_to_one_parser


class ARTICLES:
    __doc = {
        1: ("I. OF FAITH IN THE HOLY TRINITY",
            "THERE is but one living and true God, ever- lasting, without "
            "body, parts, or passions; of infinite power, wisdom, and "
            "goodness; the Maker, and Preserver of all things both visible and"
            " invisible. And in unity of this Godhead there be three Persons, "
            "of one substance, power, and eternity; the Father, the Son, and "
            "the Holy Ghost."),
        2: ("II. OF THE WORD OR SON OF GOD, WHICH WAS MADE VERY MAN",
            "THE Son, which is the Word of the Father, begotten from "
            "everlasting of the Father, the very and eternal God, and of one "
            "substance with the Father, took Man's nature in the womb of the "
            "blessed Virgin, of her substance: so that two whole and perfect "
            "Natures, that is to say, the Godhead and Manhood, were joined "
            "together in one Person, never to be divided, whereof is one "
            "Christ, very God, and very Man; who truly suffered, was "
            "crucified, dead, and buried, to reconcile his Father to us, and "
            "to be a sacrifice, not only for original guilt, but also for all"
            " actual sins of men."),
        3: ("III. OF THE GOING DOWN OF CHRIST INTO HELL",
            "AS Christ died for us, and was buried, so also is it to be "
            "believed, that he went down into Hell."),
        4: ("IV. OF THE RESURRECTION OF CHRIST",
            "CHRIST did truly rise again from death, and took again his body, "
            "with flesh, bones, and all things appertaining to the perfection "
            "of Man's nature; wherewith he ascended into Heaven, and there "
            "sitteth, until he return to judge all Men at the last day."),
        5: ("V. OF THE HOLY GHOST",
            "THE Holy Ghost, proceeding from the Father and the Son, is of "
            "one substance, majesty, and glory, with the Father and the Son, "
            "very and eternal God."),
        6: ("VI. OF THE SUFFICIENCY OF THE HOLY SCRIPTURES FOR SALVATION",
            "Holy Scripture containeth all things necessary to salvation: so "
            "that whatsoever is not read therein, nor may be proved thereby, "
            "is not to be required of any man, that it should be believed as "
            "an article of the Faith, or be thought requisite or necessary to "
            "salvation. In the name of the Holy Scripture we do understand "
            "those canonical Books of the Old and New Testament, of whose "
            "authority was never any doubt in the Church.\n\n>**Of the Names and"
            " Number of the Canonical Books**\n\n>* Genesis\n* Exodus\n* "
            "Leviticus\n* Numbers\n* Deuteronomy\n* Joshua\n* Judges\n* "
            "Ruth\n* The First Book of Samuel\n* The Second Book of Samuel\n* "
            "The First Book of Kings\n* The Second Book of Kings\n* The First "
            "Book of Chronicles\n* The Second Book of Chronicles\n* The First "
            "Book of Esdras\n* The Second Book of Esdras\n* The Book of "
            "Esther\n* The Book of Job\n* The Psalms\n* The Proverbs\n* "
            "Ecclesiastes or Preacher\n* Cantica, or Songs of Solomon\n* Four "
            "Prophets the greater\n* Twelve Prophets the less\n\n>And the other"
            " Books (as Hierome saith) the Church doth read for example of "
            "life and instruction of manners; but yet doth it not apply them "
            "to establish any doctrine; such are these following:\n\n>* The "
            "Third Book of Esdras\n* The Fourth Book of Esdras\n* The Book of "
            "Tobias\n* The Book of Judith\n* The rest of the Book of Esther\n*"
            " The Book of Wisdom\n* Jesus the Son of Sirach\n* Baruch the "
            "Prophet\n* The Song of the Three Children\n* The Story of "
            "Susanna\n* Of Bel and the Dragon\n* The Prayer of Manasses\n* "
            "The First Book of Maccabees\n* The Second Book of Maccabees\n\n>"
            "All the Books of the New Testament, as they are commonly received"
            ", we do receive, and account them Canonical."),
        7: ("VII. OF THE OLD TESTAMENT",
            "THE Old Testament is not contrary to the New: for both in the Old"
            " and New Testament everlasting life is offered to Mankind by "
            "Christ, who is the only Mediator between God and Man, being both "
            "God and Man. Wherefore they are not to be heard, which feign that "
            "the old Fathers did look only for transitory promises. Although "
            "the Law given from God by Moses, as touching Ceremonies and "
            "Rites, do not bind Christian men, nor the Civil precepts "
            "thereof ought of necessity to be received in any commonwealth; "
            "yet notwithstanding, no Christian man whatsoever is free from the"
            " obedience of the Commandments which are called Moral."),
        8: ("VIII. OF THE THREE CREEDS",
            "THE Three Creeds, Nicene Creed, Athanasius's Creed, and that "
            "which is commonly called the Apostles' Creed, ought thoroughly "
            "to be received and believed: for they may be proved by most "
            "certain warrants of holy Scripture."),
        9: ("IX. OF ORIGINAL OR BIRTH-SIN",
            "ORIGINAL Sin standeth not in the following of Adam, (as the "
            "Pelagians do vainly talk;) but it is the fault and corruption of "
            "the Nature of every man, that naturally is ingendered of the "
            "offspring of Adam; whereby man is very far gone from original "
            "righteousness, and is of his own nature inclined to evil, so that "
            "the flesh lusteth always contrary to the spirit; and therefore in"
            " every person born into this world, it deserveth God's wrath and "
            "damnation. And this infection of nature doth remain, yea in them "
            "that are regenerated; whereby the lust of the flesh, called in the"
            " Greek, \"Phronema Sarkos\", which some do expound the wisdom, some"
            " sensuality, some the affection, some the desire, of the flesh, "
            "is not subject to the Law of God. And although there is no "
            "condemnation for them that believe and are baptized, yet the "
            "Apostle doth confess, that concupiscence and lust hath of itself "
            "the nature of sin."),
        10: ("X. OF FREE-WILL",
             "THE condition of Man after the fall of Adam is such, that he "
             "cannot turn and prepare himself, by his own natural strength and "
             "good works, to faith, and calling upon God: Wherefore we have no "
             "power to do good works pleasant and acceptable to God, without "
             "the grace of God by Christ preventing us, that we may have a good"
             " will, and working with us, when we have that good will."),
        11: ("XI. OF THE JUSTIFICATION OF MAN",
             "WE are accounted righteous before God, only for the merit of our "
             "Lord and Saviour Jesus Christ by Faith, and not for our own works"
             " or deservings: Wherefore, that we are justified by Faith only is"
             " a most wholesome Doctrine, and very full of comfort, as more "
             "largely is expressed in the Homily of Justification."),
        12: ("XII. OF GOOD WORKS",
             "ALBEIT that Good Works, which are the fruits of Faith, and follow"
             " after Justification, cannot put away our sins, and endure the "
             "severity of God's Judgement; yet are they pleasing and acceptable"
             " to God in Christ, and do spring out necessarily of a true and "
             "lively Faith; insomuch that by them a lively Faith may be as "
             "evidently known as a tree discerned by the fruit."),
        13: ("XIII. OF WORKS BEFORE JUSTIFICATION",
             "WORKS done before the grace of Christ, and the Inspiration of his"
             " Spirit, are not pleasant to God, forasmuch as they spring not of"
             " faith in Jesus Christ, neither do they make men meet to receive "
             "grace, or (as the School-authors say) deserve grace of congruity:"
             " yea rather, for that they are not done as God hath willed and "
             "commanded them to be done, we doubt not but they have the nature"
             " of sin."),
        14: ("XIV. OF WORKS OF SUPEREROGATION",
             "VOLUNTARY Works besides, over, and above, God's Commandments, "
             "which they call Works of Supererogation, cannot be taught "
             "without arrogancy and impiety: for by them men do declare, that "
             "they do not only render unto God as much as they are bound to do,"
             " but that they do more for his sake, than of bounden duty is "
             "required: whereas Christ saith plainly, When ye have done all "
             "that are commanded to you, say, We are unprofitable servants."),
        15: ("XV. OF CHRIST ALONE WITHOUT SIN",
             "CHRIST in the truth of our nature was made like unto us in all "
             "things, sin only except, from which he was clearly void, both in "
             "his flesh, and in his spirit. He came to be the Lamb without spot,"
             " who, by sacrifice of himself once made, should take away the "
             "sins of the world, and sin, as Saint John saith, was not in him. "
             "But all we the rest, although baptized, and born again in Christ,"
             " yet offend in many things; and if we say we have no sin, we "
             "deceive ourselves, and the truth is not in us."),
        16: ("XVI. OF SIN AFTER BAPTISM",
             "NOT every deadly sin willingly committed after Baptism is sin "
             "against the Holy Ghost, and unpardonable. Wherefore the grant of "
             "repentance is not to be denied to such as fall into sin after "
             "Baptism. After we have received the Holy Ghost, we may depart "
             "from grace given, and fall into sin, and by the grace of God we "
             "may arise again, and amend our lives. And therefore they are to "
             "be condemned, which say, they can no more sin as long as they "
             "live here, or deny the place of forgiveness to such as truly "
             "repent."),
        17: ("XVII. OF PREDESTINATION AND ELECTION",
             "PREDESTINATION to Life is the everlasting purpose of God, whereby"
             " (before the foundations of the world were laid) he hath "
             "constantly decreed by his counsel secret to us, to deliver from "
             "curse and damnation those whom he hath chosen in Christ out of "
             "mankind, and to bring them by Christ to everlasting salvation, as"
             " vessels made to honour. Wherefore, they which be endued with so "
             "excellent a benefit of God be called according to God's purpose "
             "by his Spirit working in due season: they through Grace obey the "
             "calling: they be justified freely: they be made sons of God by "
             "adoption: they be made like the image of his only-begotten Son "
             "Jesus Christ: they walk religiously in good works, and at "
             "length, by God's mercy, they attain to everlasting felicity.\n\n>As"
             " the godly consideration of Predestination, and our Election in "
             "Christ, is full of sweet, pleasant, and unspeakable comfort to "
             "godly persons, and such as feel in themselves the working of the"
             " Spirit of Christ, mortifying the works of the flesh, and their "
             "earthly members, and drawing up their mind to high and heavenly "
             "things, as well because it doth greatly establish and confirm "
             "their faith of eternal Salvation to be enjoyed through Christ, "
             "as because it doth fervently kindle their love towards God: So, "
             "for curious and carnal persons, lacking the Spirit of Christ, to "
             "have continually before their eyes the sentence of God's "
             "Predestination, is a most dangerous downfal, whereby the Devil "
             "doth thrust them either into desperation, or into wretchlessness "
             "of most unclean living, no less perilous than desperation.\n\n>"
             "Furthermore, we must receive God's promises in such wise, as they"
             " be generally set forth to us in holy Scripture: and, in our "
             "doings, that Will of God is to be followed, which we have "
             "expressly declared unto us in the Word of God."),
        18: ("XVIII. OF OBTAINING ETERNAL SALVATION ONLY BY THE NAME OF CHRIST",
             "THEY also are to be had accursed that presume to say, That every "
             "man shall be saved by the Law or Sect which he professeth, so "
             "that he be diligent to frame his life according to that Law, and "
             "the light of Nature. For holy Scripture doth set out unto us only "
             "the Name of Jesus Christ, whereby men must be saved."),
        19: ("XIX. OF THE CHURCH",
             "THE visible Church of Christ is a congregation of faithful men, "
             "in the which the pure Word of God is preached, and the Sacraments"
             " be duly ministered according to Christ's ordinance in all those "
             "things that of necessity are requisite to the same.\n\n>As the "
             "Church of Jerusalem, Alexandria, and Antioch, have erred; so also"
             " the Church of Rome hath erred, not only in their living and "
             "manner of Ceremonies, but also in matters of Faith."),
        20: ("XX. OF THE AUTHORITY OF THE CHURCH",
             "THE Church hath power to decree Rites or Ceremonies, and "
             "authority in Controversies of Faith: And yet it is not lawful for"
             " the Church to ordain any thing that is contrary to God's Word "
             "written, neither may it so expound one place of Scripture, that it"
             " be repugnant to another. Wherefore, although the Church be a "
             "witness and a keeper of holy Writ, yet, as it ought not to decree"
             " any thing against the same, so besides the same ought it not to "
             "enforce any thing to be believed for necessity of Salvation."),
        21: ("XXI. OF THE AUTHORITY OF GENERAL COUNCILS",
             "GENERAL Councils may not be gathered together without the "
             "commandment and will of Princes. And when they be gathered "
             "together, (forasmuch as they be an assembly of men, whereof all "
             "be not governed with the Spirit and Word of God,) they may err, "
             "and sometimes have erred, even in things pertaining unto God. "
             "Wherefore things ordained by them as necessary to salvation have "
             "neither strength nor authority, unless it may be declared that "
             "they be taken out of holy Scripture."),
        22: ("XXII. OF PURGATORY",
             "THE Romish Doctrine concerning Purgatory, Pardons, Worshipping, "
             "and Adoration, as well of Images as of Reliques, and also "
             "invocation of Saints, is a fond thing vainly invented, and "
             "grounded upon no warranty of Scripture, but rather repugnant to "
             "the Word of God."),
        23: ("XXIII. OF MINISTERING IN THE CONGREGATION",
             "IT is not lawful for any man to take upon him the office of "
             "publick preaching, or ministering the Sacraments in the "
             "Congregation, before he be lawfully called, and sent to execute "
             "the same.\n\n>And those we ought to judge lawfully called and sent,"
             " which be chosen and called to this work by men who have publick"
             " authority given unto them in the Congregation, to call and send "
             "Ministers into the Lord's vineyard."),
        24: ("XXIV. OF SPEAKING IN THE CONGREGATION IN SUCH A TONGUE AS THE "
             "PEOPLE UNDERSTANDETH",
             "IT is a thing plainly repugnant to the Word of God, and the "
             "custom of the Primitive Church, to have publick Prayer in the "
             "Church, or to minister the Sacraments in a tongue not "
             "understanded of the people."),
        25: ("XXV. OF THE SACRAMENTS",
             "SACRAMENTS ordained of Christ be not only badges or tokens of "
             "Christian men's profession, but rather they be certain sure "
             "witnesses, and effectual signs of grace, and God's good will "
             "towards us, by the which he doth work invisibly in us, and doth "
             "not only quicken, but also strengthen and confirm our Faith in "
             "him.\n\n>There are two Sacraments ordained of Christ our Lord in "
             "the Gospel, that is to say, Baptism, and the Supper of the Lord."
             "\n\n>Those five commonly called Sacraments, that is to say, "
             "Confirmation, Penance, Orders, Matrimony, and extreme Unction, "
             "are not to be counted for Sacraments of the Gospel, being such "
             "as have grown partly of the corrupt following of the Apostles, "
             "partly are states of life allowed in the Scriptures; but yet have"
             " not like nature of Sacraments with Baptism, and the Lord's "
             "Supper, for that they have not any visible sign or ceremony "
             "ordained of God.\n\n>The Sacraments were not ordained of Christ "
             "to be gazed upon, or to be carried about, but that we should duly"
             " use them. And in such only as worthily receive the same they have"
             " a wholesome effect or operation: but they that receive them "
             "unworthily purchase to themselves damnation, as "
             "Saint Paul saith."),
        26: ("XXVI. OF THE UNWORTHINESS OF THE MINISTERS, WHICH HINDERS NOT "
             "THE EFFECT OF THE SACRAMENT",
             "ALTHOUGH in the visible Church the evil be ever mingled with the "
             "good, and sometimes the evil have chief authority in the "
             "Ministration of the Word and Sacraments, yet forasmuch as they do "
             "not the same in their own name, but in Christ's, and do minister "
             "by his commission and authority, we may use their Ministry, both "
             "in hearing the Word of God, and in receiving of the Sacraments. "
             "Neither is the effect of Christ's ordinance taken away by their "
             "wickedness, nor the grace of God's gifts diminished from such as "
             "by faith and rightly do receive the Sacraments ministered unto "
             "them; which be effectual, because of Christ's institution and "
             "promise, although they be ministered by evil men.\n\n>Nevertheless"
             ", it appertaineth to the discipline of the Church, that inquiry "
             "be made of evil Ministers, and that they be accused by those that"
             " have knowledge of their offences; and finally being found "
             "guilty, by just judgement be deposed."),
        27: ("XXVII. OF BAPTISM",
             "BAPTISM is not only a sign of profession, and mark of difference,"
             " whereby Christian men are discerned from others that be not "
             "christened, but it is also a sign of Regeneration or new Birth, "
             "whereby, as by an instrument, they that receive Baptism rightly"
             " are grafted into the Church; the promises of forgiveness of sin,"
             " and of our adoption to be the sons of God by the Holy Ghost, are"
             " visibly signed and sealed; Faith is confirmed, and Grace "
             "increased by virtue of prayer unto God. The Baptism of young "
             "Children is in any wise to be retained in the Church, as most "
             "agreeable with the institution of Christ."),
        28: ("XXVIII. OF THE LORD'S SUPPER",
             "THE Supper of the Lord is not only a sign of the love that "
             "Christians ought to have among themselves one to another; but "
             "rather is a Sacrament of our Redemption by Christ's death: "
             "insomuch that to such as rightly, worthily, and with faith, "
             "receive the same, the Bread which we break is a partaking of the "
             "Body of Christ; and likewise the Cup of Blessing is a partaking "
             "of the Blood of Christ.\n\n>Transubstantiation (or the change of "
             "the substance of Bread and Wine) in the Supper of the Lord, cannot"
             " be proved by holy Writ; but is repugnant to the plain words of "
             "Scripture, overthroweth the nature of a Sacrament, and hath given"
             " occasion to many superstitions.\n\n>The Body of Christ is given, "
             "taken, and eaten, in the Supper, only after an heavenly and "
             "spiritual manner. And the mean whereby the Body of Christ is "
             "received and eaten in the Supper is Faith.\n\n>The Sacrament of "
             "the Lord's Supper was not by Christ's ordinance reserved, carried"
             " about, lifted up, or worshipped."),
        29: ("XXIX. OF THE WICKED WHICH EAT NOT THE BODY OF CHRIST IN THE USE"
             " OF THE LORD'S SUPPER",
             "THE Wicked, and such as be void of a lively faith, although they"
             " do carnally and visibly press with their teeth (as Saint "
             "Augustine saith) the Sacrament of the Body and Blood of Christ, "
             "yet in no wise are they partakers of Christ: but rather, to their"
             " condemnation, do eat and drink the sign or Sacrament of so great"
             " a thing."),
        30: ("XXX. OF BOTH KINDS",
             "THE Cup of the Lord is not to be denied to the Lay-people: for "
             "both the parts of the Lord's Sacrament, by Christ's ordinance and"
             " commandment, ought to be ministered to all Christian men alike."),
        31: ("XXXI. OF THE ONE OBLATION OF CHRIST FINISHED UPON THE CROSS",
             "THE Offering of Christ once made is that perfect redemption, "
             "propitiation, and satisfaction, for all the sins of the whole "
             "world, both original and actual; and there is none other "
             "satisfaction for sin, but that alone. Wherefore the sacrifices of"
             " Masses, in the which it was commonly said, that the Priest did "
             "offer Christ for the quick and the dead, to have remission of "
             "pain or guilt, were blasphemous fables, and dangerous deceits."),
        32: ("XXXII. OF THE MARRIAGE OF PRIESTS",
             "BISHOPS, Priests, and Deacons, are not commanded by God's Law, "
             "either to vow the estate of single life, or to abstain from "
             "marriage: therefore it is lawful for them, as for all other "
             "Christian men, to marry at their own discretion, as they shall "
             "judge the same to serve better to godliness."),
        33: ("XXXIII. OF EXCOMMUNICATE PERSONS, HOW THEY ARE TO BE AVOIDED",
             "THAT person which by open denunciation of the Church is rightly "
             "cut off from the unity of the Church, and excommunicated, ought "
             "to be taken of the whole multitude of the faithful, as an Heathen"
             " and Publican, until he be openly reconciled by penance, and "
             "received into the Church by a Judge that hath authority"
             " thereunto."),
        34: ("XXXIV. OF THE TRADITIONS OF THE CHURCH",
             "IT is not necessary that Traditions and Ceremonies be in all "
             "places one, and utterly like; for at all times they have been "
             "divers, and may be changed according to the diversities of "
             "countries, times, and men's manners, so that nothing be ordained"
             " against God's Word. Whosoever through his private judgement, "
             "willingly and purposely, doth openly break the traditions and "
             "ceremonies of the Church, which be not repugnant to the Word of "
             "God, and be ordained and approved by common authority, ought to be"
             " rebuked openly, (that others may fear to do the like,) as he that"
             " offendeth against the common order of the Church, and hurteth the"
             " authority of the Magistrate, and woundeth the consciences of the"
             " weak brethren.\n\n>Every particular or national Church hath "
             "authority to ordain, change, and abolish, ceremonies or rites of "
             "the Church ordained only by man's authority, so that all things "
             "be done to edifying."),
        35: ("XXXV. OF THE HOMILIES",
             "THE second Book of Homilies, the several titles whereof we have "
             "joined under this Article, doth contain a godly and wholesome "
             "Doctrine, and necessary for these times, as doth the former Book "
             "of Homilies, which were set forth in the time of Edward the "
             "Sixth; and therefore we judge them to be read in Churches by the "
             "Ministers, diligently and distinctly, that they may be "
             "understanded of the people.\n\n>Of the Names of the Homilies\n\n>1."
             " Of the right Use of the Church.\n2. Against peril of Idolatry."
             "\n3. Of repairing and keeping clean of Churches.\n4. Of good "
             "Works: first of Fasting.\n5. Against Gluttony and Drunkenness.\n"
             "6. Against Excess of Apparel.\n7. Of Prayer.\n8. Of the Place and"
             " Time of Prayer.\n9. That Common Prayers and Sacraments ought to "
             "be ministered in a known tongue.\n10. Of the reverend estimation "
             "of God's Word.\n11. Of Alms-doing.\n12. Of the Nativity of "
             "Christ.\n13. Of the Passion of Christ.\n14. Of the Resurrection "
             "of Christ.\n15. Of the worthy receiving of the Sacrament of the "
             "Body and Blood of Christ.\n16. Of the Gifts of the Holy Ghost.\n"
             "17. For the Rogation-days.\n18. Of the State of Matrimony.\n19. "
             "Of Repentance.\n20. Against Idleness.\n21. Against Rebellion."),
        36: ("XXXVI. OF CONSECRATION OF BISHOPS AND MINISTERS",
             "THE Book of Consecration of Archbishops and Bishops, and Ordering"
             " of Priests and Deacons, lately set forth in the time of Edward "
             "the Sixth, and confirmed at the same time by authority of "
             "Parliament, doth contain all things necessary to such "
             "Consecration and Ordering: neither hath it any thing, that of "
             "itself is superstitious and ungodly. And therefore whosoever are"
             " consecrated or ordered according to the Rites of that Book, "
             "since the second year of the forenamed King Edward unto this "
             "time, or hereafter shall be consecrated or ordered according to "
             "the same Rites; we decree all such to be rightly, orderly, and "
             "lawfully consecrated and ordered."),
        37: ("XXXVII. OF THE CIVIL MAGISTRATES",
             "THE King's Majesty hath the chief power in this Realm of England,"
             " and other his Dominions, unto whom the chief Government of all "
             "Estates of this Realm, whether they be Ecclesiastical or Civil, "
             "in all causes doth appertain, and is not, nor ought to be, "
             "subject to any foreign Jurisdiction.\n\n>Where we attribute to the"
             " King's Majesty the chief government, by which Titles we "
             "understand the minds of some slanderous folks to be offended; we "
             "give not to our Princes the ministering either of God's Word, or "
             "of the Sacraments, the which thing the Injunctions also lately "
             "set forth by Elizabeth our Queen do most plainly testify; but "
             "that only prerogative, which we see to have been given always to "
             "all godly\n\n>Princes in holy Scriptures by God himself; that is, "
             "that they should rule all estates and degrees committed to their "
             "charge by God, whether they be Ecclesiastical or Temporal, and "
             "restrain with the civil sword the stubborn and evil-doers.\n\n>The"
             " Bishop of Rome hath no jurisdiction in this Realm of England."
             "\n\n>The Laws of the Realm may punish Christian men with death, "
             "for heinous and grievous offences.\n\n>It is lawful for Christian "
             "men, at the commandment of the Magistrate, to wear weapons, and "
             "serve in the wars."),
        38: ("XXXVIII. OF CHRISTIAN MEN'S GOODS, WHICH ARE NOT COMMON",
             "THE Riches and Goods of Christians are not common, as touching "
             "the right, title, and possession of the same, as certain "
             "Anabaptists do falsely boast. Notwithstanding, every man ought, "
             "of such things as he possesseth, liberally to give alms to the "
             "poor, according to his ability."),
        39: ("XXXIX. OF A CHRISTIAN MAN'S OATH",
             "AS we confess that vain and rash Swearing is forbidden Christian "
             "men by our Lord Jesus Christ, and James his Apostle, so we judge,"
             " that Christian Religion doth not prohibit, but that a man may "
             "swear when the Magistrate requireth, in a cause of faith and "
             "charity, so it be done according to the Prophet's teaching, in "
             "justice, judgement, and truth.")
    }

    __articlesRegex = r"\[\s*39\s*(?:A|Articles)\s*(?:of\s*(?:R|Religion))?\s*([\d\-,\s]+)\s*\]"

    def __init__(self):
        self.__parse = one_to_one_parser

    def __get_text(self, i, j):
        if 0 < i <= j <= 39:
            if i == j:
                return "\n>**Article " + self.__doc[i][0] + "**\n\n>" + self.__doc[i][1] + "\n", False
            if i < j:
                result = ''
                for pos in range(i, j + 1):
                    result += "\n>**Article " + self.__doc[pos][0] + "**\n\n>" + self.__doc[pos][1] + "\n"
                return result, False
            else:
                return '', True
        else:
            return '', True

    def fetch(self, full_citations):
        response_text = ''
        response_citation = ''
        response_is_malformed = False

        if full_citations:
            articles_citations = re.findall(self.__articlesRegex, full_citations, re.IGNORECASE)
            if articles_citations:
                response_citation = '[39 Articles of Religion '
                args, response_is_malformed = self.__parse(articles_citations)
                for i in args:
                    response_citation += str(i[0]) + '-' + str(i[1]) + ", "
                    quote, temp = self.__get_text(i[0], i[1])
                    response_is_malformed |= temp
                    if response_text:
                        response_text += quote
                    elif quote:
                        response_text += "\n**39 Articles**\n" + quote
                response_citation = response_citation[:-2] + "]"
        return response_text, response_citation, response_is_malformed
