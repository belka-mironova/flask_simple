

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Haunted House"

    text = """It is a dark and cold night and the moon is full. You walk up to the haunted house.  
    As you approach the door, it creaks open and a chill runs down your spine!"""

    groceries = ["bananas", "apples"]

    return render_template('count.html', title=title, text=text, groceries=groceries)


@app.route("/second")
def second():
    
    picture_url = "https://i.picsum.photos/id/289/200/300.jpg?hmac=TVh4H_Hra3e1VSDPJz-mhCgep32qIa7T6DGQvbrjMb4"

    return render_template('secondpage.html', picture_url = picture_url)

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

@app.route("/words/<string:word>")
def words(word):    
    f = open("words.txt")

    word_list = f.read().splitlines()

    is_real_word = word.upper() in word_list

    anagram = []
    for one in word_list:
        if sorted(word.upper()) == sorted(one):
            anagram.append(one)

    return render_template('words.html', word = word, is_real_word = is_real_word, anagrams = anagram)