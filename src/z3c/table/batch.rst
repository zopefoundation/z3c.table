Batching
--------

Our table implements batching out of the box. If the amount of
row items is smaller than the given ``startBatchingAt`` size, the table starts
to batch at this size. Let's define a new Table.

We need to configure our batch provider for the next step first. See the
section ``BatchProvider`` below for more infos about batch rendering:

  >>> from zope.configuration.xmlconfig import XMLConfig
  >>> import z3c.table
  >>> import zope.component
  >>> XMLConfig('meta.zcml', zope.component)()
  >>> XMLConfig('configure.zcml', z3c.table)()

Now we can create our table:

  >>> from zope.publisher.browser import TestRequest
  >>> from z3c.table.testing import Container, Content, SimpleTable
  >>> container = Container()
  >>> root['container-1'] = container
  >>> request = TestRequest()
  >>> batchingTable = SimpleTable(container, request)
  >>> batchingTable.cssClassSortedOn = None

We also need to give the table a location and a name like we normally setup
in traversing:

  >>> batchingTable.__parent__ = container
  >>> batchingTable.__name__ = u'batchingTable.html'

Now setup some items:

  >>> container[u'zero'] = Content('Zero', 0)
  >>> container[u'first'] = Content('First', 1)
  >>> container[u'second'] = Content('Second', 2)
  >>> container[u'third'] = Content('Third', 3)
  >>> container[u'fourth'] = Content('Fourth', 4)
  >>> container[u'sixth'] = Content('Sixth', 6)
  >>> container[u'seventh'] = Content('Seventh', 7)
  >>> container[u'eighth'] = Content('Eighth', 8)
  >>> container[u'ninth'] = Content('Ninth', 9)
  >>> container[u'tenth'] = Content('Tenth', 10)
  >>> container[u'eleventh'] = Content('Eleventh', 11)
  >>> container[u'twelfth '] = Content('Twelfth', 12)
  >>> container[u'thirteenth'] = Content('Thirteenth', 13)
  >>> container[u'fourteenth'] = Content('Fourteenth', 14)
  >>> container[u'fifteenth '] = Content('Fifteenth', 15)
  >>> container[u'sixteenth'] = Content('Sixteenth', 16)
  >>> container[u'seventeenth'] = Content('Seventeenth', 17)
  >>> container[u'eighteenth'] = Content('Eighteenth', 18)
  >>> container[u'nineteenth'] = Content('Nineteenth', 19)
  >>> container[u'twentieth'] = Content('Twentieth', 20)

Now let's show the full table without batching:

  >>> batchingTable.update()
  >>> print(batchingTable.render())
  <table>
    <thead>
      <tr>
        <th>My items</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Eighteenth item</td>
        <td>number: 18</td>
      </tr>
      <tr>
        <td>Eighth item</td>
        <td>number: 8</td>
      </tr>
      <tr>
        <td>Eleventh item</td>
        <td>number: 11</td>
      </tr>
      <tr>
        <td>Fifteenth item</td>
        <td>number: 15</td>
      </tr>
      <tr>
        <td>First item</td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td>Fourteenth item</td>
        <td>number: 14</td>
      </tr>
      <tr>
        <td>Fourth item</td>
        <td>number: 4</td>
      </tr>
      <tr>
        <td>Nineteenth item</td>
        <td>number: 19</td>
      </tr>
      <tr>
        <td>Ninth item</td>
        <td>number: 9</td>
      </tr>
      <tr>
        <td>Second item</td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td>Seventeenth item</td>
        <td>number: 17</td>
      </tr>
      <tr>
        <td>Seventh item</td>
        <td>number: 7</td>
      </tr>
      <tr>
        <td>Sixteenth item</td>
        <td>number: 16</td>
      </tr>
      <tr>
        <td>Sixth item</td>
        <td>number: 6</td>
      </tr>
      <tr>
        <td>Tenth item</td>
        <td>number: 10</td>
      </tr>
      <tr>
        <td>Third item</td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td>Thirteenth item</td>
        <td>number: 13</td>
      </tr>
      <tr>
        <td>Twelfth item</td>
        <td>number: 12</td>
      </tr>
      <tr>
        <td>Twentieth item</td>
        <td>number: 20</td>
      </tr>
      <tr>
        <td>Zero item</td>
        <td>number: 0</td>
      </tr>
    </tbody>
  </table>

