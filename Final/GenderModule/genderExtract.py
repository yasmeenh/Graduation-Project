from genderizer.genderizer import genderizer


class GenderDetect(object):
    Lines=[]
    Names=[]
    Kind=[]
    @classmethod
    def init(cls,s):
        cls.Lines=s #characters Body
        cls.Names=[]
        cls.Kind=[]
        cls.getGender()
        return cls.Names,cls.Kind
    @classmethod
    def getGender(cls):
        Characters=[] #characters and their descreption
        j=0
        #array of more words describe genders
        f=['female','woman','girl','wife','daughter','sister','aunt','grandma','mother','grandmother']
        m=['male','man','boy','guy','husband','son','brother','uncle','grandfa','father','grandfather']
        for Line in cls.Lines:
            if Line=='CHARACTERS' or Line=='': #ignore empty lines  & Characters word
                continue
            #check the line is anew character or addition to last Character
            #if it addition to last Character
            if ((Line[0]<'A' or Line[0]>'Z') or (Line[1]<'A' or Line[1]>'Z')) and  Line[1]!=' 'and  Line[1]!='&':
                if j!=0: #At least one character in Characters List
                    Characters[j-1]=Characters[j-1]+' '+Line #add line to last character line
                else:#no character  in Characters List 
                    continue #Ignore
            else:#if anew character
                Characters.append(Line)#add to characters List   
                j=j+1
        for Line in Characters: # for all character in list
            check=0
            words = Line.split(" ")#split its description to words
            if words[0].find('VOICE-')!=-1: #remove VOICE- from word
                words[0]=words[0][6:]
                #make name = first word in character line
            if words[0]!= 'A' and words[0]!= 'An': #remove A or An from words
                name=words[0]   
            else:
                name=words[1]
            q=0
            for word in words:
                #remove ':' & ',' from name of character if found
                if  word[len(word)-1]==':' or word[len(word)-1]==',':
                    word=word[:-1]
                    #if first name
                    if  words[0][len(words[0])-1]==':' or words[0][len(words[0])-1]==',':
                        words[0]=words[0][:-1]
                        name=name[:-1]
                    else:#if another
                        name=name +" "+ word#add to name
                    break
                else:  # if not found
                    # ignore A or An words
                    if name == word or word== 'A' or word== 'An':
                        continue
                    # some thing like TODD & JACK and now my work is JACK
                    if q==1 and ((word[0]>='A' and word[0]<='Z' and word[1]>='A' and word[1]<='Z') or (word[0]>='0' and word[0]<='9') or (word[0]=='#')):
#xxxxxxxxxxxxxxx                            
                            #add last name in this example TODD
                            cls.Names.append(name)
                            #check not captain word
                            if words[0]!=name and words[0]=='CAPTAIN':
                                kind=genderizer.genderizer.detect(firstName = words[1])
                            else:#serch in matching Data Base
                                kind=genderizer.genderizer.detect(firstName = words[0])
                            if kind==None:#if not found in DataBase check words in list f,m in descreption
                                for f1 in f:
                                    if Line.lower().find(f1)!=-1:
                                        kind='female'#if found one of this wordsmake it female
                                        check=1
                                        break
                                if check!=1: #to check it is not female
                                    for m1 in m:
                                        if Line.lower().find(m1)!=-1:
                                            kind='male'#if found one of this wordsmake it male
                                            check=1
                                            break
                                if check!=1:#if i dont now make it male
                                    kind='male'
                            cls.Kind.append(kind)#add to kind
                            q=0
                            name=word#make name equal another name in this example JACK
                            words[0]=word
                            #check this word is name
                    elif ((word[0]>='A' and word[0]<='Z' and word[1]>='A' and word[1]<='Z') or (word[0]>='0' and word[0]<='9') or (word[0]=='#')):
                        name = name + " " + word
                    elif word=='&': #know thatin this line has two names
                        q=1;
                        continue;
                    else:
                        break
#same comments in xxxxxxxxxxxxxxx                    
            cls.Names.append(name)
            if words[0]!=name and words[0]=='CAPTAIN':
                kind=genderizer.genderizer.detect(firstName = words[1])
            else:
                kind=genderizer.genderizer.detect(firstName = words[0])
            if kind==None:
                for f1 in f:
                    if Line.lower().find(f1)!=-1:
                        kind='female'
                        check=1
                        break
                if check!=1:
                    for m1 in m:
                        if Line.lower().find(m1)!=-1:
                            kind='male'
                            check=1
                            break
                if check!=1:
                    kind='male'
            cls.Kind.append(kind)
        
#file=open("characters.txt", "r") 
#s=file.read() 
#GenderDetect.init(s)
