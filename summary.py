#gensim.summarization.summarizer.summarize
from gensim.summarization import summarize 
from typing import List, Dict, NewType
from datetime import datetime
import json


Message = Dict[str, datetime]

def load_sample(file='sample.json'):
    with open(file, 'r') as f:
        return json.load(f)

def representative_msgs(messages: List[Message]) -> List[Message]:
    #print(messages)
    #return messages
    text=""
    for each_message in messages:
    	text=text+each_message["message"]
    return text
    pass

def summary(text):
	print ("summary")
	print(summarize(text, ratio=0.1, split=False)) 
	print ("representative sentences")
	print (summarize(text, ratio=0.1,split=True))

if __name__ == '__main__':
    #text=representative_msgs(load_sample())
    text="The Trump administration has brought a Qaeda suspect to the United States to face trial in federal court, backing off its hard-line position that terrorism suspects should be sent to the naval prison in Guantánamo Bay, Cuba, rather than to civilian courtrooms.The suspect, Ali Charaf Damache, was transferred from Spain and appeared on Friday in federal court in Philadelphia, making him the first foreigner brought to the United States to face terrorism charges under President Trump. The authorities believe Mr. Damache was a Qaeda recruiter. He was charged with helping plot to kill a Swedish cartoonist who depicted the Prophet Muhammad in cartoons.\
Attorney General Jeff Sessions has repeatedly said that terrorism suspects should be held and prosecuted at Guantánamo Bay. Mr. Sessions said that terrorists did not deserve the same legal rights as common criminals and that such trials were too dangerous to hold on American soil. With Mr. Damache’s transfer, Mr. Sessions has adopted a strategy that he vehemently opposed when it was carried out under President Barack Obama.\
The Justice Department did not immediately respond to questions about whether Mr. Sessions had changed his views on civilian trials or why Mr. Damache was being brought to federal court.For years, Republicans portrayed civilian trials as a weakness in Mr. Obama’s national security policy. His plan to prosecute Khalid Shaikh Mohammed, the admitted mastermind of the Sept. 11 attacks, in Manhattan fizzled amid controversy. Since then, however, federal prosecutors have consistently won convictions and lengthy prison sentences for foreign terrorists and helped glean crucial intelligence.Continue reading the main story The Trump White House\
The historic moments, head-spinning developments and inside-the-White House intrigue.\
ISIS Leader Is Still Alive, Pentagon Chief Says\
JUL 21\
From Facebook Live: Peter Baker Discusses An Exclusive Interview With Trump\
JUL 21\
Trump’s Leader for FEMA Wins Praise, but Proposed Budget Cuts Don’t\
JUL 21\
Sean Spicer Resigns as White House Press Secretary\
JUL 21\
Trump May Turn to Anthony Scaramucci for White House Communications Post\
JUL 20\
See More »\
RECENT COMMENTS\
vulcanalex 44 minutes ago\
What a joke the headline is, I bet the president was not even aware of this minor thing Sessions might have made this decision, or perhaps...\
Inkblot 1 hour ago\
1. Why US jurisdiction? Wasn't this a crime committed on Swedish soil against a Swedish citizen by a non-US citizen?2. Even if US can claim...\
PSadlon 1 hour ago\
This is one of the very few things I agree with Trump doing though I agree with everyone here he's doing it for entirely the wrong reasons.\
SEE ALL COMMENTS  WRITE A COMMENT\
RELATED COVERAGE A Holder Legacy: Shifting Terror Cases to the Civilian Courts, and Winning OCT. 21, 2014\
Spain Arrests Terrorism Suspect in Plot Against Swedish Artist DEC. 11, 2015\
“It’s good to see that the president and the attorney general now seem to share my belief in the effectiveness of the world’s greatest judicial system and its ability to keep the American people safe,” said former Attorney General Eric H. Holder Jr., the leading voice in the Obama administration for using civilian courts. “Their previous positions were political and counterproductive.”\
Mr. Damache’s transfer represents a collision of the Trump administration’s tough rhetoric and the reality of fighting terrorism in 2017. Though Mr. Trump has promised to fill Guantánamo Bay with “bad dudes,” nations worldwide, including America’s most important allies, have come to regard the prison there as a legal morass and a symbol of American abuse and mistreatment.\
Mr. Damache, 52, a dual Algerian and Irish citizen, was arrested in Ireland in 2010. But he was released after an Irish judge rejected a request from the United States to extradite him. He was arrested again in 2015 in Spain. Under Mr. Obama, the Justice Department began seeking his extradition, and that effort continued under Mr. Trump. Had the Trump administration insisted on bringing Mr. Damache to Guantánamo Bay, it would have met strong opposition from Europe.\
Mr. Damache was wanted in connection with a failed attempt to kill a Swedish cartoonist who had depicted the Prophet Muhammad with a dog’s body. His identity surfaced in the high-profile case of Colleen LaRose, who became known as “Jihad Jane.” Ms. LaRose, of Pennsburg, Pa., pleaded guilty in 2011 to providing support to a terrorist group, conspiring to murder a foreigner and lying to the F.B.I. She was sentenced in 2014 to 10 years in prison."
    #print (text)
    summary(text)


