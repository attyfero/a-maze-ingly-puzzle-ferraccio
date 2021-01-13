# -*- coding: utf-8 -*-
import json
import traceback


class Common:
    def json_validation(self, json_file):
        """Validate a json in input file"""

        if not json_file:
            print("Json bad of null")

        try:
            return json.loads(json_file)
        except:
            print("Unable to parse json input file")
            traceback.print_exc()

    def get_item_from_id(self, json_input_object, object_id):
        """Get the object item inside json file from id key"""

        try:
            finded = [json_item for json_item in json_input_object['rooms'] if json_item["id"] == object_id]

            if finded and len(finded) > 0:
                return finded[0]

            return None

        except:
            print("Unable to find json item")
            traceback.print_exc()
            return None
