ASFLAGS := -m32
CFLAGS  := -m32 -g -std=c99 -Wall -Werror -D_GNU_SOURCE
LDFLAGS := -m32
LDLIBS  := -lcrypto
PROGS   := zookld zookfs zookd

all: $(PROGS)
.PHONY: all

zookld zookd zookfs: %: %.o http.o


.PHONY: check
check:
	./check-lab6.sh
.PHONY: check-experimental
check-experimental:
	./check-lab6-experimental.sh



.PHONY: fix-flask
fix-flask: fix-flask.sh
	./fix-flask.sh

.PHONY: clean
clean:
	rm -f *.o *.pyc *.bin $(PROGS)


lab%-handin.tar.gz: clean
	tar cf - `find . -type f | grep -v '^\.*$$' | grep -v '/CVS/' | grep -v '/\.svn/' | grep -v '/\.git/' | grep -v 'lab[0-9].*\.tar\.gz' | grep -v '/submit.token$$' | grep -v libz3str.so` | gzip > $@

.PHONY: prepare-submit
prepare-submit: lab6-handin.tar.gz

.PHONY: prepare-submit-a
prepare-submit-a: lab6a-handin.tar.gz

.PHONY: prepare-submit-b
prepare-submit-b: lab6b-handin.tar.gz

.PHONY: submit-a
submit-a: lab6a-handin.tar.gz
	./submit.py $<

.PHONY: submit-b
submit-b: lab6b-handin.tar.gz
	./submit.py $<

.PHONY: submit
submit: lab6-handin.tar.gz
	./submit.py $<

.PRECIOUS: lab6-handin.tar.gz
