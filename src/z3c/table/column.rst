=============
Table Columns
=============

Let's show the different columns we offer by default. But first take a look at
the README.txt which explains the Table and Column concepts.


Sample data setup
-----------------

Let's create a sample container that we can use as our iterable context:

  >>> from zope.container import btree
  >>> class Container(btree.BTreeContainer):
  ...     """Sample container."""
  >>> container = Container()
  >>> root['container'] = container

and create a sample content object that we use as container item:

  >>> class Content(object):
  ...     """Sample content."""
  ...     def __init__(self, title, number, email):
  ...         self.title = title
  ...         self.number = number
  ...         self.email = email

Now setup some items:

  >>> container[u'zero'] = Content('Zero', 0, 'zero@example.com')
  >>> container[u'first'] = Content('First', 1, 'first@example.com')
  >>> container[u'second'] = Content('Second', 2, 'second@example.com')
  >>> container[u'third'] = Content('Third', 3, 'third@example.com')
  >>> container[u'fourth'] = Content('Fourth', 4, None)

Let's also create a simple number sortable column:

  >>> from z3c.table import column
  >>> class NumberColumn(column.Column):
  ...
  ...     header = u'Number'
  ...     weight = 20
  ...
  ...     def getSortKey(self, item):
  ...         return item.number
  ...
  ...     def renderCell(self, item):
  ...         return 'number: %s' % item.number


NameColumn
----------

Let's define a table using the NameColumn:

  >>> from z3c.table import table
  >>> class NameTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.NameColumn, u'name',
  ...                              weight=1),
  ...             column.addColumn(self, NumberColumn, name=u'number',
  ...                              weight=2, header=u'Number')
  ...             ]

Now create, update and render our table and you can see that the NameColumn
renders the name of the item using the zope.traversing.api.getName() concept:

  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> nameTable = NameTable(container, request)
  >>> nameTable.update()
  >>> print(nameTable.render())
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>first</td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td>fourth</td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td>second</td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td>third</td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td>zero</td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>


RadioColumn
-----------

Let's define a table using the RadioColumn:

  >>> class RadioTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.RadioColumn, u'radioColumn',
  ...                              weight=1),
  ...             column.addColumn(self, NumberColumn, name=u'number',
  ...                              weight=2, header=u'Number')
  ...             ]

Now create, update and render our table:

  >>> request = TestRequest()
  >>> radioTable = RadioTable(container, request)
  >>> radioTable.update()
  >>> print(radioTable.render())
  <table>
    <thead>
      <tr>
        <th>X</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="first"  /></td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="fourth"  /></td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="second"  /></td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="third"  /></td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="zero"  /></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>

As you can see, we can force to render the radio input field as selected with a
given request value:

  >>> radioRequest = TestRequest(form={'table-radioColumn-0-selectedItem': 'third'})
  >>> radioTable = RadioTable(container, radioRequest)
  >>> radioTable.update()
  >>> print(radioTable.render())
  <table>
    <thead>
      <tr>
        <th>X</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="first"  /></td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="fourth"  /></td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="second"  /></td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="third" checked="checked" /></td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td><input type="radio" class="radio-widget" name="table-radioColumn-0-selectedItem" value="zero"  /></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>


CheckBoxColumn
--------------

Let's define a table using the RadioColumn:

  >>> class CheckBoxTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.CheckBoxColumn, u'checkBoxColumn',
  ...                              weight=1),
  ...             column.addColumn(self, NumberColumn, name=u'number',
  ...                              weight=2, header=u'Number')
  ...             ]

Now create, update and render our table:


  >>> request = TestRequest()
  >>> checkBoxTable = CheckBoxTable(container, request)
  >>> checkBoxTable.update()
  >>> print(checkBoxTable.render())
  <table>
    <thead>
      <tr>
        <th>X</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="first"  /></td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="fourth"  /></td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="second"  /></td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="third"  /></td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="zero"  /></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>

