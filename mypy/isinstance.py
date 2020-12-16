import typing


class _IsInstanceForm(typing._SpecialForm, _root=True):
    def __repr__(self):
        return 'mypy.isinstance.' + self._name

    def __getitem__(self, parameters):
        return typing._GenericAlias(self, parameters)


IsInstance = _IsInstanceForm(
    'IsInstance',
    doc="""A type used as the return type of type guards.

    Mypy will treat this function as a test that confirms whether
    it should treat the passed-in value as the referenced type.""")
