from PIL import Image
from flask import Flask,jsonify,request
from classifier import getPrediction

app=Flask(__name__)
@app.route("/predict-alphabet",methods=["POST"])
def predictData():
    image=request.files.get("alphabet")
    prediction=getPrediction(image)
    return jsonify({
        "prediction":prediction
    })

if __name__=="__main__":
    app.run()


