
class CheckMKParamsHelper:

    def __init__(self, params):
        self.params = params


    def get_mandatory_params(self, mandatory_params):

        ret = {}
        for mandatory_field in mandatory_params:
            _param = self.params.get(mandatory_field)
            if _param is None:
                raise Exception(mandatory_field + " is a mandatory field")

            ret[mandatory_field] = _param

        return ret

    def get_optional_params(self, optional_params, aliases = None):

        ret = {}
        for optional_field in optional_params:
            _param = self.params.get(optional_field)

            if _param is not None:

                if type(aliases) is dict and aliases.has_key(optional_field):
                    optional_field = aliases.get(optional_field)

                ret.update({optional_field: _param})

        return ret