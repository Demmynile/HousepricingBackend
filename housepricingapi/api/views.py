from django.shortcuts import render
from rest_framework.views import APIView
import pickle
import joblib
import numpy as np
from rest_framework.response import Response



class HousepricingView(APIView):
        
        def post(self , request):
            data = request.data

            if data is not None:
                bathrooms = data["bathrooms"]
                serviced_price = data["serviced_price"]
                new_price = data["new_price"]
                estate_price = data["estate_price"]
                location_rank = data["location_rank"]
                exec_flag = data["exec_flag"]
                terrace_flag = data["terrace_flag"]
                toilets = data["toilets"]
                bedrooms = data["bedrooms"]
                location = data["location"]
                mlM = joblib.load("https://housepricing-application.herokuapp.com/api/ml_model/housePricing.pkl")
                print(mlM)
                mlm_predict = mlM.predict([[bathrooms , serviced_price , new_price , estate_price , location_rank , exec_flag , terrace_flag , toilets , bedrooms , location]])
                response_dict = {"response" : np.round(mlm_predict , decimals=2)}
                print(mlm_predict)
                return Response(response_dict, status=200)
            else:
                response_dict_err = {"response" , "data is invalid"}
                return Response(response_dict_err , status = 400)
            

  
           

    

 
        





