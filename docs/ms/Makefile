CC=dot -Tsvg microservices.dot -o microservices.svg

DIAGRAM=microservices.svg
DOT=microservices.dot

all: $(DIAGRAM)

$(DIAGRAM):
	$(CC) -Tsvg $(DOT) -o microservices.svg

clean:
	rm $(DIAGRAM)
