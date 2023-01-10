from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)



@app.route('/',methods=['GET'])
def start():

    return render_template('index.html')

def flames_func(r,s):
    r = r.strip()
    s = s.strip()
    for i in r:
        for j in s:
            if i==j:
                # print(i)
                # print(j)
                r=r.replace(j, '', 1)
                s=s.replace(j, '' ,1)
    print(r)
    print(len(r))
    print(len(s))
    total_length=len(r)+len(s)
    print(total_length)
    flames=["Frnds","love","Affection","Marriage","Enemy","sister"]
    while len(flames) > 1 : 
        split_index = (total_length % len(flames) - 1) 
        if (split_index>=0) :
            right = flames[split_index + 1 : ]
            left = flames[ : split_index] 
            flames = right + left
        else : 
            flames = flames[ : len(flames) - 1] 
    result=flames[0]
    print(result) 
    return result 
@app.route('/result',methods=['POST'])
def submit():
    your_name=request.form.get("yname")
    dolis_name=request.form.get("dname")
    final=flames_func(your_name,dolis_name)
    result={
        "result" : final,
    }
    return render_template('index.html',result=result)


if __name__ == '__main__':
	app.run(debug=True)