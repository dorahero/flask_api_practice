from flask import Flask
from flask_restplus import Api
from app.utils import setting

flask_app = Flask(__name__)
flask_app.config.from_object(setting) 

api = Api(app = flask_app,
          version="1.0"  ,
          title="Statistics Apis",
          description="WanRed exercise"          
)
ns_reduce = api.namespace('Statistics', description='Statistics APIs')

from app.Controllers import StatisticsController
from app.Expects import StatisticsExpect
from app.Models import StatisticsModel
from app.Services import StatisticsService