As you can see, the table is not ordered and it uses all items. If we like
to use the batch, we need to set the startBatchingAt size to a lower value than
it is set by default.
The default value which a batch is used is set to ``50``:

  >>> batchingTable.startBatchingAt
  50

We will set the batch start to ``5`` for now. This means the first 5 items
do not get used:

  >>> batchingTable.startBatchingAt = 5
  >>> batchingTable.startBatchingAt
  5

There is also a ``batchSize`` value which we need to set to ``5``. By default
the value gets initialized by the ``batchSize`` value:

  >>> batchingTable.batchSize
  50

  >>> batchingTable.batchSize = 5
  >>> batchingTable.batchSize
  5

Now we can update and render the table again. But you will see that we only get
a table size of 5 rows, which is correct. But the order doesn't depend on the
numbers we see in cells:

  >>> batchingTable.update()
  >>> print(batchingTable.render())
  <table>
    <thead>
      <tr>
        <th>My items</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Eighteenth item</td>
        <td>number: 18</td>
      </tr>
      <tr>
        <td>Eighth item</td>
        <td>number: 8</td>
      </tr>
      <tr>
        <td>Eleventh item</td>
        <td>number: 11</td>
      </tr>
      <tr>
        <td>Fifteenth item</td>
        <td>number: 15</td>
      </tr>
      <tr>
        <td>First item</td>
        <td>number: 1</td>
      </tr>
    </tbody>
  </table>

I think we should order the table by the second column before we show the next
batch values. We do this by simply set the ``defaultSortOn``:

  >>> batchingTable.sortOn = u'table-number-1'

Now we should see a nice ordered and batched table:

  >>> batchingTable.update()
  >>> print(batchingTable.render())
  <table>
    <thead>
      <tr>
        <th>My items</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Zero item</td>
        <td>number: 0</td>
      </tr>
      <tr>
        <td>First item</td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td>Second item</td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td>Third item</td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td>Fourth item</td>
        <td>number: 4</td>
      </tr>
    </tbody>
  </table>

The batch concept allows us to choose from all batches and render the rows
for this batched items. We can do this by set any batch as rows. as you can see
we have ``4`` batched row data available:

  >>> len(batchingTable.rows.batches)
  4

We can set such a batch as row values, then this batch data are used for
rendering. But take care, if we update the table, our rows get overridden
and reset to the previous values. this means you can set any batch as rows
data and only render them. This is possible since the update method sorted all
items and all batch contain ready-to-use data. This concept could be important
if you need to cache batches etc. :

  >>> batchingTable.rows = batchingTable.rows.batches[1]
  >>> print(batchingTable.render())
  <table>
    <thead>
      <tr>
        <th>My items</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Sixth item</td>
        <td>number: 6</td>
      </tr>
      <tr>
        <td>Seventh item</td>
        <td>number: 7</td>
      </tr>
      <tr>
        <td>Eighth item</td>
        <td>number: 8</td>
      </tr>
      <tr>
        <td>Ninth item</td>
        <td>number: 9</td>
      </tr>
      <tr>
        <td>Tenth item</td>
        <td>number: 10</td>
      </tr>
    </tbody>
  </table>

And like described above, if you call ``update`` our batch to rows setup get
reset:

  >>> batchingTable.update()
  >>> print(batchingTable.render())
  <table>
    <thead>
      <tr>
        <th>My items</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Zero item</td>
        <td>number: 0</td>
      </tr>
      <tr>
        <td>First item</td>
        <td>number: 1</td>
      </tr>
      <tr>
        <td>Second item</td>
        <td>number: 2</td>
      </tr>
      <tr>
        <td>Third item</td>
        <td>number: 3</td>
      </tr>
      <tr>
        <td>Fourth item</td>
        <td>number: 4</td>
      </tr>
    </tbody>
  </table>