And again you can set force to render the checkbox input field as selected with
a given request value:

  >>> checkBoxRequest = TestRequest(form={'table-checkBoxColumn-0-selectedItems':
  ...                                     ['first', 'third']})
  >>> checkBoxTable = CheckBoxTable(container, checkBoxRequest)
  >>> checkBoxTable.update()
  >>> print(checkBoxTable.render())
  <table>
    <thead>
      <tr>
        <th>X</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="first" checked="checked" /></td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="fourth"  /></td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="second"  /></td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="third" checked="checked" /></td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="zero"  /></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>

If you select a row, you can also give them an additional CSS style. This could
be used in combination with alternating ``even`` and ``odd`` styles:

  >>> checkBoxRequest = TestRequest(form={'table-checkBoxColumn-0-selectedItems':
  ...                                     ['first', 'third']})
  >>> checkBoxTable = CheckBoxTable(container, checkBoxRequest)
  >>> checkBoxTable.cssClasses = {'tr': 'tr'}
  >>> checkBoxTable.cssClassSelected = u'selected'
  >>> checkBoxTable.cssClassEven = u'even'
  >>> checkBoxTable.cssClassOdd = u'odd'
  >>> checkBoxTable.update()
  >>> print(checkBoxTable.render())
  <table>
    <thead>
      <tr class="tr">
        <th>X</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr class="selected even tr">
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="first" checked="checked" /></td>
        <td>number: 1</td>
      </tr>
      <tr class="odd tr">
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="fourth"  /></td>
        <td>number: 4</td>
      </tr>
      <tr class="even tr">
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="second"  /></td>
        <td>number: 2</td>
      </tr>
      <tr class="selected odd tr">
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="third" checked="checked" /></td>
        <td>number: 3</td>
      </tr>
      <tr class="even tr">
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="zero"  /></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>

Let's test the ``cssClassSelected`` without any other css class:

  >>> checkBoxRequest = TestRequest(form={'table-checkBoxColumn-0-selectedItems':
  ...                                     ['first', 'third']})
  >>> checkBoxTable = CheckBoxTable(container, checkBoxRequest)
  >>> checkBoxTable.cssClassSelected = u'selected'
  >>> checkBoxTable.update()
  >>> print(checkBoxTable.render())
  <table>
    <thead>
      <tr>
        <th>X</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr class="selected">
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="first" checked="checked" /></td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="fourth"  /></td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="second"  /></td>
        <td>number: 2</td>
      </tr>
      <tr class="selected">
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="third" checked="checked" /></td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td><input type="checkbox" class="checkbox-widget" name="table-checkBoxColumn-0-selectedItems" value="zero"  /></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>


CreatedColumn
-------------

Let's define a table using the CreatedColumn:

  >>> class CreatedColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.CreatedColumn, u'createdColumn',
  ...                              weight=1),
  ...             ]

Now create, update and render our table. Note, we use a Dublin Core stub
adapter which only returns ``01/01/01 01:01`` as created date:

  >>> request = TestRequest()
  >>> createdColumnTable = CreatedColumnTable(container, request)
  >>> createdColumnTable.update()
  >>> print(createdColumnTable.render())
  <table>
    <thead>
      <tr>
        <th>Created</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>01/01/01 01:01</td>
      </tr>
      <tr>
        <td>01/01/01 01:01</td>
      </tr>
      <tr>
        <td>01/01/01 01:01</td>
      </tr>
      <tr>
        <td>01/01/01 01:01</td>
      </tr>
      <tr>
        <td>01/01/01 01:01</td>
      </tr>
    </tbody>
  </table>


ModifiedColumn
--------------

Let's define a table using the CreatedColumn:

  >>> class ModifiedColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.ModifiedColumn,
  ...                              u'modifiedColumn', weight=1),
  ...             ]

Now create, update and render our table. Note, we use a Dublin Core stub
adapter which only returns ``02/02/02 02:02`` as modified date:

  >>> request = TestRequest()
  >>> modifiedColumnTable = ModifiedColumnTable(container, request)
  >>> modifiedColumnTable.update()
  >>> print(modifiedColumnTable.render())
  <table>
    <thead>
      <tr>
        <th>Modified</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>02/02/02 02:02</td>
      </tr>
      <tr>
        <td>02/02/02 02:02</td>
      </tr>
      <tr>
        <td>02/02/02 02:02</td>
      </tr>
      <tr>
        <td>02/02/02 02:02</td>
      </tr>
      <tr>
        <td>02/02/02 02:02</td>
      </tr>
    </tbody>
  </table>


