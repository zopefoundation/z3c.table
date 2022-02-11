=======
CHANGES
=======

2.2 (2022-02-11)
----------------

- Add support for Python 3.8, 3.9 and 3.10.


2.1.1 (2019-03-26)
------------------

- Fix: escape special HTML characters at ``Column.renderHeadCell``, 
  ``NameColumn.getName``, ``CheckBoxColumn`` name and value,
  ``RadioColumn`` name and value, ``LinkColumn`` href and link content.


2.1 (2019-01-27)
----------------

- Added support for Python 3.7 and PyPy3.

- Dropped support for running the tests using `python setup.py test`.

- Reformatted the code using black and flake8.


2.0.1 (2017-04-19)
------------------

- Required future>=0.14.0 so `html` package is available in Python 2.7.


2.0.0 (2017-04-17)
------------------

- Updated to support Python 2.7, 3.5, and 3.6 only.

- Added html title attribute on LinkColumn


2.0.0a1 (2013-02-26)
--------------------

- Added support for Python 3.3, dropped support for Python 2.5 and below.

- Got rid of testing dependencies on z3.testing and zope.app.testing.


1.0.0 (2012-08-09)
------------------

- Added sorting (``cssClassSortedOn`` and ``getCSSSortClass``) CSS options

- Added cell highlight (``getCSSHighlightClass``) CSS option

- Added ``GetItemColumn`` which gets the value by index/key access.

0.9.1 (2011-08-03)
------------------

- Fixed SelectedItemColumn.update when just one item was selected


0.9.0 (2010-08-09)
------------------

- Added ``EMailColumn`` which can be used to display mailto links.

- Fixed the default BatchProvider not to lose table sorting query arguments
  from the generated links; now batching and sorting play with each other
  nicely.

- Split single doctest file (README.txt) into different files


0.8.1 (2010-07-31)
------------------

- Added translation for the link title in the column header of the
  sortable table.


0.8.0 (2009-12-29)
------------------

- Added translation for ``LinkColumn.linkContent``.

- Added ``I18nGetAttrColumn`` which translates its content.


0.7.0 (2009-12-29)
------------------

- Allow to initialze the column definitions without requiring an
  entire table update.

- Fixed tests, so they no longer use ``zope.app.container`` (which was
  even not declared as test dependency).

- Head cell contents are now translated.

0.6.1 (2009-02-22)
------------------

- Be smart to not ``IPhysicallyLocatable`` objects if we lookup the
  ``__name__`` value in columns.


0.6.0 (2008-11-12)
------------------

- Bugfix: Allow to switch the sort order on the header link. This was
  blocked to descending after the first click

- Bugfix: CheckBoxColumn, ensure that we allways use a list for compare
  selected items. It was possible that if only one item get selected
  we compared a string. If this string was a sub string of another existing
  item the other item get selected too.

- Moved advanced batching implementation into z3c.batching

- Implemented GetAttrFormatterColumn. This column can be used for simple
  value formatting columns.

- Bad typo in columns.py: Renamed ``getLinkConent`` to ``getLinkContent``

- Bug: Changed return string in getLinkCSS. It was using css="" instead of
  class="" for CSS classes. Thanks to Dan for reporting this bugs.

- Implemented SelectedItemColumn

- Fix CheckBoxColumn, use always the correct selectedItems. Use always real
  selectedItems form the table

- Fix RadioColumn, use always the correct selectedItem from the selectedItems
  list. Use always the first selectedItems form the tables selectedItems


0.5.0 (2008-04-13)
------------------

- Initial Release.