This means you can probably update all batches, cache them and use them after.
But this is not useful for normal usage in a page without an enhanced concept
which is not a part of this implementation. This also means, there must be
another way to set the batch index. Yes there is, there are two other ways how
we can set the batch position. We can set a batch position by setting the
``batchStart`` value in our table or we can use a request variable. Let's show
the first one first:

  >>> batchingTable.batchStart = 6
  >>> batchingTable.update()
  >>> print(batchingTable.render())
  <table>
    <thead>
      <tr>
        <th>My items</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Seventh item</td>
        <td>number: 7</td>
      </tr>
      <tr>
        <td>Eighth item</td>
        <td>number: 8</td>
      </tr>
      <tr>
        <td>Ninth item</td>
        <td>number: 9</td>
      </tr>
      <tr>
        <td>Tenth item</td>
        <td>number: 10</td>
      </tr>
      <tr>
        <td>Eleventh item</td>
        <td>number: 11</td>
      </tr>
    </tbody>
  </table>

We can also set the batch position by using the batchStart value in a request.
Note that we need the table ``prefix`` and column ``__name__`` like we use in
the sorting concept:

  >>> batchingRequest = TestRequest(form={'table-batchStart': '11',
  ...                                     'table-batchSize': '5',
  ...                                     'table-sortOn': 'table-number-1'})
  >>> requestBatchingTable = SimpleTable(container, batchingRequest)
  >>> requestBatchingTable.cssClassSortedOn = None
  
We also need to give the table a location and a name like we normally set up
in traversing:

  >>> requestBatchingTable.__parent__ = container
  >>> requestBatchingTable.__name__ = u'requestBatchingTable.html'

Note: our table needs to start batching at smaller amount of items than we
have by default otherwise we don't get a batch:

  >>> requestBatchingTable.startBatchingAt = 5
  >>> requestBatchingTable.update()
  >>> print(requestBatchingTable.render())
  <table>
    <thead>
      <tr>
        <th>My items</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Twelfth item</td>
        <td>number: 12</td>
      </tr>
      <tr>
        <td>Thirteenth item</td>
        <td>number: 13</td>
      </tr>
      <tr>
        <td>Fourteenth item</td>
        <td>number: 14</td>
      </tr>
      <tr>
        <td>Fifteenth item</td>
        <td>number: 15</td>
      </tr>
      <tr>
        <td>Sixteenth item</td>
        <td>number: 16</td>
      </tr>
    </tbody>
  </table>


BatchProvider
-------------

The batch provider allows us to render the batch HTML independently of our
table. This means by default the batch gets not rendered in the render method.
You can change this in your custom table implementation and return the batch
and the table in the render method.

As we can see, our table rows provides IBatch if it comes to batching:

  >>> from z3c.batching.interfaces import IBatch
  >>> IBatch.providedBy(requestBatchingTable.rows)
  True

Let's check some batch variables before we render our test. This let us compare
the rendered result. For more information about batching see the README.txt in
z3c.batching:

  >>> requestBatchingTable.rows.start
  11

  >>> requestBatchingTable.rows.index
  2

  >>> requestBatchingTable.rows.batches
  <z3c.batching.batch.Batches object at ...>

  >>> len(requestBatchingTable.rows.batches)
  4

We use our previous batching table and render the batch with the built-in
``renderBatch`` method:

  >>> requestBatchingTable.update()
  >>> print(requestBatchingTable.renderBatch())
  <a href="...html?table-batchSize=5&table-batchStart=0&..." class="first">1</a>
  <a href="...html?table-batchSize=5&table-batchStart=5&...">2</a>
  <a href="...html?table-batchSize=5&table-batchStart=11&..." class="current">3</a>
  <a href="...html?table-batchSize=5&table-batchStart=15&..." class="last">4</a>

Now let's add more items so that we can test the skipped links in large
batches:

  >>> for i in range(1000):
  ...     idx = i+20
  ...     container[str(idx)] = Content(str(idx), idx)

