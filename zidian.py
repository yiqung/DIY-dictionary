from tkinter import*
import os
os.chdir('words')
root=Tk()
root.title('自典')
root.resizable(width=False,height=False)
menubar=Menu(root,font='微软雅黑')
root.config(menu=menubar)
input_word=Entry(root,font='微软雅黑',borderwidth=0)
input_word.grid(row=0,columnspan=4)
alphabet=Listbox(root,borderwidth=0,font='微软雅黑')
alphabet.grid(row=1,columnspan=4)

#=============================================================================================
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
        explain=str(add_explain.get())
        
        Word=word.capitalize()
        list_Words=list(Word)
        frist=list_Words[0]
        file=frist+'.txt'
        f=open(file)
        str_word=f.read()
        list_word=str_word.split(';\n')
        list_all=[]
        for each in list_word:
            list_each=each.split(':')
            list_all.append(list_each[0])
        if word in list_all:
                exsit=Toplevel()
                Label(exsit,text='单词已存在!',font='微软雅黑').grid()
        else :
            word=word+':'+explain
            f=open(file,'a')
            f.write(word+';\n')
        f.close()
        add_word.delete(0,END)
        add_explain.delete(0,END)
           
    Button(add,text='添加',borderwidth=0,font='微软雅黑',command=show).grid(row=3,column=1,sticky=E)
addword=menubar.add_command(label='添加',font='微软雅黑',command=add_button)
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
input_word.bind('<KeyPress-Return>',search_word)
#===========================
def alphabet_list():
    def word_list():
        def delete_word():
            word=alphabet.get(ACTIVE)
            f=open(word[0]+'.txt')
            word_str=f.read()
            word_list=word_str.split(';\n')
            if word in word_list:
                word_list.remove(word)
                f=open(word[0]+'.txt','w')
                for each in word_list:
                    if each!='':
                        f.write(each+';\n')
                f.close()
#=================================
        word=str(alphabet.get(ACTIVE))
        word=str(word[0])
        alphabet.delete(0,END)
        f=open(word+'.txt')
        wordstr=f.read()
        wordlist=wordstr.split(';\n')
        for each in wordlist:
            alphabet.insert(END,each)
        f.close()
        
        delete_button=Button(root,text='删除',font='微软雅黑',borderwidth=0,command=delete_word)
        delete_button.grid(row=2,columnspan=4,sticky=W+E)
        
        return_button=Button(root,text='返回',font='微软雅黑',borderwidth=0,command=alphabet_list)
        return_button.grid(row=2,column=0,sticky=W)
                
        flash1_button=Button(root,text='刷新',font='微软雅黑',borderwidth=0,command=word_list)
        flash1_button.grid(row=2,column=3,sticky=E)
#==================================
    list_alphabet=os.listdir('.')
    word_count=0
    alphabet.delete(0,END)
    for each_file in list_alphabet:
        file_name=each_file.split('.')
        frist=file_name[0]
        f=open(frist+'.txt')
        str_all_word=f.read()
        word_count=str_all_word.count (':')
        list_all_word=str_all_word.split(';')
        for each_word in list_all_word:
            if word_count==1:
                last_word=list_all_word[0]
            else:
                last_word=list_all_word.pop()
        alphabet.insert(END,frist+'-'+last_word+'-'+str(word_count))
        
    f.close()
    open_button=Button(root,text='打开',font='微软雅黑',borderwidth=0,command=word_list)
    open_button.grid(row=2,column=0,columnspan=2,sticky=W+E)
    flash2_button=Button(root,text='刷新',font='微软雅黑',borderwidth=0,command=alphabet_list)
    flash2_button.grid(row=2,column=2,columnspan=2,sticky=W+E)

#=====================================================
alphabet_list()
#================================================================================================================
root.mainloop ()
