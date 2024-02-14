#part3 (File)
from graphics import *   #import the graphics.py module 
Progress=0#Define Variables
Trailer=0
Retriver=0
Exclude=0
Range= [0, 20, 40, 60, 80, 100, 120]        
Prompt="y"  # for quit or contiinue program
def ErrorCorrection(Input):
    while True:
        try:#For ValueError
            credits = int(input(Input))
            if credits in Range:
                return credits
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")
def Bar(Bar_Number,CountOfOutcomes,ColorOfBar,BarName):
    #Bar position calculations
    RectanglePoint1 = 165+(Bar_Number-1)*150
    RectanglePoint2 = 285+(Bar_Number-1)*150
    NamePoint = 226+(Bar_Number-1)*150
    #Create Bar
    Size=475-(CountOfOutcomes*20)
    Bar = Rectangle(Point(RectanglePoint1,475),Point(RectanglePoint2,Size))
    Bar.setFill(ColorOfBar)#bar colour
    Bar.setOutline("White")#Outline color
    Bar.draw(win)#Display bar
    Bar_name = Text(Point(NamePoint,485),BarName)#Create name
    Bar_name.setSize(16)#name size
    Bar_name.setTextColor(color_rgb(121, 130, 146))#set color of text
    Bar_name.draw(win)#display on the window
    #Create Number Display Above the graph
    OutcomeNumber = Text(Point(RectanglePoint1+60,Size-10),CountOfOutcomes)
    OutcomeNumber.setTextColor(color_rgb(121, 130, 146))#set color of text
    OutcomeNumber.setSize(16)#size
    OutcomeNumber.draw(win)
file = open('text.txt','w')#Create writable File

file.write("Part 3:\n")
while Prompt != "q":#This should be false to exit loop
    print("")
    while True:#For Total check
        print("")
        passCredits = ErrorCorrection("Please enter your credits at pass: ")
        deferCredits = ErrorCorrection("Please enter your credits at defer: ")
        failCredits = ErrorCorrection("Please enter your credits at fail: ")
        total = passCredits + deferCredits + failCredits#Total Calculation
        if total!=120:
           print("Total incorrect")
        else:
            break
        
    if passCredits == 120:
        ProgressionOutcome="Progress"
        Progress+=1
        print(ProgressionOutcome)
    elif passCredits == 100:
        ProgressionOutcome="Progress (module trailer)"
        Trailer+=1
        print(ProgressionOutcome)
    elif failCredits == 80 or failCredits == 100 or failCredits ==120:
        ProgressionOutcome="Exclude"
        Exclude+=1
        print(ProgressionOutcome)
    else:
        ProgressionOutcome="Module retriever"
        Retriver+=1
        print(ProgressionOutcome)
    print("")
    file.write(f"{ProgressionOutcome} - {passCredits}, {deferCredits}, {failCredits}\n")
    Prompt =input('''Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')
    print('')
    while True:
        Prompt =input('''Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: ''')
        if Prompt == 'y':
            break
        elif Prompt == 'q':
            break
        else:
            print('''Invalid Input
''')

FinalAnwser=Progress+Trailer+Retriver+ExcludeFinalAnwser=Progress+Trailer+Retriver+Exclude#Calculate Outcome total
file = open('text.txt','r')
for line in file:
    print(line, end='')
file.close()
#OPEN THE WINDOW
win = GraphWin("Histogram", 800, 600)#open a window object called "win" with size and title 
win.setBackground(color_rgb(237, 242, 236))# Set the background colour of the window
# Used https://imagecolorpicker.com to find colour RGB Value
Topic = Text(Point(175,50),"Histogram Results")#Create topic
Topic.setStyle("bold")#bold the text
Topic.setSize(20)#Topic size
Topic.setTextColor(color_rgb(96, 99, 95))#set color of text
Topic.draw(win)#display on the window
#total Outcome Total message
OutcomeTotal = Text(Point(175,550),f"{FinalAnwser} outcome in total")#Create Outcome
OutcomeTotal.setStyle("bold")#bold the text
OutcomeTotal.setSize(18)#Topic size
OutcomeTotal.setTextColor(color_rgb(121, 130, 146))#set color of text
OutcomeTotal.draw(win)#display on the window
#Create Progress Bar

ProgressBar = Bar(1,Progress,color_rgb(172, 239, 164),"Progress")# Used https://imagecolorpicker.com to find colour RGB Value
TrailerBar = Bar(2,Trailer,color_rgb(160, 199, 136),"Trailer")
RetriverBar = Bar(3,Retriver,color_rgb(168, 189, 121),"Retriver")
ExcludeBar = Bar(4,Exclude,color_rgb(210, 182, 181),"Excluded")            
    
           
    
        
        


