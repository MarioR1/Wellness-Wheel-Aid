import tkinter as tk
from tkinter import Label, ttk
  
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, quiz_page, Wellness_Wheel, intelectual, physical, social, spiritual, environment, emotional):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="    The Wellness Wheel Aid", font = LARGEFONT)
        label_intro = ttk.Label(self, text='           Welcome, The Wellness Wheel Aid is a program designed to make information on how to improve mental health easier to access\n First you will go through a short quiz to create an estimate of YOUR own Wellness Wheel.', justify='center')

         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        label_intro.grid(row=1, column=0)
  
        button1 = ttk.Button(self, text ="Next Page",
        command = lambda : controller.show_frame(quiz_page))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 2, column = 0, columnspan=2, padx = 10, pady = 10)
  
          
  
  
# second window frame page1
class quiz_page(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="         Quick Quiz", font = LARGEFONT, justify='center')
        label_intro = ttk.Label(self, text= '                                                    Answer the next few questions to the best of your ability for the best results', justify='center')
        label_NOT = ttk.Label(self,text= '                                                 WORK IN PROGRESS', foreground='red')

        label.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan=2)
        label_intro.grid(row=1, column=0)
        label_NOT.grid(row=2, column=0)

        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Done Quiz",
                            command = lambda : controller.show_frame(Wellness_Wheel))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 9, column = 0, padx = 10, pady = 10, )
  
  
  
  
# third window frame page2
class Wellness_Wheel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="    YOUR Wellness Wheel", font = LARGEFONT)
        label_intro = ttk.Label(self, text ='Click on the areas that you wish to improve on')
        label_intelectual = ttk.Label(self, text = 'Intelectual\n 5/5')
        label_physical = ttk.Label(self, text = 'Physical\n 2/5', foreground= 'red' )
        label_social = ttk.Label(self, text = 'Social\n 5/5')
        label_spiritual = ttk.Label(self, text = 'Spiritual\n 2/5', foreground= 'red')
        label_environmental = ttk.Label(self, text = 'Environmental\n 5/5')
        label_emotional = ttk.Label(self, text = 'Emotional\n 5/5')

        label.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan= 6)
        label_intro.grid(row=1, column=0, columnspan=6)
        label_intelectual.grid(row= 2, column= 0)
        label_physical.grid(row= 2, column= 1)
        label_social.grid(row= 2, column= 2)
        label_spiritual.grid(row= 2, column= 3)
        label_environmental.grid(row= 2, column= 4)
        label_emotional.grid(row= 2, column= 5)
  

        button_int = ttk.Button(self, text ="Intelectual",
                            command = lambda : controller.show_frame(intelectual))
        button_phy = ttk.Button(self, text ="Physical",
                            command = lambda : controller.show_frame(physical))
        button_soc = ttk.Button(self, text ="Social",
                            command = lambda : controller.show_frame(social))
        button_spi = ttk.Button(self, text ="Spiritual",
                            command = lambda : controller.show_frame(spiritual))
        button_env = ttk.Button(self, text ="Environment",
                            command = lambda : controller.show_frame(environment))
        button_emo = ttk.Button(self, text ="Emotional",
                            command = lambda : controller.show_frame(emotional))

        button_int.grid(row = 3, column = 0, padx = 10, pady = 10)
        button_phy.grid(row = 3, column = 1, padx = 10, pady = 10)
        button_soc.grid(row = 3, column = 2, padx = 10, pady = 10)
        button_spi.grid(row = 3, column = 3, padx = 10, pady = 10)
        button_env.grid(row = 3, column = 4, padx = 10, pady = 10)
        button_emo.grid(row = 3, column = 5, padx = 10, pady = 10)

class intelectual(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="INTELECTUAL", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button_back = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Wellness_Wheel))

        button_back.grid(row = 1, column = 0, padx = 10, pady = 10)

class physical(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="      PHYSICAL", font = LARGEFONT, foreground='blue')
        label_intro = ttk.Label(self, text = 'The Physical section of the Wellness Wheel is all about creating and maintaining a healthy excersice and nutritional routine.\nSome great software applications to help you with this section are listed below', justify='center')
        label_app1 = ttk.Label(self, text = 'Calorie Counter - MyFitnessPal\n https://play.google.com/store/apps/details?id=com.myfitnesspal.android\nhttps://apps.apple.com/ca/app/myfitnesspal/id341232718', justify='center')



        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        label_intro.grid(row=1, column=0)
        label_app1.grid(row=2, column=0)
        button_back = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Wellness_Wheel))

        button_back.grid(row = 3, column = 0, padx = 10, pady = 10)

class social(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="SOCIAL", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button_back = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Wellness_Wheel))

        button_back.grid(row = 2, column = 0, padx = 10, pady = 10)

class spiritual(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="SPIRITUAL", font = LARGEFONT, foreground='orange')
        label_intro = ttk.Label(self, text='The Spiritual section of the Wellness Wheel is all about creating and maintaining healthy moral values and finding and giving life a new meaning.\nSome great software applications to help you with this section are listed below', justify='center')
        label_app1 = ttk.Label(self, text= 'Headspace: Meditation & Sleep\nhttps://play.google.com/store/apps/details?id=com.getsomeheadspace.android\nhttps://apps.apple.com/us/app/headspace-meditation-sleep/id493145008', justify='center')


        label.grid(row = 0, column = 0, padx = 10, pady = 10)
        label_intro.grid(row=1, column=0)
        label_app1.grid(row=2, column=0)

        button_back = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Wellness_Wheel))

        button_back.grid(row = 3, column = 0, padx = 10, pady = 10)

class environment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="ENVIRONMENT", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button_back = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Wellness_Wheel))

        button_back.grid(row = 1, column = 0, padx = 10, pady = 10)

class emotional(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="EMOTIONAL", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        button_back = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(Wellness_Wheel))

        button_back.grid(row = 1, column = 0, padx = 10, pady = 10)


  
  
# Driver Code
app = tkinterApp()
app.title('The Wellness Wheel Aid')
app.mainloop()