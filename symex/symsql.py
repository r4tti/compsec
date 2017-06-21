## This module wraps SQLalchemy's methods to be friendly to
## symbolic / concolic execution.

import fuzzy
import sqlalchemy.orm

oldget = sqlalchemy.orm.query.Query.get
def newget(query, primary_key):
  ## Exercise 5: your code here.
  ##
  ## Find the object with the primary key "primary_key" in SQLalchemy
  ## query object "query", and do so in a symbolic-friendly way.
  ##
  ## Hint: given a SQLalchemy row object r, you can find the name of
  ## its primary key using r.__table__.primary_key.columns.keys()[0]
 # for r in query.all():
 #    print r

  v = oldget(query, primary_key)

  for row in query.all():
    pk = row.__table__.primary_key.columns.keys()[0]
    v = getattr(row, pk)
    if v == primary_key:
      return row
  # if v is None:
  # return None    
  return None # fuzzy.concolic_int(fuzzy.sym_int(fuzzy.ast(v)), v)

sqlalchemy.orm.query.Query.get = newget
