Age extraction content how prepare our Model to extract Human's Age from his text.
we have three files
first file is 1prepareDataSet.py:
    in this file I take data and prepare it using (lemmatize - stimming -remove stop words - Tokenize -decontracted)
    I use it twice 1 of first half in data set and save it in file PreprocessedData.csv and run it again to second half of data and save
    it in PreprocessedData2.csv because My Data is very very big.
Second file is 2saveCSVFilesInOneFile.py:
    In this file I read 2 files PreprocessedData.csv and PreprocessedData2.csv and save them in one file PreprocessedData3.csv
Third file is 3TryDifferent Model-SaveModel-LoadModel.py
    In this file I read file PreprocessedData3.csv and make data balanced, try different Models, Save Model and Load Model
Iad3.py how generate different Models 
