<h1>Basic concepts of Text Analytics</h1>
One of the most frequent types of day-to-day conversion is text communication. In our
everyday routine, we chat, message, tweet, share status, email, create blogs, and offer
opinions and criticism. All of these actions lead to a substantial amount of unstructured
text being produced. It is critical to examine huge amounts of data in this sector of the
online world and social media to determine people's opinions.
Text mining is also referred to as text analytics. Text mining is a process of exploring
sizable textual data and finding patterns. Text Mining processes the text itself, while NLP
processes with the underlying metadata. Finding frequency counts of words, length of the
sentence, presence/absence of specific words is known as text mining. Natural language
processing is one of the components of text mining. NLP helps identify sentiment,
finding entities in the sentence, and category of blog/article. Text mining is preprocessed
data for text analytics. In Text Analytics, statistical and machine learning algorithms are
used to classify information.

<h1>2. Text Analysis Operations using natural language toolkit</h1>
NLTK(natural language toolkit) is a leading platform for building Python programs to
work with human language data. It provides easy-to-use interfaces and lexical resources
such as WordNet, along with a suite of text processing libraries for classification,
tokenization, stemming, tagging, parsing, and semantic reasoning and many more.
Analysing movie reviews is one of the classic examples to demonstrate a simple NLP
Bag-of-words model, on movie reviews.

<h1>2.1. Tokenization:</h1>
Tokenization is the first step in text analytics. The process of breaking down a text
paragraph into smaller chunks such as words or sentences is called Tokenization.
Token is a single entity that is the building blocks for a sentence or paragraph.
● Sentence tokenization : split a paragraph into list of sentences using
sent_tokenize() method
SNJB’s Late Sau. K B Jain College of Engineering, Chandwad Dist. Nashik, MS
Department of Computer Engineering Subject : DSBDAL
● Word tokenization : split a sentence into list of words using word_tokenize()
method

<h1>2.2. Stop words removal</h1>
Stopwords considered as noise in the text. Text may contain stop words such as is,
am, are, this, a, an, the, etc. In NLTK for removing stopwords, you need to create
a list of stopwords and filter out your list of tokens from these words.

<h1>2.3. Stemming and Lemmatization</h1>
Stemming is a normalization technique where lists of tokenized words are
converted into shortened root words to remove redundancy. Stemming is the
process of reducing inflected (or sometimes derived) words to their word stem,
base or root form.
A computer program that stems word may be called a stemmer.
E.g.
A stemmer reduces the words like fishing, fished, and fisher to the stem fish.
The stem need not be a word, for example the Porter algorithm reduces, argue,
argued, argues, arguing, and argus to the stem argu .
Lemmatization in NLTK is the algorithmic process of finding the lemma of a
word depending on its meaning and context. Lemmatization usually refers to the
morphological analysis of words, which aims to remove inflectional endings. It
helps in returning the base or dictionary form of a word known as the lemma.
Eg. Lemma for studies is study

<h1>Lemmatization Vs Stemming</h1>
Stemming algorithm works by cutting the suffix from the word. In a broader sense
cuts either the beginning or end of the word.
On the contrary, Lemmatization is a more powerful operation, and it takes into
consideration morphological analysis of the words. It returns the lemma which is
the base form of all its inflectional forms. In-depth linguistic knowledge is
SNJB’s Late Sau. K B Jain College of Engineering, Chandwad Dist. Nashik, MS
Department of Computer Engineering Subject : DSBDAL
required to create dictionaries and look for the proper form of the word.
Stemming is a general operation while lemmatization is an intelligent operation
where the proper form will be looked in the dictionary. Hence, lemmatization
helps in forming better machine learning features.

<h1>2.4. POS Tagging</h1>
POS (Parts of Speech) tell us about grammatical information of words of the
sentence by assigning specific token (Determiner, noun, adjective , adverb ,
verb,Personal Pronoun etc.) as tag (DT,NN ,JJ,RB,VB,PRP etc) to each words.
Word can have more than one POS depending upon the context where it is used.
We can use POS tags as statistical NLP tasks. It distinguishes a sense of word
which is very helpful in text realization and infer semantic information from text
for sentiment analysis.

Data Visualisation plays a very important role in Data mining. Various data scientists spent their
time exploring data through visualisation. To accelerate this process we need to have a
well-documentation of all the plots.
Even plenty of resources can’t be transformed into valuable goods without planning and
architecture
<h1>1. Seaborn Library Basics</h1>
Seaborn is a Python data visualisation library based on matplotlib. It provides a
high-level interface for drawing attractive and informative statistical graphics.

<h1>2. Know your data</h1>
The dataset that we are going to use to draw our plots will be the Titanic dataset, which is
downloaded by default with the Seaborn library. All you have to do is use the load_dataset
function and pass it the name of the dataset.
The dataset contains 891 rows and 15 columns and contains information about the passengers
who boarded the unfortunate Titanic ship. The original task is to predict whether or not the
passenger survived depending upon different features such as their age, ticket, cabin they
boarded, the class of the ticket, etc. We will use the Seaborn library to see if we can find any
patterns in the data.

<h1>Joint Plot</h1>
● It is the combination of the distplot of two variables.
● It is an example of bivariate analysis.
SNJB’s Late Sau. K B Jain College of Engineering, Chandwad Dist. Nashik, MS
Department of Computer Engineering Subject : DSBDAL
● We additionally obtain a scatter plot between the variables to reflect their linear
relationship. We can customise the scatter plot into a hexagonal plot, where, the
more the colour intensity, the more will be the number of observations.

<h1>Histoplot</h1>
In Seaborn, histplot is a function that allows you to create a histogram to visualize the distribution of a univariate (single-variable) dataset. It provides a convenient way to understand the frequency or count of observations falling into different bins or intervals.By default, histplot automatically determines the appropriate number of bins based on the data range and distribution. However, you can customize the number of bins by specifying the bins parameter in the function call.
The resulting histogram displays the count or frequency of observations falling within each bin. The x-axis represents the variable values, and the y-axis represents the count or frequency.
histplot in Seaborn offers additional options and parameters to customize the appearance of the histogram, such as specifying color, adding a kernel density estimate, adjusting bin width, adding labels, and more. 

<h1>The Box Plot</h1>
The box plot is used to display the distribution of the categorical data in the form of quartiles.
The centre of the box shows the median value. The value from the lower whisker to the bottom
of the box shows the first quartile. From the bottom of the box to the middle of the box lies the
second quartile. From the middle of the box to the top of the box lies the third quartile and finally
from the top of the box to the top whisker lies the last quartile.
Now let's plot a box plot that displays the distribution for the age with respect to each gender.
You need to pass the categorical column as the first parameter (which is sex in our case) and the
numeric column (age in our case) as the second parameter.
