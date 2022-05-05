from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


data = {
"1":{
"id": "1",
"title": "Loss of Soccer Teammates",
"image": "https://cdn.pixabay.com/photo/2016/06/15/18/12/football-1459573_1280.png",
"About": "I grew up playing soccer, so my teammates were always my best friends. I spent more time with the team than any of my other friends. The bond between teammates goes beyond a typical friendship. After I stopped playing soccer, I lost the support network and family that I was used to having. It was also a loss of identity, but I was more sad about losing that bond between teammates.",
"Quote": "Physical geographic segregation is a potent metaphor for the multiple sites of separation and oppositions"
}, 

"2":{
"id": "2",
"title": "Loss of Hometown Bestfriends",
"image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8uIDMkwT7sW0bIMITBRi8sqYT9QJNYM9giA&usqp=CAU",
"About": "After graduating from high school, I have not been nearly as close with my childhood friends from my hometown, San Mateo. Beyond the physical separation, I also noticed that we were growing apart due to going to very different schools and pursuing very different career paths. While I still am very close to there friends, our friendships are nothing near how they used to be when we saw eachother everyday.",
"Quote": "Physical geographic segregation is a potent metaphor for the multiple sites of separation and oppositions"
},

"3":{
"id": "3",
"title": "Loss of Significant Others",
"image": "https://thumbs.dreamstime.com/z/young-boy-girl-love-flat-vector-illustration-cute-boyfriend-girlfriend-holding-hands-cartoon-characters-young-boy-185755044.jpg",
"About": "This was inspired by Hannah and Allison's contribution. I also realized that my contribution video featured some of my ex-boyfriends from high school who I have lost touch with because of moving away for college. It's funny how someone can go from being the most important person in your life to not being in it at all.",
"Quote": "Physical geographic segregation is a potent metaphor for the multiple sites of separation and oppositions"
},

}

currentid=11

searchresults=[]

# ROUTES


@app.route('/')
def welcome():
    global data

    food=data["1"]
    food2=data["2"]
    food3=data["3"]

    return render_template('welcome.html', food=food , food2=food2 , food3=food3)   

@app.route('/search/<keyword>')
def search(keyword):
    global data
    searchresults.clear()

    for i in range(1,len(data)+1):
        index=str(i)
        if keyword in data[index]["title"]:
            searchresults.append(data[index])
        
        elif keyword in data[index]["About"]:
            searchresults.append(data[index])
        
        elif keyword in data[index]["Quote"]:
            searchresults.append(data[index])

    matches=len(searchresults)

    #edge case for no search results
    if searchresults==[]:
        searchresults.append({
"title": "No Matches",
"image": "https://i.pinimg.com/564x/60/f9/18/60f9181e51ef5f4e6ebe3b62e2247a1c.jpg",
},)

    #TODO: before sending, bold wkeywords in search results
    return render_template('search.html', searchresults=searchresults, matches=matches,keyword=keyword) 

@app.route('/search/')
def searcherror():
    searchresults.clear()
    return render_template('search.html',searchresults=searchresults)


@app.route('/view/<id>', methods=['GET', 'POST'])
def view(id):
        view_item=data[id]
        return render_template('view.html', view_item=view_item)
 

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add_entry', methods=['GET', 'POST'])
def add_name():
    global data
    global currentid 

    new_id=currentid  
    #increment current id
    currentid=currentid+1

    json_data = request.get_json() 
    title = json_data["title"] 
    image = json_data["image"] 
    about = json_data["about"] 
    Quote = json_data["Quote"]
    
    # add new entry to array with 
    new_entry = {
        "id": new_id,
        "title":  title,
        "image": image,
        "About":about,
        "Quote":Quote
    }
    new_id=str(new_id)
    data[new_id]=new_entry

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(new_entry=new_entry)

if __name__ == '__main__':
   app.run(debug = True)




