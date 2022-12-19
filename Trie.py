# Trie is used for mainly text 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
# insertion in Trie
    def insertString(self,word):        #Time Complexity = O(N) && Space Complexity = O(N)
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None :
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print ("Successfully Inserted")
        
# seraching in a Trie
    def searchString(self,word):            #Time Complexity = O(N) && Space Complexity = O(1)
        currentNode = self.root
        for i in word :
            node = currentNode.children.get(i)
            if node == None :
                return False
            currentNode = node 
        if currentNode.endOfString == True :
            return True
        else:
            return False
        
# delete String in a Trie
def deleteString(root,word,index):      #Time Complexity = O(N) && Space Complexity = O(1)
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False
    # Case 1 
    if len(currentNode.children) > 1 :
        deleteString(currentNode,word,index +1)
        return False
    
    # Case 2
    if index == len(word) - 1 :
        if len(currentNode.children) >= 1 :
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
    # Case 3
    if currentNode.endOfString == True :
        deleteString(currentNode,word, index+1)
        return False
    canThisNodeBeDeleted = deleteString(currentNode, word, index +1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False
    
    
    
        
 
# Code to run the above code 
newTrie = Trie()        #Time Complexity = O(1) && Space Complexity = O(1)  >> CREATING A TRIE
newTrie.insertString("App")
newTrie.insertString("Appl")
deleteString(newTrie.root,"App",0)
print(newTrie.searchString("App"))