Now let's test the batching table again with the new amount of items and
the same ``startBatchingAt`` of 5 but starting the batch at item ``100``
and sorted on the second numbered column:

  >>> batchingRequest = TestRequest(form={'table-batchStart': '100',
  ...                                     'table-batchSize': '5',
  ...                                     'table-sortOn': 'table-number-1'})
  >>> requestBatchingTable = SimpleTable(container, batchingRequest)
  >>> requestBatchingTable.startBatchingAt = 5
  >>> requestBatchingTable.cssClassSortedOn = None

We also need to give the table a location and a name like we normally setup
in traversing:

  >>> requestBatchingTable.__parent__ = container
  >>> requestBatchingTable.__name__ = u'requestBatchingTable.html'

  >>> requestBatchingTable.update()
  >>> print(requestBatchingTable.render())
  <table>
    <thead>
      <tr>
        <th>My items</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>100 item</td>
        <td>number: 100</td>
      </tr>
      <tr>
        <td>101 item</td>
        <td>number: 101</td>
      </tr>
      <tr>
        <td>102 item</td>
        <td>number: 102</td>
      </tr>
      <tr>
        <td>103 item</td>
        <td>number: 103</td>
      </tr>
      <tr>
        <td>104 item</td>
        <td>number: 104</td>
      </tr>
    </tbody>
  </table>

And test the batch. Note the three dots between the links are rendered by the
batch provider and are not a part of the doctest:

  >>> print(requestBatchingTable.renderBatch())
  <a href="...html?table-batchSize=5&table-batchStart=0&table-sortOn=table-number-1" class="first">1</a>
  ...
  <a href="...html?table-batchSize=5&table-batchStart=85&table-sortOn=table-number-1">18</a>
  <a href="...html?table-batchSize=5&table-batchStart=90&table-sortOn=table-number-1">19</a>
  <a href="...html?table-batchSize=5&table-batchStart=95&table-sortOn=table-number-1">20</a>
  <a href="...html?table-batchSize=5&table-batchStart=100&table-sortOn=table-number-1" class="current">21</a>
  <a href="...html?table-batchSize=5&table-batchStart=105&table-sortOn=table-number-1">22</a>
  <a href="...html?table-batchSize=5&table-batchStart=110&table-sortOn=table-number-1">23</a>
  <a href="...html?table-batchSize=5&table-batchStart=115&table-sortOn=table-number-1">24</a>
  ...
  <a href="...html?table-batchSize=5&table-batchStart=1015&table-sortOn=table-number-1" class="last">204</a>

You can change the spacer in the batch provider if you set the ``batchSpacer``
value:

  >>> from z3c.table.batch import BatchProvider
  >>> from z3c.table.interfaces import IBatchProvider
  >>> from zope.interface import implementer
  >>> @implementer(IBatchProvider)
  ... class XBatchProvider(BatchProvider):
  ...     """Just another batch provider."""
  ...     batchSpacer = u'xxx'

Now register the new batch provider for our batching table:

  >>> import zope.publisher.interfaces.browser
  >>> from zope.component import getSiteManager
  >>> sm = getSiteManager(container)
  >>> sm.registerAdapter(XBatchProvider,
  ...     (zope.interface.Interface,
  ...      zope.publisher.interfaces.browser.IBrowserRequest,
  ...      SimpleTable), name='batch')

If we update and render our table, the new batch provider should get used.
As you can see the spacer get changed now:

  >>> requestBatchingTable.update()
  >>> requestBatchingTable.batchProvider
  <...XBatchProvider object at ...>
  >>> print(requestBatchingTable.renderBatch())
  <a href="...html?table-batchSize=5&table-batchStart=0&table-sortOn=table-number-1" class="first">1</a>
  xxx
  <a href="...html?table-batchSize=5&table-batchStart=85&table-sortOn=table-number-1">18</a>
  <a href="...html?table-batchSize=5&table-batchStart=90&table-sortOn=table-number-1">19</a>
  <a href="...html?table-batchSize=5&table-batchStart=95&table-sortOn=table-number-1">20</a>
  <a href="...html?table-batchSize=5&table-batchStart=100&table-sortOn=table-number-1" class="current">21</a>
  <a href="...html?table-batchSize=5&table-batchStart=105&table-sortOn=table-number-1">22</a>
  <a href="...html?table-batchSize=5&table-batchStart=110&table-sortOn=table-number-1">23</a>
  <a href="...html?table-batchSize=5&table-batchStart=115&table-sortOn=table-number-1">24</a>
  xxx
  <a href="...html?table-batchSize=5&table-batchStart=1015&table-sortOn=table-number-1" class="last">204</a>