GetAttrColumn
-------------

The ``GetAttrColumn`` column is a handy column that retrieves the value from
the item by attribute access.
It also provides a ``defaultValue`` in case an exception happens.

  >>> class GetTitleColumn(column.GetAttrColumn):
  ...
  ...     attrName = 'title'
  ...     defaultValue = u'missing'

  >>> class GetAttrColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, GetTitleColumn, u'title'),
  ...             ]

Render and update the table:

  >>> request = TestRequest()
  >>> getAttrColumnTable = GetAttrColumnTable(container, request)
  >>> getAttrColumnTable.update()
  >>> print(getAttrColumnTable.render())
  <table>
    <thead>
      <tr>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>First</td>
      </tr>
      <tr>
        <td>Fourth</td>
      </tr>
      <tr>
        <td>Second</td>
      </tr>
      <tr>
        <td>Third</td>
      </tr>
      <tr>
        <td>Zero</td>
      </tr>
    </tbody>
  </table>

If we use a non-existing Attribute, we do not raise an AttributeError, we will
get the default value:

  >>> class UndefinedAttributeColumn(column.GetAttrColumn):
  ...
  ...     attrName = 'undefined'
  ...     defaultValue = u'missing'

  >>> class GetAttrColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, UndefinedAttributeColumn, u'missing'),
  ...             ]

Render and update the table:

  >>> request = TestRequest()
  >>> getAttrColumnTable = GetAttrColumnTable(container, request)
  >>> getAttrColumnTable.update()
  >>> print(getAttrColumnTable.render())
  <table>
    <thead>
      <tr>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>missing</td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
    </tbody>
  </table>

A missing ``attrName`` in ``GetAttrColumn`` would also end in return the
``defaultValue``:

  >>> class BadAttributeColumn(column.GetAttrColumn):
  ...
  ...     defaultValue = u'missing'

  >>> firstItem = container[u'first']
  >>> simpleTable = table.Table(container, request)
  >>> badColumn = column.addColumn(simpleTable, BadAttributeColumn, u'bad')
  >>> badColumn.renderCell(firstItem)
  u'missing'

If we try to access a protected attribute the object raises an ``Unauthorized``.
In this case we also return the defaultValue. Let's setup an object which
raises such an error if we access the title:

  >>> from zope.security.interfaces import Unauthorized
  >>> class ProtectedItem(object):
  ...
  ...     @property
  ...     def forbidden(self):
  ...         raise Unauthorized('forbidden')

Setup and test the item:

  >>> protectedItem = ProtectedItem()
  >>> protectedItem.forbidden
  Traceback (most recent call last):
  ...
  Unauthorized: forbidden

Now define a column:

  >>> class ForbiddenAttributeColumn(column.GetAttrColumn):
  ...
  ...     attrName = 'forbidden'
  ...     defaultValue = u'missing'

And test the attribute access:

  >>> simpleTable = table.Table(container, request)
  >>> badColumn = column.addColumn(simpleTable, ForbiddenAttributeColumn, u'x')
  >>> badColumn.renderCell(protectedItem)
  u'missing'


GetItemColumn
-------------

The ``GetItemColumn`` column is a handy column that retrieves the value from
the item by index or key access. That means the item can be a tuple, list, dict
or anything that implements that.
It also provides a ``defaultValue`` in case an exception happens.

Dict-ish
.........

  >>> sampleDictData = [
  ...     dict(name='foo', value=1),
  ...     dict(name='bar', value=7),
  ...     dict(name='moo', value=42),]

  >>> class GetDictColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.GetItemColumn, u'name',
  ...                              header=u'Name',
  ...                              idx='name', defaultValue='missing'),
  ...             column.addColumn(self, column.GetItemColumn, u'value',
  ...                              header=u'Value',
  ...                              idx='value', defaultValue='missing'),
  ...             ]
  ...     @property
  ...     def values(self):
  ...         return sampleDictData

