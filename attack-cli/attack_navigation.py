from models import Tactic, Technique, APT, TacticTechniqueMap

class AttackNavigator(object):
    def __init__(self):
        self.apts = {}
        self.tactics = {}
        self.techniques = {}


    def initialize(self):
        self._fetch_data()

    def get_tactics(self, query=None):
        if query is None:
            return [tactic.get_details(relation=True) for tactic in self.tactics.values()]

        result = self._search(self.tactics, ['name'], query)
        return result


    def _get_details(self, param_dict, key, raise_exception=False):
        instance = param_dict.get(key)
        if not instance:
            if raise_exception:
                raise Exception("Instance not found")
            else:
                return None

        return instance.get_details(relation=True)

    def _search(self, param_dict, search_keys, search_value):
        result = set()
        for id, value in param_dict.items():
            for search_key in search_keys:
                if search_value in getattr(value, search_key, None):
                    result.add(value)

        return [value.get_details(relation=True) for value in result]

    def get_tactic(self, id_param, raise_exception=False):
        return self._get_details(self.tactics, id_param, raise_exception)

    def get_techniques(self, search_param=None):
        return

    def get_technique(self, id_param, raise_exception=False):
        return self._get_details(self.techniques, id_param, raise_exception)

    def get_apts(self, search_params=None):
        return

    def get_apt(self, id_param, raise_exception=False):
        return self._get_details(self.apts, id_param, raise_exception)

    def _fetch_data(self):
        a = Tactic('Hello')
        self.tactics[a.id] = a

        a = Tactic('World')
        self.tactics[a.id] = a


        b = Technique('test technique')
        self.techniques[b.id] = b

        e = TacticTechniqueMap()
        e.add_mapping(a, b)

        c = APT('test apt')
        self.apts[c.id] = c
