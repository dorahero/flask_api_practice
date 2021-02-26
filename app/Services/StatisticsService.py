from app.Models.StatisticsModel import Statistics

def dataStatistics(request):
    operator = []
    all_function = []
    try:
        json_data=request.json
        data = [float(j) for j in json_data['data']]
        operator = json_data['operator']
        sta = Statistics(
            data = data,
            operator = operator
        )       
        all_function = [method for method in dir(sta) if method[:2] != '__']
        res = {o: getattr(sta, o)() for o in operator}

        return res
    except:
        if operator:
            for o in operator:
                if o not in all_function:
                    return {"status": "Failed", "Information": f"{o} is not in the functions."}, 404
        else:
            return {"status": "Failed"}, 404
