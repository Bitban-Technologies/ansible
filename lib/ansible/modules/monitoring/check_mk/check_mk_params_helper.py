
class CheckMKParamsHelper:

    def __init__(self, params):
        self.params = params


    def get_mandatory_params(self, mandatory_params):

        ret = {}
        for mandatory in mandatory_params:
            _param = self.params.get(mandatory)
            if _param is None:
                raise Exception(mandatory + " is a mandatory field")

            ret[mandatory] = _param

        return ret

    def get_optional_params(self, optional_params):

        ret = {}
        for optional in optional_params:
            ret.update({optional: self.params.get(optional)})

        return ret