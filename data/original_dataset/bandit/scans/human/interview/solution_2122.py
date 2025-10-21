import sys
import heapq
from collections import namedtuple

Record = namedtuple('Record', ['index', 'book_id'])

l1 = sys.stdin.readline()
l2 = sys.stdin.readline()

n, k = list(map(int, l1.split(' ')))
books = list(map(int, l2.split(' ')))

cost = 0
cache = set()
prev = dict() # book_id -> index
next = [n+1] * n # index of next with the same value
inactive_ids = set() # set of inactive object id()s
book_to_record = dict()


def serve_book(book_id, i):
	cache.add(book_id)
	record = Record(-next[i], book_id)
	heapq.heappush(h, record)
	book_to_record[book_id] = record

h = []
for i, book_id in enumerate(books):
	if book_id in prev:
		next[prev[book_id]] = i
	prev[book_id] = i

for i, book_id in enumerate(books):
	# print("book_id=%s, h=%s, inactive=%s" %(book_id, h, inactive_ids))
	if book_id in cache:
		previous_record = book_to_record[book_id]
		inactive_ids.add(id(previous_record))
		serve_book(book_id, i)
		# print('--> Serve book from library ', book_id)
		continue

	if len(cache) < k:
		cost += 1
		serve_book(book_id, i)
		# print('--> Buy book', book_id)
		continue

	while True:
		item = heapq.heappop(h)
		if id(item) in inactive_ids:
			# print("--> Ignore record", item)
			inactive_ids.remove(id(item))
			continue
		cache.remove(item.book_id)
		serve_book(book_id, i)
		cost += 1
		# print('--> Throw away book', item.book_id)
		# print('--> Add book to libary', book_id)
		break
	# print("To evict %s" % to_evict)
	

print(cost)