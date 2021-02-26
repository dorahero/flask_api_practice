from app import ns_reduce
from flask import request
from flask_restplus import Resource
from app.Services.StatisticsService import dataStatistics
from app.Expects.StatisticsExpect import res


@ns_reduce.route('/reduce')
class Statistics(Resource):
    @ns_reduce.expect(res)
    def post(self, **kwargs):            
        return dataStatistics(request)  