Render and update the table:

  >>> request = TestRequest()
  >>> getDictColumnTable = GetDictColumnTable(sampleDictData, request)
  >>> getDictColumnTable.update()
  >>> print(getDictColumnTable.render())
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>bar</td>
        <td>7</td>
      </tr>
      <tr>
        <td>foo</td>
        <td>1</td>
      </tr>
      <tr>
        <td>moo</td>
        <td>42</td>
      </tr>
    </tbody>
  </table>

If we use a non-existing index/key, we do not raise an exception, we will
get the default value:

  >>> class GetDictColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.GetItemColumn, u'name',
  ...                              idx='not-existing', defaultValue='missing'),
  ...             ]
  ...     @property
  ...     def values(self):
  ...         return sampleDictData

Render and update the table:

  >>> request = TestRequest()
  >>> getDictColumnTable = GetDictColumnTable(container, request)
  >>> getDictColumnTable.update()
  >>> print(getDictColumnTable.render())
  <table>
    <thead>
      <tr>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>missing</td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
    </tbody>
  </table>

A missing ``idx`` in ``GetItemColumn`` would also end in return the
``defaultValue``:

  >>> class BadIdxColumn(column.GetItemColumn):
  ...
  ...     defaultValue = u'missing'

  >>> firstItem = sampleDictData[0]
  >>> simpleTable = table.Table(sampleDictData, request)
  >>> badColumn = column.addColumn(simpleTable, BadIdxColumn, u'bad')
  >>> badColumn.renderCell(firstItem)
  u'missing'

Tuple/List-ish
...............

  >>> sampleTupleData = [
  ...     (50, 'bar'),
  ...     (42, 'cent'),
  ...     (7, 'bild'),]

  >>> class GetTupleColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.GetItemColumn, u'name',
  ...                              header=u'Name',
  ...                              idx=1, defaultValue='missing'),
  ...             column.addColumn(self, column.GetItemColumn, u'value',
  ...                              header=u'Value',
  ...                              idx=0, defaultValue='missing'),
  ...             ]
  ...     @property
  ...     def values(self):
  ...         return sampleTupleData

Render and update the table:

  >>> request = TestRequest()
  >>> getTupleColumnTable = GetTupleColumnTable(sampleTupleData, request)
  >>> getTupleColumnTable.update()
  >>> print(getTupleColumnTable.render())
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>bar</td>
        <td>50</td>
      </tr>
      <tr>
        <td>bild</td>
        <td>7</td>
      </tr>
      <tr>
        <td>cent</td>
        <td>42</td>
      </tr>
    </tbody>
  </table>

If we use a non-existing index/key, we do not raise an exception, we will
get the default value:

  >>> class GetTupleColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.GetItemColumn, u'name',
  ...                              idx=42, defaultValue='missing'),
  ...             ]
  ...     @property
  ...     def values(self):
  ...         return sampleTupleData

Render and update the table:

  >>> request = TestRequest()
  >>> getTupleColumnTable = GetTupleColumnTable(container, request)
  >>> getTupleColumnTable.update()
  >>> print(getTupleColumnTable.render())
  <table>
    <thead>
      <tr>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>missing</td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
    </tbody>
  </table>

A missing ``idx`` in ``GetItemColumn`` would also end in return the
``defaultValue``:

  >>> class BadIdxColumn(column.GetItemColumn):
  ...
  ...     defaultValue = u'missing'

  >>> firstItem = sampleTupleData[0]
  >>> simpleTable = table.Table(sampleTupleData, request)
  >>> badColumn = column.addColumn(simpleTable, BadIdxColumn, u'bad')
  >>> badColumn.renderCell(firstItem)
  u'missing'


GetAttrFormatterColumn
----------------------

The ``GetAttrFormatterColumn`` column is a get attr column which is able to
format the value. Let's use the Dublin Core adapter for our sample:

  >>> from zope.dublincore.interfaces import IZopeDublinCore
  >>> class GetCreatedColumn(column.GetAttrFormatterColumn):
  ...
  ...     def getValue(self, item):
  ...         dc = IZopeDublinCore(item, None)
  ...         return dc.created

  >>> class GetAttrFormatterColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, GetCreatedColumn, u'created'),
  ...             ]

