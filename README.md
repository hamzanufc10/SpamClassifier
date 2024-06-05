# SpamClassifier


Hello my name is hamza shakeel i have overall 5+ year experience out of which 4 year is in python,ml,ds,sql
i have worked for 2 company namely TCS,kyndrl ibm.In tcs used to work as fulltime ml/python developer 
i worked on retial based company and categorical dataset and classifaction algos like random,svc,decion tree.
Also created a chatgpt like solotion on retial dataset using LLm,langchain,google palm,hugging face
in kyndryl i am woring on cloud tech like openstack,openshift,aws,promethue,elk for montiorning and logging solution.



PITCH --

1.Get data after scanning of botel
2.Clean data using verious NLP technique(lower case,remove punt,alpha numeric,remove stopwords,single-double work remover,tokentization,lemization)
3.Vectoriization (Bag of words,TF-IDF)
4.Feature Engineering (Smote technique to balance data,Chi square test)
5.train test split
6.Model train (Linear SVC)
7.Confusion matrix Model Evaluation, Tuning, 


5g chatbot -

1.Data source - excel sheet with historic Q&A (CSVloader)
2.creating embeeding(from text to numeric) of data (Hugging face)
3.save those embeeding into vector database (Chroma)
4.the question asked by user will convert into embedding and search in the vector database which Q&A embeeding matches the most. (Retervial QA)
5.Those embedding will convert into text and a promt will be create and be given to LLM and LLM will give human readble answer.(Google Palm)


LLM-SQL --

1.Taking to sql in plain english langauge
2.Convert text into sql querty using google palm sqlsequentialchain.
3.create Fewshot learning so that model doesnt fail
4.creating embeeding(from text to numeric) of data (Hugging face)
5.save those embeeding into vector database (ChromaDB)
6.Few shot promt template (SQLdatabase chain)
	

SMS-Classifier --

1)Read the csv
2)Impute missing value,remove unnecessary column,remove duplicate value
3)LabelEncoding of ouput column to 0 and 1
4)Feture enginnering -- Make 3 column out of 1 column based on number_character,number_sentence(sent_tokenize),number_words(word_tokenize)
5)check correlation if someone is highly correleted among themsleve remove one of them
6)dowload nltk.download('punkt')
7)Do Data preporcessing -tokenize,remove alphanumeric,stopwords,stemming
8)Model building --vectorize using TF-IDF,train_tst_spli,use naieve baies
9)pickle and use in flask app
