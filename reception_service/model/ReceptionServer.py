from flask_restful import Resource, reqparse

from reception_service.model.Reception import Reception

reception = Reception()

text_arg = "text"

reception_get_args = reqparse.RequestParser()
reception_get_args.add_argument(text_arg)


class ReceptionServer(Resource):
    def get(self):
        args = reception_get_args.parse_args()
        text: str = args[text_arg]
        response = reception.get_response(text)
        return response, 200
