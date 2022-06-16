#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
app = Flask(__name__)


# In[2]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        storey = request.form.get("storey")
        area = request.form.get("area")
        lease = request.form.get("lease")
        town = request.form.get("town")      
        print(storey, area, lease, town)
        model = joblib.load("Price Model")
        pred = model.predict([[float(storey), float(area), float(lease), float(town)]])
        s = f""" You have entered the following details:
    Storey Code: {storey}
    Floor Area: {area} sqm
    Number of Remaining Lease: {lease} years
    Town Code: {town}

The predicted house price will be {str(pred[0])} """
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Model loading..."))


# In[3]:


if __name__== "__main__":
    app.run()

