page ='http://en.wikipedia.org/wiki/Main_Page'
keyword='definition'

words = page.split()



#print counts



def test_hash_function(func, keys, size):
    results = [0]*size
    keys_used = []
    for w in keys:
        if w not in keys_used:
             hv = func(w, size)
             results[hv] += 1
             keys_used.append(w)
    return results


def hash_string(keyword,buckets):
    h=0                         #keeep postion 
    for c in keyword:
        h= (h +ord(c))%buckets
    return h
print hash_string('udacity ',1000 )
print hash_string('',12)   #0

hash_string(keyword,8)
print test_hash_function(hash_string,words,12)
