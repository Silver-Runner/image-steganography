#import modules
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import  os

class IMG_Stegno:
    output_image_size = 0

    #main frame or start page
    def main(self, root):
        root.title('IMAGE STEGANOGRAPHY ')
        root.geometry('600x700')
        root.resizable(width =False, height=False)
       # root.iconbitmap('C:\\python\\favicon.ico')
        root.config(bg = '#FFFFFF')
        frame = Frame(root)
        frame.grid()
        
        title = Label(frame,text='IMAGE STAGNOGRAPHY')
        title.config(font=('TIMES NEW ROMAN',25, 'bold'))
        title.grid(pady=10)
        title.config(bg = '#FFFFFF')
        title.grid(row=1)
     
        

        encode = Button(frame,text="ENCODE",command= lambda :self.encode_frame1(frame), padx=14,bg = '#FFFFFF' )
        encode.config(font=('Times new roman',14), bg='#33FF33')
        encode.grid(row=2)
        decode = Button(frame, text="DECODE",command=lambda :self.decode_frame1(frame),padx=14,bg = '#FFFFFF')
        decode.config(font=('Times new roman',14), bg='#FF0000')
        decode.grid(pady = 12)
        decode.grid(row=3)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)



    #back function to loop back to main screen
    def back(self,frame):
        frame.destroy()
        self.main(root)

    
    #frame for encode page
    def encode_frame1(self,F):
        F.destroy()
        F2 = Frame(root)
        label1= Label(F2,text='SELECT THE IMAGE IN WHICH \nYOU WANT TO HIDE TEXT:')
        label1.config(font=('TIMES NEW ROMAN',25, 'bold'),bg = '#FFFFFF')
        label1.grid()

        button_bws = Button(F2,text='SELECT',command=lambda : self.encode_frame2(F2))
        button_bws.config(font=('TIMES NEW ROMAN',18), bg='#33FF33')
        button_bws.grid()
        button_back = Button(F2, text='CANCEL', command=lambda : IMG_Stegno.back(self,F2))
        button_back.config(font=('TIMES NEW ROMAN',18),bg='#FF0000')
        button_back.grid(pady=15)
        button_back.grid()
        F2.grid()

    #frame for decode page
    def decode_frame1(self,F):
        F.destroy()
        d_f2 = Frame(root)
        label1 = Label(d_f2, text='Select Image with Hidden text:')
        label1.config(font=('Times new roman',25,'bold'),bg = '#FFFFFF')
        label1.grid()
        label1.config(bg = '#e3f4f1')
        button_bws = Button(d_f2, text='SELECT', command=lambda :self.decode_frame2(d_f2))
        button_bws.config(font=('TIMES NEW ROMAN',18), bg='#33FF33')
        button_bws.grid()
       
        button_back = Button(d_f2, text='CANCEL', command=lambda : IMG_Stegno.back(self,d_f2))
        button_back.config(font=('TIMES NEW ROMAN',18), bg='#FF0000')
        button_back.grid(pady=15)
        button_back.grid()
        d_f2.grid()


    #function to encode image 
    def encode_frame2(self,e_F2):
        e_pg= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("ERROR","YOU HAVE SELECTED NOTHING !")
        else:
            my_img = Image.open(myfile)
            new_image = my_img.resize((300,200))
            img = ImageTk.PhotoImage(new_image)
            label3= Label(e_pg,text='SELECTED IMAGE')
            label3.config(font=('TIMES NEW ROMAN',14,'bold'))
            label3.grid()
            board = Label(e_pg, image=img)
            board.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid()
            label5=Label(e_pg,text='ENTER PASSWORD(MINIMUM 6 CHARACTERS)')
            label5.config(font=('TIMES NEW ROMAN',14,'bold'))
            label5.grid(pady=12)
            text_b=Text(e_pg,width=20,height=2)
            text_b.grid()
            
            label2 = Label(e_pg, text='ENTER THE MESSAGE')
            label2.config(font=('TIMES NEW ROMAN',14,'bold'))
            label2.grid(pady=15)
            text_a = Text(e_pg, width=50, height=10)
            text_a.grid()
        
            encode_button = Button(e_pg, text='CANCEL', command=lambda : IMG_Stegno.back(self,e_pg))
            encode_button.config(font=('TIMES NEW ROMAN',14), bg='#FF0000')
            data = text_a.get("1.0", "end-1c")
            button_back = Button(e_pg, text='ENCODE', command=lambda : [self.enc_fun(text_a,my_img,text_b),IMG_Stegno.back(self,e_pg)])
            button_back.config(font=('TIMES NEW ROMAN',14), bg='#33FF33')
            button_back.grid(pady=15)
            encode_button.grid()
            e_pg.grid(row=1)
            e_F2.destroy()





    #function to decode image 
    def decode_frame2(self,d_F2):
        d_F3 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfiles:
            messagebox.showerror("ERROR","YOU HAVE SELECTED NOTHING !")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(d_F3,text='SELECTED IMAGE :')
            label4.config(font=('TIMES NEW ROMAN',14,'bold'))
            label4.grid()
            board = Label(d_F3, image=img)
            board.image = img
            board.grid()
            label6=Label(d_F3,text='ENTER YOUR PASSWORD')
            label6.config(font=('TIMES NEW ROMAN',14,'bold'))
            label6.grid(pady=12)
            text_c=Text(d_F3,width=20,height=2)
            text_c.grid()
            
            hidden_data = self.decode(my_img)
            button_bws = Button(d_F3, text='DECODE', command=lambda :self.password(text_c,hidden_data,text_a))
            button_bws.config(font=('TIMES NEW ROMAN',18), bg='#33FF33')
            button_bws.grid(pady=15)
            
            label2 = Label(d_F3, text='HIDEEN DATA IS :')
            label2.config(font=('TIMES NEW ROMAN',14,'bold'))
            label2.grid(pady=10)
            text_a = Text(d_F3, width=50, height=10)
          
            text_a.grid()
            button_back = Button(d_F3, text='CANCEL', command= lambda :self.frame_3(d_F3))
            button_back.config(font=('TIMES NEW ROMAN',14),bg='#FF0000')
            button_back.grid(pady=15)
            button_back.grid()
            d_F3.grid(row=1)
            d_F2.destroy()

    def password(self,text_c,data,text_a):
        data3= text_c.get("1.0", "end-1c")
        if(len(data3)>6 or len(data)<6 or len(data3)==0):
            messagebox.showinfo("WARNING",'PLEASE ENTER VALID PASSWORD')
        else:
            data4=data[-6:]
            data5=data[0:-6]
            if(data4==data3):
                text_a.insert(INSERT,data5)
                text_a.configure(state='disabled')
            else:
                messagebox.showinfo('WARNING','INCORRECT PASSWORD')
            
        
            
    
    #function to decode data
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''

        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]
            binary_str = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binary_str += '0'
                else:
                    binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data

    #function to generate data
    def generate_Data(self,data):
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data


    #function to modify the pixels of image
    def modify_Pix(self,pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            # Extracting 3 pixels at a time
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]
            
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            
            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    
    
    #function to enter the data pixels in image
    def encode_enc(self,newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    
    #function to enter hidden text
    def enc_fun(self,text_a,myImg,text_b):
        data1 = text_a.get("1.0", "end-1c")
        data2=text_b.get("1.0","end-1c")
        if(len(data2)==0):
            messagebox.showinfo("WARNING","PASSWORD IS REQUIRED \nTRY AGAIN")
           
        elif(len(data2)<6 or len(data2)>6):
            messagebox.showinfo("WARNING","PASSWORD MUST BE OF 6 CHARACTERS\n TRY AGAIN")
         
            
        else:            
            if (len(data1) == 0):
                messagebox.showinfo("ALERT","KINDLY ENTER TEXT IN THE TEXT BOX")
                
            else:
                    newImg = myImg.copy()
                    self.encode_enc(newImg, (data1+data2))
                    my_file = BytesIO()
                    temp=os.path.splitext(os.path.basename(myImg.filename))[0]
                    newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
                    self.d_image_size = my_file.tell()
                    self.d_image_w,self.d_image_h = newImg.size
                    messagebox.showinfo("Success","Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")
                    return (data2) 
    def frame_3(self,frame):
        frame.destroy()
        self.main(root)


#GUI loop
root = Tk()
o = IMG_Stegno()
o.main(root)
root.mainloop()
