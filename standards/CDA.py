#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from utils.Parsers import chapter_paragraph_parser


class CDA:
    __CHPTRMAX = {
        1: 18,
        2: 9,
        3: 17,
        4: 17}

    __text = {
        1: {
            0: "**FIRST HEAD OF DOCTRINE**\n\n>**Of Divine Predestination**",
            1: ("As all men have sinned in Adam, lie under the curse, and are deserving of eternal death, God would "
                "have done no injustice by leaving them all to perish, and delivering them over to condemnation on "
                "account of sin, according to the words of the apostle, \"that every mouth may be stopped, "
                "and all the world may become guilty before God\" (Rom. 3:19). And verse 23: \"For all have sinned, "
                "and come short of the glory of God.\" And Romans 6:23: \"For the wages of sin is death.\""),
            2: ("But in this the love of God was manifested, that He sent His only begotten Son into the world, "
                "that whosoever believeth on Him should not perish, but have everlasting life. \"In this was "
                "manifested the love of God toward us, because that God sent His only begotten Son into the world, "
                "that we might live through Him\" (1 John 4:9). \"For God so loved the world, that He gave His only "
                "begotten Son, that whosoever believeth in Him should not perish, but have everlasting life\" (John "
                "3:16)."),
            3: ("And that men may be brought to believe, God mercifully sends the messengers of these most joyful "
                "tidings to whom He will and at what time He pleaseth; by whose ministry men are called to repentance "
                "and faith in Christ crucified. \"How then shall they call on Him in whom they have not believed? and "
                "how shall they believe in Him of whom they have not heard? and how shall they hear without a "
                "preacher? And how shall they preach, except they be sent?\" (Rom. 10:14–15)."),
            4: ("The wrath of God abideth upon those who believe not this gospel. But such as receive it, and embrace "
                "Jesus the Savior by a true and living faith, are by Him delivered from the wrath of God and from "
                "destruction, and have the gift of eternal life conferred upon them."),
            5: ("The cause or guilt of this unbelief, as well as of all other sins, is no wise in God, but in man "
                "himself; whereas faith in Jesus Christ and salvation through Him is the free gift of God, "
                "as it is written: \"For by grace are ye saved through faith; and that not of yourselves: it is the "
                "gift of God\" (Eph. 2:8). \"For unto you it is given in the behalf of Christ, not only to believe on "
                "Him,\" etc. (Phil. 1:29)"),
            6: ("That some receive the gift of faith from God and others do not receive it proceeds from God's "
                "eternal decree, for \"known unto God are all His works from the beginning of the world\" (Acts "
                "15:18). \"Who worketh all things after the counsel of His own will\" (Eph. 1:11). According to which "
                "decree, He graciously softens the hearts of the elect, however obstinate, and inclines them to "
                "believe, while He leaves the non-elect in His just judgment to their own wickedness and obduracy. "
                "And herein is especially displayed the profound, the merciful, and at the same time the righteous "
                "discrimination between men, equally involved in ruin; or that decree of election and reprobation "
                "revealed in the Word of God, which though men of perverse, impure and unstable minds wrest to their "
                "own destruction, yet to holy and pious souls affords unspeakable consolation"),
            7: ("Election is the unchangeable purpose of God, whereby, before the foundation of the world, "
                "He hath out of mere grace, according to the sovereign good pleasure of His own will, chosen, "
                "from the whole human race, which had fallen through their own fault from their primitive state of "
                "rectitude into sin and destruction, a certain number of persons to redemption in Christ, "
                "whom He from eternity appointed the Mediator and Head of the elect, and the foundation of "
                "salvation.\n\n>This elect number, though by nature neither better nor more deserving than others, "
                "but with them involved in one common misery, God hath decreed to give to Christ, to be saved by Him, "
                "and effectually to call and draw them to His communion by His Word and Spirit, to bestow upon them "
                "true faith, justification and sanctification; and having powerfully preserved them in the fellowship "
                "of His Son, finally, to glorify them for the demonstration of His mercy and for the praise of His "
                "glorious grace, as it is written: \"According as He hath chosen us in Him before the foundation of "
                "the world, that we should be holy and without blame before Him in love: having predestinated us unto "
                "the adoption of children by Jesus Christ to Himself, according to the good pleasure of His will, "
                "to the praise of the glory of His grace, wherein He hath made us accepted in the beloved\" (Eph. "
                "1:4–6). And elsewhere: \"Whom He did predestinate, them He also called: and whom He called, "
                "them He also justified: and whom He justified them He also glorified\" (Rom. 8:30)."),
            8: ("There are not various decrees of election, but one and the same decree respecting all those who "
                "shall be saved, both under the Old and New Testament; since the Scripture declares the good "
                "pleasure, purpose and counsel of the divine will to be one, according to which He hath chosen us "
                "from eternity, both to grace and glory, to salvation and the way of salvation, which He hath "
                "ordained that we should walk therein."),
            9: ("This election was not founded upon foreseen faith, and the obedience of faith, holiness, "
                "or any other good quality or disposition in man, as the prerequisite, cause or condition on which it "
                "depended; but men are chosen to faith and to the obedience of faith, holiness, etc.; therefore "
                "election is the fountain of every saving good, from which proceeds faith, holiness, and the other "
                "gifts of salvation, and finally eternal life itself, as its fruits and effects, according to that of "
                "the apostle: \"He hath chosen us [not because we were but] that we should be holy, and without "
                "blame, before Him in love\" (Eph. 1:4)."),
            10: ("The good pleasure of God is the sole cause of this gracious election, which doth not consist "
                 "herein, that out of all possible qualities and actions of men God has chosen some as a condition of "
                 "salvation; but that He was pleased out of the common mass of sinners to adopt some certain persons "
                 "as a peculiar people to Himself, as it is written, \"For the children being not yet born, "
                 "neither having done any good or evil,\" etc., it was said (namely to Rebecca): \"The elder shall "
                 "serve the younger. As it is written, Jacob have I loved, but Esau have I hated\" (Rom. 9:11-13). "
                 "\"And as many as were ordained to eternal life believed\" (Acts 13:48)."),
            11: ("And as God Himself is most wise, unchangeable, omniscient and omnipotent, so the election made by "
                 "Him can neither be interrupted nor changed, recalled or annulled; neither can the elect be cast "
                 "away, nor their number diminished."),
            12: ("The elect in due time, though in various degrees and in different measures, attain the assurance of "
                 "this their eternal and unchangeable election, not by inquisitively prying into the secret and deep "
                 "things of God, but by observing in themselves, with a spiritual joy and holy pleasure, "
                 "the infallible fruits of election pointed out in the Word of God — such as a true faith in Christ, "
                 "filial fear, a godly sorrow for sin, a hungering and thirsting after righteousness, etc."),
            13: ("The sense and certainty of this election afford to the children of God additional matter for daily "
                 "humiliation before Him, for adoring the depth of His mercies, for cleansing themselves, "
                 "and rendering grateful returns of ardent love to Him, who first manifested so great love towards "
                 "them. The consideration of this doctrine of election is so far from encouraging remissness in the "
                 "observance of the divine commands or from sinking men in carnal security, that these, in the just "
                 "judgment of God, are the usual effects of rash presumption or of idle and wanton trifling with the "
                 "grace of election in those who refuse to walk in the ways of the elect."),
            14: ("As the doctrine of divine election by the most wise counsel of God was declared by the prophets, "
                 "by Christ Himself, and by the apostles, and is clearly revealed in the Scriptures, both of the Old "
                 "and New Testament, so it is still to be published in due time and place in the Church of God, "
                 "for which it was peculiarly designed, provided it be done with reverence, in the spirit of "
                 "discretion and piety, for the glory of God's most holy Name, and for enlivening and comforting His "
                 "people, without vainly attempting to investigate the secret ways of the Most High. \"For I have not "
                 "shunned to declare unto you all the counsel of God\" (Acts 20:27); \"O the depth of the riches both "
                 "of the wisdom and knowledge of God! how unsearchable are His judgments, and His ways past finding "
                 "out! For who hath known the mind of the Lord? or who hath been His counsellor?\" (Rom. 11:33–34); "
                 "\"For I say, through the grace given unto me, to every man that is among you, not to think of "
                 "himself more highly than he ought to think; but to think soberly, according as God hath dealt to "
                 "every man the measure of faith\" (Rom. 12:3); \"Wherein God, willing more abundantly to shew unto "
                 "the heirs of promise the immutability of His counsel, confirmed it by an oath: that by two "
                 "immutable things, in which it was impossible for God to lie, we might have a strong consolation, "
                 "who have fled for refuge to lay hold upon the hope set before us\" (Heb. 6:17–18)."),
            15: ("What peculiarly tends to illustrate and recommend to us the eternal and unmerited grace of "
                 "election, is the express testimony of sacred Scripture that not all, but some only are elected, "
                 "while others are passed by in the eternal decree; whom God, out of His sovereign, most just, "
                 "irreprehensible and unchangeable good pleasure, hath decreed to leave in the common misery into "
                 "which they have wilfully plunged themselves, and not to bestow upon them saving faith and the grace "
                 "of conversion; but permitting them in His just judgment to follow their own ways, at last for the "
                 "declaration of His justice, to condemn and perish them forever, not only on account of their "
                 "unbelief, but also for all their other sins. And this is the decree of reprobation which by no "
                 "means makes God the author of sin (the very thought of which is blasphemy), but declares Him to be "
                 "an awful, irreprehensible, and righteous Judge and avenger thereof."),
            16: ("Those who do not yet experience a lively faith in Christ, an assured confidence of soul, peace of "
                 "conscience, an earnest endeavor after filial obedience, and glorying in God through Christ, "
                 "efficaciously wrought in them, and do nevertheless persist in the use of the means which God hath "
                 "appointed for working these graces in us, ought not to be alarmed at the mention of reprobation, "
                 "nor to rank themselves among the reprobate, but diligently to persevere in the use of means, "
                 "and with ardent desires devoutly and humbly to wait for a season of richer grace. Much less cause "
                 "have they to be terrified by the doctrine of reprobation, who, though they seriously desire to be "
                 "turned to God, to please Him only, and to be delivered from the body of death, cannot yet reach "
                 "that measure of holiness and faith to which they aspire; since a merciful God has promised that He "
                 "will not quench the smoking flax nor break the bruised reed. But this doctrine is justly terrible "
                 "to those, who, regardless of God and of the Savior Jesus Christ, have wholly given themselves up to "
                 "the cares of the world and the pleasures of the flesh, so long as they are not seriously converted "
                 "to God."),
            17: ("Since we are to judge of the will of God from His Word which testifies that the children of "
                 "believers are holy, not by nature, but in virtue of the covenant of grace, in which they, "
                 "together with the parents, are comprehended, godly parents have no reason to doubt of the election "
                 "and salvation of their children whom it pleaseth God to call out of this life in their infancy."),
            18: ("To those who murmur at the free grace of election and just severity of reprobation, we answer with "
                 "the apostle: \"Nay but, O man, who art thou that repliest against God?\" (Rom. 9:20), and quote the "
                 "language of our Savior: \"Is it not lawful for Me to do what I will with Mine own?\" (Matt. 20:15). "
                 "And therefore with holy adoration of these mysteries, we exclaim in the words of the apostle: \"O "
                 "the depth of the riches both of the wisdom and knowledge of God! how unsearchable are His "
                 "judgments, and His ways past finding out! For who hath known the mind of the Lord? or who hath been "
                 "His counsellor? Or who hath first given to Him, and it shall be recompensed unto him again? For of "
                 "Him, and through Him, and to Him, are all things: to whom be glory for ever. Amen\" (Rom. 11:33– "
                 "36).")
        },
        2: {
            0: "**SECOND HEAD OF DOCTRINE**\n\n>**Of the Death of Christ and the Redemption of Men Thereby**",
            1: ("God is not only supremely merciful, but also supremely just. And His justice requires (as He hath "
                "revealed Himself in His Word), that our sins committed against His infinite majesty should be "
                "punished, not only with temporal, but with eternal punishment, both in body and soul; which we "
                "cannot escape unless satisfaction be made to the justice of God."),
            2: ("Since therefore we are unable to make that satisfaction in our own persons or to deliver ourselves "
                "from the wrath of God, He hath been pleased in His infinite mercy to give His only begotten Son, "
                "for our surety, who was made sin, and became a curse for us and in our stead, that He might make "
                "satisfaction to divine justice on our behalf."),
            3: ("The death of the Son of God is the only and most perfect sacrifice and satisfaction for sin, "
                "and is of infinite worth and value, abundantly sufficient to expiate the sins of the whole world."),
            4: ("This death derives its infinite value and dignity from these considerations because the person who "
                "submitted to it was not only really man and perfectly holy, but also the only begotten Son of God, "
                "of the same eternal and infinite essence with the Father and the Holy Spirit, which qualifications "
                "were necessary to constitute Him a Savior for us; and because it was attended with a sense of the "
                "wrath and curse of God due to us for sin."),
            5: ("Moreover, the promise of the gospel is, that whosoever believeth in Christ crucified, shall not "
                "perish, but have everlasting life. This promise, together with the command to repent and believe, "
                "ought to be declared and published to all nations, and to all persons promiscuously and without "
                "distinction, to whom God out of His good pleasure sends the gospel."),
            6: ("And whereas many who are called by the gospel do not repent nor believe in Christ, but perish in "
                "unbelief, this is not owing to any defect or insufficiency in the sacrifice offered by Christ upon "
                "the cross, but is wholly to be imputed to themselves."),
            7: ("But as many as truly believe, and are delivered and saved from sin and destruction through the death "
                "of Christ, are indebted for this benefit solely to the grace of God, given them in Christ from "
                "everlasting, and not to any merit of their own."),
            8: ("For this was the sovereign counsel, and most gracious will and purpose of God the Father, "
                "that the quickening and saving efficacy of the most precious death of His Son should extend to all "
                "the elect, for bestowing upon them alone the gift of justifying faith, thereby to bring them "
                "infallibly to salvation: that is, it was the will of God, that Christ by the blood of the cross, "
                "whereby He confirmed the new covenant, should effectually redeem out of every people, tribe, nation, "
                "and language, all those, and those only, who were from eternity chosen to salvation and given to Him "
                "by the Father; that He should confer upon them faith, which together with all the other saving gifts "
                "of the Holy Spirit, He purchased for them by His death; should purge them from all sin, "
                "both original and actual, whether committed before or after believing; and having faithfully "
                "preserved them even to the end, should at last bring them free from every spot and blemish to the "
                "enjoyment of glory in His own presence forever."),
            9: ("This purpose proceeding from everlasting love towards the elect has from the beginning of the world "
                "to this day been powerfully accomplished, and will henceforward still continue to be accomplished, "
                "notwithstanding all the ineffectual opposition of the gates of hell, so that the elect in due time "
                "may be gathered together into one, and that there never may be wanting a church composed of "
                "believers, the foundation of which is laid in the blood of Christ, which may steadfastly love and "
                "faithfully serve Him as their Savior, who as a bridegroom for his bride, laid down His life for them "
                "upon the cross, and which may celebrate His praises here and through all eternity.")
        },
        3: {
            0: ("**THIRD AND FOURTH HEADS OF DOCTRINE**\n\n>**Of the Corruption of Man, His Conversion to God, "
                "and the Manner Thereof**"),
            1: ("Man was originally formed after the image of God. His understanding was adorned with a true and "
                "saving knowledge of his Creator and of spiritual things; his heart and will were upright; all his "
                "affections pure; and the whole man was holy; but revolting from God by the instigation of the devil, "
                "and abusing the freedom of his own will, he forfeited these excellent gifts; and on the contrary "
                "entailed on himself blindness of mind, horrible darkness, vanity and perverseness of judgment, "
                "became wicked, rebellious, and obdurate in heart and will, and impure in his affections."),
            2: ("Man after the fall begat children in his own likeness. A corrupt stock produced a corrupt offspring. "
                "Hence all the posterity of Adam, Christ only excepted, have derived corruption from their original "
                "parent, not by imitation, as the Pelagians of old asserted, but by the propagation of a vicious "
                "nature."),
            3: ("Therefore all men are conceived in sin, and by nature children of wrath, incapable of saving good, "
                "prone to evil, dead in sin, and in bondage thereto, and without the regenerating grace of the Holy "
                "Spirit, they are neither able nor willing to return to God, to reform the depravity of their nature, "
                "or to dispose themselves to reformation."),
            4: ("There remain, however, in man since the fall, the glimmerings of natural light, whereby he retains "
                "some knowledge of God, of natural things, and of the differences between good and evil, "
                "and discovers some regard for virtue, good order in society, and for maintaining an orderly external "
                "deportment. But so far is this light of nature from being sufficient to bring him to a saving "
                "knowledge of God and to true conversion, that he is incapable of using it aright even in things "
                "natural and civil. Nay, further, this light, such as it is, man in various ways renders wholly "
                "polluted and holds it in unrighteousness, by doing which he becomes inexcusable before God."),
            5: ("In the same light are we to consider the law of the decalogue, delivered by God to His peculiar "
                "people the Jews by the hands of Moses. For though it discovers the greatness of sin, and more and "
                "more convinces man thereof, yet as it neither points out a remedy nor imparts strength to extricate "
                "him from misery, and thus being weak through the flesh leaves the transgressor under the curse, "
                "man cannot by this law obtain saving grace."),
            6: ("What therefore neither the light of nature, nor the law could do, that God performs by the operation "
                "of the Holy Spirit through the Word or ministry of reconciliation, which is the glad tidings "
                "concerning the Messiah, by means whereof it hath pleased God to save such as believe, as well under "
                "the Old, as under the New Testament."),
            7: ("This mystery of His will God discovered to but a small number under the Old Testament; under the New "
                "(the distinction between various peoples having been removed), He reveals Himself to many without "
                "any distinction of people. The cause of this dispensation is not to be ascribed to the superior "
                "worth of one nation above another, nor to their making a better use of the light of nature, "
                "but results wholly from the sovereign good pleasure and unmerited love of God. Hence they, "
                "to whom so great and so gracious a blessing is communicated above their desert, or rather "
                "notwithstanding their demerits, are bound to acknowledge it with humble and grateful hearts, "
                "and with the apostle to adore, not curiously to pry into the severity and justice of God's judgments "
                "displayed to others, to whom this grace is not given."),
            8: ("As many as are called by the gospel are unfeignedly called. For God hath most earnestly and truly "
                "declared in His Word what will be acceptable to Him; namely, that all who are called, should comply "
                "with the invitation. He, moreover, seriously promises eternal life and rest to as many as shall come "
                "to Him and believe on Him."),
            9: ("It is not the fault of the gospel nor of Christ, offered therein, nor of God, who calls men by the "
                "gospel and confers upon them various gifts, that those who are called by the ministry of the Word "
                "refuse to come and be converted. The fault lies in themselves, some of whom when called, regardless "
                "of their danger, reject the word of life; others, though they receive it, suffer it not to make a "
                "lasting impression on their heart; therefore, their joy, arising only from a temporary faith, "
                "soon vanishes and they fall away; while others choke the seed of the Word by perplexing cares and "
                "the pleasures of this world, and produce no fruit. This our Savior teaches in the parable of the "
                "sower (Matt. 13)."),
            10: ("But that others who are called by the gospel obey the call and are converted is not to be ascribed "
                 "to the proper exercise of free will, whereby one distinguishes himself above others, "
                 "equally furnished with grace sufficient for faith and conversions as the proud heresy of Pelagius "
                 "maintains; but it must be wholly ascribed to God, who as He has chosen His own from eternity in "
                 "Christ, so He confers upon them faith and repentance, rescues them from the power of darkness, "
                 "and translates them into the kingdom of His own Son, that they may show forth the praises of Him "
                 "who hath called them out of darkness into His marvelous light; and may glory not in themselves, "
                 "but in the Lord according to the testimony of the apostles in various places."),
            11: ("But when God accomplishes His good pleasure in the elect or works in them true conversion, "
                 "He not only causes the gospel to be externally preached to them and powerfully illuminates their "
                 "mind by His Holy Spirit, that they may rightly understand and discern the things of the Spirit of "
                 "God; but by the efficacy of the same regenerating Spirit, pervades the inmost recesses of the man; "
                 "He opens the closed, and softens the hardened heart, and circumcises that which was uncircumcised, "
                 "infuses new qualities into the will, which though heretofore dead, He quickens; from being evil, "
                 "disobedient, and refractory, He renders it good, obedient, and pliable; actuates and strengthens "
                 "it, that like a good tree, it may bring forth the fruits of good actions."),
            12: ("And this is the regeneration so highly celebrated in Scripture and denominated a new creation: a "
                 "resurrection from the dead, a making alive, which God works in us without our aid. But this is in "
                 "no wise effected merely by the external preaching of the gospel, by moral suasion, or such a mode "
                 "of operation, that after God has performed His part, it still remains in the power of man to be "
                 "regenerated or not, to be converted or to continue unconverted; but it is evidently a supernatural "
                 "work, most powerful, and at the same time most delightful, astonishing, mysterious, and ineffable; "
                 "not inferior in efficacy to creation or the resurrection from the dead, as the Scripture inspired "
                 "by the author of this work declares; so that all in whose heart God works in this marvelous manner "
                 "are certainly, infallibly, and effectually regenerated, and do actually believe. Whereupon the will "
                 "thus renewed is not only actuated and influenced by God, but in consequence of this influence, "
                 "becomes itself active. Wherefore also, man is himself rightly said to believe and repent, "
                 "by virtue of that grace received"),
            13: ("The manner of this operation cannot be fully comprehended by believers in this life. "
                 "Notwithstanding which, they rest satisfied with knowing and experiencing that by this grace of God "
                 "they are enabled to believe with the heart, and love their Savior."),
            14: ("Faith is therefore to be considered as the gift of God, not on account of its being offered by God "
                 "to man, to be accepted or rejected at his pleasure; but because it is in reality conferred, "
                 "breathed, and infused into him; or even because God bestows the power or ability to believe, "
                 "and then expects that man should by the exercise of his own free will, consent to the terms of "
                 "salvation and actually believe in Christ; but because He who works in man both to will and to do, "
                 "and indeed all things in all, produces both the will to believe and the act of believing also."),
            15: ("God is under no obligation to confer this grace upon any; for how can He be indebted to man, "
                 "who had no previous gifts to bestow, as a foundation for such recompense? Nay, who has nothing of "
                 "his own but sin and falsehood? He therefore who becomes the subject of this grace, owes eternal "
                 "gratitude to God, and gives Him thanks forever. Whoever is not made partaker thereof, "
                 "is either altogether regardless of these spiritual gifts and satisfied with his own condition, "
                 "or is in no apprehension of danger and vainly boasts the possession of that which he has not. With "
                 "respect to those who make an external profession of faith and live regular lives, we are bound, "
                 "after the example of the apostle, to judge and speak of them in the most favorable manner. For the "
                 "secret recesses of the heart are unknown to us. And as to others, who have not yet been called, "
                 "it is our duty to pray for them to God, who calls the things that are not, as if they were. But we "
                 "are in no wise to conduct ourselves towards them with haughtiness, as if we had made ourselves to "
                 "differ."),
            16: ("But as man by the fall did not cease to be a creature endowed with understanding and will, "
                 "nor did sin which pervaded the whole race of mankind deprive him of the human nature, but brought "
                 "upon him depravity and spiritual death; so also this grace of regeneration does not treat men as "
                 "senseless stocks and blocks, nor takes away their will and its properties, neither does violence "
                 "thereto; but spiritually quickens, heals, corrects, and at the same time sweetly and powerfully "
                 "bends it; that where carnal rebellion and resistance formerly prevailed, a ready and sincere "
                 "spiritual obedience begins to reign, in which the true and spiritual restoration and freedom of our "
                 "will consist. Wherefore unless the admirable Author of every good work wrought in us, "
                 "man could have no hope of recovering from his fall by his own free will, by the abuse of which, "
                 "in a state of innocence, he plunged himself into ruin."),
            17: ("As the almighty operation of God, whereby He prolongs and supports this our natural life, "
                 "does not exclude, but requires the use of means, by which God of His infinite mercy and goodness "
                 "hath chosen to exert His influence, so also the beforementioned supernatural operation of God, "
                 "by which we are regenerated, in no wise excludes or subverts the use of the gospel, which the most "
                 "wise God has ordained to be the seed of regeneration and food of the soul. Wherefore, "
                 "as the apostles, and teachers who succeeded them, piously instructed the people concerning this "
                 "grace of God, to His glory, and the abasement of all pride, and in the meantime, however, "
                 "neglected not to keep them by the sacred precepts of the gospel in the exercise of the Word, "
                 "sacraments and discipline; so even to this day, be it far from either instructors or instructed to "
                 "presume to tempt God in the church by separating what He of His good pleasure hath most intimately "
                 "joined together. For grace is conferred by means of admonitions; and the more readily we perform "
                 "our duty, the more eminent usually is this blessing of God working in us, and the more directly is "
                 "His work advanced; to whom alone all the glory both of means, and of their saving fruit and "
                 "efficacy is forever due. Amen.")
        },
        4: {
            0: ("**THIRD AND FOURTH HEADS OF DOCTRINE**\n\n>**Of the Corruption of Man, His Conversion to God, "
                "and the Manner Thereof**"),
            1: ("Man was originally formed after the image of God. His understanding was adorned with a true and "
                "saving knowledge of his Creator and of spiritual things; his heart and will were upright; all his "
                "affections pure; and the whole man was holy; but revolting from God by the instigation of the devil, "
                "and abusing the freedom of his own will, he forfeited these excellent gifts; and on the contrary "
                "entailed on himself blindness of mind, horrible darkness, vanity and perverseness of judgment, "
                "became wicked, rebellious, and obdurate in heart and will, and impure in his affections."),
            2: ("Man after the fall begat children in his own likeness. A corrupt stock produced a corrupt offspring. "
                "Hence all the posterity of Adam, Christ only excepted, have derived corruption from their original "
                "parent, not by imitation, as the Pelagians of old asserted, but by the propagation of a vicious "
                "nature."),
            3: ("Therefore all men are conceived in sin, and by nature children of wrath, incapable of saving good, "
                "prone to evil, dead in sin, and in bondage thereto, and without the regenerating grace of the Holy "
                "Spirit, they are neither able nor willing to return to God, to reform the depravity of their nature, "
                "or to dispose themselves to reformation."),
            4: ("There remain, however, in man since the fall, the glimmerings of natural light, whereby he retains "
                "some knowledge of God, of natural things, and of the differences between good and evil, "
                "and discovers some regard for virtue, good order in society, and for maintaining an orderly external "
                "deportment. But so far is this light of nature from being sufficient to bring him to a saving "
                "knowledge of God and to true conversion, that he is incapable of using it aright even in things "
                "natural and civil. Nay, further, this light, such as it is, man in various ways renders wholly "
                "polluted and holds it in unrighteousness, by doing which he becomes inexcusable before God."),
            5: ("In the same light are we to consider the law of the decalogue, delivered by God to His peculiar "
                "people the Jews by the hands of Moses. For though it discovers the greatness of sin, and more and "
                "more convinces man thereof, yet as it neither points out a remedy nor imparts strength to extricate "
                "him from misery, and thus being weak through the flesh leaves the transgressor under the curse, "
                "man cannot by this law obtain saving grace."),
            6: ("What therefore neither the light of nature, nor the law could do, that God performs by the operation "
                "of the Holy Spirit through the Word or ministry of reconciliation, which is the glad tidings "
                "concerning the Messiah, by means whereof it hath pleased God to save such as believe, as well under "
                "the Old, as under the New Testament."),
            7: ("This mystery of His will God discovered to but a small number under the Old Testament; under the New "
                "(the distinction between various peoples having been removed), He reveals Himself to many without "
                "any distinction of people. The cause of this dispensation is not to be ascribed to the superior "
                "worth of one nation above another, nor to their making a better use of the light of nature, "
                "but results wholly from the sovereign good pleasure and unmerited love of God. Hence they, "
                "to whom so great and so gracious a blessing is communicated above their desert, or rather "
                "notwithstanding their demerits, are bound to acknowledge it with humble and grateful hearts, "
                "and with the apostle to adore, not curiously to pry into the severity and justice of God's judgments "
                "displayed to others, to whom this grace is not given."),
            8: ("As many as are called by the gospel are unfeignedly called. For God hath most earnestly and truly "
                "declared in His Word what will be acceptable to Him; namely, that all who are called, should comply "
                "with the invitation. He, moreover, seriously promises eternal life and rest to as many as shall come "
                "to Him and believe on Him."),
            9: ("It is not the fault of the gospel nor of Christ, offered therein, nor of God, who calls men by the "
                "gospel and confers upon them various gifts, that those who are called by the ministry of the Word "
                "refuse to come and be converted. The fault lies in themselves, some of whom when called, regardless "
                "of their danger, reject the word of life; others, though they receive it, suffer it not to make a "
                "lasting impression on their heart; therefore, their joy, arising only from a temporary faith, "
                "soon vanishes and they fall away; while others choke the seed of the Word by perplexing cares and "
                "the pleasures of this world, and produce no fruit. This our Savior teaches in the parable of the "
                "sower (Matt. 13)."),
            10: ("But that others who are called by the gospel obey the call and are converted is not to be ascribed "
                 "to the proper exercise of free will, whereby one distinguishes himself above others, "
                 "equally furnished with grace sufficient for faith and conversions as the proud heresy of Pelagius "
                 "maintains; but it must be wholly ascribed to God, who as He has chosen His own from eternity in "
                 "Christ, so He confers upon them faith and repentance, rescues them from the power of darkness, "
                 "and translates them into the kingdom of His own Son, that they may show forth the praises of Him "
                 "who hath called them out of darkness into His marvelous light; and may glory not in themselves, "
                 "but in the Lord according to the testimony of the apostles in various places."),
            11: ("But when God accomplishes His good pleasure in the elect or works in them true conversion, "
                 "He not only causes the gospel to be externally preached to them and powerfully illuminates their "
                 "mind by His Holy Spirit, that they may rightly understand and discern the things of the Spirit of "
                 "God; but by the efficacy of the same regenerating Spirit, pervades the inmost recesses of the man; "
                 "He opens the closed, and softens the hardened heart, and circumcises that which was uncircumcised, "
                 "infuses new qualities into the will, which though heretofore dead, He quickens; from being evil, "
                 "disobedient, and refractory, He renders it good, obedient, and pliable; actuates and strengthens "
                 "it, that like a good tree, it may bring forth the fruits of good actions."),
            12: ("And this is the regeneration so highly celebrated in Scripture and denominated a new creation: a "
                 "resurrection from the dead, a making alive, which God works in us without our aid. But this is in "
                 "no wise effected merely by the external preaching of the gospel, by moral suasion, or such a mode "
                 "of operation, that after God has performed His part, it still remains in the power of man to be "
                 "regenerated or not, to be converted or to continue unconverted; but it is evidently a supernatural "
                 "work, most powerful, and at the same time most delightful, astonishing, mysterious, and ineffable; "
                 "not inferior in efficacy to creation or the resurrection from the dead, as the Scripture inspired "
                 "by the author of this work declares; so that all in whose heart God works in this marvelous manner "
                 "are certainly, infallibly, and effectually regenerated, and do actually believe. Whereupon the will "
                 "thus renewed is not only actuated and influenced by God, but in consequence of this influence, "
                 "becomes itself active. Wherefore also, man is himself rightly said to believe and repent, "
                 "by virtue of that grace received"),
            13: ("The manner of this operation cannot be fully comprehended by believers in this life. "
                 "Notwithstanding which, they rest satisfied with knowing and experiencing that by this grace of God "
                 "they are enabled to believe with the heart, and love their Savior."),
            14: ("Faith is therefore to be considered as the gift of God, not on account of its being offered by God "
                 "to man, to be accepted or rejected at his pleasure; but because it is in reality conferred, "
                 "breathed, and infused into him; or even because God bestows the power or ability to believe, "
                 "and then expects that man should by the exercise of his own free will, consent to the terms of "
                 "salvation and actually believe in Christ; but because He who works in man both to will and to do, "
                 "and indeed all things in all, produces both the will to believe and the act of believing also."),
            15: ("God is under no obligation to confer this grace upon any; for how can He be indebted to man, "
                 "who had no previous gifts to bestow, as a foundation for such recompense? Nay, who has nothing of "
                 "his own but sin and falsehood? He therefore who becomes the subject of this grace, owes eternal "
                 "gratitude to God, and gives Him thanks forever. Whoever is not made partaker thereof, "
                 "is either altogether regardless of these spiritual gifts and satisfied with his own condition, "
                 "or is in no apprehension of danger and vainly boasts the possession of that which he has not. With "
                 "respect to those who make an external profession of faith and live regular lives, we are bound, "
                 "after the example of the apostle, to judge and speak of them in the most favorable manner. For the "
                 "secret recesses of the heart are unknown to us. And as to others, who have not yet been called, "
                 "it is our duty to pray for them to God, who calls the things that are not, as if they were. But we "
                 "are in no wise to conduct ourselves towards them with haughtiness, as if we had made ourselves to "
                 "differ."),
            16: ("But as man by the fall did not cease to be a creature endowed with understanding and will, "
                 "nor did sin which pervaded the whole race of mankind deprive him of the human nature, but brought "
                 "upon him depravity and spiritual death; so also this grace of regeneration does not treat men as "
                 "senseless stocks and blocks, nor takes away their will and its properties, neither does violence "
                 "thereto; but spiritually quickens, heals, corrects, and at the same time sweetly and powerfully "
                 "bends it; that where carnal rebellion and resistance formerly prevailed, a ready and sincere "
                 "spiritual obedience begins to reign, in which the true and spiritual restoration and freedom of our "
                 "will consist. Wherefore unless the admirable Author of every good work wrought in us, "
                 "man could have no hope of recovering from his fall by his own free will, by the abuse of which, "
                 "in a state of innocence, he plunged himself into ruin."),
            17: ("As the almighty operation of God, whereby He prolongs and supports this our natural life, "
                 "does not exclude, but requires the use of means, by which God of His infinite mercy and goodness "
                 "hath chosen to exert His influence, so also the beforementioned supernatural operation of God, "
                 "by which we are regenerated, in no wise excludes or subverts the use of the gospel, which the most "
                 "wise God has ordained to be the seed of regeneration and food of the soul. Wherefore, "
                 "as the apostles, and teachers who succeeded them, piously instructed the people concerning this "
                 "grace of God, to His glory, and the abasement of all pride, and in the meantime, however, "
                 "neglected not to keep them by the sacred precepts of the gospel in the exercise of the Word, "
                 "sacraments and discipline; so even to this day, be it far from either instructors or instructed to "
                 "presume to tempt God in the church by separating what He of His good pleasure hath most intimately "
                 "joined together. For grace is conferred by means of admonitions; and the more readily we perform "
                 "our duty, the more eminent usually is this blessing of God working in us, and the more directly is "
                 "His work advanced; to whom alone all the glory both of means, and of their saving fruit and "
                 "efficacy is forever due. Amen.")
        }
    }

    __cdaRegex = r"\[\s*(?:C|Canons)\s*(?:of)?\s*(?:D|Dort|Dordt)\s*(?:A|Article|Articles)\s*([\d\,\-\:\s.]+)\]"

    def __init__(self):
        self.__parse = chapter_paragraph_parser

    def __get_text(self, from_chptr, from_para, to_chptr, to_para):
        if (0 < from_chptr <= to_chptr <= 4) and \
                (0 < from_para <= self.__CHPTRMAX[from_chptr]) and \
                (0 < to_para <= self.__CHPTRMAX[to_chptr]):
            result = ''
            for i in range(from_chptr, to_chptr + 1):
                result += "\n>" + self.__text[i][0] + "\n\n"
                for j in range(from_para if i == from_chptr else 1,
                               to_para + 1 if i == to_chptr else self.__CHPTRMAX[i] + 1):
                    result += ">**Article " + str(j) + "**\n\n>" + self.__text[i][j] + "\n\n"
            return result, False
        else:
            return '', True

    def fetch(self, full_citations):
        response_text = ''
        response_citation = ''
        response_is_malformed = False

        if full_citations:
            cda_citations = re.findall(self.__cdaRegex, full_citations, re.IGNORECASE)
            if cda_citations:
                response_citation = '[CDA '
                args, response_is_malformed = self.__parse(cda_citations)
                for i in args:
                    response_citation += str(i[0]) + ':' + str(i[1]) + "-" + str(i[2]) + ':' + str(i[3]) + ", "
                    quote, temp = self.__get_text(i[0], i[1], i[2], i[3])
                    response_is_malformed |= temp
                    if response_text:
                        response_text += quote
                    elif quote:
                        response_text += "\n**Canons of Dort**\n" + quote
                response_citation = response_citation[:-2] + "]"
        return response_text, response_citation, response_is_malformed
