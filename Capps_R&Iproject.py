import csv #import csv library with functions to manipulate csv
stopwords=['america','american','americans','president','citizens','our','citizen','people','nation','country','applause','and','the','of','to','with','other','who','in','shall','or','be','is','are','a','an','for','as','their','theirs','they','them','we','you','no','such','this','that','those','by','on','onto','into','not','its','from','by','also','too','upon']
from gensim.parsing.preprocessing import remove_stopwords
from wordcloud import WordCloud
from matplotlib import pyplot as plt

#Bring in Obama's address as a text file
file1=open('obama_speech.txt') #REPLACE WITH WHAT I DO 
#transform into text

unfiltered_obama_speech=file1.read()
obama_speech = remove_stopwords(unfiltered_obama_speech)

#CLEAN THE TEXT
things_to_eliminate=['.',',',';',':','-','—','(',')','[',']',"'",'"','\n','\t',"’"]
for thing in things_to_eliminate:
    obama_speech=obama_speech.replace(thing,' ')

#clean double space
while '  ' in obama_speech: #while loop
    obama_speech=obama_speech.replace('  ',' ') #easiest way to clean double space

obama_speech=obama_speech.lower()

obama_words=obama_speech.split(' ')
#print (obama_words)

obama_dictionary={}
obama_total_of_words=len(obama_words)
obama_text=''
for word in obama_words:
    if word not in stopwords and len(word)>2:
        obama_text=obama_text+' '+word
        if word not in obama_dictionary.keys():
            obama_dictionary[word]=1
        else:
            obama_dictionary[word]=obama_dictionary[word]+1
obama_wordcloud=WordCloud(width=6000, height=8000, random_state=1, collocations=False, max_words=75,background_color='blue',colormap='Reds').generate(obama_text)

#calculate percentages
for key,item in obama_dictionary.items():
    obama_dictionary[key]=round((item/obama_total_of_words)*100,2)
    
#order dictionary
obama_sorted_words=sorted(obama_dictionary.items(),key=lambda x:x[1],reverse=True)
#print(obama_sorted_words)
#
#
#
#
#
#Bring in Trump's address as a text file
file2=open('trump_speech.txt') #REPLACE WITH WHAT I DO 
#transform into text
unfiltered_trump_speech=file2.read()
trump_speech = remove_stopwords(unfiltered_trump_speech)

#CLEAN THE TEXT
things_to_eliminate=['.',',',';',':','-','—','(',')','[',']',"'",'"','\n','\t',"’"]
for thing in things_to_eliminate:
    trump_speech=trump_speech.replace(thing,' ')
    
#clean double space
while '  ' in trump_speech: #while loop
    trump_speech=trump_speech.replace('  ',' ') #easiest way to clean double space

trump_speech=trump_speech.lower()

trump_words=trump_speech.split(' ')
#print (trump_words)

trump_dictionary={}
trump_total_of_words=len(trump_words)
trump_text=''

for word in trump_words:
    if word not in stopwords and len(word)>2:
        trump_text=trump_text+' '+word
        if word not in trump_dictionary.keys():
            trump_dictionary[word]=1
        else:
            trump_dictionary[word]=trump_dictionary[word]+1
trump_wordcloud=WordCloud(width=6000, height=8000, random_state=1, collocations=False, max_words=75,background_color='red',colormap='Blues').generate(trump_text)

#calculate percentages
for key,item in trump_dictionary.items():
    trump_dictionary[key]=round((item/trump_total_of_words)*100,2)
    
#order dictionary
trump_sorted_words=sorted(trump_dictionary.items(),key=lambda x:x[1],reverse=True)
#print(trump_sorted_words)
#
#
#
#
#
#Bring in Biden's address from a text file
file3=open('biden_speech.txt') #REPLACE WITH WHAT I DO 
#transform into text

unfiltered_biden_speech=file3.read()
biden_speech = remove_stopwords(unfiltered_biden_speech)

#CLEAN THE TEXT
things_to_eliminate=['.',',',';',':','-','—','(',')','[',']',"'",'"','\n','\t',"’"]
for thing in things_to_eliminate:
    biden_speech=biden_speech.replace(thing,' ')
    
#clean double space
while '  ' in biden_speech: #while loop
    biden_speech=biden_speech.replace('  ',' ') #easiest way to clean double space

biden_speech=biden_speech.lower()

biden_words=biden_speech.split(' ')
#print(biden_words)

biden_dictionary={}
biden_total_of_words=len(biden_words)
biden_text=''

for word in biden_words:
    if word not in stopwords and len(word)>2:
        biden_text=biden_text+' '+word
        if word not in biden_dictionary.keys():
            biden_dictionary[word]=1
        else:
            biden_dictionary[word]=biden_dictionary[word]+1
biden_wordcloud=WordCloud(width=6000, height=8000, random_state=1, collocations=False, max_words=75,background_color='blue',colormap='Reds').generate(biden_text)

#calculate percentages
for key,item in biden_dictionary.items():
    biden_dictionary[key]=round((item/biden_total_of_words)*100,2)
    
#order dictionary
biden_sorted_words=sorted(biden_dictionary.items(),key=lambda x:x[1],reverse=True)
#print(biden_sorted_words)
#
#
#
#
#
#create output file
output_file=open("address_analysis.csv","w") #open this file for writing
#create a writer
my_writer=csv.writer(output_file) #create a writer, which is the agent
#that will write the data into the file

for (key,item) in obama_sorted_words:
    my_writer.writerow([key,item,"obama"])
for (key,item) in trump_sorted_words:
    my_writer.writerow([key,item,"trump"])
for (key,item) in biden_sorted_words:
    my_writer.writerow([key,item,"biden"])


output_file.close()

fig=plt.figure(figsize=(10,7))
plt.title("2013-2021 U.S Inaugural Addresses", fontsize=20)
plt.axis('off')

fig.add_subplot(1,3,1)
plt.imshow(obama_wordcloud)
plt.title("Obama 2013")
plt.axis('off')

fig.add_subplot(1,3,2)
plt.imshow(trump_wordcloud)
plt.title("Trump 2017")
plt.axis('off')

fig.add_subplot(1,3,3)
plt.imshow(biden_wordcloud)
plt.title("Biden 2021")
plt.axis('off')
#fig,axs=plt.subplots(3) #make a figure and 3 axes
#axs is a list containing our axes: axs[0] is first ax[1] is second
#(obama_wordcloud).plot(ax=axs[0])
#(trump_wordcloud).plot(ax=axs[1])
#(biden_wordcloud).plot(ax=axs[2])

#plt.imshowsubplot(obama_wordcloud,trump_wordcloud,biden_wordcloud)

#plt.show()

plt.savefig("addressartifact.png", bbox_inches='tight')

print ("program concluded")