Render and update the table:

  >>> request = TestRequest()
  >>> getAttrFormatterColumnTable = GetAttrFormatterColumnTable(container,
  ...     request)
  >>> getAttrFormatterColumnTable.update()
  >>> print(getAttrFormatterColumnTable.render())
  <table>
    <thead>
      <tr>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>2001 1 1  01:01:01 </td>
      </tr>
      <tr>
        <td>2001 1 1  01:01:01 </td>
      </tr>
      <tr>
        <td>2001 1 1  01:01:01 </td>
      </tr>
      <tr>
        <td>2001 1 1  01:01:01 </td>
      </tr>
      <tr>
        <td>2001 1 1  01:01:01 </td>
      </tr>
    </tbody>
  </table>


We can also change the formatter settings in such a column:

  >>> class LongCreatedColumn(column.GetAttrFormatterColumn):
  ...
  ...     formatterCategory = u'dateTime'
  ...     formatterLength = u'long'
  ...     formatterCalendar = u'gregorian'
  ...
  ...     def getValue(self, item):
  ...         dc = IZopeDublinCore(item, None)
  ...         return dc.created

  >>> class LongFormatterColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, LongCreatedColumn, u'created'),
  ...             ]

Render and update the table:

  >>> request = TestRequest()
  >>> longFormatterColumnTable = LongFormatterColumnTable(container,
  ...     request)
  >>> longFormatterColumnTable.update()
  >>> print(longFormatterColumnTable.render())
  <table>
    <thead>
      <tr>
        <th></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>2001 1 1  01:01:01 +000</td>
      </tr>
      <tr>
        <td>2001 1 1  01:01:01 +000</td>
      </tr>
      <tr>
        <td>2001 1 1  01:01:01 +000</td>
      </tr>
      <tr>
        <td>2001 1 1  01:01:01 +000</td>
      </tr>
      <tr>
        <td>2001 1 1  01:01:01 +000</td>
      </tr>
    </tbody>
  </table>


EMailColumn
-----------

The ``EMailColumn`` column is ``GetAttrColumn`` which is used to
display a mailto link. By default in the link content the e-mail
address is displayed, too.


  >>> class EMailColumn(column.EMailColumn):
  ...
  ...     attrName = 'email'
  ...     defaultValue = u'missing'

  >>> class EMailColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, EMailColumn, u'email'),
  ...             ]

When a cell does not contain an e-mail address, the ``defaultValue``
is rendered:

  >>> request = TestRequest()
  >>> eMailColumnTable = EMailColumnTable(container, request)
  >>> eMailColumnTable.update()
  >>> print(eMailColumnTable.render())
  <table>
    <thead>
      <tr>
        <th>E-Mail</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="mailto:first@example.com">first@example.com</a></td>
      </tr>
      <tr>
        <td><a href="mailto:second@example.com">second@example.com</a></td>
      </tr>
      <tr>
        <td><a href="mailto:third@example.com">third@example.com</a></td>
      </tr>
      <tr>
        <td><a href="mailto:zero@example.com">zero@example.com</a></td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
    </tbody>
  </table>

The link content can be overwriten by setting the ``linkContent`` attribute:

  >>> class StaticEMailColumn(column.EMailColumn):
  ...
  ...     attrName = 'email'
  ...     defaultValue = u'missing'
  ...     linkContent = 'Mail me'

  >>> class StaticEMailColumnTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, StaticEMailColumn, u'mail'),
  ...             ]

Render and update the table:

  >>> request = TestRequest()
  >>> staticEMailColumnTable = StaticEMailColumnTable(container, request)
  >>> staticEMailColumnTable.update()
  >>> print(staticEMailColumnTable.render())
  <table>
    <thead>
      <tr>
        <th>E-Mail</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="mailto:first@example.com">Mail me</a></td>
      </tr>
      <tr>
        <td><a href="mailto:second@example.com">Mail me</a></td>
      </tr>
      <tr>
        <td><a href="mailto:third@example.com">Mail me</a></td>
      </tr>
      <tr>
        <td><a href="mailto:zero@example.com">Mail me</a></td>
      </tr>
      <tr>
        <td>missing</td>
      </tr>
    </tbody>
  </table>


