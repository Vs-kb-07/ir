import nltk
from nltk.corpus import stopwords
document1= "the quick brown fox jump over the lazy dog"
document2= "the lazy dog slept in the sun"
nltk.download('stopwords')
stopWords=stopwords.words('english')
tokens1=document1.lower().split()
tokens2=document2.lower().split()
terms=list(set(tokens1+tokens2))
inverted_index={}
occ_num_doc1={}
occ_num_doc2={}
for term in terms:
    if terms in stopWords:
        continue
        document=[]
        if term in tokens1:
            document.append("document1")
            occ_num_doc1[term]=tokens1.count(term)
        if term in tokens2:
            document.append("document2")
            occ_num_doc2[term]=tokens2.count(term)
            inverted_index[term]=documents
for term,documents in inverted_index.items():
    print(term,"->",end=" ")
    for doc in documents:
        if doc=="document1":
            print(f"{doc}({occ_num_doc1.get(term,0)}),",end=" ")
        else:
          print(f"{doc}({occ_num_doc2.get(term,0)}),",end=" ")
          print()
print("perform by 702_vansh & 765_ankit")