Now test the extremities, need to define a new batchingRequest:
Beginning by the left end point:

  >>> leftBatchingRequest = TestRequest(form={'table-batchStart': '10',
  ...                                        'table-batchSize': '5',
  ...                                       'table-sortOn': 'table-number-1'})
  >>> leftRequestBatchingTable = SimpleTable(container, leftBatchingRequest)
  >>> leftRequestBatchingTable.__parent__ = container
  >>> leftRequestBatchingTable.__name__ = u'leftRequestBatchingTable.html'
  >>> leftRequestBatchingTable.update()
  >>> print(leftRequestBatchingTable.renderBatch())
  <a href="http://...html?table-batchSize=5&table-batchStart=0&table-sortOn=table-number-1" class="first">1</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=5&table-sortOn=table-number-1">2</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=10&table-sortOn=table-number-1" class="current">3</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=15&table-sortOn=table-number-1">4</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=20&table-sortOn=table-number-1">5</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=25&table-sortOn=table-number-1">6</a>
  xxx
  <a href="http://...html?table-batchSize=5&table-batchStart=1015&table-sortOn=table-number-1" class="last">204</a>

Go on with the right extremity:

  >>> rightBatchingRequest = TestRequest(form={'table-batchStart': '1005',
  ...                                     'table-batchSize': '5',
  ...                                     'table-sortOn': 'table-number-1'})
  >>> rightRequestBatchingTable = SimpleTable(container, rightBatchingRequest)
  >>> rightRequestBatchingTable.__parent__ = container
  >>> rightRequestBatchingTable.__name__ = u'rightRequestBatchingTable.html'
  >>> rightRequestBatchingTable.update()
  >>> print(rightRequestBatchingTable.renderBatch())
  <a href="http://...html?table-batchSize=5&table-batchStart=0&table-sortOn=table-number-1" class="first">1</a>
  xxx
  <a href="http://...html?table-batchSize=5&table-batchStart=990&table-sortOn=table-number-1">199</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=995&table-sortOn=table-number-1">200</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=1000&table-sortOn=table-number-1">201</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=1005&table-sortOn=table-number-1" class="current">202</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=1010&table-sortOn=table-number-1">203</a>
  <a href="http://...html?table-batchSize=5&table-batchStart=1015&table-sortOn=table-number-1" class="last">204</a>


None previous and next batch size. Probably it doesn't make sense but let's
show what happens if we set the previous and next batch size to 0 (zero):

  >>> from z3c.table.batch import BatchProvider
  >>> class ZeroBatchProvider(BatchProvider):
  ...     """Just another batch provider."""
  ...     batchSpacer = u'xxx'
  ...     previousBatchSize = 0
  ...     nextBatchSize = 0

Now register the new batch provider for our batching table:

  >>> import zope.publisher.interfaces.browser
  >>> sm.registerAdapter(ZeroBatchProvider,
  ...     (zope.interface.Interface,
  ...      zope.publisher.interfaces.browser.IBrowserRequest,
  ...      SimpleTable), name='batch')

Update the table and render the batch:

  >>> requestBatchingTable.update()
  >>> print(requestBatchingTable.renderBatch())
  <a href="...html?table-batchSize=5&table-batchStart=0&table-sortOn=table-number-1" class="first">1</a>
  xxx
  <a href="...html?table-batchSize=5&table-batchStart=100&table-sortOn=table-number-1" class="current">21</a>
  xxx
  <a href="...html?table-batchSize=5&table-batchStart=1015&table-sortOn=table-number-1" class="last">204</a>
