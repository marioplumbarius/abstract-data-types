"""
  Types of errors:
  - Syntax errors
    .when
      translating the source code into byte code
    .e.g.
      omitting the colon: if, def, while, etc
      creating a variable with a python keyword
      strings not matching quotation marks
      = instead of ==

  - runtime errors
    .when
      produced by the runtime system if something goes wrong while the program is running
    .e.g.
      infinite loop
    errors:
      NameError => variable does not exists
      TypeError => object type related
      KeyError => dictionary related
      AttributeError => attr/method does not exists
      IndexError => index does not exists on list, string, tuple, etc
  - semantic errors
    .when
      problems with a program that compiles and runs bug does not do the right thing
    .e.g.
      expression being evaluated in an unexpected order
"""