LinkColumn
----------

Let's define a table using the LinkColumn. This column allows us to write
columns which can point to a page with the item as context:

  >>> class MyLinkColumns(column.LinkColumn):
  ...     linkName = 'myLink.html'
  ...     linkTarget = '_blank'
  ...     linkCSS = 'myClass'
  ...     linkTitle = 'Click >'

  >>> class MyLinkTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, MyLinkColumns, u'link',
  ...                              weight=1),
  ...             column.addColumn(self, NumberColumn, name=u'number',
  ...                              weight=2, header=u'Number')
  ...             ]

Now create, update and render our table:

  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> myLinkTable = MyLinkTable(container, request)
  >>> myLinkTable.__parent__ = container
  >>> myLinkTable.__name__ = u'myLinkTable.html'
  >>> myLinkTable.update()
  >>> print(myLinkTable.render())
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="http://127.0.0.1/container/first/myLink.html" target="_blank" class="myClass" title="Click &gt;">first</a></td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/fourth/myLink.html" target="_blank" class="myClass" title="Click &gt;">fourth</a></td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/second/myLink.html" target="_blank" class="myClass" title="Click &gt;">second</a></td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/third/myLink.html" target="_blank" class="myClass" title="Click &gt;">third</a></td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/zero/myLink.html" target="_blank" class="myClass" title="Click &gt;">zero</a></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>


ContentsLinkColumn
------------------

There are some predefined link columns available. This one will generate a
``contents.html`` link for each item:

  >>> class ContentsLinkTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.ContentsLinkColumn, u'link',
  ...                              weight=1),
  ...             column.addColumn(self, NumberColumn, name=u'number',
  ...                              weight=2, header=u'Number')
  ...             ]

  >>> contentsLinkTable = ContentsLinkTable(container, request)
  >>> contentsLinkTable.__parent__ = container
  >>> contentsLinkTable.__name__ = u'contentsLinkTable.html'
  >>> contentsLinkTable.update()
  >>> print(contentsLinkTable.render())
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="http://127.0.0.1/container/first/contents.html">first</a></td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/fourth/contents.html">fourth</a></td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/second/contents.html">second</a></td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/third/contents.html">third</a></td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/zero/contents.html">zero</a></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>


IndexLinkColumn
---------------

This one will generate a ``index.html`` link for each item:

  >>> class IndexLinkTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.IndexLinkColumn, u'link',
  ...                              weight=1),
  ...             column.addColumn(self, NumberColumn, name=u'number',
  ...                              weight=2, header=u'Number')
  ...             ]

  >>> indexLinkTable = IndexLinkTable(container, request)
  >>> indexLinkTable.__parent__ = container
  >>> indexLinkTable.__name__ = u'indexLinkTable.html'
  >>> indexLinkTable.update()
  >>> print(indexLinkTable.render())
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="http://127.0.0.1/container/first/index.html">first</a></td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/fourth/index.html">fourth</a></td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/second/index.html">second</a></td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/third/index.html">third</a></td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/zero/index.html">zero</a></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>


EditLinkColumn
--------------

And this one will generate a ``edit.html`` link for each item:

  >>> class EditLinkTable(table.Table):
  ...     cssClassSortedOn = None
  ...
  ...     def setUpColumns(self):
  ...         return [
  ...             column.addColumn(self, column.EditLinkColumn, u'link',
  ...                              weight=1),
  ...             column.addColumn(self, NumberColumn, name=u'number',
  ...                              weight=2, header=u'Number')
  ...             ]

  >>> editLinkTable = EditLinkTable(container, request)
  >>> editLinkTable.__parent__ = container
  >>> editLinkTable.__name__ = u'editLinkTable.html'
  >>> editLinkTable.update()
  >>> print(editLinkTable.render())
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="http://127.0.0.1/container/first/edit.html">first</a></td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/fourth/edit.html">fourth</a></td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/second/edit.html">second</a></td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/third/edit.html">third</a></td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td><a href="http://127.0.0.1/container/zero/edit.html">zero</a></td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>
