__author__ = 'Hari'





def generateEmptyDatabase():

    databaseCursor.execute('CREATE TABLE IF NOT EXISTS Documents(docID INTEGER,url TEXT)')
    databaseCursor.execute('CREATE TABLE IF NOT EXISTS Lexicon(wordID INTEGER, word TEXT)')


def insertIntoDocumentTable(docID,url):

    databaseCursor.execute('''INSERT INTO Documents (docID, url)VALUES (?,?)''',(docID,url))

def insertIntoLexiconTable(wordID, word):

    databaseCursor.execute('INSERT INTO Lexicon VALUES (?,?)',[wordID,word])




