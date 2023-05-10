# [Convo-Sense](http://sdp.ecs.umass.edu/sdp23/team06/)

### Team: Anthony Carneiro, [Sohan Show](https://github.com/sohanshow), Jessica Peters, David Price, [Professor Tilman Wolf](https://people.umass.edu/wolf/)


## Problem Statement:
Everyone has been in a situation where either you or the person you are talking to needs to interrupt the conversation in order to look something up. It breaks the train of thought, causes you to divert attention away from the speaker, and in some cases can be rude. Or maybe you cannot keep up with a lecture, and end up losing valuable intuition about a subject simply because you do not understand a term.

Therefore, we decided to develop a system to mitigate this problem and automate the entire reference searching and note taking process during a conversation. Convo-sense listens to conversation between two peole and does offline analysis to find out relevant context and keywords of the conversation. This preserves user privacy and automates reference searching and note taking for the user.

## Specifications:

### The system should be able to:
- Detect conversation from up to 6 feet away.
- Audio signal converted to digital text with 95% accuracy from close range and 87% accuracy from 6 feet away.
- Capture more than 110 words per minute.
- Support four user professions (Engineer, Medical,
Financial, and Law).
- Display reference material in less than 6 seconds
from the time of speech.
- Is Compatible with any system so long as there is an
internet connection and microphone support.
- Run on a microcontroller.

## How to run on any micro-controller:

There are a few things that you need to make sure before starting with the testing:
 - Make sure that the micro-controller runs Linux or any OS that supports python3.
 - Make sure you have your API keys ready for openai and GoogleImageSearch for the reference script.

#### Once you have all of these:
1. ```git clone https://github.com/sohanshow/Convo_Sense_Public.git``` into a valid ```dir``` in your OS.
2. ```cd``` into the ```dir``` and initiate ```python3 app.py```

## References and Acknowledgements:

- [1] “Voice frequency,” Wikipedia, 22-Jul-2022. [Online]. Available:
https://en.wikipedia.org/wiki/Voice_frequency. [Accessed: 27-Oct-2022].
- [2] P. author B. jpolanowski and Post author By Jairo, “Arch Linux and Eduroam on a Raspberry
Pi, No Ethernet Cable Required,” Techbytes. [Online]. Available:
https://blogs.umass.edu/Techbytes/tag/eduroam/. [Accessed: 27-Oct-2022].
- [3] Cephei, Alpha. Vosk Offline Speech Recognition API, https://alphacephei.com/vosk/.
- [4] SpaCy, Industrial-Strength Natural Language Processing, https://spacy.io/
- [5] NLTK, Natural Language Toolkit, https://www.nltk.org/
- [6] OpenAI API, https://openai.com
- [7] Google Images Search, https://cloud.google.com/







