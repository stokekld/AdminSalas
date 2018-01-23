CC=dot

DIAGRAM=../images/microservices.svg
DOT=microservices.dot

all: $(DIAGRAM)

$(DIAGRAM):
	$(CC) -Tsvg $(DOT) -o $(DIAGRAM)

clean:
	rm $(DIAGRAM)
