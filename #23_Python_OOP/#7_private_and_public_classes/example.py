from classes import NotPrivate, _Private

test_private = _Private('puppy')


test_public = NotPrivate('tommy')              
test_public.display()                          
test_public._display()                       
