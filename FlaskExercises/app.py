
from tkinter import W
from flask import Flask, render_template
import string

app = Flask(__name__)

@app.route("/")
def home():
    title = "FLASK EXAMPLES"
    text = "Select anything on the menu bar to find out more!"
    return render_template('home.html', title=title, text=text)



@app.route("/dictionary/")
def alphabet():    
    alphabet = list(string.ascii_lowercase)
    print(alphabet)
    return render_template('firstpage.html', alphabet = alphabet)

@app.route("/dictionary/<string:letters>")
def tryletters(letters):
    f = open("words.txt")

    word_list = f.read().splitlines()

    is_real_word = letters.upper() in word_list 

    words_starts = []
    
    for w in word_list:
        if w.startswith(letters.upper()):
            words_starts.append(w)
    
    amount = len(words_starts)
    combo = []
    alphabet = list(string.ascii_lowercase)
    for a in alphabet:
        newword = letters+a
        combo.append(newword)

    return render_template('newpage.html', combo = combo, is_real_word=is_real_word, letters = letters, amount = amount, words_starts=words_starts)

@app.route("/words/")
def wordshome():
    return render_template('words1.html')

@app.route("/words/<string:word>")
def words(word):    
    f = open("words.txt")

    word_list = f.read().splitlines()

    is_real_word = word.upper() in word_list

    anagram = []
    for one in word_list:
        if sorted(word.upper()) == sorted(one):
            anagram.append(one)

    return render_template('dictionary.html', word = word, is_real_word = is_real_word, anagrams = anagram)


@app.route("/magicworld/")
def ourworld(): 
    title = "The Magic World of Unicorns"
    
    text = """🌈🌞🦄 If you enter this magic world, you will forget about everything. There are no problems here. Just fun. Are you ready to join us?  🌈🌞🦄 """

    choices = [
        ('enter_house',"Be happy with unicorns"),
        ('run_away',"Decide to stay in ordinary mortal world")
    ]

    return render_template('magicalworld.html', title=title, text=text, choices=choices)




@app.route("/inside")
def enter_house():
    title = "Welcome"
    
    text = """🌈🌞🦄Live with us forever, there wont be any worries in your life🌈🌞🦄"""

    choices = [
        ('up_stairs',"Find out how does the life with unicorns look like"),
        ('run_away',"It is too boring. I want home")
    ]


    return render_template('magicalworld.html', title=title, text=text, choices=choices)

@app.route("/escape")
def run_away():
    title = "Stay safe!"
    
    text = """You have decided to choose a harder way. It deserves respect. Good luck"""

    choices = []

    return render_template('magicalworld.html', title=title, text=text, choices=choices)

@app.route("/stairs")
def up_stairs():
    title = "Plan of our day"
    
    text = """We just eat an sleep 🦄🦄🦄"""

    choices = []


    return render_template('magicalworld.html', title=title, text=text, choices=choices)


@app.route("/fizzbuzz/")
def fizzbuzzhome():
    return render_template('fizzbuzz1.html')



@app.route("/fizzbuzz/<int:count_to>")
def count(count_to):
    l = []
    a=0
    while a<count_to:
        if a%3 == 0 and a%5 ==0:
            l.append("FizzBuzz")
        elif a%3 == 0:
            l.append("Fizz")
        elif a%5 == 0:
            l.append("Buzz")
        else:
            l.append(a)
        a +=1

    return render_template('fizzbuzz.html', numbers=l)

