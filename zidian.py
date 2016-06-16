from tkinter import*
import os
os.chdir('words')
#=======================================函数==========================================================

def add_button():
        

    add=Tk()
    add.title('添加')

    Label(add,text='单词:',font='微软雅黑').grid(row=0)
    Label(add,text='解释:',font='微软雅黑').grid(row=1)
        
        
    add_word=Entry(add,borderwidth=0,font='微软雅黑')
    add_word.grid(row=0,column=1)
        
    add_explain=Entry(add,borderwidth=0,font='微软雅黑')
    add_explain.grid(row=1,column=1)
        
        

    def show():
        word=str(add_word.get())
        Word=word.capitalize()
        list_Words=list(Word)
        frist=list_Words[0]
        file=frist+'.txt'
        f=open(file)
        str_word=f.read()
        list_word=str_word.split(';\n')
        for each in list_word:
            list_each=each.split(':')
            if word==list_each[0]:
                existword=Toplevel()
                existword.title('提示')
                existword.geometry('200x50+200+50')
                Label(existword,text='单词已存在!',font='微软雅黑').grid()
                break
            else:
                expain=str(add_explain.get())
                word=word+':'+expain
                f=open(file,'a')
                f.write(word+';\n')
            f.close()
            add_word.delete(0,END)
            add_explain.delete(0,END)
         
    Button(add,text='添加',borderwidth=0,font='微软雅黑',command=show).grid(row=3,column=1,sticky=E)
       
#==================================================================================================    
def search_word(event):

    search=input_word.get()
    Search=search.capitalize()
    list_search=list(Search)
    frist=list_search[0]

    f=open(frist+'.txt')
    str_all_word=f.read()

    list_all_word=str_all_word.split(';\n')

    for each in list_all_word:
        list_each_word=each.split(':')
        if list_each_word[0]==search:
            show_word=Toplevel()
            show_word.title(search)
            Label(show_word,text=list_each_word[1],font='微软雅黑').grid()
               
    f.close()
    #=====================================================

        
        
    #==========================================================
def button_word(event):
    def delete_button():
     
        word=listword.get(ACTIVE)
    
        f=open(word[0]+'.txt')
        wordstr=f.read()
      
        wordstr=wordstr.replace(word+';\n','')
    
        f=open(word[0]+'.txt','w')
        f.write(wordstr)
        f.close()
    word=str(alphabet.get(ACTIVE))
    word=str(word[0])

    f=open(word+'.txt')
    wordstr=f.read()

    word_button=Toplevel()    
    word_button.title(word)
 
    menubar=Menu(word_button,font='微软雅黑')
        
    word_button.config(menu=menubar)
    addword=menubar.add_command(label='add',font='微软雅黑',command=add_button)
        
    deleteword=menubar.add_command(label='delete',font='微软雅黑',command=delete_button)
        
    listword=Listbox(word_button,font='微软雅黑')
    listword.pack()
    wordlist=wordstr.split(';\n')
    for each in wordlist:
        listword.insert(END,each)
        alphabet.update_idletasks()
            
    f.close()
#=============================================页面===================================================================
  
root=Tk()
root.title('自典')
root.resizable(width=False,height=False)
#===============================================添加=================================================================
menubar=Menu(root,font='微软雅黑')
root.config(menu=menubar)
addword=menubar.add_command(label='add',font='微软雅黑',command=add_button)

#=============================================搜索====================================================================

input_word=Entry(root,font='微软雅黑',borderwidth=0)
input_word.grid()

input_word.bind('<KeyPress-Return>',search_word)

#===========================================字母表=================================================================

alphabet=Listbox(root,borderwidth=0,font='微软雅黑')

alphabet.grid()

list_alphabet=os.listdir('.')

word_count=0

for each_file in list_alphabet:
    file_name=each_file.split('.')
    
    frist=file_name[0]
    f=open(frist+'.txt')
    str_all_word=f.read()
    word_count=str_all_word.count (':')
    list_all_word=str_all_word.split(';\n')
   
    for each_word in list_all_word:

        last_word=list_all_word.pop()
   
    alphabet.insert(END,frist+'    '+last_word+'     '+str(word_count))
    alphabet.bind('<ButtonRelease>',button_word)

    
f.close()

#================================================================================================================
root.mainloop ()


