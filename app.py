from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)



@app.route('/',methods=['GET'])
def start():

    return render_template('index.html')

def flames_func(r,s):
    for i in r:
        for j in s:
            if i==j:
                r=r.replace(j, '', 1)
                s=s.replace(j,'',1)
#             
    total_length=len(r)+len(s)
    flames=["Frnds","love","Affection","Marriage","Enemy","sister"]
    n=6
    for i in range(0,6):
        if n==1:
            break
        if n!=1:
        
            index=total_length%n
            flames.pop(index-1)
            n=n-1    
    result=flames[0]
    return result


@app.route('/result',methods=['POST'])
def submit():
    your_name=request.form.get("yname")
    dolis_name=request.form.get("dname")
    final=flames_func(your_name,dolis_name)
    result={
        "result" : final,
    }
    return render_template('result.html',result=result)


if __name__ == '__main__':
	app.run(debug=True)