from xml.dom.minidom import Document
import config as c
import sys
import pandas as pd
from classes.documentExtraction import DocumentModel

DM=DocumentModel()
document_paths = c.document_paths
budget_description = pd.read_csv(c.dataFilepath)

def main():
    try:
        budget_tabledata = DM.extractTable(document_paths)
        data = DM.extractDescription(budget_description)
        budget_Dataframe=DM.mergeDocumentData(budget_tabledata,data)
        budget_Dataframe.to_csv(c.resultFileName, header=False, index=False)
        return True
    except:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        return False



if __name__ == '__main__':
   flag=main()
   if flag:
    print("Document Extraction module executed succesfully.!")


