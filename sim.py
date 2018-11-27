#文本相似度计算
#使用TF-IDF计算文本相似度

from gensim import corpora,models,similarities
import jieba

def doc2str(path):
    d=open(path,encoding='utf-8').read()
    data=jieba.cut(d)
    data_str=""
    stopwords=[line.strip() for line in open("stopwords.txt",encoding='utf-8')]
    for item in data:
        if item not in stopwords:
            data_str+=item+" "
    return data_str

def compare(dictionary,data,texts):
    new_doc=data
    new_vec=dictionary.doc2bow(new_doc.split())
    corpus=[dictionary.doc2bow(text) for text in texts]
    tfidf=models.TfidfModel(corpus)
    new_tfidf=tfidf[corpus]
    featureNum=len(dictionary.token2id.keys())
    index=similarities.SparseMatrixSimilarity(new_tfidf,num_features=featureNum)
    new_vec_tfidf=tfidf[new_vec]
    sim=index[new_vec_tfidf]
    print(sim)

def main():
    documents=[]
    path=".txt"
    for i in range(1,6):
        documents.append(doc2str(str(i)+path))
    texts=[[word for word in document.split()] for document in documents]
    dictionary=corpora.Dictionary(texts)
    dictionary.save("simyuliaoku.txt")
    data_str = doc2str('6'+path)
    compare(dictionary,data_str,texts)

if __name__ == '__main__':
    main()



