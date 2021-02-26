from app import ns_reduce
from flask_restplus import fields

res = ns_reduce.model(
                        "Statistics",
                        {
                           "data": fields.String(description="data", required=True),
                           "operator": fields.String(description="operator", required=True)
                        }
                     )
