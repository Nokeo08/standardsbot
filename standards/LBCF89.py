#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from utils.Parsers import chapter_paragraph_parser


class LBCF89:
    __CHPTRMAX = {
        1: 10,
        2: 3,
        3: 7,
        4: 3,
        5: 7,
        6: 5,
        7: 3,
        8: 10,
        9: 5,
        10: 4,
        11: 6,
        12: 1,
        13: 3,
        14: 3,
        15: 5,
        16: 7,
        17: 3,
        18: 4,
        19: 7,
        20: 4,
        21: 3,
        22: 8,
        23: 5,
        24: 3,
        25: 4,
        26: 15,
        27: 2,
        28: 2,
        29: 4,
        30: 8,
        31: 3,
        32: 3}

    __text = {
        1: {
            0: "Chapter I. Of the Holy Scriptures",
            1: ("The Holy Scripture is the only sufficient, certain, and infallible rule of all saving Knowledge, "
                "Faith and Obedience; Although the light of Nature, and the works of Creation and Providence do so "
                "far manifest the goodness, wisdom and power of God, as to leave men unexcusable; yet are they not "
                "sufficient to give that knowledge of God and His will, which is necessary unto Salvation. Therefore "
                "it pleased the Lord at sundry times, and in divers manners, to reveal himself, and to declare that "
                "His will unto his Church; and afterward for the better preserving, and propagating of the Truth, and "
                "for the more sure Establishment, and Comfort of the Church against the corruption of the flesh, and "
                "the malice of Satan, and of the World, to commit the same wholly unto writing; which maketh the Holy "
                "Scriptures to be most necessary, those former ways of Gods revealing his will unto his people "
                "being now ceased."),
            2: ("Under the Name of Holy Scripture or the Word of God written; are now contained all the Books of the "
                "Old and New Testament which are these: Of the Old Testament: Genesis, Exodus, Leviticus, Numbers, "
                "Deuteronomy, Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings, 1 Chronicles, 2 Chronicles, "
                "Ezra, Nehemiah, Esther, Job, Psalms, Proverbs, Ecclesiastes, The Song of Songs, Isaiah, Jeremiah, "
                "Lamentations, Ezekiel, Daniel, Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, "
                "Haggai, Zechariah, Malachi. Of the New Testament: Matthew, Mark, Luke, John, The Acts of the "
                "Apostles, Pauls Epistle to the Romans, 1 Corinthians, 2 Corinthians, Galatians, Ephesians, "
                "Phillippians, Colossians, 1 Thessalonians, 2 Thessalonians, 1 Timothy, 2 Timothy, to Titus, "
                "to Philemon, the Epistle to the Hebrews, the Epistle of James, the First and Second Epistles of "
                "Peter, the First, Second and Third Epistles of John, the Epistle of Jude, the Revelation."),
            3: ("The Books commonly called Apocrypha not being of Divine inspiration, are no part of the Canon (or "
                "rule) of the Scripture, and therefore are of no authority to the Church of God, nor to be any "
                "otherwise approved or made use of, then other humane writings."),
            4: ("The Authority of the Holy Scripture for which it ought to be believed dependeth not upon the "
                "testimony of any man, or Church; but wholly upon God (who is truth it self) the Author thereof; "
                "therefore it is to be received, because it is the Word of God."),
            5: ("We may be moved and induced by the testimony of the Church of God, to an high and reverent esteem of "
                "the Holy Scriptures; and the heavenliness of the matter, the efficacy of the Doctrine, "
                "and the Majesty of the stile, the consent of all the parts, the scope of the whole (which is to give "
                "all glory to God) the full discovery it makes of the only way of mans salvation, and many other "
                "incomparable Excellencies, and intire perfections thereof, are arguments whereby it doth abundantly "
                "evidence it self to be the Word of God; yet notwithstanding; our full perswasion, and assurance of "
                "the infallible truth, and divine authority thereof, is from the inward work of the Holy Spirit, "
                "bearing witness by and with the Word in our Hearts."),
            6: ("The whole Councel of God concerning all things necessary for his own Glory, Mans Salvation, "
                "Faith and Life, is either expressely set down or necessarily contained in the Holy Scripture; unto "
                "which nothing at any time is to be added, whether by new Revelation of the Spirit, or traditions of "
                "men.Nevertheless we acknowledge the inward illumination of the Spirit of God, to be necessary for "
                "the saving understanding of such things as are revealed in the Word, and that there are some "
                "circumstances concerning the worship of God, and government of the Church common to humane actions "
                "and societies; which are to be ordered by the light of nature, and Christian prudence according to "
                "the general rules of the Word, which are always to be observed."),
            7: ("All things in Scripture are not alike plain in themselves, nor alike clear unto all; yet those "
                "things which are necessary to be known, believed, and observed for Salvation, are so clearly "
                "propounded, and opened in some place of Scripture or other, that not only the learned, "
                "but the unlearned, in a due use of ordinary means, may attain to a sufficient understanding of "
                "them."),
            8: ("The Old Testament in Hebrew, (which was the Native language of the people of God of old) and the New "
                "Testament in Greek (which at the time of the writing of it was most generally known to the Nations "
                "being immediately inspired by God, and by his singular care and Providence kept pure in all Ages, "
                "are therefore authentical; so as in all controversies of Religion the Church is finally to appeal "
                "unto them But because these original tongues are not known to all the people of God, who have a "
                "right unto, and interest in the Scriptures, and are commanded in the fear of God to read and search "
                "them, therefore they are to be translated into the vulgar language of every Nation, unto which they "
                "come, that the Word of God dwelling plentifully in all, they may worship him in an acceptable "
                "manner, and through patience and comfort of the Scriptures may have hope."),
            9: ("The infallible rule of interpretation of Scripture is the Scripture it self: And therefore when "
                "there is a question about the true and full sense of any Scripture (which is not manifold but one) "
                "it must be searched by other places that speak more clearly."),
            10: ("The supream judge by which all controversies of Religion are to be determined, and all Decrees of "
                 "Councels, opinions of antient Writers, Doctrines of men, and private Spirits, are to be examined, "
                 "and in whose sentence we are to rest, can be no other but the Holy Scripture delivered by the "
                 "Spirit, into which Scripture so delivered, our faith is finally resolved.")},
        2: {
            0: "Chapter II. Of God and of the Holy Trinity",
            1: ("The Lord our God is but one only living, and true God; whose subsistence is in and of himself, "
                "infinite in being, and perfection, whose Essence cannot be comprehended by any but himself; a most "
                "pure spirit, invisible, without body, parts, or passions, who only hath immortality, dwelling in the "
                "light, which no man can approach unto, who is immutable, immense, eternal, incomprehensible, "
                "Almighty, every way infinit, most holy, most wise, most free, most absolute, working all things "
                "according to the councel of his own immutable, and most righteous will, for his own glory, "
                "most loving, gracious, merciful, long suffering, abundant in goodness and truth, forgiving iniquity, "
                "transgression and sin, the rewarder of them that diligently seek him, and withall most just, "
                "and terrible in his judgements, hating all sin, and who will by no means clear the guilty."),
            2: ("God having all life, glory, goodness, blessedness, in and of himself: is alone in, and unto himself "
                "all-sufficient, not standing in need of any Creature which he hath made, nor deriving any glory from "
                "them, but onely manifesting his own glory in, by, unto, and upon them, he is the alone fountain of "
                "all Being, of whom, through whom, and to whom are all things, and he hath most soveraign dominion "
                "over all creatures, to do by them, for them, or upon them, whatsoever himself pleaseth; in his sight "
                "all things are open and manifest, his knowledge is infinite, infallible, and independant upon the "
                "Creature, so as nothing is to him contingent, or uncertain; he is most holy in all his Councels, "
                "in all his Works, and in all his Commands; to him is due from Angels and men, whatsoever worship, "
                "service, or obedience as Creatures they owe unto the Creator, and whatever he is further pleased to "
                "require of them."),
            3: ("In this divine and infinite Being there are three subsistences, the Father the Word (or Son) and "
                "Holy Spirit, of one substance, power, and Eternity, each having the whole Divine Essence, "
                "yet the Essence undivided, the Father is of none neither begotten nor proceeding, the Son is "
                "Eternally begotten of the Father, the holy Spirit proceeding from the Father and the Son, "
                "all infinite, without beginning, therefore but one God, who is not to be divided in nature and "
                "Being; but distinguished by several peculiar, relative properties, and personal relations; which "
                "doctrine of the Trinity is the foundation of all our Communion with God, and comfortable dependance "
                "on him.")},
        3: {
            0: "Chapter III. Of God's Decree",
            1: ("God hath Decreed in himself from all Eternity, by the most wise and holy Councel of his own will, "
                "freely and unchangeably, all things whatsoever comes to passe; yet so as thereby is God neither the "
                "author of sin, nor hath fellowship with any therein, nor is violence offered to the will of the "
                "Creature, nor yet is the liberty, or contingency of second causes taken away, but rather "
                "established, in which appears his wisdom in disposing all things, and power, and faithfulness in "
                "accomplishing his Decree."),
            2: ("Although God knoweth whatsoever may, or can come to passe upon all supposed conditions; yet hath he "
                "not Decreed anything, because he foresaw it as future, or as that which would come to pass upon such "
                "conditions."),
            3: ("By the decree of God for the manifestation of his glory some men and Angels, are predestinated, "
                "or fore-ordained to Eternal Life, through Jesus Christ to the praise of his glorious grace; others "
                "being left to act in their sin to their just condemnation, to the praise of his glorious justice."),
            4: ("These Angels and Men thus predestinated, and fore-ordained, are particularly, and unchangeably "
                "designed; and their number so certain, and definite, that it cannot be either increased, "
                "or diminished."),
            5: ("Those of mankind that are predestinated to life, God before the foundation of the world was laid, "
                "according to his eternal and immutable purpose, and the secret Councel and good pleasure of his "
                "will, hath chosen in Christ unto everlasting glory, out of his meer free grace and love; without any "
                "other thing in the creature as a condition or cause moving him thereunto."),
            6: ("As God hath appointed the Elect unto glory, so he hath by the eternal and most free purpose of his "
                "will, fore-ordained all the means thereunto, wherefore they who are elected, being faln in Adam, "
                "are redeemed by Christ, are effectually called unto faith in Christ, by his spirit working in due "
                "season, are justifyed, adopted, sanctified, and kept by his power through faith unto salvation; "
                "neither are any other redeemed by Christ, or effectually called, justified, adopted, sanctified, "
                "and saved, but the Elect only."),
            7: ("The Doctrine of this high mystery of predestination, is to be handled with special prudence, "
                "and care; that men attending the will of God revealed in his word, and yeilding obedience thereunto, "
                "may from the certainty of their effectual vocation, be assured of their eternal election; so shall "
                "this doctrine afford matter of praise, reverence, and admiration of God, and of humility, diligence, "
                "and abundant consolation, to all that sincerely obey the Gospel.")},
        4: {
            0: "Chapter IV. Of Creation",
            1: ("In the beginning it pleased God the Father, Son, and Holy Spirit, for the manifestation of the glory "
                "of his eternal power, wisdom, and goodness, to Create or make the world, and all things therein, "
                "whether visible or invisible, in the space of six days, and all very good."),
            2: ("After God had made all other Creatures, he Created man, male and female, with reasonable and "
                "immortal souls, rendring them fit unto that life to God; for which they were Created; being made "
                "after the image of God, in knowledge, righteousness, and true holyness; having the Law of God "
                "written in their hearts, and power to fulfill it; and yet under a possibility of transgressing, "
                "being left to the liberty of their own will, which was subject to change."),
            3: ("Besides the Law written in their hearts, they received a command not to eat of the tree of knowledge "
                "of good and evil; which whilst they kept, they were happy in their Communion with God, "
                "and had dominion over the Creatures.")},
        5: {
            0: "Chapter V. Of Divine Providence",
            1: ("God the good Creator of all things, in his infinite power, and wisdom, doth uphold, direct, dispose, "
                "and govern all Creatures, and things, from the greatest even to the least, by his most wise and holy "
                "providence, to the end for the which they were Created; according unto his infallible foreknowledge, "
                "and the free and immutable Councel of his own will; to the praise of the glory of his wisdom, power, "
                "justice, infinite goodness and mercy."),
            2: ("Although in relation to the foreknowledge and Decree of God, the first cause, all things come to "
                "pass immutably and infallibly; so that there is not any thing, befalls any by chance, or without his "
                "Providence; yet by the same Providence he ordereth them to fall out, according to the nature of "
                "second causes, either necessarily, freely, or contingently."),
            3: ("God in his ordinary Providence maketh use of means; yet is free to work, without, above, and against "
                "them at his pleasure."),
            4: ("The Almighty power, unsearchable wisdom, and infinite goodness of God, so far manifest themselves in "
                "his Providence, that his determinate Councel extendeth it self even to the first fall, and all other "
                "sinful actions both of Angels, and Men; (and that not by a bare permission) which also he most "
                "wisely and powerfully boundeth, and otherwise ordereth, and governeth, in a manifold dispensation to "
                "his most holy ends: yet so, as the sinfulness of their acts proceedeth only from the Creatures, "
                "and not from God; who being most holy and righteous, neither is nor can be, the author or approver "
                "of sin."),
            5: ("The most wise, righteous, and gracious God, doth oftentimes, leave for a season his own children to "
                "manifold temptations, and the corruptions of their own heart, to chastise them for their former "
                "sins, or to discover unto them the hidden strength of corruption, and deceitfulness of their hearts, "
                "that they may be humbled; and to raise them to a more close, and constant dependence for their "
                "support, upon himself; and to make them more watchful against all future occasions of sin, "
                "and for other just and holy ends."),
            6: ("As for those wicked and ungodly men, whom God as a righteous judge, for former sin doth blind and "
                "harden; from them he not only withholdeth his Grace, whereby they might have been inlightned in "
                "their understanding, and wrought upon in their hearts: But sometimes also withdraweth the gifts "
                "which they had, and exposeth them to such objects as their corruptions makes occasion of sin; and "
                "withall gives them over to their own lusts, the temptations of the world, and the power of Satan, "
                "whereby it comes to pass, that they harden themselves, even under those means which God useth for "
                "the softning of others."),
            7: ("As the Providence of God doth in general reach to all Creatures, so after a most special manner it "
                "taketh care of his Church, and disposeth of all things to the good thereof.")},
        6: {
            0: "Chapter VI. Of the Fall of Man, of Sin, and of the Punishment thereof",
            1: "Although God created Man upright, and perfect, and gave him a righteous law, which had been unto life "
               "had he kept it, and threatned death upon the breach thereof; yet he did not long abide in this "
               "honour; Satan using the subtilty of the serpent to seduce Eve, then by her seducing Adam, who without "
               "any compulsion, did wilfully transgress the Law of their Creation, and the command given unto them, "
               "in eating the forbidden fruit; which God was pleased according to his wise and holy Councel to "
               "permit, having purposed to order it, to his own glory.",
            2: "Our first Parents by this Sin, fell from their original righteousness and communion with God, "
               "and we in them, whereby death came upon all; all becoming dead in Sin, and wholly defiled, "
               "in all the faculties, and parts, of soul, and body.",
            3: "They being the root, and by Gods appointment, standing in the room, and stead of all mankind; the "
               "guilt of the Sin was imputed, and corrupted nature conveyed, to all their posterity descending from "
               "them by ordinary generation, being now conceived in Sin, and by nature children of wrath, "
               "the servants of Sin, the subjects of death and all other miseries, spiritual, temporal and eternal, "
               "unless the Lord Jesus set them free.",
            4: "From this original corruption, whereby we are utterly indisposed, disabled, and made opposite to all "
               "good, and wholly inclined to all evil, do proceed all actual transgressions.",
            5: "The corruption of nature, during this Life, doth remain in those that are regenerated: and although "
               "it be through Christ pardoned, and mortified, yet both it self, and the first motions thereof, "
               "are truely and properly Sin."},
        7: {
            0: "Chapter VII. Of God's Covenant",
            1: "The distance between God and the Creature is so great, that although reasonable Creatures do owe "
               "obedience unto him as their Creator, yet they could never have attained the reward of Life, "
               "but by some voluntary condescension on Gods part, which he hath been pleased to express, "
               "by way of Covenant.",
            2: "Moreover Man having brought himself under the curse of the Law by his fall, it pleased the Lord to "
               "make a Covenant of Grace wherein he freely offereth unto Sinners, Life and Salvation by Jesus Christ, "
               "requiring of them Faith in him, that they may be saved; and promising to give unto all those that are "
               "ordained unto eternal Life, his holy Spirit, to make them willing, and able to believe.",
            3: "This Covenant is revealed in the Gospel; first of all to Adam in the promise of Salvation by the seed "
               "of the woman, and afterwards by farther steps, untill the full discovery thereof was compleated in "
               "the new Testament; and it is founded in that Eternal Covenant transaction, that was between the "
               "Father and the Son, about the Redemption of the Elect; and it is alone by the Grace of this Covenant, "
               "that all of the posterity of fallen Adam, that ever were saved, did obtain life and a blessed "
               "immortality; Man being now utterly uncapable of acceptance with God upon those terms, on which Adam "
               "stood in his state of innocency."},
        8: {
            0: "Chapter VIII. Of Christ the Mediator",
            1: "It pleased God in his eternal purpose, to chuse and ordain the Lord Jesus his only begotten Son, "
               "according to the Covenant made between them both, to be the Mediator between God and Man; the "
               "Prophet, Priest and King; Head and Saviour of his Church, the heir of all things, and judge of the "
               "world: Unto whom he did from all Eternity give a people to be his seed, and to be by him in time "
               "redeemed, called, justified, sanctified, and glorified.",
            2: "The Son of God, the second Person in the Holy Trinity, being very and eternal God, the brightness of "
               "the Fathers glory, of one substance and equal with him: who made the World, who upholdeth and "
               "governeth all things he hath made: did when the fullness of time was come take unto him mans nature, "
               "with all the Essential properties, and common infirmities thereof, yet without sin: being conceived "
               "by the Holy Spirit in the Womb of the Virgin Mary, the Holy Spirit coming down upon her, "
               "and the power of the most High overshadowing her, and so was made of a Woman, of the Tribe of Judah, "
               "of the Seed of Abraham, and David according to the Scriptures: So that two whole, perfect, "
               "and distinct natures, were inseparably joined together in one Person: without conversion, "
               "composition, or confusion: which Person is very God, and very Man; yet one Christ, the only Mediator "
               "between God and Man.",
            3: "The Lord Jesus in his humane nature thus united to the divine, in the Person of the Son, "
               "was sanctified, and anointed with the Holy Spirit, above measure; having in him all the treasures of "
               "wisdom and knowledge; in whom it pleased the Father that all fullness should dwell: To the end that "
               "being holy, harmless, undefiled, and full of Grace, and Truth, he might be throughly furnished to "
               "execute the office of a Mediator, and Surety; which office he took not upon himself, "
               "but was thereunto called by his Father; who also put all power and judgement in his hand, "
               "and gave him Commandement to execute the same.",
            4: "This office the Lord Jesus did most willingly undertake, which that he might discharge he was made "
               "under the Law, and did perfectly fulfill it, and underwent the punishment due to us, which we should "
               "have born and suffered, being made Sin and a Curse for us: enduring most grievous sorrows in his "
               "Soul; and most painful sufferings in his body; was crucified, and died, and remained in the state of "
               "the dead; yet saw no corruption: on the third day he arose from the dead, with the same body in which "
               "he suffered; with which he also ascended into heaven: and there sitteth at the right hand of his "
               "Father, making intercession; and shall return to judge Men and Angels, at the end of the World.",
            5: "The Lord Jesus by his perfect obedience and sacrifice of himself, which he through the Eternal Spirit "
               "once offered up unto God, hath fully satisfied the Justice of God, procured reconciliation, "
               "and purchased an Everlasting inheritance in the Kingdom of Heaven, for all those whom the Father hath "
               "given unto him.",
            6: "Although the price of Redemption was not actually paid by Christ, till after his Incarnation, "
               "yet the vertue, efficacy, and benefit thereof were communicated to the Elect in all ages "
               "successively, from the beginning of the World, in and by those Promises, Types, and Sacrifices, "
               "wherein he was revealed, and signified to be the Seed of the Woman, which should bruise the Serpents "
               "head; and the Lamb slain from the foundation of the World: Being the same yesterday, and to day, "
               "and for ever.",
            7: "Christ in the work of Mediation acteth according to both natures, by each nature doing that which is "
               "proper to it self; yet by reason of the Unity of the Person, that which is proper to one nature, "
               "is sometimes in Scripture attributed to the Person denominated by the other nature.",
            8: "To all those for whom Christ hath obtained eternal redemption, he doth certainly, and effectually "
               "apply, and communicate the same; making intercession for them, uniting them to himself by his spirit, "
               "revealing unto them, in and by the word, the mystery of salvation; perswading them to believe, "
               "and obey; governing their hearts by his word and spirit, and overcoming all their enemies by his "
               "Almighty power, and wisdom; in such manner, and wayes as are most consonant to his wonderful, "
               "and unsearchable dispensation; and all of free, and absolute Grace, without any condition foreseen in "
               "them, to procure it.",
            9: "This office of Mediator between God and Man, is proper onely to Christ, who is the Prophet, Priest, "
               "and King of the Church of God; and may not be either in whole, or any part thereof transfer'd from "
               "him to any other.",
            10: "This number and order of Offices is necessary; for in respect of our ignorance, we stand in need of "
                "his prophetical Office; and in respect of our alienation from God, and imperfection of the best of "
                "our services, we need his Priestly office, to reconcile us, and present us acceptable unto God: and "
                "in respect our averseness, and utter inability to return to God, and for our rescue, and security "
                "from our spiritual adversaries, we need his Kingly office, to convince, subdue, draw, uphold, "
                "deliver, and preserve us to his Heavenly Kingdome."},
        9: {
            0: "Chapter IX. Of Free Will",
            1: "God hath indued the Will of Man, with that natural liberty, and power of acting upon choice; that it "
               "is neither forced, nor by any necessity of nature determined to do good or evil.",
            2: "Man in his state of innocency, had freedom, and power, to will, and to do that which was good, "
               "and well-pleasing to God; but yet was mutable, so that he might fall from it.",
            3: "Man by his fall into a state of sin hath wholly lost all ability of Will, to any spiritual good "
               "accompanying salvation; so as a natural man, being altogether averse from that good, and dead in Sin, "
               "is not able, by his own strength, to convert himself; or to prepare himself thereunto.",
            4: "When God converts a sinner, and translates him into the state of Grace he freeth him from his natural "
               "bondage under sin, and by his grace alone, enables him freely to will, and to do that which is "
               "spiritually good; yet so as that by reason of his remaining corruptions he doth not perfectly nor "
               "only will that which is good; but doth also will that which is evil.",
            5: "The Will of Man is made perfectly, and immutably free to good alone, in the state of Glory only."},
        10: {
            0: "Chapter X. Of Effectual Calling",
            1: "Those whom God hath predestinated unto Life, he is pleased in his appointed, and accepted time, "
               "effectually to call by his word, and Spirit, out of that state of sin, and death, in which they are "
               "by nature, to grace and Salvation by Jesus Christ; inlightning their minds, spiritually, and savingly "
               "to understand the things of God; taking away their heart of stone, and giving unto them an heart of "
               "flesh; renewing their wills, and by his Almighty power determining them to that which is good, "
               "and effectually drawing them to Jesus Christ; yet so as they come most freely, being made willing by "
               "his Grace.",
            2: "This Effectual Call is of God's free, and special grace alone, not from any thing at all foreseen in "
               "man, nor from any power, or agency in the Creature, coworking with his special Grace, the Creature "
               "being wholly passive therein, being dead in sins and trespasses, until being quickned & renewed by "
               "the holy Spirit, he is thereby enabled to answer this call, and to embrace the Grace offered and "
               "conveyed in it; and that by no less power, then that which raised up Christ from the dead.",
            3: "Elect Infants dying in infancy, are regenerated and saved by Christ through the Spirit; who worketh "
               "when, and where, and how he pleaseth: so also are all other elect persons, who are uncapable of being "
               "outwardly called by the Ministry of the Word.",
            4: "Others not elected, although they may be called by the Ministry of the word, and may have some common "
               "operations of the Spirit, yet not being effectually drawn by the Father, they neither will, "
               "nor can truly come to Christ; and therefore cannot be saved: much less can men that receive not the "
               "Christian Religion be saved; be they never so diligent to frame their lives according to the light of "
               "nature, and the Law of that Religion they do profess."},
        11: {
            0: "Chapter XI. Of Justification",
            1: "Those whom God Effectually calleth, he also freely justifieth, not by infusing Righteousness into "
               "them, but by pardoning their sins, and by accounting, and accepting their Persons as Righteous; not "
               "for any thing wrought in them, or done by them, but for Christ's sake alone, not by imputing faith it "
               "self, the act of beleiving, or any other evangelical obedience to them, as their Righteousness; but "
               "by imputing Christs active obedience unto the whole Law, and passive obedience in his death, "
               "for their whole and sole Righteousnnss, they receiving, and resting on him, and his Righteousness, "
               "by Faith; which faith they have not of themselves, it is the gift of God.",
            2: "Faith thus receiving and resting on Christ, and his Righteousness, is the alone instrument of "
               "Justification: yet it is not alone in the person justified, but is ever accompanied with all other "
               "saving Graces, and is no dead faith, but worketh by love.",
            3: "Christ by his obedience, and death, did fully discharge the debt of all those that are justified; and "
               "did by the sacrifice of himself, in the blood of his cross, undergoing in their stead, the penalty "
               "due unto them: make a proper, real and full satisfaction to Gods justice in their behalf: yet in "
               "asmuch as he was given by the Father for them, and his Obedience and Satisfaction accepted in their "
               "stead, and both freely, not for any thing in them; their Justification is only of Free Grace, "
               "that both the exact justice and rich Grace of God, might be glorified in the Justification of "
               "sinners.",
            4: "God did from all eternity decreeto justifie all the Elect, and Christ did in the fulness of time die "
               "for their sins, and rise again for their Justification; Nevertheless they are not justified "
               "personally, untill the Holy Spirit, doth in due time actually apply Christ unto them.",
            5: "God doth continue to Forgive the sins of those that are justified, and although they can never fall "
               "from the state of justication; yet they may by their sins fall under Gods Fatherly displeasure; and "
               "in that condition, they have not usually the light of his Countenance restored unto them, untill they "
               "humble themselves, confess their sins, beg pardon, and renew their faith, and repentance.",
            6: "The Justification of Believers under the Old Testament was in all these respects, one and the same "
               "with the justification of Believers under the New Tement."},
        12: {
            0: "Chapter XII. Of Adoption",
            1: "All those that are justified, God vouchsafed, in, and for the sake of his only Son Jesus Christ, "
               "to make partakers of the Grace of Adoption; by which they are taken into the number, and enjoy the "
               "Liberties, and Priveledges of Children of God; have his name put upon them, receive the Spirit of "
               "Adoption, have access to the throne of Grace with boldness, are enabled to cry Abba, Father, "
               "are pitied, protected, provided for, and chastned by him, as by a Father; yet never cast off; but "
               "sealed to the day of Redemption, and inherit the promises, as heirs, of everlasting Salvation."},
        13: {
            0: "Chapter XIII. Of Sanctification",
            1: "They who are united to Christ, Effectually called, and regenerated, having a new heart, and a new "
               "Spirit created in them, through the vertue of Christ's death, and Resurrection; are also farther "
               "sanctified, really, and personally, through the same vertue, by his word and Spirit dwelling in them; "
               "the dominion of the whole body of sin is destroyed, and the several lusts thereof, are more and more "
               "weakned, and mortified; and they more and more quickened, and strengthned in all saving graces, "
               "to the practice of all true holyness, without which no man shall see the Lord.",
            2: "This Sanctification is throughout, in the whole man, yet imperfect in this life; there abideth still "
               "some remnants of corruption in every part, whence ariseth a continual, and irreconcilable war; the "
               "Flesh lusting against the Spirit, and the Spirit against the Flesh.",
            3: "In which war, although the remaining corruption for a time may much prevail; yet through the "
               "continual supply of strength from the sanctifying Spirit of Christ the regenerate part doth overcome; "
               "and so the Saints grow in Grace, perfecting holiness in the fear of God, pressing after an heavenly "
               "life, in Evangelical Obedience to all the commands which Christ as Head and King, in his Word hath "
               "prescribed to them."},
        14: {
            0: "Chapter XIV. Of Saving Faith",
            1: "The Grace of Faith, whereby the Elect are enabled to beleive to the saving of their souls, "
               "is the work of the Spirit of Christ in their hearts; and is ordinarily wrought by the Ministry of the "
               "Word; by which also, and by the administration of Baptisme, and the Lords Supper, Prayer and other "
               "Means appointed of God, it is increased, and strengthned.",
            2: "By this Faith, a Christian believeth to be true, whatsoever is revealed in the Word, "
               "for the Authority of God himself; and also apprehendeth an excellency therein, above all other "
               "Writings; and all things in the world: as it bears forth the Glory of God in his Attributes, "
               "the excellency of Christ in his Nature and Offices; and the Power and Fullness of the Holy Spirit in "
               "his Workings, and Operations; and so is enabled to cast his Soul upon the truth thus beleived; and "
               "also acteth differently, upon that which each particular, passage thereof containeth; yeilding "
               "obedience to the commands, trembling at the threatnings, and embracing the promises of God, "
               "for this life, and that which is to come: But the principal acts of Saving Faith, have immediate "
               "relation to Christ, accepting, receiving, and resting upon him alone, for Justification, "
               "Sanctification, and Eternal Life, by vertue of the Covenant of Grace.",
            3: "This Faith although it be different in degrees, and may be weak, or strong; yet it is in the least "
               "degree of it, different in the kind, or nature of it (as is all other saving Grace) from the Faith, "
               "and common grace of temporary beleivers; and therefore though it may be many times assailed, "
               "and weakned; yet it gets the victory; growing up in many, to the attainment of a full assurance "
               "through Christ, who is both the Author and finisher of our Faith."},
        15: {
            0: "Chapter XV. Of Repentance unto Life and Salvation",
            1: "Such of the Elect as are converted at riper years, having sometimes lived in the state of nature, "
               "and therein served divers lusts and pleasures, God in their Effectual Calling giveth them Repentance "
               "unto Life.",
            2: "Whereas there is none that doth good, and sinneth not; and the best of men may through the power, "
               "and deceitfulness of their corruption dwelling in them, with the prevalency of temptation, "
               "fall into great sins, and provocations; God hath in the Covenant of Grace, mercifully provided that "
               "Beleivers so sinning, and falling, be renewed through Repentance unto Salvation.",
            3: "This saving Repentance is an evangelical Grace, whereby a person being by the Holy Spirit made "
               "sensible of the manifold evils of his sin, doth, by Faith in Christ, humble himself for it, "
               "with godly sorrow, detestation of it, and self abhorrency; praying for pardon, and strength of grace, "
               "with a purpose and endeavour by supplies of the Spirit, to walk before God unto all well pleasing in "
               "all things.",
            4: "As Repentance is to be continued through the whole course of our lives, upon the account of the body "
               "of death, and the motions thereof; so it is every mans duty, to repent of his particular known sins, "
               "particularly.",
            5: "Such is the provision which God hath made through Christ in the Covenant of Grace, "
               "for the preservation of Believers unto Salvation, that although there is no sin so small, "
               "but it deserves damnation; yet there is no sin so great, that it shall bring damnation on them that "
               "repent; which makes the constant preaching of Repentance necessary."},
        16: {
            0: "Chapter XVI. Of Good Works",
            1: "Good Works are only such as God hath commanded in his Holy word; and not such as without the warrant "
               "thereof, are devised by men, out of blind zeal, or upon any pretence of good intentions.",
            2: "These good works, done in obedience to Gods commandments, are the fruits, and evidences of a true, "
               "and lively faith; and by them Believers manifest their thankfullness, strengthen their assurance, "
               "edifie their brethren, adorn the profession of the Gospel, stop the mouths of the adversaries and "
               "glorifie God whose workmanship they are, created in Christ Jesus thereunto, that having their fruit "
               "unto holiness, they may have the end eternal life.",
            3: "Their ability to do good works, is not at all of themselves; but wholly from the Spirit of Christ; "
               "and that they may be enabled thereunto, besides the graces they have already received, "
               "there is necessary an actual influence of the same Holy Spirit, to work in them to will, and to do, "
               "of his good pleasure; yet are they not hereupon to grow negligent, as if they were not bound to "
               "perform any duty, unless upon a special motion of the Spirit; but they ought to be diligent in "
               "stirring up the Grace of God that is in them.",
            4: "They who in their obedience attain to the greatest height which is possible in this life, are so far "
               "from being able to superrogate, and to do more then God requires, as that they fall short of much "
               "which in duty they are bound to do.",
            5: "We cannot by our best works merit pardon of Sin or Eternal Life at the hand of God, by reason of the "
               "great disproportion that is between them and the glory to come; and the infinite distance that is "
               "between us and God, whom by them we can neither profit, nor satisfie for the debt of our former sins; "
               "but when we have done all we can, we have done but our duty, and are unprofitable servants; and "
               "because as they are good they proceed from his Spirit, and as they are wrought by us they are defiled "
               "and mixed with so much weakness and imperfection that they cannot endure the severity of Gods "
               "judgement.",
            6: "Yet notwithstanding the persons of Believers being accepted through Christ their good works also are "
               "accepted in him; not as though they were in this life wholly unblameable and unreprovable in Gods "
               "sight; but that he looking upon them in his Son is pleased to accept and reward that which is sincere "
               "although accompanied with many weaknesses and imperfections.",
            7: "Works done by unregenerate men although for the matter of them they may be things which God commands, "
               "and of good use, both to themselves and others; yet because they proceed not from a heart purified by "
               "faith, nor are done in a right manner according to the word, nor to a right end the glory of God; "
               "they are therefore sinful and cannot please God; nor make a man meet to receive grace from God; and "
               "yet their neglect of them is more sinful and displeasing to God."},
        17: {
            0: "Chapter XVII. Of The Perseverance of the Saints",
            1: "Those whom God hath accepted in the beloved, effectually called and Sanctified by his Spirit, "
               "and given the precious faith of his Elect unto, can neither totally nor finally fall from the state "
               "of grace; but shall certainly persevere therein to the end and be eternally saved, seeing the gifts "
               "and callings of God are without Repentance, (whence he still begets and nourisheth in them Faith, "
               "Repentance, Love, Joy, Hope, and all the graces of the Spirit unto immortality) and though many "
               "storms and floods arise and beat against them, yet they shall never be able to take them off that "
               "foundation and rock which by faith they are fastned upon: notwithstanding through unbelief and the "
               "temptations of Satan the sensible sight of the light and love of God, may for a time be clouded, "
               "and obscured from them, yet he is still the same and they shall be sure to be kept by the power of "
               "God unto Salvation, where they shall enjoy their purchased possession, they being engraven upon the "
               "palm of his hands, and their names having been written in the book of life from all Eternity.",
            2: "This perseverance of the Saints depends not upon their own free will; but upon the immutability of "
               "the decree of Election flowing from the free and unchangeable love of God the Father; upon the "
               "efficacy of the merit and intercession of Jesus Christ and Union with him, the oath of God, "
               "the abiding of his Spirit & the seed of God within them, and the nature of the Covenant of Grace from "
               "all which ariseth also the certainty and infallibility thereof.",
            3: "And though they may through the temptation of Satan and of the world, the prevalency of corruption "
               "remaining in them, and the neglect of means of their preservation fall into grievous sins, "
               "and for a time continue therein; whereby they incur Gods displeasure, and grieve his holy Spirit, "
               "come to have their graces and comforts impaired have their hearts hardened, and their Consciences "
               "wounded, hurt, and scandalize others, and bring temporal judgements upon themselves: yet they shall "
               "renew their repentance and be preserved through faith in Christ Jesus to the end."},
        18: {
            0: "Chapter XVIII. Of the Assurance of Grace and Salvation",
            1: "Although temporary Believers, and other unregenerate men, may vainly deceive themselves with false "
               "hopes, and carnal presumptions, of being in the favour of God, and state of salvation, which hope of "
               "theirs shall perish; yet such as truely believe in the Lord Jesus, and love him in sincerity, "
               "endeavouring to walk in all good Conscience before him, may in this life be certainly assured that "
               "they are in the state of Grace; and may rejoyce in the hope of the glory of God which hope shall "
               "never make them ashamed.",
            2: "This certainty is not a bare conjectural, and probable perswasion, grounded upon a fallible hope; but "
               "an infallible assurance of faith founded on the Blood and Righteousness of Christ revealed in the "
               "Gospel; and also upon the inward evidence of those graces of the Spirit unto which promises are made, "
               "and on the testimony of the Spirit of adoption, witnessing with our Spirits that we are the children "
               "of God; and as a fruit thereof keeping the heart both humble and holy.",
            3: "This infallible assurance doth not so belong to the essence of faith, but that a true Believer, "
               "may wait long and conflict with many difficulties before he be partaker of it; yet being enabled by "
               "the Spirit to know the things which are freely given him of God, he may without extraordinary "
               "revelation in the right use of means attain thereunto: and therefore it is the duty of every one, "
               "to give all diligence to make their Calling and Election sure, that thereby his heart may be enlarged "
               "in peace and joy in the holy Spirit, in love and thankfulness to God, and in strength and "
               "chearfulness in the duties of obedience, the proper fruits of this Assurance; so far is it from "
               "inclining men to looseness.",
            4: "True Believers may have the assurance of their Salvation divers ways shaken, diminished, "
               "and intermitted; as by negligence in preserving of it, by falling into som special Sin, "
               "which woundeth the Conscience, and grieveth the Spirit, by some sudden or vehement temptation, "
               "by Gods withdrawing the light of his countenance and suffering even such as fear him to walk in "
               "darkness and to have no light; yet are they never destitute of the seed of God, and Life of Faith, "
               "that Love of Christ, and the brethren, that sincerity of Heart, and Conscience of duty, out of which "
               "by the operation of the Spirit, this Assurance may in due time be revived: and by the which in the "
               "mean time they are preserved from utter despair."},
        19: {
            0: "Chapter XIX. Of the Law of God",
            1: "God gave to Adam a Law of universal obedience, written in his Heart, and a particular precept of not "
               "eating the Fruit of the tree of knowledge of good and evil; by which he bound him, and all his "
               "posterity to personal entire exact and perpetual obedience; promised life upon the fulfilling, "
               "and threatned death upon the breach of it; and indued him with power and ability to keep it.",
            2: "The same Law that was first written in the heart of man, continued to be a perfect rule of "
               "Righteousness after the fall; & was delivered by God upon Mount Sinai, in Ten Commandments and "
               "written in two Tables; the four first containing our duty towards God, and the other six our duty to "
               "man.",
            3: "Besides this Law commonly called moral, God was pleased to give to the people of Israel Ceremonial "
               "Laws, containing several typical ordinances, partly of worship, prefiguring Christ, his graces, "
               "actions, sufferings, and benefits; and partly holding forth divers instructions of moral duties, "
               "all which Ceremonial Laws being appointed only to the time of reformation, are by Jesus Christ the "
               "true Messiah and only Law-giver who was furnished with power from the Father, for that end, "
               "abrogated and taken away.",
            4: "To them also he gave sundry judicial Laws, which expired together with the state of that people, "
               "not obliging any now by vertue of that institution; their general equity onely, being of moral use.",
            5: "The moral Law doth for ever bind all, as well justified persons as others, to the obedience thereof, "
               "and that not only in regard of the matter contained in it, but also in respect of the authority of "
               "God the Creator; who gave it: Neither doth Christ in the Gospel any way dissolve, but much strengthen "
               "this obligation.",
            6: "Although true Believers be not under the Law, as a Covenant of Works, to be thereby Justified or "
               "condemned; yet it is of great use to them as well as to others: in that, as a Rule of Life, "
               "informing them of the Will of God, and their Duty, it directs and binds them, to walk accordingly; "
               "discovering also the sinfull pollutions of their Natures, Hearts and Lives; so as Examining "
               "themselves thereby, they may come to further Conviction of, Humiliation for, and Hatred against Sin; "
               "together with a clearer sight of the need they have of Christ and the perfection of his Obedience: It "
               "is likewise of use to the Regenerate to restrain their Corruptions, in that it forbids Sin; and the "
               "Threatnings of it serve to shew what even their Sins deserve; and what afflictions in this Life they "
               "may expect for them, although free'd from the Curse and unallayed Rigor thereof. The Promises of it "
               "likewise shew them Gods approbation of Obedience, and what blessings they may expect upon the "
               "performance thereof, though not as due to them by the Law as a Covenant of Works; so as mans doing "
               "Good and refraining from Evil, because the Law incourageth to the one and deterreth from the other, "
               "is no Evidence of his being under the Law and not under Grace.",
            7: "Neither are the forementioned uses of the Law contrary to the Grace of the Gospel; but do sweetly "
               "comply with it; the Spirit of Christ subduing and inabling the Will of man, to do that freely and "
               "chearfully, which the will of God revealed in the Law, requireth to be done."},
        20: {
            0: "Chapter XX. Of Christian Liberty and Liberty of Conscience",
            1: "The Covenant of Works being broken by Sin, and made unprofitable unto Life; God was pleased to give "
               "forth the promise of Christ, the Seed of the Woman, as the means of calling the Elect, and begetting "
               "in them Faith and Repentance; in this Promise, the Gospel, as to the substance of it, was revealed, "
               "and therein Effectual, for the Conversion and Salvation of Sinners.",
            2: "This Promise of Christ, and Salvation by him, is revealed only by the Word of God; neither do the "
               "Works of Creation, or Providence, with the light of Nature, make discovery of Christ, or of Grace by "
               "him; so much as in a general, or obscure way; much less that men destitute of the Revelation of him "
               "by the Promise, or Gospel; should be enabled thereby, to attain saving Faith, or Repentance.",
            3: "The Revelation of the Gospel unto Sinners, made in divers times, and by sundry parts; with the "
               "addition of Promises, and Precepts for the Obedience required therein, as to the Nations, "
               "and Persons, to whom it is granted, is meerly of the Soveraign Will and good Pleasure of God; not "
               "being annexed by vertue of any Promise, to the due improvement of mens natural abilities, "
               "by vertue of Common light received, without it; which none ever did make, or can so do: And therefore "
               "in all Ages the preaching of the Gospel hath been granted unto persons and Nations, as to the extent, "
               "or streightning of it, in great variety, according to the Councell of the Will of God.",
            4: "Although the Gospel be the only outward means, of revealing Christ, and saving Grace; and is, "
               "as such, abundantly sufficient thereunto; yet that men who are dead in Trespasses, may be born again, "
               "Quickned or Regenerated; there is moreover necessary, an effectual, insuperable work of the Holy "
               "Spirit, upon the whole Soul, for the producing in them a new spiritual Life; without which no other "
               "means will effect their Conversion unto God."},
        21: {
            0: "Chapter XXI. Of Christian Liberty and Liberty of Consciencey",
            1: "The Liberty which Christ hath purchased for Believers under the Gospel, consists in their freedom "
               "from the guilt of Sin, the condemning wrath of God, the Rigour and Curse of the Law; and in their "
               "being delivered from this present evil World, Bondage to Satan, and Dominion of Sin; from the Evil of "
               "Afflictions; the Fear, and Sting of Death, the Victory of the Grave, and Everlasting Damnation; as "
               "also in their free access to God; and their yielding Obedience unto him not out of a slavish fear, "
               "but a Child-like love, and willing mind.",
            2: "God alone is Lord of the Conscience, and hath left it free from the Doctrines and Commandments of "
               "men, which are in any thing contrary to his Word, or not contained in it. So that to Believe such "
               "Doctrines, or obey such Commands out of Conscience, is to betray true liberty of Conscience; and the "
               "requiring of an implicit Faith, and absolute and blind Obedience, is to destroy Liberty of "
               "Conscience, and Reason also.",
            3: "They who upon pretence of Christian Liberty do practice any sin, or cherish any sinfull lust; as they "
               "do thereby pervert the main design of the Grace of the Gospel, to their own Destruction; so they "
               "wholy destroy the end of Christian Liberty, which is, that being delivered out of the hands of all "
               "our Enemies we might serve the Lord without fear in Holiness, and Righteousness before him, "
               "all the days of our Life."},
        22: {
            0: "Chapter XXII. Of Religious Worship and the Sabbath Day",
            1: "The light of Nature shews that there is a God, who hath Lordship, and Soveraigntye over all; is just, "
               "good, and doth good unto all; and is therefore to be feared, loved, praised, called upon, trusted in, "
               "and served, with all the Heart, and all the Soul, and with all the Might. But the acceptable way of "
               "Worshipping the true God, is instituted by himself; and so limited by his own revealed will, "
               "that he may not be Worshipped according to the imaginations, and devices of Men, or the suggestions "
               "of Satan, under any visible representations, or any other way, not prescribed in the Holy Scriptures.",
            2: "Religious Worship is to be given to God the Father, Son, and Holy Spirit, and to him alone; not to "
               "Angels, Saints, or any other Creatures; and since the fall, not without a Mediator, nor in the "
               "Mediation of any other but Christ alone.",
            3: "Prayer with thanksgiving, being one special part of natural worship, is by God required of all men. "
               "But that it may be accepted, it is to be made in the Name of the Son, by the help of the Spirit, "
               "according to his Will; with understanding, reverence, humility, fervency, faith, love, "
               "and perseverance; and when with others, in a known tongue.",
            4: "Prayer is to be made for things lawful, and for all sorts of men living, or that shall live "
               "hereafter; but not for the dead, nor for those of whom it may be known that they have sinned the sin "
               "unto death.",
            5: "The reading of the Scriptures, Preaching, and hearing the word of God, teaching and admonishing one "
               "another in Psalms, Hymns and Spiritual songs, singing with grace in our Hearts to the Lord; as also "
               "the Administration of Baptism, and the Lords Supper are all parts of Religious worship of God, "
               "to be performed in obedience to him, with understanding, faith, reverence, and godly fear; moreover "
               "solemn humiliation with fastings; and thanksgiving upon special occasions, ought to be used in an "
               "holy and religious manner.",
            6: "Neither Prayer, nor any other part of Religious worship, is now under the Gospel tied unto, "
               "or made more acceptable by, any place in which it is performed, or towards which it is directed; but "
               "God is to be worshipped every where in Spirit, and in truth; as in private families daily, "
               "and in secret each one by himself, so more solemnly in the publick Assemblies, which are not "
               "carelessely, nor wilfuly, to be neglected, or forsaken, when God by his word, or providence calleth "
               "thereunto.",
            7: "As it is of the Law of nature, that in general a proportion of time by Gods appointment, be set a "
               "part for the Worship of God; so by his Word in a positive-moral, and perpetual Commandement, "
               "binding all men, in all Ages, he hath particularly appointed one day in seven for a Sabbath to be "
               "kept holy unto him, which from the beginning of the World to the Resurrection of Christ, was the last "
               "day of the week; and from the resurrection of Christ, was changed into the first day of the week "
               "which is called the Lords day; and is to be continued to the end of the World, as the Christian "
               "Sabbath; the observation of the last day of the week being abolished.",
            8: "The Sabbath is then kept holy unto the Lord, when men after a due preparing of their hearts, "
               "and ordering their common affairs aforehand, do not only observe an holy rest all the day, "
               "from their own works, words, and thoughts, about their worldly employment, and recreations, "
               "but also are taken up the whole time in the publick and private exercises of his worship, and in the "
               "duties of necessity and mercy."},
        23: {
            0: "Chapter XXIII. Of Lawful Oaths and Vows",
            1: "A lawful Oath is a part of religious worship, wherein the person swearing in Truth, Righteousness, "
               "and Judgement, solemnly calleth God to witness what he sweareth; and to judge him according to the "
               "Truth or falseness thereof.",
            2: "The Name of God only is that by which men ought to swear; and therein it is to be used, with all Holy "
               "Fear and reverence, therefore to swear vainly or rashly by that glorious, and dreadful name; or to "
               "swear at all by any other thing, is sinful and to be abhorred; yet as in matter of weight and moment "
               "for confirmation of truth, and ending all strife, an Oath is warranted by the Word of God; so a "
               "lawful Oath being imposed, by lawful Authority, in such matters, ought to be taken.",
            3: "Whosoever taketh an Oath warranted by the Word of God, ought duely to consider the weightiness of so "
               "solemn an act; and therein to avouch nothing, but what he knoweth to be the truth; for that by rash, "
               "false, and vain Oaths the Lord is provoked, and for them this Land mournes.",
            4: "An Oath is to be taken in the plain, and common sense of the words; without equivocation, or mental "
               "reservation.",
            5: "A Vow which is not to be made to any Creature, but to God alone, is to be made and performed with all "
               "Religious care, and faithfulness: But Popish Monastical Vows, of perpetual single life, "
               "professed poverty, and regular obedience, are so far from being degrees of higher perfection, "
               "that they are superstitious, and sinful snares, in which no Christian may intangle himself."},
        24: {
            0: "Chapter XXIV. Of the Civil Magistrate",
            1: "God the supream Lord, and King of all the World, hath ordained Civil Magistrates to be under him, "
               "over the people for his own glory, and the publick good; and to this end hath armed them with the "
               "power of the Sword, for defence and encouragement of them that do good, and for the punishment of "
               "evil doers.",
            2: "It is lawful for Christians to Accept, and Execute the Office of a Magistrate when called thereunto; "
               "in the management whereof, as they ought especially to maintain Justice, and Peace, according to the "
               "wholsome Laws of each Kingdome, and Commonwealth: so for that end they may lawfully now under the New "
               "Testament wage war upon just and necessary occasions.",
            3: "Civil Magistrates being set up by God, for the ends aforesaid; subjection in all lawful things "
               "commanded by them, ought to be yeilded by us, in the Lord; not only for wrath but for Conscience "
               "sake; and we ought to make supplications and prayers for Kings, and all that are in Authority, "
               "that under them we may live a quiet and peaceable life, in all godliness and honesty."},
        25: {
            0: "Chapter XXV. Of the Civil Magistrate",
            1: "Marriage is to be between one Man and one Woman; neither is it lawful for any man to have more then "
               "one Wife, nor for any Woman to have more then one Husband at the same time.",
            2: "Marriage was ordained for the mutual help of Husband and Wife, for the increase of Man-kind, "
               "with a legitimate issue, and for preventing of uncleanness.",
            3: "It is lawful for all sorts of people to Marry, who are able with judgment to give their consent; yet "
               "it is the duty of Christians to marry in the Lord, and therefore such as profess the true Religion, "
               "should not Marry with Infidels, or Idolaters; neither should such as are godly be unequally yoked, "
               "by marrying with such as are wicked, in their life, or maintain damnable Heresie.",
            4: "Marriage ought not to be within the degrees of consanguinity, or Affinity forbidden in the word; nor "
               "can such incestuous Marriage ever be made lawful, by any law of Man or consent of parties, "
               "so as those persons may live together as Man and Wife."},
        26: {
            0: "Chapter XXVI. Of the Church",
            1: "The Catholick or universal Church, which (with respect to the internal work of the Spirit, and truth "
               "of grace) may be called invisible, consists of the whole number of the Elect, that have been, are, "
               "or shall be gathered into one, under Christ the head thereof; and is the spouse, the body, "
               "the fulness of him that filleth all in all.",
            2: "All persons throughout the world, professing the faith of the Gospel, and obedience unto God by "
               "Christ, according unto it; not destroying their own profession by any Errors everting the foundation, "
               "or unholyness of conversation, are and may be called visible Saints; and of such ought all particular "
               "Congregations to be constituted.",
            3: "The purest Churches under heaven are subject to mixture, and error; and som have so degenerated as to "
               "become no Churches of Christ, but Synagogues of Satan; nevertheless Christ always hath had, "
               "and ever shall have a Kingdome in this world, to the end thereof, of such as believe in him, "
               "and make profession of his Name.",
            4: "The Lord Jesus Christ is the Head of the Church, in whom by the appointment of the Father, all power "
               "for the calling, institution, order, or Government of the Church, is invested in a supream & "
               "soveraigne manner, neither can the Pope of Rome in any sense be head thereof, but is that Antichrist, "
               "that Man of sin, and Son of perdition, that exalteth himself in the Church against Christ, "
               "and all that is called God; whom the Lord shall destroy with the brightness of his coming.",
            5: "In the execution of this power wherewith he is so intrusted, the Lord Jesus calleth out of the World "
               "unto himself, through the Ministry of his word, by his Spirit, those that are given unto him by his "
               "Father; that they may walk before him in all the ways of obedience, which he prescribeth to them in "
               "his Word. Those thus called he commandeth to walk together in particular societies, or Churches, "
               "for their mutual edification; and the due performance of that publick worship, which he requireth of "
               "them in the World.",
            6: "The Members of these Churches are Saints by calling, visibly manifesting and evidencing (in and by "
               "their profession and walking) their obedience unto that call of Christ; and do willingly consent to "
               "walk together according to the appointment of Christ, giving up themselves, to the Lord & one to "
               "another by the will of God, in professed subjection to the Ordinances of the Gospel.",
            7: "To each of these Churches thus gathered, according to his mind, declared in his word, he hath given "
               "all that power and authority, which is any way needfull, for their carrying on that order in worship, "
               "and discipline, which he hath instituted for them to observe; with commands, and rules, for the due "
               "and right exerting, and executing of that power.",
            8: "A particular Church gathered, and compleatly Organized, according to the mind of Christ, consists of "
               "Officers, and Members; And the Officers appointed by Christ to be chosen and set apart by the Church "
               "(so called and gathered) for the peculiar Administration of Ordinances, and Execution of Power, "
               "or Duty, which he intrusts them with, or calls them to, to be continued to the end of the World are "
               "Bishops or Elders and Deacons.",
            9: "The way appointed by Christ for the Calling of any person, fitted, and gifted by the Holy Spirit, "
               "unto the Office of Bishop, or Elder, in a Church, is, that he be chosen thereunto by the common "
               "suffrage of the Church it self; and Solemnly set apart by Fasting and Prayer, with imposition of "
               "hands of the Eldership of the Church, if there be any before Constituted therein; And of a Deacon "
               "that he be chosen by the like suffrage, and set apart by Prayer, and the like Imposition of hands.",
            10: "The work of Pastors being constantly to attend the Service of Christ, in his Churches, "
                "in the Ministry of the Word, and Prayer, with watching for their Souls, as they that must give an "
                "account to him; it is incumbent on the Churches to whom they Minister, not only to give them all due "
                "respect, but also to communicate to them of all their good things according to their ability, "
                "so as they may have a comfortable supply, without being themselves entangled in Secular Affairs; and "
                "may also be capable of exercising Hospitality toward others; and this is required by the Law of "
                "Nature, and by the Express order of our Lord Jesus, who hath ordained that they that preach the "
                "Gospel, should live of the Gospel.",
            11: "Although it be incumbent on the Bishops or Pastors of the Churches to be instant in Preaching the "
                "Word, by way of Office; yet the work of Preaching the Word, is not so peculiarly confined to them; "
                "but that others also gifted, and fitted by the Holy Spirit for it, and approved, and called by the "
                "Church, may and ought to perform it.",
            12: "As all Believers are bound to joyn themselves to particular Churches, when and where they have "
                "opportunity so to do; So all that are admitted unto the priviledges of a Church, are also under the "
                "Censures and Government thereof, according to the Rule of Christ.",
            13: "No Church-members upon any offence taken by them, having performed their Duty required of them "
                "towards the person they are offended at, ought to disturb any Church order, or absent themselves "
                "from the Assemblies of the Church, or Administration of any Ordinances, upon the account of such "
                "offence at any of their fellow-members; but to wait upon Christ, in the further proceeding of the "
                "Church.",
            14: "As each Church, and all the Members of it are bound to pray continually, for the good and prosperity "
                "of all the Churches of Christ, in all places; and upon all occasions to further it (every one within "
                "the bounds of their places, and callings, in the Exercise of their Gifts and Graces) so the Churches "
                "(when planted by the providence of God so as they may injoy opportunity and advantage for it) ought "
                "to hold communion amongst themselves for their peace, increase of love, and mutual edification.",
            15: "In cases of difficulties or differences, either in point of Doctrine, or Administration; wherein "
                "either the Churches in general are concerned, or any one Church in their peace, union, "
                "and edification; or any member, or members, of any Church are injured, in or by any proceedings in "
                "censures not agreeable to truth, and order: it is according to the mind of Christ, that many "
                "Churches holding communion together, do by their messengers meet to consider, and give their advice, "
                "in or about that matter in difference, to be reported to all the Churches concerned; howbeit these "
                "messengers assembled are not entrusted with any Church-power properly so called; or with any "
                "jurisdiction over the Churches themselves, to exercise any censures either over any Churches, "
                "or Persons: or to impose their determination on the Churches, or Officers."},
        27: {
            0: "Chapter XXVII. Of the Communion of the Saints",
            1: "All Saints that are united to Jesus Christ their Head, by his Spirit, and Faith; although they are "
               "not made thereby one person with him, have fellowship in his Graces, sufferings, death, resurrection, "
               "and glory; and being united to one another in love, they have communion in each others gifts, "
               "and graces; and are obliged to the performance of such duties, publick and private, in an orderly "
               "way, as do conduce to their mutual good, both in the inward and outward man.",
            2: "Saints by profession are bound to maintain an holy fellowship and communion in the worship of God, "
               "and in performing such other spiritual services, as tend to their mutual edification; as also in "
               "relieving each other in outward things according to their several abilities, and necessities; which "
               "communion according to the rule of the Gospel, though especially to be exercised by them, "
               "in the relations wherein they stand, whether in families, or Churches; yet as God offereth "
               "opportunity is to be extended to all the houshold of faith, even all those who in every place call "
               "upon the name of the Lord Jesus; nevertheless their communion one with another as Saints, "
               "doth not take away or infringe, the title or propriety, which each man hath in his goods and "
               "possessions."},
        28: {
            0: "Chapter XXVIII. Of Baptism and the Lord's Supper",
            1: "Baptism and the Lords Supper are ordinances of positive, and soveraign institution; appointed by the "
               "Lord Jesus the only Law-giver, to be continued in his Church to the end of the world.",
            2: "These holy appointments are to be administred by those only, who are qualified and thereunto called "
               "according to the commission of Christ."},
        29: {
            0: "Chapter XXIX. Of Baptism",
            1: "Baptism is an Ordinance of the New Testament, ordained by Jesus Christ, to be unto the party "
               "Baptized, a sign of his fellowship with him, in his death, and resurrection; of his being engrafted "
               "into him; of remission of sins; and of his giving up unto God through Jesus Christ to live and walk "
               "in newness of Life.",
            2: "Those who do actually professe repentance towards God, faith in, and obedience, to our Lord Jesus, "
               "are the only proper subjects of this ordinance.",
            3: "The outward element to be used in this ordinance is water, wherein the party is to be baptized, "
               "in the name of the Father, and of the Son, and of the Holy Spirit.",
            4: ("Immersion, or dipping of the person in water, "
                "is necessary to the due administration of this ordinance.")},
        30: {
            0: "Chapter XXX. Of the Lord's Supper",
            1: "The Supper of the Lord Jesus, was instituted by him, the same night wherein he was betrayed, "
               "to be observed in his Churches unto the end of the world, for the perpetual remembrance, and shewing "
               "forth the sacrifice of himself in his death confirmation of the faith of believers in all the "
               "benefits thereof, their spiritual nourishment, and growth in him, their further ingagement in, "
               "and to, all duties which they owe unto him; and to be a bond and pledge of their communion with him, "
               "and with each other.",
            2: "In this ordinance Christ is not offered up to his Father, nor any real sacrifice made at all, "
               "for remission of sin of the quick or dead; but only a memorial of that one offering up of himself, "
               "by himself, upon the crosse, once for all; and a spiritual oblation of all possible praise unto God "
               "for the same; so that the Popish sacrifice of the Mass (as they call it) is most abominable, "
               "injurious to Christs own only sacrifice, the alone propitiation for all the sins of the Elect.",
            3: "The Lord Jesus hath in this Ordinance, appointed his Ministers to Pray, and bless the Elements of "
               "Bread and Wine, and thereby to set them apart from a common to an holy use, and to take and break the "
               "Bread; to take the Cup, and (they communicating also themselves) to give both to the Communicants.",
            4: "The denyal of the Cup to the people, worshiping the Elements, the lifting them up, or carrying them "
               "about for adoration, and reserving them for any pretended religious use, are all contrary to the "
               "nature of this Ordinance, and to the institution of Christ.",
            5: "The outward Elements in this Ordinance, duely set apart to the uses ordained by Christ, have such "
               "relation to him crucified, as that truely, although in terms used figuratively, they are sometimes "
               "called by the name of the things they represent, to wit the body and Blood of Christ; albeit in "
               "substance, and nature, they still remain truly, and only Bread, and Wine, as they were before.",
            6: "That doctrine which maintains a change of the substance of Bread and Wine, into the substance of "
               "Christs body and blood (commonly called Transubstantiation) by consecration of a Priest, "
               "or by any other way, is repugnant not to Scripture alone, but even to common sense and reason; "
               "overthroweth the nature of the ordinance, and hath been and is the cause of manifold superstitions, "
               "yea, of gross Idolatries.",
            7: "Worthy receivers, outwardly partaking of the visible Elements in this Ordinance, do then also "
               "inwardly by faith, really and indeed, yet not carnally, and corporally, but spiritually receive, "
               "and feed upon Christ crucified & all the benefits of his death: the Body and Blood of Christ, "
               "being then not corporally, or carnally, but spiritually present to the faith of Believers, "
               "in that Ordinance, as the Elements themselves are to their outward senses.",
            8: "All ignorant and ungodly persons, as they are unfit to enjoy communion with Christ; so are they "
               "unworthy of the Lords Table; and cannot without great sin against him, while they remain such, "
               "partake of these holy mysteries, or be admitted thereunto: yea whosoever shall receive unworthily are "
               "guilty of the Body and Blood of the Lord, eating and drinking judgement to themselves."},
        31: {
            0: "Chapter XXXI. Of the State of Man after Death and of the Resurrection of the Dead",
            1: "The Bodies of Men after Death return to dust, and see corruption; but their Souls (which neither die "
               "nor sleep) having an immortal subsistence, immediately return to God who gave them: the Souls of the "
               "Righteous being then made perfect in holyness, are received into paradise where they are with Christ, "
               "and behold the face of God, in light and glory; waiting for the full Redemption of their Bodies; and "
               "the souls of the wicked, are cast into hell; where they remain in torment and utter darkness, "
               "reserved to the judgement of the great day; besides these two places for Souls separated from their "
               "bodies, the Scripture acknowledgeth none.",
            2: "At the last day such of the Saints as are found alive shall not sleep but be changed; and all the "
               "dead shall be raised up with the self same bodies, and none other; although with different qualities, "
               "which shall be united again to their Souls for ever.",
            3: "The bodies of the unjust shall by the power of Christ, be raised to dishonour; the bodies of the just "
               "by his spirit unto honour, and be made conformable to his own glorious Body."},
        32: {
            0: "Chapter XXXII. Of the Last Judgment",
            1: "God hath appointed a Day wherein he will judge the world in Righteousness, by Jesus Christ; to whom "
               "all power and judgement is given of the Father; in which Day not only the Apostate Angels shall be "
               "judged; but likewise all persons that have lived upon the Earth, shall appear before the Tribunal of "
               "Christ; to give an account of their Thoughts, Words, and Deeds, and to receive according to what they "
               "have done in the body, whether good or evil.",
            2: "The end of Gods appointing this Day, is for the manifestation of the glory of his Mercy, "
               "in the Eternal Salvation of the Elect; and of his Justice in the Eternal damnation of the Reprobate, "
               "who are wicked and disobedient; for then shall the Righteous go into Everlasting Life, and receive "
               "that fulness of Joy, and Glory, with everlasting reward, in the presence of the Lord: but the wicked "
               "who know not God, and obey not the Gospel of Jesus Christ, shall be cast into Eternal torments, "
               "and punished with everlasting destruction, from the presence of the Lord, and from the glory of his "
               "power.",
            3: "As Christ would have us to be certainly perswaded that there shall be a Day of judgement, "
               "both to deter all men from sin, and for the greater consolation of the godly, in their adversity; so "
               "will he have that day unknown to Men, that they may shake off all carnal security, and be always "
               "watchful, because they know not at what hour, the Lord will come; and may ever be prepared to say, "
               "Come Lord Jesus, Come quickly, Amen."}
    }

    __lbcf89Regex = (r"\[\s*(?:(?:L|London)\s*(?:B|Baptist)\s*(?:C|Confession)\s*(?:of)?\s*"
                     "(?:F|Faith))?\s*1689\s*([\d\,\-\:\s.]+)\]")

    def __init__(self):
        self.__parse = chapter_paragraph_parser

    def __get_text(self, from_chptr, from_para, to_chptr, to_para):
        if (0 < from_chptr <= to_chptr <= 32) and \
                (0 < from_para <= self.__CHPTRMAX[from_chptr]) and \
                (0 < to_para <= self.__CHPTRMAX[to_chptr]):
            result = ''
            for i in range(from_chptr, to_chptr + 1):
                result += "\n>**" + self.__text[i][0] + "**\n\n"
                for j in range(from_para if i == from_chptr else 1,
                               to_para + 1 if i == to_chptr else self.__CHPTRMAX[i] + 1):
                    result += ">**" + str(j) + ".** " + self.__text[i][j] + "\n\n"
            return result, False
        else:
            return '', True

    def fetch(self, full_citations):
        response_text = ''
        response_citation = ''
        response_is_malformed = False

        if full_citations:
            lbcf89_citations = re.findall(self.__lbcf89Regex, full_citations, re.IGNORECASE)
            if lbcf89_citations:
                response_citation = '[LBCF 1689 '
                args, response_is_malformed = self.__parse(lbcf89_citations)
                for i in args:
                    response_citation += str(i[0]) + ':' + str(i[1]) + "-" + str(i[2]) + ':' + str(i[3]) + ", "
                    quote, temp = self.__get_text(i[0], i[1], i[2], i[3])
                    response_is_malformed |= temp
                    if response_text:
                        response_text += quote
                    elif quote:
                        response_text += "\n**London Baptist Confession of Faith**\n" + quote
                response_citation = response_citation[:-2] + "]"
        return response_text, response_citation, response_is_malformed
