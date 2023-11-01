from flask import Flask,render_template,request,redirect
import sqlite3

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def func():  
    conn=sqlite3.connect("youtube.db")
    conn.row_factory=sqlite3.Row
    cur=conn.cursor() 
    cur.execute("select * from thumbnailList")
    data=cur.fetchall()
   
    if request.method=="POST":
     res =request.json
     print(res)
     cur.execute("insert into thumbnailList(THUMBNAIL,PROFILEPIC,DESCRIPTION,UPLOADED_BEFORE,CHANNEL,VIEWS) values(?,?,?,?,?,?)",
                (res["thumbnail"],res["profilePic"],res["description"],res["uploaded_before"],res["channel"],res["views"]))

    conn.commit()
    return render_template("index.html",thumbnailList=data)

@app.route("/a/<string:id>",methods=["GET","POST"])
def play(id):
    conn=sqlite3.connect("youtube.db")
    conn.row_factory=sqlite3.Row
    cur=conn.cursor() 
    cur.execute("select * from thumbnailList")
    data=cur.fetchall()
    cur.execute("Select * from thumbnailList where videoID=?",(id,))
    data2=cur.fetchone()
    conn.commit
    return render_template("play.html",thumbnailList=data,d=data2)

@app.route("/upload",methods=["GET","POST"])
def upload():
    if request.method=="POST":
        videoID=request.form.get("videoID")
        description=request.form.get("description")
        thumbnail=request.form.get("thumbnail")
        channel=request.form.get("channel")
        views=request.form.get("views")
        uploadInfo=request.form.get("upload-info")
        profile=request.form.get("profile")
        conn=sqlite3.connect("youtube.db")
        cur=conn.cursor()
        cur.execute("insert into thumbnailList (VIDEOID,THUMBNAIL,PROFILEPIC,DESCRIPTION,UPLOADED_BEFORE,CHANNEL,VIEWS) values(?,?,?,?,?,?,?)",
                    (videoID,thumbnail,profile,description,uploadInfo,channel,views))
        conn.commit()
        return redirect("/")
    return render_template("form.html")


if "__main__"==__name__:
    app.run(debug=True)