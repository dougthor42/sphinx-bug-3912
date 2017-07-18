# -*- coding: utf-8 -*-
"""
Helper classes that let us proxy objects.

The intended use for these is to add properties to ORM classes which
let us access similarly named attributes in list or dict form.

Examples
--------
>>>    ...
>>>    Data_1 = Column('Data 1', Float(asdecimal=True))
>>>    Data_2 = Column('Data 2', Float(asdecimal=True))
>>>    Data_3 = Column('Data 3', Float(asdecimal=True))
>>>    Data_4 = Column('Data 4', Float(asdecimal=True))
>>>    Data_5 = Column('Data 5', Float(asdecimal=True))
>>>    Data_6 = Column('Data 6', Float(asdecimal=True))
>>>    Data_7 = Column('Data 7', Float(asdecimal=True))
>>>    Data_8 = Column('Data 8', Float(asdecimal=True))
>>>    Data_9 = Column('Data 9', Float(asdecimal=True))
>>>    Data_10 = Column('Data 10', Float(asdecimal=True))
>>>    ...
>>>
>>>    def __init__(self):
>>>        self.init_on_load()
>>>
>>>    @reconstructor
>>>    def init_on_load(self):
>>>        attrs = ['Data_{}'.format(i) for i in range(1, 11)]
>>>        self._Data = ListAttributeProxy(self, attrs)
>>>
>>>    @property
>>>    def data(self):
>>>        return self._Data
"""

try:
    from collections.abc import Sequence, Mapping
except ImportError:
    from collections import Sequence, Mapping


class ListAttributeProxy(Sequence):
    """
    A list-like proxy to a subset of an objects attributes.

    Updates to a ``ListAttributeProxy`` are reflected in the base
    object, and visa-versa.

    Parameters
    ----------
    base : :class:`sqlalchemy.ext.declarative.api.DeclarativeMeta` object
        The object to be proxied.
    attrs : list of str
        The attributes of base to be made accessible through this
        ``ListAttributeProxy``.

    Raises
    ------
    ValueError
        If base does not have all the attributes in attrs

    Examples
    --------
    >>> lap = ListAttributeProxy(x, ['a', 'b'])
    >>> x.a
    1
    >>> lap[0]
    1
    >>> lap[0] = 2
    >>> x.a
    2
    >>> x.b = 10
    >>> lap[1]
    10
    """

    def __init__(self, base, attrs):
        missing = [a for a in attrs if not hasattr(base, a)]
        if missing:
            raise ValueError("Missing attributes {!r}".format(missing))
        else:
            self._data = attrs
            self._base = base

    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self[j]
                    for j
                    in range(i.start or 0, i.stop or len(self), i.step or 1)]
        else:
            return getattr(self._base, self._data[i])

    def __setitem__(self, i, x):
        if isinstance(i, slice):
            range_ = range(i.start or 0, i.stop or len(self), i.step or 1)
            for j, val in zip(range_, x):
                self[j] = val
        else:
            setattr(self._base, self._data[i], x)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return "<ListAttributeProxy of {!r}>".format(self._base)

    def __str__(self):
        return str([x for x in self])


class DictAttributeProxy(Mapping):
    """
    A dict-like proxy to a subset of an objects attributes.

    Updates to a ``DictAttributeProxy`` are reflected in the base object,
    and visa-versa.

    Parameters
    ----------
    base : :class:`sqlalchemy.ext.declarative.api.DeclarativeMeta` object
        The object to be proxied.
    map_ : Dict of keys to strings
        A map of keys to strings representing attributes of base.

    Raises
    ------
    ValueError
        If base does not have all the attributes in attrs

    Examples
    --------
    >>> dap = DictAttributeProxy(y, {(0,'A'): 'Data0A', (0, 'B'): 'Data0B'})
    >>> y.Data0A
    1
    >>> dap[(0,'A')]
    1
    >>> dap[(0,'A')] = 2
    >>> y.Data0A
    2
    >>> y.Data0B = 10
    >>> dap[(0,'B')]
    10
    """

    def __init__(self, base, map_):
        missing = [a for a in map_.values() if not hasattr(base, a)]
        if missing:
            raise ValueError("Missing attributes {!r}".format(missing))
        else:
            self.data = map_
            self.base = base

    def __getitem__(self, key):
        return getattr(self.base, self.data[key])

    def __setitem__(self, key, x):
        setattr(self.base, self.data[key], x)

    def __len__(self):
        return len(self.data)

    def __contains__(self, key):
        return key in self.data

    def __iter__(self):
        return self.data.__iter__()

    def __repr__(self):
        return "<DictAttributeProxy of {!r}>".format(self.base)

    def __str__(self):
        return str({k: self[k] for k in self})
