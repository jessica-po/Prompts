class Node(object):
    def __init__(self):
        super(Node, self).__init__()
        self.next = [-1] * 26
        self.trans = []
        self.matches = 0
        self.leaf = 0
        self.link = 0

class AhoCorasick(object):
    def __init__(self):
        super(AhoCorasick, self).__init__()
        self.T = [Node()]
        self.T[0].link = 0

    def insert_trie(self, s):
        v = 0
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            if(self.T[v].next[c] == -1):
                self.T[v].trans.append(c)
                self.T[v].next[c] = len(self.T)
                self.T.append(Node())
            v = self.T[v].next[c]
        self.T[v].leaf += 1
        self.T[v].matches += 1

    def set_suffix_link(self, S):
        Q = []
        for j in range(len(S)):
            Q.append((j, 0, 0, 0))
            #string index, index in string, state, suff state, 
        i = 0
        while(i < len(Q)):
            j,ind,v,suff = Q[i]
            i += 1
            c = ord(S[j][ind]) - ord('a')
            if(ind>0):
                while(suff>0 and self.T[suff].next[c]==-1):
                    suff = self.T[suff].link
                if(self.T[suff].next[c] != -1):
                    suff = self.T[suff].next[c]
            v = self.T[v].next[c]
            self.T[v].link = suff
            if(ind+1 < len(S[j])):
                Q.append((j,ind+1,v,suff))

    def set_matches(self):
        i = 0
        Q = [0]
        while(i < len(Q)):
            v = Q[i]
            self.T[v].matches = self.T[v].leaf + self.T[self.T[v].link].matches
            for c in self.T[v].trans:
                Q.append(self.T[v].next[c])
            i += 1

    def build(self, S):
        for i in range(len(S)):
            self.insert_trie(S[i])
        self.set_suffix_link(S)
        #self.printTree()
        self.set_matches()

    def get(self, s):
        v = 0
        matches = []
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            while(v>0 and self.T[v].next[c] == -1):
                v = self.T[v].link
            if(self.T[v].next[c] != -1):
                v = self.T[v].next[c]
            matches.append(self.T[v].matches)
        return matches

    def printTree(self):
        for i in range(len(self.T)):
            print(str(i)+" leaf:"+str(self.T[i].leaf)+" link:"+str(self.T[i].link)+" matches:"+str(self.T[i].matches)+" : " , end='')
            for j in range(26):
                print(" "+str(chr(j+ord('a')))+"-"+(str(self.T[i].next[j]) if (self.T[i].next[j]!=-1) else "_")+" ", end='')
            print()

t = input()
n = int(input())
patterns = []
patterns_rev = []
for i in range(n):
    s = input()
    patterns.append(s)
    patterns_rev.append(s[::-1])
t1 = AhoCorasick()
t2 = AhoCorasick()
t1.build(patterns)
t2.build(patterns_rev)

x1 = t1.get(t)
x2 = t2.get(t[::-1])[::-1]

#print(x1)
#print(x2)

ans = 0
for i in range(len(x1)-1):
    ans += x1[i] * x2[i+1]

print(ans)